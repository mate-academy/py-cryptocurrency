from unittest.mock import patch
import pytest

from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "current_rate,predicted_rate,expected_action",
    [
        # Caso 1: Taxa prevista > 5% acima da atual -> "Buy more cryptocurrency"
        (100.0, 105.1, "Buy more cryptocurrency"),
        (100.0, 110.0, "Buy more cryptocurrency"),
        
        # Caso 2: Taxa prevista exatamente 5% acima da atual -> "Do nothing" (limite)
        (100.0, 105.0, "Do nothing"),
        
        # Caso 3: Diferença entre -5% e +5% -> "Do nothing"
        (100.0, 104.9, "Do nothing"),
        (100.0, 100.0, "Do nothing"),
        (100.0, 95.1, "Do nothing"),
        
        # Caso 4: Taxa prevista exatamente 5% abaixo da atual -> "Do nothing" (limite)
        (100.0, 95.0, "Do nothing"),
        
        # Caso 5: Taxa prevista > 5% abaixo da atual -> "Sell all your cryptocurrency"
        (100.0, 94.9, "Sell all your cryptocurrency"),
        (100.0, 90.0, "Sell all your cryptocurrency"),
    ],
)
@patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action(
    mock_prediction,
    current_rate: float,
    predicted_rate: float,
    expected_action: str,
) -> None:
    mock_prediction.return_value = predicted_rate

    result = cryptocurrency_action(current_rate)

    assert result == expected_action
    mock_prediction.assert_called_once_with(current_rate)
