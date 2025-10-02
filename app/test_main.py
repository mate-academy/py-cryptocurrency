from .main import cryptocurrency_action
from pytest import mark
from unittest.mock import MagicMock, patch


@mark.parametrize([
    "current_rate", "prediction", "result"
], [
    (4, 2, "Sell all your cryptocurrency"),
    (2, 5, "Buy more cryptocurrency"),
    (5, 5.2, "Do nothing"),
])
@patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_acton_logic(
    mock_prediction: MagicMock,
    current_rate: int,
    prediction: int,
    result: str
) -> None:
    mock_prediction.return_value = prediction
    assert cryptocurrency_action(current_rate) == result
    mock_prediction.assert_called_once_with(current_rate)
