from unittest import mock
from unittest.mock import MagicMock

import pytest

from app.main import cryptocurrency_action


@pytest.mark.parametrize("predict, advice",
                         [
                             (1.06, "Buy more cryptocurrency"),
                             (0.94, "Sell all your cryptocurrency"),
                             (1, "Do nothing"),
                         ]
                         )
@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action(
        mock_prediction: MagicMock,
        predict: int | float,
        advice: str) -> None:
    mock_prediction.return_value = predict
    assert cryptocurrency_action(1) == advice

