import pytest
import os
import analysis
import reader
import numpy as np 
import pandas as pd


def get_data_frame_fft_input():
    np_array = np.ones(50)
    my_label = "test_set"
    df = pd.DataFrame(np_array,columns=my_label)
    return df, my_label



def test_fft_with_freq_analysis():
    assert type(analysis.fft_with_freq_analysis(get_data_frame_fft_input())) == type(pd.Dateframe())