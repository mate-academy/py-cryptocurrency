from unittest import mock
from app.main import cryptocurrency_action


@mock.patch("app.main.random.choice", return_value="increase")
@mock.patch("app.main.random.random", return_value=0.8)
def test_if_random_choose_increase_and_0_dot_8(
        mocked_rate: float,
        mocked_choice: str) -> None:
    assert cryptocurrency_action(5) == "Buy more cryptocurrency"


@mock.patch("app.main.random.choice", return_value="decrease")
@mock.patch("app.main.random.random", return_value=0.8)
def test_if_random_choose_decrease_and_0_dot_8(
        mocked_rate: float,
        mocked_choice: str) -> None:
    assert cryptocurrency_action(5) == "Sell all your cryptocurrency"


@mock.patch("app.main.random.choice", return_value="increase")
@mock.patch("app.main.random.random", return_value=0.99)
def test_if_random_choose_increase_and_0_dot_99(
        mocked_rate: float,
        mocked_choice: int) -> None:
    assert cryptocurrency_action(5) == "Do nothing"


@mock.patch("app.main.prediction_rate / current_rate", return_value=1.05)
@mock.patch("app.main.random.choice", return_value="decrease")
@mock.patch("app.main.random.random", return_value=0.8)
def test_if_random_choose_increase_and_1_dot_05(
        mocked_rate: float,
        mocked_choice: str) -> None:
    assert cryptocurrency_action(5) == "Do nothing"
