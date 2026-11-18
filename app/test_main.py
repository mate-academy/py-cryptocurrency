from typing import Union

import pytest

from app import main


@pytest.mark.parametrize(
    "current_rate,predicted_rate,expected_result",
    [
        (100, 105.01, "Buy more cryptocurrency"),
        (100, 105, "Do nothing"),
        (100, 104.99, "Do nothing"),
        (100, 100, "Do nothing"),
        (100, 95.01, "Do nothing"),
        (100, 95, "Do nothing"),
        (100, 94.99, "Sell all your cryptocurrency"),
    ],
)
def test_cryptocurrency_action(
        monkeypatch: pytest.MonkeyPatch,
        current_rate: Union[int, float],
        predicted_rate: float,
        expected_result: str,
) -> None:
    def mock_exchange_rate_prediction(
            exchange_rate: Union[int, float],
    ) -> float:
        return predicted_rate

    monkeypatch.setattr(
        main,
        "get_exchange_rate_prediction",
        mock_exchange_rate_prediction,
    )

    assert main.cryptocurrency_action(current_rate) == expected_result
