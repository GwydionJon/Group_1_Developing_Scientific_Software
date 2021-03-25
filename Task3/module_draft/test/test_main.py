import pytest
import os
import main

@pytest.mark.input
@pytest.mark.parametrize('cmd_string, exp_args',
    [
        ('test/', {'path': 'test/', 'output': os.getcwd()}),
        ('test2/ -o output/', {'path': 'test/', 'output': 'output/'}),
        ('test2/ --output output/', {'path': 'test/', 'output': 'output/'}),
        ('test2/ OUTPUT output/', {'path': 'test/', 'output': 'output/'}),
    ])
def test_user_input(cmd_string, exp_args):
    """Fuction to test user_input() correct assignemnt of command line args.

    Args:
        cmd_string ([type]): [description]
        exp_args ([type]): [description]
    """
    sys_argv = cmd_string.split()
    assert main.user_input(sys_argv).path == exp_args['path']
    assert main.user_input(sys_argv).output == exp_args['output']

@pytest.mark.input
@pytest.mark.parametrize('cmd_string, exp_err',
    [
        ('', )
    ])
def test_error_user_input(cmd_string, exp_err):
    """Fucntion to test correct Error Messages of user_input.

    Args:
        cmd_string ([type]): [description]
        exp_err ([type]): [description]
    """
    sys_argv = cmd_string.split()
    with pytest.raises(exp_err):
        main.user_input(sys_argv)


