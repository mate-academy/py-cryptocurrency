from typing import Any
import pytest

import app.main as main


@pytest.mark.parametrize(
    "current_rate, predicted_rate, expected",
    [
        (100, 106, "Buy more cryptocurrency"),        # > 5% acima
        (100, 94, "Sell all your cryptocurrency"),   # > 5% abaixo
        (100, 105, "Do nothing"),                     # exatamente +5%
        (100, 95, "Do nothing"),                      # exatamente -5%
        (100, 100, "Do nothing"),                     # sem mudança
    ],
)
def test_cryptocurrency_action(
    monkeypatch: Any,
    current_rate: float,
    predicted_rate: float,
    expected: str,
) -> None:
    # simula a função de previsão
    monkeypatch.setattr(main, "get_exchange_rate_prediction", lambda: predicted_rate)

    result = main.cryptocurrency_action(current_rate)

    assert result == expected
