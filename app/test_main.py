from unittest.mock import MagicMock, patch

from app.main import cryptocurrency_action


@patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action_buy(mock_prediction: MagicMock) -> None:
    # Predicción mayor a 5% (ej. 106 / 100 = 1.06 > 1.05) -> Buy
    mock_prediction.return_value = 106.0
    result = cryptocurrency_action(100)
    assert result == "Buy more cryptocurrency"


@patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action_sell(mock_prediction: MagicMock) -> None:
    # Predicción menor a 5% (ej. 94 / 100 = 0.94 < 0.95) -> Sell
    mock_prediction.return_value = 94.0
    result = cryptocurrency_action(100)
    assert result == "Sell all your cryptocurrency"


@patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action_do_nothing(
    mock_prediction: MagicMock,
) -> None:
    # Dentro del rango permitido (ej. 101 / 100 = 1.01) -> Do nothing
    mock_prediction.return_value = 101.0
    result = cryptocurrency_action(100)
    assert result == "Do nothing"


@patch("app.main.get_exchange_rate_prediction")
def test_rate_105_percent_do_nothing(
    mock_prediction: MagicMock,
) -> None:
    # Caso límite exacto: 105 / 100 = 1.05 -> Do nothing (no debe comprar)
    mock_prediction.return_value = 105.0
    result = cryptocurrency_action(100)
    assert result == "Do nothing"


@patch("app.main.get_exchange_rate_prediction")
def test_rate_95_percent_do_nothing(
    mock_prediction: MagicMock,
) -> None:
    # Caso límite exacto: 95 / 100 = 0.95 -> Do nothing (no debe vender)
    mock_prediction.return_value = 95.0
    result = cryptocurrency_action(100)
    assert result == "Do nothing"
