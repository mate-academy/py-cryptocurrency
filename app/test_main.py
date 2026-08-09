from unittest.mock import patch

from app.main import cryptocurrency_action


def _call_with_mocked_prediction(
    current_rate: int | float,
    prediction_rate: int | float,
) -> str:
    with patch(
        "app.main.get_exchange_rate_prediction",
        return_value=prediction_rate,
    ):
        return cryptocurrency_action(current_rate)


def test_buy_more_when_prediction_greater_than_5_percent() -> None:
    assert (
        _call_with_mocked_prediction(100, 106)
        == "Buy more cryptocurrency"
    )


def test_do_nothing_when_prediction_exactly_5_percent_higher() -> None:
    assert _call_with_mocked_prediction(100, 105) == "Do nothing"


def test_do_nothing_when_prediction_between_minus5_and_plus5() -> None:
    assert _call_with_mocked_prediction(100, 99) == "Do nothing"


def test_do_nothing_when_prediction_exactly_5_percent_lower() -> None:
    assert _call_with_mocked_prediction(100, 95) == "Do nothing"


def test_sell_all_when_prediction_less_than_5_percent() -> None:
    assert (
        _call_with_mocked_prediction(100, 94)
        == "Sell all your cryptocurrency"
    )
