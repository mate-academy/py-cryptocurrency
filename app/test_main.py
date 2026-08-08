# write your code here
from unittest import mock

from app import main


@mock.patch("app.main.get_exchange_rate_prediction")
def test_should_by_crypto(
    mocked_prediction: mock.MagicMock
) -> None:
    mocked_prediction.return_value = 106
    assert main.cryptocurrency_action(100) == "Buy more cryptocurrency"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_should_not_by_crypto(
    mocked_prediction: mock.MagicMock
) -> None:
    mocked_prediction.return_value = 94
    assert main.cryptocurrency_action(100) == "Sell all your cryptocurrency"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_should_nothing_do(
    mocked_prediction: mock.MagicMock
) -> None:
    mocked_prediction.return_value = 103
    assert main.cryptocurrency_action(100) == "Do nothing"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_should_nothing_do_upper(
    mocked_prediction: mock.MagicMock
) -> None:
    mocked_prediction.return_value = 105
    assert main.cryptocurrency_action(100) == "Do nothing"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_should_nothing_do_lower(
    mocked_prediction: mock.MagicMock
) -> None:
    mocked_prediction.return_value = 95
    assert main.cryptocurrency_action(100) == "Do nothing"
