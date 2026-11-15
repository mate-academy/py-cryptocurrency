from unittest import mock

import pytest

from app import main


@pytest.mark.parametrize(
    "predicted_rate, expected_action",
    [
        (110, "Buy more cryptocurrency"),
        (105.01, "Buy more cryptocurrency"),
        (105, "Do nothing"),
        (100, "Do nothing"),
        (95, "Do nothing"),
        (94.99, "Sell all your cryptocurrency"),
        (90, "Sell all your cryptocurrency"),
    ],
)
@mock.patch("app.main.get_exchange_rate_prediction")
def test_action_depends_on_predicted_rate(
    mocked_prediction: mock.MagicMock,
    predicted_rate: float,
    expected_action: str,
) -> None:
    mocked_prediction.return_value = predicted_rate

    result = main.cryptocurrency_action(100)

    assert result == expected_action


@mock.patch("app.main.get_exchange_rate_prediction")
def test_prediction_is_requested_with_current_rate(
    mocked_prediction: mock.MagicMock,
) -> None:
    mocked_prediction.return_value = 100

    main.cryptocurrency_action(100)

    mocked_prediction.assert_called_once_with(100)
