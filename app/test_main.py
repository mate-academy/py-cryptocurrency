from unittest import mock

from app.main import cryptocurrency_action


def test_should_by_more() -> None:
    with (mock.patch("app.main.get_exchange_rate_prediction")
          as mocked_get_exchange_rate_prediction):
        mocked_get_exchange_rate_prediction.return_value = 54535.32

        assert cryptocurrency_action(51938.40) != "Buy more cryptocurrency"


def test_should_sell() -> None:
    with (mock.patch("app.main.get_exchange_rate_prediction")
          as mocked_get_exchange_rate_prediction):
        mocked_get_exchange_rate_prediction.return_value = 49341.48

        assert cryptocurrency_action(51938.40) == ("Sell "
                                                   "all your cryptocurrency")
