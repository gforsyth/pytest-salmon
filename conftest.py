import pytest

from test_a import xfail_params


def pytest_runtest_setup(item: pytest.Item) -> None:
    if (patch_marker := xfail_params.get(item.nodeid)) is not None:
        item.add_marker(patch_marker)
