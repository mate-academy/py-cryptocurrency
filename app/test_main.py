from unittest import mock

import pytest

from app.main import cryptocurrency_action


class TestCryptocurrencyAction:
    @staticmethod
    @pytest.fixture
    def mocked_get_exchange_rate_predict() -> None:
        with (mock.patch("app.main.get_exchange_rate_prediction")
              as get_exchange_rate):
            yield get_exchange_rate

    @pytest.mark.parametrize(
        "exchange_rate,current_rate,result",
        [
            (120, 75, "Buy more cryptocurrency"),
            (21, 48, "Sell all your cryptocurrency"),
            (39, 39, "Do nothing"),
            (39 * 1.05, 39, "Do nothing"),
            (39 * 0.95, 39, "Do nothing"),
        ]
    )
    def test_cryptocurrency_action(self,
                                   exchange_rate: int,
                                   current_rate: int,
                                   result: str,
                                   mocked_get_exchange_rate_predict:
                                   mock.MagicMock)\
            -> None:
        mocked_get_exchange_rate_predict.return_value = exchange_rate
        assert cryptocurrency_action(current_rate) == result
