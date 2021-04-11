import pytest
import os
from module_draft import user_input


@pytest.mark.input
@pytest.mark.parametrize('cmd_string, exp_args',
                         [
                             ('test/', {'path': 'test/',
                                        'output': os.getcwd()}),
                             ('test/ -o output', {'path': 'test/',
                                                  'output': 'output'}),
                             ('test/ --output output',
                                 {'path': 'test/', 'output': 'output'}),
                         ])
def test_user_input(cmd_string, exp_args):
    """Fuction to test user_input() correct assignemnt of command line args.

    Args:
        cmd_string ([type]): [description]
        exp_args ([type]): [description]
    """
    sys_argv = cmd_string.split()
    args = user_input.user_input(sys_argv)
    assert args.path == exp_args['path']
    assert args.output == exp_args['output']
