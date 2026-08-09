import pytest
from unittest import mock

from app.main import cryptocurrency_action


class TestCryptoCurrencyAction:
    def test_should_check_non_rate_argument(self) -> None:
        with pytest.raises(TypeError):
            cryptocurrency_action(None)

    @pytest.mark.parametrize(
        "amount,coef",
        [
            pytest.param(
                18000,
                0.95,
                id="test without changes"
            ),
            pytest.param(
                18000,
                0.95,
                id="test 5% lower"
            ),
            pytest.param(
                18000,
                1.05,
                id="test 5% higher"
            )
        ]
    )
    @mock.patch("app.main.get_exchange_rate_prediction")
    def test_should_return_do_nothing(self,
                                      mocked_prediction: object,
                                      amount: float, coef: float) -> None:
        mocked_prediction.return_value = amount * coef
        expected = cryptocurrency_action(amount)
        mocked_prediction.assert_called_once_with(amount)
        assert expected == "Do nothing"

    @mock.patch("app.main.get_exchange_rate_prediction")
    def test_should_return_do_buy(self, mocked_prediction: object) -> None:
        mocked_prediction.return_value = 18000
        expected = cryptocurrency_action(18000)
        mocked_prediction.assert_called_once_with(18000)
        assert expected == "Do nothing"

    @mock.patch("app.main.get_exchange_rate_prediction")
    def test_should_return_buy(self, mocked_prediction: object) -> None:
        mocked_prediction.return_value = 18000 * 1.05 + 0.01
        expected = cryptocurrency_action(18000)
        mocked_prediction.assert_called_once_with(18000)
        assert expected == "Buy more cryptocurrency"

    @mock.patch("app.main.get_exchange_rate_prediction")
    def test_should_return_sell(self, mocked_prediction: object) -> None:
        mocked_prediction.return_value = 18000 * 0.95 - 0.01
        expected = cryptocurrency_action(18000)
        mocked_prediction.assert_called_once_with(18000)
        assert expected == "Sell all your cryptocurrency"
