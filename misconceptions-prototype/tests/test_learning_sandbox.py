"""Opt-in real execution of authored fixtures, never historical student code."""

import json
import os
from pathlib import Path

import pytest

from misconceptions.learning_problems import PROBLEMS, get_problem
from misconceptions.learning_sandbox import DockerSandbox

SOLUTIONS = json.loads((Path(__file__).parent / 'fixtures/learning_solutions.json').read_text())
docker_test = pytest.mark.skipif(os.environ.get('AAI_RUN_DOCKER_TESTS') != '1',
                                 reason='Opt in to authored-code Docker integration checks')


def test_docker_command_has_bounded_isolation():
    sandbox = DockerSandbox()
    sandbox.image_id = 'sha256:fixture'
    command = sandbox._command('aai-fixture', 'execute.py')
    for flag in ['--network=none', '--read-only', '--cap-drop=ALL',
                 '--security-opt=no-new-privileges', '--pids-limit=32',
                 '--memory=256m', '--memory-swap=256m', '--user=65534:65534']:
        assert flag in command
    assert not any(flag.startswith(('--volume', '--mount', '--privileged')) for flag in command)


@docker_test
@pytest.mark.parametrize('problem', PROBLEMS, ids=lambda p: p['id'])
def test_authored_reference_passes_public_oracles(problem):
    result = DockerSandbox().evaluate(SOLUTIONS[problem['id']], problem['tests'])
    assert result['verdict'] == 'accepted', result
    assert result['passed'] == 6
    assert result['provenance']['image_id'].startswith('sha256:')


@docker_test
@pytest.mark.parametrize(('source', 'expected'), [
    ('int main(void){while(1){}}', 'timeout'),
    ('int main(void){return 7;}', 'runtime_error'),
    ('#include <stdio.h>\nint main(void){while(1)putchar(65);}', 'runtime_error'),
    ('#include <stdio.h>\nint main(void){puts("0");}', 'fail'),
])
def test_runtime_limits_and_wrong_answer(source, expected):
    result = DockerSandbox().evaluate(source, [get_problem('sum-range')['tests'][1]])
    assert result['tests'][0]['outcome'] == expected


@docker_test
def test_compilation_failure_has_no_fabricated_test_observations():
    result = DockerSandbox().evaluate('int main( broken', get_problem('swap')['tests'])
    assert result['verdict'] == 'compile_error'
    assert result['tests'] == [] and result['diagnostics']


@docker_test
def test_network_and_read_only_nonroot_boundary():
    source = '''#include <stdio.h>
#include <unistd.h>
#include <sys/socket.h>
#include <arpa/inet.h>
int main(void) {
    int s=socket(AF_INET,SOCK_STREAM,0);
    struct sockaddr_in a={0}; a.sin_family=AF_INET; a.sin_port=htons(53);
    inet_pton(AF_INET,"1.1.1.1",&a.sin_addr);
    FILE *f=fopen("/opt/aai/unwanted-file","w");
    if (getuid()==65534 && f==NULL && connect(s,(struct sockaddr*)&a,sizeof(a))<0)
        puts("ISOLATED");
    else puts("UNSAFE");
    return 0;
}'''
    result = DockerSandbox().evaluate(source, [
        {'test_id': 'isolation', 'input': '', 'expected': 'ISOLATED\n'}])
    assert result['verdict'] == 'accepted', result


@docker_test
def test_non_utf8_output_keeps_original_bytes():
    result = DockerSandbox().evaluate('#include <stdio.h>\nint main(){putchar(255);return 0;}', [
        {'test_id': 'encoding', 'input': '', 'expected': 'x\n'}])
    test = result['tests'][0]
    assert test['outcome'] == 'runtime_error'
    assert test['output_encoding'] == 'invalid_utf8'
    assert test['output_bytes_base64'] == '/w=='
