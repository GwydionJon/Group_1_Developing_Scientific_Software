import pytest
from reader import FileReader


@pytest.fixture
def create_temp_dir(tmp_path):
    # filename and directory constants
    sub_dir = "sub_dir/"
    fns = ['file1.txt', 'file2.csv', 'file3.t', 'file4.dat']

    # make sub directory in tmp for files
    tmp_path.mkdir(sub_dir)

    # create temporary files
    for fn in fns:
        fn_path = tmp_path / sub_dir + fn
        fn_path.touch()

    return tmp_path / sub_dir


@pytest.mark.reader
@pytest.mark.parametrize('dir_path, expected',
                         [
                             (),
                         ])
def test_FileReader(dir_path, expected):
