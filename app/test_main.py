import pytest
from unittest import mock

from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "current_amount, prediction, expected_action",
    (
        pytest.param(
            100, 100,
            "Do nothing",
            id="stable"
        ),
        pytest.param(
            100, 95,
            "Do nothing",
            id="bottom border do nothing"
        ),
        pytest.param(
            100, 105,
            "Do nothing",
            id="top border do nothing"
        ),
        pytest.param(
            100, 105.00001,
            "Buy more cryptocurrency",
            id="bottom border buy"
        ),
        pytest.param(
            100, 1575.3,
            "Buy more cryptocurrency",
            id="huge growth buy"
        ),
        pytest.param(
            100, 94.99999,
            "Sell all your cryptocurrency",
            id="bottom border sell"
        ),
        pytest.param(
            100, 0.00001,
            "Sell all your cryptocurrency",
            id="huge recession sell"
        )
    )
)
def test_cryptocurrency_action(current_amount: int | float,
                               prediction: int | float,
                               expected_action: str) -> None:
    with (mock.patch("app.main.get_exchange_rate_prediction")
          as rate_change_prediction):
        rate_change_prediction.return_value = prediction
        assert cryptocurrency_action(current_amount) == expected_action
