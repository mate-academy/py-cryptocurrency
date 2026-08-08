from unittest import mock
from unittest.mock import MagicMock
from app.main import cryptocurrency_action


@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action_over_1_05(mocked_prediction: MagicMock) -> None:
    mocked_prediction.return_value = 2.11

    assert cryptocurrency_action(2) == "Buy more cryptocurrency"

    mocked_prediction.assert_called_once_with(2)


@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action_under_0_95(
        mocked_prediction: MagicMock
) -> None:
    mocked_prediction.return_value = 1.89

    assert cryptocurrency_action(2) == "Sell all your cryptocurrency"

    mocked_prediction.assert_called_once_with(2)


@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action_between_0_95_and_1_05(
        mocked_prediction: MagicMock
) -> None:
    mocked_prediction.return_value = 2.02

    assert cryptocurrency_action(2) == "Do nothing"

    mocked_prediction.assert_called_once_with(2)


@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action_equal_1_05(
        mocked_prediction: MagicMock
) -> None:
    mocked_prediction.return_value = 2.10

    assert cryptocurrency_action(2) == "Do nothing"

    mocked_prediction.assert_called_once_with(2)


@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action_equal_0_95(
        mocked_prediction: MagicMock
) -> None:
    mocked_prediction.return_value = 1.90

    assert cryptocurrency_action(2) == "Do nothing"

    mocked_prediction.assert_called_once_with(2)
