from unittest import mock

from app.main import cryptocurrency_action


@mock.patch("app.main.get_exchange_rate_prediction")
def test_buy_more_cryptocurrency(
    mocked_prediction: mock.MagicMock,
) -> None:
    mocked_prediction.return_value = 106.0
    assert cryptocurrency_action(100) == "Buy more cryptocurrency"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_sell_all_cryptocurrency(
    mocked_prediction: mock.MagicMock,
) -> None:
    mocked_prediction.return_value = 94.0
    assert cryptocurrency_action(100) == "Sell all your cryptocurrency"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_do_nothing_when_rate_unchanged(
    mocked_prediction: mock.MagicMock,
) -> None:
    mocked_prediction.return_value = 100.0
    assert cryptocurrency_action(100) == "Do nothing"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_do_nothing_when_rate_exactly_105_percent(
    mocked_prediction: mock.MagicMock,
) -> None:
    mocked_prediction.return_value = 105.0
    assert cryptocurrency_action(100) == "Do nothing"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_do_nothing_when_rate_exactly_95_percent(
    mocked_prediction: mock.MagicMock,
) -> None:
    mocked_prediction.return_value = 95.0
    assert cryptocurrency_action(100) == "Do nothing"
