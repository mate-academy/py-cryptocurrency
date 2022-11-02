from unittest import mock, TestCase

from app.main import cryptocurrency_action


@mock.patch("app.main.random.random")
@mock.patch("app.main.random.choice")
class TestApp(TestCase):
    def test_cryptocurrency_action_buy_more(
            self, random_choice: str,
            random_mock: int,) -> None:
        random_choice.return_value = "decrease"
        random_mock.return_value = 1.05
        assert cryptocurrency_action(90) == "Buy more cryptocurrency"

    def test_cryptocurrency_action_sell_all(
            self, random_choice: str,
            random_mock: int, ) -> None:
        random_choice.return_value = "decrease"
        random_mock.return_value = 0.95
        assert cryptocurrency_action(90) == "Sell all your cryptocurrency"

    def test_cryptocurrency_action_do_nothing(
            self, random_choice: str,
            random_mock: int, ) -> None:
        random_choice.return_value = "increase"
        random_mock.return_value = 1
        assert cryptocurrency_action(90) == "Do nothing"
