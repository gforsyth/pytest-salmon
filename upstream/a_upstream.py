import pytest
from pytest import param


def test_a():
    print("a")
    assert True


def test_raises():
    with pytest.raises(AssertionError):
        assert False


def test_that_fails_downstream():
    assert False


@pytest.mark.parametrize(
    "mybool, someint",
    [
        param(True, 1, id="first"),
        param(True, 2, id="second"),
        param(False, 0, id="third"),
    ],
)
def test_param_needs_mark(mybool, someint):
    assert mybool
