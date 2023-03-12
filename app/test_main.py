from unittest import mock

import pytest

from app.main import cryptocurrency_action


@pytest.fixture()
def mocked_rate_prediction() -> mock:
    with mock.patch(
            "app.main.get_exchange_rate_prediction"
    ) as rate_prediction:
        rate_prediction.return_value = 0.95
        yield rate_prediction


def test_if_function_was_called(mocked_rate_prediction: mock) -> None:
    cryptocurrency_action(8000)
    mocked_rate_prediction.assert_called_with(8000)


def test_cryptocurrency_should_be_sold(mocked_rate_prediction: mock) -> None:
    current_rate = 8000
    mocked_rate_prediction.return_value = 7580
    assert cryptocurrency_action(current_rate) == \
           "Sell all your cryptocurrency"


def test_cryptocurrency_should_be_bought(mocked_rate_prediction: mock) -> None:
    current_rate = 8000
    mocked_rate_prediction.return_value = 8480
    assert cryptocurrency_action(current_rate) == "Buy more cryptocurrency"


def test_should_do_nothing_more_5(mocked_rate_prediction: mock) -> None:
    current_rate = 8000
    mocked_rate_prediction.return_value = 8400
    assert cryptocurrency_action(current_rate) == "Do nothing"


def test_should_do_nothing_less_5(mocked_rate_prediction: mock) -> None:
    current_rate = 8000
    mocked_rate_prediction.return_value = 7600
    assert cryptocurrency_action(current_rate) == "Do nothing"
