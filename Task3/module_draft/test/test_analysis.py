import pytest
# import os
import analysis
# import reader
import numpy as np
import pandas as pd

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
