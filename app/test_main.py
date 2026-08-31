from unittest import mock

import pytest

from app import main


@pytest.mark.parametrize(
    ("prediction_rate", "expected_action"),
    [
        (106, "Buy more cryptocurrency"),
        (105, "Do nothing"),
        (100, "Do nothing"),
        (95, "Do nothing"),
        (94, "Sell all your cryptocurrency"),
    ],
)
def test_cryptocurrency_action(
    prediction_rate: float,
    expected_action: str,
) -> None:
    current_rate = 100

    with mock.patch(
        "app.main.get_exchange_rate_prediction",
        return_value=prediction_rate,
    ) as mocked_prediction:
        result = main.cryptocurrency_action(current_rate)

    assert result == expected_action
    mocked_prediction.assert_called_once_with(current_rate)
