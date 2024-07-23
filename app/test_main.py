import pytest

from unittest import mock
from app.main import cryptocurrency_action


class TestCryptoCurrencyAction:
    @pytest.mark.parametrize(
        "predicted_rate,expected_action",
        [
            (1.06, "Buy more cryptocurrency"),
            (0.94, "Sell all your cryptocurrency"),
            (0.95, "Do nothing"),
            (1.05, "Do nothing"),
        ],
        ids=["Buy more(1.06)",
             "Sell all(0.94)",
             "Do nothing(0.95)",
             "Do nothing(0.95)"
             ]
    )
    @mock.patch("app.main.get_exchange_rate_prediction")
    def test_action(self,
                    mocked_exchange_rate_prediction: mock,
                    predicted_rate: int | float,
                    expected_action: str) -> None:
        mocked_exchange_rate_prediction.return_value = predicted_rate
        assert cryptocurrency_action(1) == expected_action
