from unittest import mock

import pytest

from app.main import cryptocurrency_action, get_exchange_rate_prediction


class TestGetExchangeRatePrediction:
    @pytest.fixture()
    def mock_random(self):
        with mock.patch("random.random") as mock_random:
            yield mock_random

    @pytest.fixture()
    def mock_choice(self):
        with mock.patch("random.choice") as mock_choice:
            yield mock_choice

    def test_get_exchange_rate_prediction_increase(self, mock_random, mock_choice):
        mock_random.return_value = 0.1
        mock_choice.return_value = "increase"

        assert get_exchange_rate_prediction(10) == 100

    def test_get_exchange_rate_prediction_decrease(self, mock_random, mock_choice):
        mock_random.return_value = 0.1
        mock_choice.return_value = "decrease"

        assert get_exchange_rate_prediction(10) == 1


class TestCryptoCurrencyAction:
    @pytest.fixture()
    def mock_rate_prediction(self):
        with mock.patch("app.main.get_exchange_rate_prediction") as mock_rate:
            yield mock_rate

    def test_buy_more(self, mock_rate_prediction):
        mock_rate_prediction.return_value = 106
        assert cryptocurrency_action(100) == "Buy more cryptocurrency"

    def test_sell_all(self, mock_rate_prediction):
        mock_rate_prediction.return_value = 100
        assert cryptocurrency_action(106) == "Sell all your cryptocurrency"

    def test_do_nothing(self, mock_rate_prediction):
        mock_rate_prediction.return_value = 100
        assert cryptocurrency_action(100) == "Do nothing"




