import pytest
from unittest import mock

from app import main


@pytest.fixture()
def mocked_prediction():
    with mock.patch("app.main.get_exchange_rate_prediction") as mocked_rate:
        yield mocked_rate


@pytest.mark.parametrize("current_rate,prediction_rate,expected_result",
                         [
                             (1, 1, "Do nothing"),
                             (1, 0.4, "Sell all your cryptocurrency"),
                             (1, 1.5, "Buy more cryptocurrency"),
                             (1, 0.95, "Do nothing"),
                             (1, 1.05, "Do nothing")
                         ]
                         )
def test_cryptocurrency_action(mocked_prediction,
                               current_rate,
                               prediction_rate,
                               expected_result):
    mocked_prediction.return_value = prediction_rate
    assert main.cryptocurrency_action(current_rate) == expected_result
