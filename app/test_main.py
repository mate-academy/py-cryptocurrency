from unittest import mock

from app.main import cryptocurrency_action


def test_cryptocurrency_action() -> None:
    current_rate = 100
    with mock.patch("app.main.get_exchange_rate_prediction", return_value=95):
        assert cryptocurrency_action(current_rate) == "Do nothing"
        with mock.patch("app.main.get_exchange_rate_prediction",
                        return_value=105):
            assert cryptocurrency_action(current_rate) == "Do nothing"
    with mock.patch("app.main.get_exchange_rate_prediction", return_value=106):
        assert cryptocurrency_action(current_rate) == "Buy more cryptocurrency"
    with mock.patch("app.main.get_exchange_rate_prediction", return_value=94):
        assert cryptocurrency_action(current_rate) == ("Sell all your"
                                                       " cryptocurrency")
