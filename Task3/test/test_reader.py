import pytest
from module_draft import reader

sub_dir = "sub_dir/"
fns = ['file1.txt', 'file2.csv', 'file3.t', 'file4.dat']


@pytest.fixture
def create_temp_dir(tmp_path, sub_dir, fns):
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
    pass
