import pytest
from unittest import mock
from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "current_rate, exchange_rate, result",
    [
        pytest.param(
            10,
            12,
            "Buy more cryptocurrency",
            id="predicted exchange rate is more than "
               "5% higher from the current"
        ),
        pytest.param(
            10,
            8,
            "Sell all your cryptocurrency",
            id="predicted exchange rate is more than "
               "5% lower from the current"
        ),
        pytest.param(
            10,
            10.3,
            "Do nothing",
            id="difference is not than 5% from the current"
        ),
        pytest.param(
            10,
            9.7,
            "Do nothing",
            id="difference is not than 5% from the current"
        )
    ]
)
@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action(
        mock_exchange_rate_prediction,
        current_rate,
        exchange_rate,
        result
):
    mock_exchange_rate_prediction.return_value = exchange_rate

    assert cryptocurrency_action(current_rate) == result
