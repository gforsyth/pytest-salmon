import pytest

from upstream.a_upstream import *

notimpl = pytest.mark.xfail(reason="not implemented in backend")
notyet = pytest.mark.xfail(reason="not implemented upstream")

xfails = {
    "test_param_needs_mark[third]": notimpl,
    "test_param_needs_mark[4]": notyet,
    "test_that_fails_downstream": pytest.mark.xfail(),
}
