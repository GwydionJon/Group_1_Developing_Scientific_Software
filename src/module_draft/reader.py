# Author: Tobias Kaczun
# Date: 18.03.21
# Package: DSS analysis package

import os
import numpy as np
import pandas as pd


class FileReader:
    """Class for reading the input files and returning them as pandas
    DataFrames.
    """

    def __init__(self, dir_path):
        """__init__ Method of FileReader class detects all files in folder
        and safes their paths and filenames as dict or does the same for just a
        single file given.

        Args:
            dir_path (str): path to directory or file
        """
        self.file_dict = {}

        # checks if path is directory
        if os.path.isdir(dir_path):
            # gets files and subdirectories
            # checks which ones are files and adds them to the dict containing
            # their paths
            for path in os.listdir(dir_path):
                full_path = os.path.join(dir_path, path)
                if os.path.isfile(full_path):
                    self.file_dict[os.path.basename(full_path)] = full_path
        # if path is file only uses that path
        elif os.path.isfile(dir_path):
            self.file_dict[os.path.basename(dir_path)] = dir_path
        # raises error if it is neither a directory nor a file
        else:
            raise OSError("no valid path given, neither file nor directory")

    def read_numpy(self, file_path):
        """Function to read text files with numpy, transform to complex number
        and into DataFrame.

        Args:
            file_path (str): filepath

        Returns:
            DataFrame: DataFrame from file, dtype=complex and 'time' column
        """
        temp_np = np.loadtxt(file_path, skiprows=1)
        # saves first columns as time seperatly
        time = temp_np[:, 0]
        temp_np = temp_np[:, 1:]

        # creates new np.array with complex numbers
        imag_np = np.zeros(
            (temp_np.shape[0], int(temp_np.shape[1] / 2)), dtype=complex)
        for i in range(imag_np.shape[1]):
            imag_np[:, i] = temp_np[:, 2 * i] + 1j * temp_np[:, 2 * i + 1]

        # creates DataFrame from complex numpy array and adds
        # the time column again
        df = pd.DataFrame(data=imag_np)
        df['time'] = time

        return df

    def read_pandas_c(self, file_path):
        """Function to read text files to pandas DataFrame that are whitespace
        separated.

        Args:
            file_path (str): filepath

        Returns:
            DataFrame: DataFrame as read from file
        """
        return pd.read_csv(file_path, delim_whitespace=True)

    def read(self):
        """Fucntion to read all files in Reader Class

        Returns:
            Dict: Dict containing the DataFrames with filenames as keys
        """
        self.df_dict = {}

        for fn in self.file_dict:
            # reads file with standard routine
            file_path = self.file_dict[fn]
            df = self.read_pandas_c(file_path)

            # extracts column names directly from file
            fline = open(file_path).readline().rstrip()
            column = fline.split("  ")
            column = [string for string in column if not string.isspace()]
            column = [string for string in column if string]
            # compares directly extracted column names to those
            # from pandas
            # if they do not match it will read in the file with numpy
            # this should only happen for 'nstate_i.t'!
            if len(column) != df.shape[1]:
                df = self.read_numpy(file_path)

            self.df_dict[fn] = df

        return self.df_dict







        
