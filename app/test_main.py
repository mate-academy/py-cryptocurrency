import pytest
from unittest.mock import patch

import app.main as main


def _run_with_factor(current_rate: float, factor: float) -> str:
    """Pomocniczo: uruchom funkcję z zamockowaną prognozą =
    current_rate * factor."""
    with patch("app.main.get_exchange_rate_prediction",
               return_value=current_rate * factor):
        return main.cryptocurrency_action(current_rate)


def test_buy_more_when_prediction_is_more_than_5_percent_higher() -> None:
    """> 5% w górę ⇒ 'Buy more cryptocurrency'."""
    current = 100.0
    # 5.1% wzrost
    assert _run_with_factor(current, 1.051) == "Buy more cryptocurrency"


def test_sell_all_when_prediction_is_more_than_5_percent_lower() -> None:
    """> 5% w dół ⇒ 'Sell all your cryptocurrency'."""
    current = 200.0
    # 5.1% spadek
    assert _run_with_factor(current, 0.949) == "Sell all your cryptocurrency"


@pytest.mark.parametrize("factor", [1.00, 1.05, 0.95])
def test_do_nothing_on_boundary_and_small_changes(factor: float) -> None:
    """
    Dokładnie +5%, dokładnie -5% oraz brak zmiany ⇒ 'Do nothing',
    bo warunek w treści mówi o 'więcej niż 5%' (strictly more than).
    """
    current = 123.45
    assert _run_with_factor(current, factor) == "Do nothing"
