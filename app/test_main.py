import pytest
from unittest import mock
from unittest.mock import MagicMock
from app.main import cryptocurrency_action


@mock.patch("app.main.get_exchange_rate_prediction")
class TestCryptocurrencyAction:
    @pytest.mark.parametrize(
        "current_rate,mock_exchange_rate,expected_result",
        [
            (50, 45, "Sell all your cryptocurrency"),
            (100, 106, "Buy more cryptocurrency"),
            (100, 100, "Do nothing"),
            (100, 105, "Do nothing"),
            (100, 95, "Do nothing")
        ],
        ids=[
            "sell when drops over five percent",
            "buy when rises over five persent",
            "do nothing when unchanged",
            "do nothing when at upper boundary",
            "do nothing when at lower boundary"
        ]
    )
    def test_cryptocurrency_action(
            self,
            mock_get_exchange_rate: MagicMock,
            current_rate: int | float,
            mock_exchange_rate: int | float,
            expected_result: str
    ) -> None:
        mock_get_exchange_rate.return_value = mock_exchange_rate
        result = cryptocurrency_action(current_rate)

        assert result == expected_result
