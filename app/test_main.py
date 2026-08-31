from app import main
from unittest import mock


def test_cryptocurrency_action() -> None:
    with mock.patch("app.main.get_exchange_rate_prediction") as mock_predict:
        mock_predict.return_value = 106

        assert main.cryptocurrency_action(100) == "Buy more cryptocurrency"

    with mock.patch("app.main.get_exchange_rate_prediction") as mock_predict:
        mock_predict.return_value = 94

        assert (
            main.cryptocurrency_action(100)
            == "Sell all your cryptocurrency"
        )
    with mock.patch("app.main.get_exchange_rate_prediction") as mock_predict:
        mock_predict.return_value = 95

        assert main.cryptocurrency_action(100) == "Do nothing"

    with mock.patch("app.main.get_exchange_rate_prediction") as mock_predict:
        mock_predict.return_value = 105

        assert main.cryptocurrency_action(100) == "Do nothing"
