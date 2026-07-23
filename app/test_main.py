from unittest import mock


from app.main import cryptocurrency_action


def test_the_test_should_be_returned_if_more_than_five_percent() -> None:
    with mock.patch("app.main.get_exchange_rate_prediction", return_value=10):
        assert cryptocurrency_action(5) == "Sell all your cryptocurrency"


def test_test_when_the_indicator_is_five_percent_lower() -> None:
    with mock.patch("app.main.get_exchange_rate_prediction", return_value=10):
        assert cryptocurrency_action(12) == "Buy more cryptocurrency"


def test_the_should_return_when_there_is_a_small_difference() -> None:
    with mock.patch("app.main.get_exchange_rate_prediction", return_value=10):
        assert cryptocurrency_action(10) == "Do nothing"
