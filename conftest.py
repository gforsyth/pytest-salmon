import pytest

from test_a import xfail_params


def pytest_runtest_setup(item: pytest.Item) -> None:
    if (patch_param := xfail_params.get(item.nodeid)) is not None:
        new_params = []
        for i, mark in enumerate(item.own_markers):
            if mark.name == "parametrize":
                index = i
        mark = item.own_markers[index]
        for param in mark.args[1]:
            if param.id != patch_param.id:
                new_params.append(param)
            else:
                new_params.append(patch_param)

        patch_mark = pytest.Mark(mark.name, (mark.args[0], new_params), mark.kwargs)
        item.own_markers.pop(index)
        item.add_marker(pytest.MarkDecorator(patch_mark))
