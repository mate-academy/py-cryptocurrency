from unittest import mock
from app.main import cryptocurrency_action
import pytest


@pytest.fixture(scope="module")
def mocked_prediction() -> None:
    with (
        mock.patch("app.main.get_exchange_rate_prediction")
        as mocked_test_prediction
    ):
        yield mocked_test_prediction


def test_prediction_function_was_called(
        mocked_prediction: mock.MagicMock
) -> None:
    mocked_prediction.return_value = 50
    cryptocurrency_action(40)
    print(type(mocked_prediction))
    mocked_prediction.assert_called_once_with(40)


def test_exchange_rate_five_percent_lower(
        mocked_prediction: mock.MagicMock
) -> None:

    assert cryptocurrency_action(100) == "Sell all your cryptocurrency"


def test_exchange_rate_five_percent_higher(
        mocked_prediction: mock.MagicMock
) -> None:

    assert cryptocurrency_action(30) == "Buy more cryptocurrency"


def test_exchange_rate_is_not_much_difference(
        mocked_prediction: mock.MagicMock
) -> None:

    assert cryptocurrency_action(49) == "Do nothing"


def test_rate_95_percent_do_nothing(
        mocked_prediction: mock.MagicMock
) -> None:
    mocked_prediction.return_value = 95

    assert cryptocurrency_action(100) == "Do nothing"


def test_rate_105_percent_do_nothing(
        mocked_prediction: mock.MagicMock
) -> None:
    mocked_prediction.return_value = 105

    assert cryptocurrency_action(100) == "Do nothing"
