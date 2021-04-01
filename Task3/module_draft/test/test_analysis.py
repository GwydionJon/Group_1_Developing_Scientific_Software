import pytest
# import os
import analysis
# import reader
import numpy as np
import pandas as pd


def get_data_frame_fft_input():
    print(pytest)
    np_array = np.ones(50)
    my_label = "test_set"
    df = pd.DataFrame(np_array, columns=[my_label])
    return df, my_label


def get_data_frame_autocorr_input():
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
