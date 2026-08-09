import pytest
from unittest import mock

from app.main import cryptocurrency_action


@mock.patch("app.main.get_exchange_rate_prediction")
@pytest.mark.parametrize("current_rate,predicted_rate,expected_value",
                         [
                             (4.32,
                              16.02,
                              "Buy more cryptocurrency"),
                             (4.32,
                              1.32,
                              "Sell all your cryptocurrency"),
                             (1,
                              0.95,
                              "Do nothing"),
                             (1,
                              1.05,
                              "Do nothing")
                         ])
def test_crypto_action(mocked_get_exchange_rate_prediction: mock.MagicMock,
                       current_rate: int | float,
                       predicted_rate: int | float,
                       expected_value: str) -> None:
    mocked_get_exchange_rate_prediction.return_value = predicted_rate
    assert cryptocurrency_action(current_rate) == expected_value
