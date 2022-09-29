from unittest import mock

import pytest

from app.main import cryptocurrency_action


@pytest.fixture()
def mocked_rate():
    with mock.patch("app.main.get_exchange_rate_prediction") as mocked_rate:
        yield mocked_rate


@pytest.mark.parametrize(
    "current_rate, predicted_rate, expected_result",
    [
        (10, 16, "Buy more cryptocurrency"),
        (15, 8, "Sell all your cryptocurrency"),
        (10, 10.5, "Do nothing"),
        (22, 20.9, "Do nothing"),
        (45, 22, "Sell all your cryptocurrency"),
        (26, 25, "Do nothing"),
    ])
def test_returned_correct_values(mocked_rate,
                                 current_rate,
                                 predicted_rate,
                                 expected_result):
    mocked_rate.return_value = predicted_rate
    assert cryptocurrency_action(current_rate) == expected_result
