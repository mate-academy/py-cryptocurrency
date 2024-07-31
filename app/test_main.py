from unittest import mock

import pytest

from app.main import cryptocurrency_action


@pytest.fixture
def mock_rate_prediction():
    with mock.patch("app.main.get_exchange_rate_prediction") as mocked_rate:
        yield mocked_rate


@pytest.mark.parametrize(
    "rate_prediction, current_rate, expected_result",
    [
        (2, 1, "Buy more cryptocurrency"),
        (21, 20, "Do nothing"),
        (1, 2, "Sell all your cryptocurrency"),
        (19, 20, "Do nothing"),
        (1, 1, "Do nothing")
    ]
)
def test_return_correct_prediction(
        mock_rate_prediction,
        rate_prediction,
        current_rate,
        expected_result
):
    mocked_rate = mock_rate_prediction
    mocked_rate.return_value = rate_prediction

    assert cryptocurrency_action(current_rate) == expected_result
