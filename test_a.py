import pytest

notimpl = pytest.mark.xfail(reason="not implemented in backend")
notyet = pytest.mark.xfail(reason="not implemented upstream")

xfail_params = {
    "test_a.py::test_param_needs_mark[third]": notimpl,
    "test_a.py::test_param_needs_mark[4]": notyet,
}

from upstream.a_upstream import *

test_that_fails_downstream = pytest.mark.xfail()(test_that_fails_downstream)
