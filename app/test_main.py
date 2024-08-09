from unittest import mock


from app.main import cryptocurrency_action


@mock.patch("app.main.random.choice")
@mock.patch("app.main.get_exchange_rate_prediction")
def test_advice_sell(
        mocked_get_exchange_rate_prediction: float,
        mocked_random_choice: str) -> None:
    mocked_random_choice.return_value = "decrease"
    mocked_get_exchange_rate_prediction.return_value = 0.9 * 5
    assert cryptocurrency_action(5) == "Sell all your cryptocurrency"


@mock.patch("app.main.random.choice")
@mock.patch("app.main.get_exchange_rate_prediction")
def test_advice_do_nothing(
        mocked_get_exchange_rate_prediction: float,
        mocked_random_choice: str
) -> None:
    mocked_random_choice.return_value = "increase"
    mocked_get_exchange_rate_prediction.return_value = 1.05 * 85
    assert cryptocurrency_action(85) == "Do nothing"


@mock.patch("app.main.random.choice")
@mock.patch("app.main.get_exchange_rate_prediction")
def test_do_nothing(
        mocked_get_exchange_rate_prediction: float,
        mocked_random_choice: str
) -> None:
    mocked_random_choice.return_value = "increase"
    mocked_get_exchange_rate_prediction.return_value = 0.95 * 85
    assert cryptocurrency_action(85) == "Do nothing"


@mock.patch("app.main.random.choice")
@mock.patch("app.main.get_exchange_rate_prediction")
def test_advice_buy(
        mocked_get_exchange_rate_prediction: float,
        mocked_random_choice: str
) -> None:
    mocked_random_choice.return_value = "increase"
    mocked_get_exchange_rate_prediction.return_value = 1.1 * 85
    assert cryptocurrency_action(85) == "Buy more cryptocurrency"
