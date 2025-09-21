# app/test_main.py
import pytest
import app.main as main
from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    ("current_rate", "predicted_rate", "expected"),
    [
        # > +5%  → Buy
        (100.0, 106.0, "Buy more cryptocurrency"),
        (200.0, 210.1, "Buy more cryptocurrency"),

        # < -5%  → Sell
        (100.0, 94.0, "Sell all your cryptocurrency"),
        (80.0, 75.9, "Sell all your cryptocurrency"),

        # Limites exatos (±5%) → Do nothing
        (100.0, 105.0, "Do nothing"),
        (100.0, 95.0, "Do nothing"),

        # Dentro da faixa → Do nothing
        (100.0, 104.99, "Do nothing"),
        (100.0, 95.01, "Do nothing"),
    ],
)
def test_cryptocurrency_action_with_mock(
    monkeypatch: pytest.MonkeyPatch,
    current_rate: float,
    predicted_rate: float,
    expected: str,
) -> None:
    """Mocka get_exchange_rate_prediction(current_rate) e testa a decisão."""
    def fake_prediction(_current: float) -> float:  # aceita o arg e ignora
        return predicted_rate

    monkeypatch.setattr(main, "get_exchange_rate_prediction", fake_prediction)
    assert cryptocurrency_action(current_rate) == expected
