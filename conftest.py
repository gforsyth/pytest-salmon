import re

import pytest

from test_a import xfails

TEST_NAME_IDS = re.compile(r"(.*)\[(?:(.*)-)*(.*)\]")


def pytest_runtest_setup(item: pytest.Item) -> None:
    if (patch_marker := xfails.get(item.originalname)) is not None:
        # This is the case where we have a parametrized test but we want to fail
        # ALL of them so the item.name might be
        # `test_corr_cov[no_cond-covar_pop]` but we need to check if
        # `test_corr_cov` by itself is a marker key
        item.add_marker(patch_marker)
    elif (patch_marker := xfails.get(item.name)) is not None:
        # This is the case where we have specified an exact test to fail, contra
        # to the previous condition, maybe we explicitly want to fail _only_
        # `test_corr_cov[no_cond-covar_pop]`.
        item.add_marker(patch_marker)
    else:
        # Finally, we may have specified a parameter to fail and want to mark
        # any test that it has been attached to via combination with other
        # parameters.
        # So for the test `test_corr_cov[no_cond-covar_pop]`, we may have specified
        # `test_corr_cov[covar_pop]` as a failure case. So we split out the 1+
        # parameter names and check them all in sequence
        for single_node_id in _unnest_node_ids(item.name):
            if (patch_marker := xfails.get(single_node_id)) is not None:
                item.add_marker(patch_marker)


def _unnest_node_ids(itemname: str) -> list[str]:
    match = re.match(TEST_NAME_IDS, itemname)
    if match is None:
        yield itemname
    else:
        test_name, *ids = match.groups()

        for _id in filter(None, ids):
            yield f"{test_name}[{_id}]"
