import pytest
import os
from module_draft import reader


@pytest.fixture
def dir_filenames():
    return ['file1.txt', 'file2.csv', 'file3.t', 'file4.dat']


@pytest.fixture
def subdir_name():
    return "sub_dir/"


@pytest.fixture
def create_temp_dir(tmp_path, subdir_name, dir_filenames):
    """fixture to create temporary directory containing a subdir and files.

    Args:
        tmp_path (path obj): pytest fixture for temporary paths
        subdir_name (str): fixture providing subdir name as string
        dir_filenames ([str]): fixture providing list of strings with filenames

    Returns:
        tmp_dir (path obj): pointing to the temporary directory as created by
                            this fixture
    """
    # make sub directory in tmp for files
    tmp_dir = tmp_path / subdir_name
    tmp_dir.mkdir()
    # create temporary files
    for fn in dir_filenames:
        fn_path = tmp_dir / fn
        fn_path.touch()

    return tmp_dir


@pytest.fixture
def expected_dir_dict(create_temp_dir):
    """fixture to create expected output from the initiated temporary directory

    Args:
        create_temp_dir (path obj): fixture creating temporary dictionary with
                                    files for testing

    Returns:
        dir_dict (dict): dictionary with filenames as keys and paths as values
    """
    dir_dict = {}
    dir_path = create_temp_dir
    for path in os.listdir(dir_path):
        full_path = full_path = os.path.join(dir_path, path)
        if os.path.isfile(full_path):
            dir_dict[os.path.basename(full_path)] = full_path

    return dir_dict


@pytest.mark.reader
def test_FileReader(create_temp_dir, expected_dir_dict):
    """function to test FileReader init correctly gathering all filenames and
    paths in a dictionary.

    Args:
        create_temp_dir (path obj): fixture providing temporary directory
        expected_dir_dict (dict): fixture providing expected output
    """
    reader_obj = reader.FileReader(create_temp_dir)

    assert reader_obj.file_dict == expected_dir_dict
