import pytest

xfail = pytest.mark.xfail("my_downstream_thing")

xfail_params = {
    "test_a.py::test_param_needs_mark[third]": pytest.param(
        "False, 0", id="third", marks=pytest.mark.xfail("nope")
    )
}

from upstream.a_upstream import *

test_that_fails_downstream = pytest.mark.xfail()(test_that_fails_downstream)
