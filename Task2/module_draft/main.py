# Author: Tobias Kaczun
# Date: 19.03.21
# Package: DSS Analysis Package

import sys
import os
import argparse
from reader import FileReader
import analysis


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


def main():
    """Main function for commandline call
    """
    # end user version for user_input
    # args = user_input(sys.argv[1:])

    # add your own args = user_input() for testing and debugging so that you
    # don't have to call the script with full command line input

    args = user_input(['C:\\Users\\windo\\OneDrive\\Dokumente\\Uni\\Sustainable_development_course\\Group_1_Developing_Scientific_Software\\Input\\Task1', '-o',
    'C:\\Users\\windo\\OneDrive\\Dokumente\\Uni\\Sustainable_development_course\\Group_1_Developing_Scientific_Software\\Output\\Task2'])

    # read files
    reader = FileReader(args.path)
    input_df = reader.read()

    # perform statistical analysis
    stat_ana = analysis.Statistical_Analysis(args.output)
    stat_ana.correlation(input_df['npop.t'])
    stat_ana.eucl_distance(input_df['table.dat'])

    # perfomr numerical analysis


if __name__ == "__main__":
    main()
