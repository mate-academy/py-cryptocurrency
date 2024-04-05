import pytest

from unittest import TestCase

from app.main import get_exchange_rate_prediction, cryptocurrency_action


class TestCrypto(TestCase):

    def setUp(self) -> None:
        self.exchange_rate = 2.6
        self.current_rate = 2

    def test_get_exchange_rate_prediction(self) -> None:
        assert isinstance(
            get_exchange_rate_prediction(self.exchange_rate),
            int | float
        )

    def test_get_current_rate_prediction_not_equal_to_the_past(self) -> None:
        assert (get_exchange_rate_prediction(self.exchange_rate)
                != self.exchange_rate)

    def test_crypto_sure_answer(self) -> None:
        prediction_rate = get_exchange_rate_prediction(self.exchange_rate)
        if prediction_rate / self.current_rate > 1.05:
            assert (cryptocurrency_action(self.current_rate)
                    == "Buy more cryptocurrency")
        elif prediction_rate / self.current_rate < 0.95:
            assert (cryptocurrency_action(self.current_rate)
                    == "Sell all your cryptocurrency"
                    )
        else:
            assert cryptocurrency_action(self.crypto_rate) == "Do nothing"

    @pytest.fixture()
    def mocked_random(self) -> None:
        with mock.patch(random.choice) as mock_test:
            yield mock_test
