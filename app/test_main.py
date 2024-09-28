from unittest import mock

from app.main import cryptocurrency_action


def test_should_by_more() -> None:
    with (mock.patch("app.main.get_exchange_rate_prediction")
          as mocked_get_exchange_rate_prediction):
        mocked_get_exchange_rate_prediction.return_value = 54600.48

        assert cryptocurrency_action(51938.40) == "Buy more cryptocurrency"


def test_should_sell() -> None:
    with (mock.patch("app.main.get_exchange_rate_prediction")
          as mocked_get_exchange_rate_prediction):
        mocked_get_exchange_rate_prediction.return_value = 41550.72

        assert cryptocurrency_action(51938.40) == ("Sell "
                                                   "all your cryptocurrency")


def test_should_do_nothing_with_rate_105() -> None:
    with (mock.patch("app.main.get_exchange_rate_prediction")
          as mocked_get_exchange_rate_prediction):
        mocked_get_exchange_rate_prediction.return_value = 54535.32

        assert cryptocurrency_action(51938.40) == "Do nothing"


def test_should_do_nothing_with_rate_95() -> None:
    with (mock.patch("app.main.get_exchange_rate_prediction")
          as mocked_get_exchange_rate_prediction):
        mocked_get_exchange_rate_prediction.return_value = 1.9

        assert cryptocurrency_action(2) == "Do nothing"
