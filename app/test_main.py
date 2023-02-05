from unittest import mock
from app.main import cryptocurrency_action
import pytest


@pytest.mark.parametrize(
    "prediction_rate, current_rate, result",
    [
        (1.05, 1, "Do nothing"),
        (0.95, 1, "Do nothing"),
        (1.2, 1, "Buy more cryptocurrency"),
        (0.85, 1, "Sell all your cryptocurrency")
    ]
)
@mock.patch("app.main.get_exchange_rate_prediction")
def test_mock_cryptocurrency_action(mocked_cryptocurrency_action,
                                    current_rate,
                                    prediction_rate,
                                    result):
    mocked_cryptocurrency_action.return_value = prediction_rate
    assert cryptocurrency_action(current_rate) == result


# @mock.patch("app.main.get_exchange_rate_prediction")
# def test_cryptocurrency_action(mock_cryptocurrency_action):
#     mock_cryptocurrency_action.return_value = 1.05
#     assert cryptocurrency_action(1) == "Do nothing"
#
#
# @mock.patch("app.main.get_exchange_rate_prediction")
# def test_cryptocurrency_action_1(mock_cryptocurrency_action):
#     mock_cryptocurrency_action.return_value = 0.95
#     assert cryptocurrency_action(1) == "Do nothing"
#
#
# @mock.patch("app.main.get_exchange_rate_prediction")
# def test_cryptocurrency_action_2(mock_cryptocurrency_action):
#     mock_cryptocurrency_action.return_value = 1.2
#     assert cryptocurrency_action(1) == "Buy more cryptocurrency"
#
#
# @mock.patch("app.main.get_exchange_rate_prediction")
# def test_cryptocurrency_action_3(mock_cryptocurrency_action):
#     mock_cryptocurrency_action.return_value = 0.85
#     assert cryptocurrency_action(1) == "Sell all your cryptocurrency"
