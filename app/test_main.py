from unittest import mock
from unittest.mock import MagicMock

from app.main import cryptocurrency_action


@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action(
        mocked_exchange_rate_prediction: MagicMock
) -> None:
    mocked_exchange_rate_prediction.return_value = 10
    assert cryptocurrency_action(10) == "Do nothing"
    assert cryptocurrency_action(100) == "Sell all your cryptocurrency"
    assert cryptocurrency_action(5) == "Buy more cryptocurrency"
    assert cryptocurrency_action(10.5) == "Do nothing"
    assert cryptocurrency_action(9.5) == "Do nothing"
