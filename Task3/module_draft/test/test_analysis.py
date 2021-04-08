import pytest
# import os
import analysis
# import reader
import numpy as np
import pandas as pd


def test_correlation():
    """This tests verifys, that the output of correlation is of the correct type and format
    """
    df, label = get_data_frame_fft_input()
    # test for correct type of DataFrame
    assert isinstance(analysis.Statistical_Analysis.correlation(analysis.Numerical_Analysis,
                                                                         df, label), pd.DataFrame)

    assert analysis.Statistical_Analysis.correlation(
        analysis.Numerical_Analysis, df, label).columns.tolist() == ["freq", "intensitys"]


def test_eucl_distance():
    """This tests verifys, that the output of eucl_distance is of the correct type and format
    """
    df, label = get_data_frame_fft_input()
    # test for correct type of DataFrame
    assert isinstance(analysis.Statistical_Analysis.eucl_distance(analysis.Numerical_Analysis,
                                                                         df, label), pd.DataFrame)

    assert analysis.Statistical_Analysis.eucl_distance(
        analysis.Numerical_Analysis, df, label).columns.tolist() == ["freq", "intensitys"]
