from unittest import mock
from app.main import cryptocurrency_action


@mock.patch("app.main.get_exchange_rate_prediction")
def test_crypto_action_buy(
        mock_exchange_rate: mock.MagicMock
) -> None:
    mock_exchange_rate.return_value = 110

    result = cryptocurrency_action(100)

    assert result == "Buy more cryptocurrency"
    mock_exchange_rate.assert_called_once_with(100)


@mock.patch("app.main.get_exchange_rate_prediction")
def test_crypto_action_sell(
        mock_exchange_rate: mock.MagicMock
) -> None:
    mock_exchange_rate.return_value = 100

    result = cryptocurrency_action(110)

    assert result == "Sell all your cryptocurrency"
    mock_exchange_rate.assert_called_once_with(110)


@mock.patch("app.main.get_exchange_rate_prediction")
def test_crypto_action_0_95(
        mock_exchange_rate: mock.MagicMock
) -> None:
    mock_exchange_rate.return_value = 100

    result = cryptocurrency_action(95)

    assert result == "Do nothing"
    mock_exchange_rate.assert_called_once_with(95)


@mock.patch("app.main.get_exchange_rate_prediction")
def test_crypto_action_1_05(
        mock_exchange_rate: mock.MagicMock
) -> None:
    mock_exchange_rate.return_value = 100

    result = cryptocurrency_action(105)

    assert result == "Do nothing"
    mock_exchange_rate.assert_called_once_with(105)
