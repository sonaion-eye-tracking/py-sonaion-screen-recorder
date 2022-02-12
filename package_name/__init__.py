from . import package_name_rs


def some_function(x):
    """
    Double the value of x by calling into the package_name_rs module.
    :param x: int
    :return:
    """
    return package_name_rs.py_some_function(x)
