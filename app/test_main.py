from unittest import mock
from app.main import cryptocurrency_action

@mock.patch('app.main.get_exchange_rate_prediction')
def test_cryptocurrency_action_buy_more(
        mocked_get_exchange_rate_prediction: mock.MagicMock) -> None:
    mocked_get_exchange_rate_prediction.return_value = 22
    assert cryptocurrency_action(20) == "Buy more cryptocurrency"
