import pytest
from unittest import mock
from unittest.mock import MagicMock
from app.main import cryptocurrency_action


@mock.patch("app.main.get_exchange_rate_prediction")
@pytest.mark.parametrize("current_rate,return_value,expected_message",
                         [
                             (100,
                              125,
                              "Buy more cryptocurrency"),
                             (100,
                              50,
                              "Sell all your cryptocurrency"),
                             (100,
                              95,
                              "Do nothing"),
                             (100,
                              105,
                              "Do nothing")])
def test_should_return_correct_message(mocked_get_prediction: MagicMock,
                                       current_rate: int | float,
                                       return_value: int | float,
                                       expected_message: str,) -> None:
    mocked_get_prediction.return_value = return_value
    assert cryptocurrency_action(current_rate) == expected_message
