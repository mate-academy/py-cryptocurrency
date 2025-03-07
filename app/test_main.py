from unittest import mock
from unittest.mock import MagicMock, patch
import app.main
import pytest



@pytest.mark.parametrize("prediction, current_rate, expectation",
                         [
                             (200, 100, "Buy more cryptocurrency"),
                             (106, 100, "Buy more cryptocurrency"),
                             (94, 100, "Sell all your cryptocurrency"),
                             (95, 100, "Do nothing"),
                             (105, 100, "Do nothing"),
                             (100, 120, "Sell all your cryptocurrency")
                         ],
                         ids=[
                             "Prediction more bigger than current",
                             "Prediction is slightly bigger than current",
                             "Prediction is slightly less than current",
                             "prediction_rate / current_rate = 0.95",
                             "prediction_rate / current_rate = 1.05",
                             "Current more than prediction"
                         ]
                         )
@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action(mocked_get_exchange: MagicMock,
                               prediction: int | float,
                               current_rate: int | float,
                               expectation: str,
                               ) -> None:
    mocked_get_exchange.return_value = prediction
    assert app.main.cryptocurrency_action(current_rate) == expectation


