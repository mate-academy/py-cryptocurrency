from unittest import mock

import pytest

from app.main import cryptocurrency_action


class TestCryptocurrencyAction:
    @pytest.mark.parametrize(
        "interest,result",
        [
            (1.06, "Buy more cryptocurrency"),
            (0.94, "Sell all your cryptocurrency"),
            (1, "Do nothing"),
            (1.05, "Do nothing"),
            (0.95, "Do nothing")
        ]
    )
    @mock.patch("app.main.get_exchange_rate_prediction")
    def test_cryptocurrency_action(
        self,
        mock_get_exchange: mock.MagicMock,
        interest: int | float,
        result: str
    ) -> None:
        mock_get_exchange.return_value = interest
        assert cryptocurrency_action(1) == result
