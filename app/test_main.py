from unittest import mock

from app.main import cryptocurrency_action


@mock.patch("app.main.get_exchange_rate_prediction")
def test_buy_when_rate_is_more_than_five_percent_higher(
    mocked_prediction: mock.MagicMock,
) -> None:
    mocked_prediction.return_value = 106

    assert cryptocurrency_action(100) == "Buy more cryptocurrency"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_sell_when_rate_is_more_than_five_percent_lower(
    mocked_prediction: mock.MagicMock,
) -> None:
    mocked_prediction.return_value = 94

    assert cryptocurrency_action(100) == "Sell all your cryptocurrency"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_do_nothing_when_rate_is_unchanged(
    mocked_prediction: mock.MagicMock,
) -> None:
    mocked_prediction.return_value = 100

    assert cryptocurrency_action(100) == "Do nothing"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_do_nothing_at_exactly_five_percent_higher(
    mocked_prediction: mock.MagicMock,
) -> None:
    mocked_prediction.return_value = 105

    assert cryptocurrency_action(100) == "Do nothing"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_do_nothing_at_exactly_five_percent_lower(
    mocked_prediction: mock.MagicMock,
) -> None:
    mocked_prediction.return_value = 95

    assert cryptocurrency_action(100) == "Do nothing"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_do_nothing_within_five_percent(
    mocked_prediction: mock.MagicMock,
) -> None:
    mocked_prediction.return_value = 103

    assert cryptocurrency_action(100) == "Do nothing"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_prediction_is_called_with_current_rate(
    mocked_prediction: mock.MagicMock,
) -> None:
    mocked_prediction.return_value = 100

    cryptocurrency_action(200)

    mocked_prediction.assert_called_once_with(200)
