from unittest.mock import MagicMock

import pytest

from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "curent_rate, predicted_rate, expected_action",
    [
        (100.0, 110.0, "Buy more cryptocurrency"),
        (100.0, 105.0, "Do nothing"),
        (100.0, 95.0, "Do nothing"),
        (100.0, 90.0, "Sell all your cryptocurrency"),
        (100.0, 100.0, "Do nothing"),
    ],
)
def test_cryptocurrency_action_scenarios(
    monkeypatch: pytest.MonkeyPatch,
    curent_rate: int | float,
    predicted_rate: int | float,
    expected_action: str
) -> None:
    mock_get_exchange_rate_prediction = MagicMock(return_value=predicted_rate)

    monkeypatch.setattr(
        "app.main.get_exchange_rate_prediction",
        mock_get_exchange_rate_prediction
    )

    assert cryptocurrency_action(curent_rate) == expected_action
