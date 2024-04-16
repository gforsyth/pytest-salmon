import pytest


def pytest_collection_modifyitems(session, config, items):
    breakpoint()
    matchexpr = config.option.markexpr
    if not matchexpr:
        return

    breakpoint()
    remaining = []
    deselected = []
    for colitem in items:
        if matchexpr:
            if eval(matchexpr, {}, Fauxcals(colitem.keywords)):
                # print "Deselecting %r (mark removed by @pytest.unmark)" % colitem
                deselected.append(colitem)
                continue
        remaining.append(colitem)

    if deselected:
        config.hook.pytest_deselected(items=deselected)
        items[:] = remaining
