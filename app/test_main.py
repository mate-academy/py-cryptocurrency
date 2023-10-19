from unittest.mock import patch, MagicMock

from app.main import cryptocurrency_action


@patch("app.main.get_exchange_rate_prediction")
def test_predicted_rate_equal_current(
    mocked_exchnage_rate: MagicMock
) -> None:
    mocked_exchnage_rate.return_value = 20
    assert cryptocurrency_action(20) == "Do nothing"


@patch("app.main.get_exchange_rate_prediction")
def test_predicted_rate_is_105_percent_of_current(
    mocked_exchnage_rate: MagicMock
) -> None:
    mocked_exchnage_rate.return_value = 21
    assert cryptocurrency_action(20) == "Do nothing"


@patch("app.main.get_exchange_rate_prediction")
def test_predicted_rate_is_95_percent_of_current(
    mocked_exchnage_rate: MagicMock
) -> None:
    mocked_exchnage_rate.return_value = 19
    assert cryptocurrency_action(20) == "Do nothing"


@patch("app.main.get_exchange_rate_prediction")
def test_predicted_rate_is_more_then_current(
    mocked_exchnage_rate: MagicMock
) -> None:
    mocked_exchnage_rate.return_value = 21.1
    assert cryptocurrency_action(20) == "Buy more cryptocurrency"


@patch("app.main.get_exchange_rate_prediction")
def test_predicted_rate_is_less_then_current(
    mocked_exchnage_rate: MagicMock
) -> None:
    mocked_exchnage_rate.return_value = 18.9
    assert cryptocurrency_action(20) == "Sell all your cryptocurrency"
