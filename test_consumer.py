from csv import DictReader

import pytest

from consumer import consume_invoices


@pytest.fixture
def invoices():
    with open("invoices.csv") as f:
        yield list(DictReader(f))


def test_empty_list():
    consume_invoices([])
