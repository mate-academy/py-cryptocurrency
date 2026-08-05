from unittest.mock import MagicMock, patch
import pytest

from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "current_rate, prediction_rate, expected_action",
    [
        pytest.param(
            100, 105.1, "Buy more cryptocurrency", id="buy_when_above_5_percent"
        ),
        pytest.param(
            100, 105.0, "Do nothing", id="do_nothing_when_exact_5_percent_increase"
        ),
        pytest.param(100, 100.0, "Do nothing", id="do_nothing_when_no_change"),
        pytest.param(
            100, 95.0, "Do nothing", id="do_nothing_when_exact_5_percent_decrease"
        ),
        pytest.param(
            100, 94.9, "Sell all your cryptocurrency", id="sell_when_below_5_percent"
        ),
    ],
)
@patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action(
    mock_prediction: MagicMock,
    current_rate: float,
    prediction_rate: float,
    expected_action: str,
) -> None:
    mock_prediction.return_value = prediction_rate

    # Викликаємо основну функцію
    result = cryptocurrency_action(current_rate)

    # Перевіряємо результат
    assert result == expected_action

    # Перевіряємо, чи викликався мок із правильним аргументом current_rate
    mock_prediction.assert_called_once_with(current_rate)
