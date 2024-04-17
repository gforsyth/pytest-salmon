# Idea:

For upstream tests that pass, already covered by `import *`

For upstream tests that we need to mark, import them, manually decorate.

```python
test_that_fails_downstream = pytest.mark.xfail()(test_that_fails_downstream)
```

Tricky bit is xfail marks inside parameterized tests:

If we can state safely (enough) that all parametrized tests of note have IDs (well, they all do, but some would be numbered):

dictionary of 
nodeid : `pytest.Param(param, values, id="same_as_upstream", marks=theseus_marker)`

then we mutate the tests on collection and for a given nodeid, if there's a param with a matching id, we replace it.

