from unittest import mock

import pytest

from app.main import cryptocurrency_action, get_exchange_rate_prediction


class TestGetExchangeRatePrediction:
    @pytest.fixture()
    def mock_random(self) -> object:
        with mock.patch("random.random") as mock_random:
            yield mock_random

    @pytest.fixture()
    def mock_choice(self) -> object:
        with mock.patch("random.choice") as mock_choice:
            yield mock_choice

    def test_get_exchange_rate_prediction_increase(
            self,
            mock_random: object,
            mock_choice: object
    ) -> None:
        mock_random.return_value = 0.1
        mock_choice.return_value = "increase"

        assert get_exchange_rate_prediction(10) == 100

    def test_get_exchange_rate_prediction_decrease(
            self,
            mock_random: object,
            mock_choice: object
    ) -> None:
        mock_random.return_value = 0.1
        mock_choice.return_value = "decrease"

        assert get_exchange_rate_prediction(10) == 1


class TestCryptoCurrencyAction:
    @pytest.fixture()
    def mock_rate_prediction(self) -> object:
        with mock.patch("app.main.get_exchange_rate_prediction") as mock_rate:
            yield mock_rate

    @pytest.mark.parametrize(
        "init_prediction, init_rate, error_str",
        [
            pytest.param(
                106,
                100,
                "Buy more cryptocurrency",
                id="test_buy_more"

            ),
            pytest.param(
                105,
                100,
                "Do nothing",
                id="test_not_buy_more"

            ),
            pytest.param(
                100,
                106,
                "Sell all your cryptocurrency",
                id="test_sell_all"

            ),
            pytest.param(
                95,
                100,
                "Do nothing",
                id="test_no_sell_all"

            ),
            pytest.param(
                100,
                100,
                "Do nothing",
                id="test_do_nothing"

            ),
        ]
    )
    def test_crypto_currency_action(self,
                                    init_prediction: int,
                                    init_rate: int,
                                    error_str: str,
                                    mock_rate_prediction: object) -> None:
        mock_rate_prediction.return_value = init_prediction
        assert cryptocurrency_action(init_rate) == error_str
