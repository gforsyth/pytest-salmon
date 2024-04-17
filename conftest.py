import pytest

from test_a import xfail_params


def pytest_runtest_setup(item: pytest.Item) -> None:
    if (patch_param := xfail_params.get(item.nodeid)) is not None:
        new_params = []
        for mark in item.iter_markers():
            if mark.name == "parametrize":
                for param in mark.args[1]:
                    if param.id != patch_param.id:
                        new_params.append(param)
                    else:
                        new_params.append(patch_param)

                patch_mark = pytest.Mark(
                    mark.name, (mark.args[0], new_params), mark.kwargs
                )
                item.own_markers.remove(mark)
                item.add_marker(pytest.MarkDecorator(patch_mark))
