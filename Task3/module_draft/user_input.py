import os
import argparse


def user_input(sys_argv):
    """Function to parse command line arguments from user.

    Args:
        sys_argv (list): command line arguments as saved in sys.argv

    Returns:
        ArgumentParser: Object containing user arguments
    """
    parser = argparse.ArgumentParser()

    # positional command line arguments
    parser.add_argument("path", help="path to input directory or file",
                        type=str)

    # optional command line arguments
    parser.add_argument("-o", "--output", help="where to save output files",
                        type=str, default=os.getcwd())

    return parser.parse_args(sys_argv)
