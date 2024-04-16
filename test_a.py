import pytest

from upstream.a_upstream import *

test_that_fails_downstream = pytest.mark.xfail()(test_that_fails_downstream)
