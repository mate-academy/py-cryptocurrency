import pytest
from unittest import mock
from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "current_rate, prediction_rate, expected_result",
    [
        pytest.param(0.95, 1.0, "Buy more cryptocurrency",
                     id="predicted exchange rate is more than 5% "
                        "higher from the current"),
        pytest.param(0.93, 1.1, "Buy more cryptocurrency",
                     id="predicted exchange rate is more than 5% "
                        "igher from the current"),
        pytest.param(1.00, 0.95, "Do nothing",
                     id="difference is not that much"),
        pytest.param(1.00, 1.05, "Do nothing",
                     id="difference is not that much"),
        pytest.param(1.40, 1.1, "Sell all your cryptocurrency",
                     id="predicted exchange rate is more than 5% "
                        "lower from the current"),
        pytest.param(1.20, 1.0, "Sell all your cryptocurrency",
                     id="predicted exchange rate is more than 5% "
                        "lower from the current"),
    ]
)
@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action(
        mock_function: mock,
        current_rate: int,
        prediction_rate: int,
        expected_result: str
) -> None:
    mock_function.return_value = prediction_rate
    assert expected_result == cryptocurrency_action(current_rate)
