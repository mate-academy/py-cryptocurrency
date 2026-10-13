from unittest import mock

from app.main import cryptocurrency_action


@mock.patch("app.main.get_exchange_rate_prediction")
def test_buy_more_cryptocurrency_when_rate_increases_more_than_5_percent(
    mocked_get_exchange_rate_prediction: mock.MagicMock,
) -> None:
    mocked_get_exchange_rate_prediction.return_value = 1.06
    assert cryptocurrency_action(1) == "Buy more cryptocurrency"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_sell_all_cryptocurrency_when_rate_decreases_more_than_5_percent(
    mocked_get_exchange_rate_prediction: mock.MagicMock,
) -> None:
    mocked_get_exchange_rate_prediction.return_value = 0.94
    assert cryptocurrency_action(1) == "Sell all your cryptocurrency"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_do_nothing_when_rate_increases_exactly_5_percent(
    mocked_get_exchange_rate_prediction: mock.MagicMock,
) -> None:
    mocked_get_exchange_rate_prediction.return_value = 1.05
    assert cryptocurrency_action(1) == "Do nothing"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_do_nothing_when_rate_decreases_exactly_5_percent(
    mocked_get_exchange_rate_prediction: mock.MagicMock,
) -> None:
    mocked_get_exchange_rate_prediction.return_value = 0.95
    assert cryptocurrency_action(1) == "Do nothing"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_do_nothing_when_rate_changes_less_than_5_percent(
    mocked_get_exchange_rate_prediction: mock.MagicMock,
) -> None:
    mocked_get_exchange_rate_prediction.return_value = 1.03
    assert cryptocurrency_action(1) == "Do nothing"
