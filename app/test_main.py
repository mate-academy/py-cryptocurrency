import pytest
from unittest import mock
from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "exchange_rate, expected",
    [
        pytest.param(
            110, "Buy more cryptocurrency",
            id="should return 'Buy more cryptocurrency' if exchange_rate > 5%"
        ),
        pytest.param(
            90, "Sell all your cryptocurrency",
            id="should return 'Sell all your cryptocurrency' "
               "if exchange_rate < 5%"
        ),
        pytest.param(
            105, "Do nothing",
            id="should return 'Do nothing' if exchange_rate is 5%"
        ),
        pytest.param(
            95, "Do nothing",
            id="should return 'Do nothing' if exchange_rate is -5%"
        ),
        pytest.param(
            100, "Do nothing",
            id="should return 'Do nothing' if "
               "exchange_rate are between 5% and -5%"
        )
    ]
)
@mock.patch("app.main.get_exchange_rate_prediction")
def test_modify_cryptocurrency_action(
        mock_rate_prediction: type,
        exchange_rate: int,
        expected: str
) -> None:

    mock_rate_prediction.return_value = exchange_rate
    current_rate = 100
    result = cryptocurrency_action(current_rate)

    assert result == expected
