from csv import DictReader

import pytest

from consumer import consume_invoices


@pytest.fixture
def invoices():
    with open("invoices.csv") as f:
        yield list(DictReader(f))


def test_empty_list():
    consume_invoices([])


def test_something_with_fixture(invoices):
    # this just a dummy test to show what the
    # invoices fixture does and how to use it
    assert len(invoices) == 11
    assert invoices[0] == {
        "amount": "1000",
        "due_date": "2019-10-20",
        "id": "1",
        "organisation_id": "1000",
        "paid_date": "2019-10-15",
        "raised_date": "2019-10-10",
        "status": "PAID",
    }
