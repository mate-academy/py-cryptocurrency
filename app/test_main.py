import pytest
from unittest import mock

from app.main import cryptocurrency_action


class TestCryptocurrencyAction:
    @mock.patch("app.main.get_exchange_rate_prediction", return_value=19)
    def test_rate_95_do_nothing(
        self,
        mocked_rate_prediction: mock.MagicMock
    ) -> None:
        assert cryptocurrency_action(20) == "Do nothing"

    @mock.patch("app.main.get_exchange_rate_prediction", return_value=21)
    def test_rate_105_do_nothing(
        self,
        mocked_rate_prediction: mock.MagicMock
    ) -> None:
        assert cryptocurrency_action(20) == "Do nothing"

    @mock.patch("app.main.get_exchange_rate_prediction", return_value=47)
    def test_rate_94_sell_all_your_cryptocurrency(
        self,
        mocked_rate_prediction: mock.MagicMock
    ) -> None:
        assert cryptocurrency_action(50) == "Sell all your cryptocurrency"

    @mock.patch("app.main.get_exchange_rate_prediction", return_value=53)
    def test_rate_106_buy_more_cryptocurrency(
        self,
        mocked_rate_prediction: mock.MagicMock
    ) -> None:
        assert cryptocurrency_action(50) == "Buy more cryptocurrency"

    def test_when_current_rate_is_zero_should_raise_zero_division_error(
        self
    ) -> None:
        with pytest.raises(ZeroDivisionError):
            cryptocurrency_action(0)
