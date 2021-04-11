import pytest
# import os
# import analysis
# import reader
import numpy as np
import pandas as pd
from module_draft import analysis

print(pytest)

d = {'time': [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0],
     'MO1': [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
     'MO2': [0.1524017, 0.5356461, 1.7423169, -0.1427532, 1.6225221, -0.3763554, 0.6635818, 0.3619019, 0.6592663, -0.7464501],
     'MO3': [1.78686092, 1.86001193, -1.81850292, -0.37167939, 1.10741963, -0.88304761, 1.29881338, 0.14487047, -1.84921077, -0.07427954]}
df = pd.DataFrame(data=d)


def test_correlation():
    """This tests verifys, that the output of correlation is of the correct type and format
    """
    # test for correct type of DataFrame
    obj = analysis.Statistical_Analysis(df)
    assert isinstance(obj.correlation(df, writecsv=False), pd.DataFrame)

    assert obj.correlation(df, writecsv=False).columns.tolist() == ["variable", "value"]

d2 = [[0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0], [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0], [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0],
      [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0], [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0], [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]]
df2 = pd.DataFrame(data=d2)


def test_eucl_distance():
    """This tests verifys, that the output of eucl_distance is of the correct type and value
    """
    # test for correct types of entries in the list
    obj2 = analysis.Statistical_Analysis("tmp_path")
    assert isinstance(obj2.eucl_distance(df2), list)

    assert type(obj2.eucl_distance(df2)[1]) == np.float64


def get_data_frame_fft_input():
    """This is a setup for the fft test and generates a df with 0s

    Returns:
        df: one column named "test_set" containing 0s
    """
    np_array = np.ones(50)
    my_label = "test_set"
    df = pd.DataFrame(np_array, columns=[my_label])
    return df, my_label


def get_data_frame_autocorr_input():
    """This is a setup for the autocorr test and generates a df with 0s, 1s and a time series.

    Returns:
        df: time, ones, zeros
    """
    np_time_range = np.linspace(0, 10, 50)
    np_zeros = np.zeros((50, 50))
    np_ones = np.ones((50, 50))
    time_stamp = "time"

    df_time = pd.DataFrame(np_time_range, columns=["time"])
    df_ones = pd.DataFrame(np_ones)
    df_ones = pd.concat([df_time, df_ones], axis=1)

    df_zeros = pd.DataFrame(np_zeros)
    df_zeros = pd.concat([df_time, df_zeros], axis=1)

    return df_ones, df_zeros, time_stamp


def get_data_frame_autocorr_output():
    """this generates the wanted output for the autocorr test

    Returns:
        df: ["time", "autocorr", "autocorr_abs",
                   "autocorr_real", "autocorr_imag"]
    """
    np_time_range = np.linspace(0, 10, 50)
    np_zero_autocorr = np.zeros(50, dtype=complex)
    np_zero_all = np.zeros(50)

    np_ones_autocorr = np.ones(50, dtype=complex) * 50
    np_ones_autocorr_abs = np.ones(50) * 50
    np_ones_autocorr_real = np.ones(50) * 50
    np_ones_autocorr_imag = np.zeros(50)
    column_list = ["time", "autocorr", "autocorr_abs",
                   "autocorr_real", "autocorr_imag"]

    df_zeros = pd.DataFrame(zip(np_time_range, np_zero_autocorr, np_zero_all, np_zero_all, np_zero_all),
                            columns=column_list)
    df_ones = pd.DataFrame(zip(np_time_range, np_ones_autocorr, np_ones_autocorr_abs,
                               np_ones_autocorr_real, np_ones_autocorr_imag),
                           columns=column_list)
    return df_zeros, df_ones


def test_fft_with_freq_analysis():
    """This tests verifys, that the output of fft_with_freq_analysis is of the correct type and format

    """
    df, label = get_data_frame_fft_input()
    # test for correct type of DataFrame
    assert isinstance(analysis.Numerical_Analysis.fft_with_freq_analysis(analysis.Numerical_Analysis,
                                                                         df, label), pd.DataFrame)

    assert analysis.Numerical_Analysis.fft_with_freq_analysis(
        analysis.Numerical_Analysis, df, label).columns.tolist() == ["freq", "intensitys"]


def test_autocorrelation():
    """ This tests wether the results of autocorrelation are df and verifys they are equal to the desired output
    """

    df_ones, df_zeros, time_stamp = get_data_frame_autocorr_input()
    df_zeros_out, df_ones_out = get_data_frame_autocorr_output()
    # tests output type for 1 array
    assert isinstance(analysis.Numerical_Analysis.autocorrelation(analysis.Numerical_Analysis,
                                                                  df_ones, time_stamp), pd.DataFrame)
    # tests output type for 0 array
    assert isinstance(analysis.Numerical_Analysis.autocorrelation(analysis.Numerical_Analysis,
                                                                  df_zeros, time_stamp), pd.DataFrame)
    # assert analysis.Numerical_Analysis.autocorrelation(analysis.Numerical_Analysis,
    #                                                   df_zeros, time_stamp) == df_zeros_out
    print(df_zeros_out.head())
    print(analysis.Numerical_Analysis.autocorrelation(analysis.Numerical_Analysis,
                                                      df_zeros, time_stamp).head())

    pd.testing.assert_frame_equal(analysis.Numerical_Analysis.autocorrelation(
        analysis.Numerical_Analysis,
        df_zeros, time_stamp), df_zeros_out)

    pd.testing.assert_frame_equal(analysis.Numerical_Analysis.autocorrelation(
        analysis.Numerical_Analysis,
        df_ones, time_stamp), df_ones_out)
