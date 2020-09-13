from typing import Iterable

import pytest

from uncertainties.var import Var


def assert_approx(got: Var, expected: Var) -> bool:
    got_value, got_uncertainty = (got.value, got.uncertainty) if isinstance(got, Var) else (got, 0)
    ex_value, ex_uncertainty = (expected.value, expected.uncertainty) if isinstance(expected, Var) else (expected, 0)
    assert (got_value, got_uncertainty) == pytest.approx((ex_value, ex_uncertainty))


def traverse(items):
    for item in items:
        if isinstance(item, Iterable):
            for value in traverse(item):
                yield value
        else:
            yield item
