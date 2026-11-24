from unittest import mock

import pytest

from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "prediction, expected",
    [
        (120, "Buy more cryptocurrency"),
        (105.01, "Buy more cryptocurrency"),
        (105, "Do nothing"),
        (100, "Do nothing"),
        (95, "Do nothing"),
        (94.99, "Sell all your cryptocurrency"),
        (80, "Sell all your cryptocurrency"),
    ],
)
@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action_depends_on_predicted_rate(
        mocked_prediction: mock.MagicMock,
        prediction: float,
        expected: str,
) -> None:
    mocked_prediction.return_value = prediction
    assert cryptocurrency_action(100) == expected


@mock.patch("app.main.get_exchange_rate_prediction")
def test_should_pass_current_rate_to_prediction(
        mocked_prediction: mock.MagicMock,
) -> None:
    mocked_prediction.return_value = 100
    cryptocurrency_action(100)
    mocked_prediction.assert_called_once_with(100)
