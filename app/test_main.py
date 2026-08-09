import pytest
from unittest import mock
from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "current_rate, exchange_rate, action", [
        pytest.param(
            100,
            190,
            "Buy more cryptocurrency",
            id="should return buy when rate more then 5%"
        ),
        pytest.param(
            100,
            70,
            "Sell all your cryptocurrency",
            id="should return sell when rate less then 5%"
        ),
        pytest.param(
            100,
            105,
            "Do nothing",
            id="should return Do nothing when rate equal +5%"
        ),
        pytest.param(
            100,
            95,
            "Do nothing",
            id="should return Do nothing when rate equal -5%"
        )
    ]
)
@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action(
        mock_get_exchange_rate_prediction: int | float,
        current_rate: int | float,
        exchange_rate: int | float,
        action: str
) -> None:
    mock_get_exchange_rate_prediction.return_value = exchange_rate

    assert cryptocurrency_action(current_rate) == action
