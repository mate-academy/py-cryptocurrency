from unittest.mock import patch
from app.main import cryptocurrency_action


@patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action_buy(mock_prediction: any) -> None:
    # Caso 1: Predicción sube un 10% ( > 5%)
    mock_prediction.return_value = 110
    assert cryptocurrency_action(100) == "Buy more cryptocurrency"


@patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action_sell(mock_prediction: any) -> None:
    # Caso 2: Predicción baja un 10% ( < -5%)
    mock_prediction.return_value = 90
    assert cryptocurrency_action(100) == "Sell all your cryptocurrency"


@patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action_do_nothing(mock_prediction: any) -> None:
    # Caso 3: Predicción sube solo un 2% ( <= 5%)
    mock_prediction.return_value = 102
    assert cryptocurrency_action(100) == "Do nothing"


@patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action_boundary_buy(mock_prediction: any) -> None:
    # Caso Límite: Exactamente 5% arriba no debería disparar la compra
    # (El requisito dice "more than 5%")
    mock_prediction.return_value = 105
    assert cryptocurrency_action(100) == "Do nothing"


@patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action_boundary_sell(mock_prediction: any) -> None:
    # Caso Límite: Exactamente 5% abajo no debería disparar la venta
    mock_prediction.return_value = 95
    assert cryptocurrency_action(100) == "Do nothing"
