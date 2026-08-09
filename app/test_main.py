import pytest
from typing import Union
from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "current_rate, prediction_increase, prediction_decrease, expected_action",
    [
        (100.0, 105.1, 90.0, "Buy more cryptocurrency"),
        (100.0, 105.0, 95.0, "Do nothing"),
        (100.0, 110.0, 94.0, "Sell all your cryptocurrency"),
        (50.0, 52.6, 47.0, "Buy more cryptocurrency"),
        (50.0, 52.0, 48.0, "Do nothing"),
        (50.0, 55.0, 47.4, "Sell all your cryptocurrency"),
        (1000.0, 1050.1, 949.9, "Buy more cryptocurrency"),
        (1000.0, 1040.0, 960.0, "Do nothing"),
        (1000.0, 1100.0, 949.0, "Sell all your cryptocurrency"),
        (0.1, 0.106, 0.09, "Buy more cryptocurrency"),
        (0.1, 0.104, 0.096, "Do nothing"),
        (0.1, 0.11, 0.08, "Sell all your cryptocurrency"),
    ],
)
def test_cryptocurrency_action(
    current_rate: float,
    prediction_increase: float,
    prediction_decrease: float,
    expected_action: str,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    def mock_get_exchange_rate_prediction_increase(
            rate: Union[int, float]
    ) -> float:
        return prediction_increase

    def mock_get_exchange_rate_prediction_decrease(
            rate: Union[int, float]
    ) -> float:
        return prediction_decrease

    monkeypatch.setattr(
        "app.main.get_exchange_rate_prediction",
        mock_get_exchange_rate_prediction_increase
    )
    if expected_action == "Buy more cryptocurrency":
        assert cryptocurrency_action(current_rate) == expected_action

    monkeypatch.setattr(
        "app.main.get_exchange_rate_prediction",
        mock_get_exchange_rate_prediction_decrease
    )
    if expected_action == "Sell all your cryptocurrency":
        assert cryptocurrency_action(current_rate) == expected_action

    monkeypatch.setattr(
        "app.main.get_exchange_rate_prediction",
        mock_get_exchange_rate_prediction_increase
    )
    if (expected_action == "Do nothing"
            and prediction_increase / current_rate <= 1.05):
        assert cryptocurrency_action(current_rate) == expected_action

    monkeypatch.setattr(
        "app.main.get_exchange_rate_prediction",
        mock_get_exchange_rate_prediction_decrease
    )
    if (expected_action == "Do nothing"
            and prediction_decrease / current_rate >= 0.95):
        assert cryptocurrency_action(current_rate) == expected_action
