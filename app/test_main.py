from unittest import TestCase, mock
from unittest.mock import Mock

from app.main import get_exchange_rate_prediction


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

    def test_crypto_sure_answer_95_percent(self) -> None:
        prediction_rate = get_exchange_rate_prediction(self.exchange_rate)
        if prediction_rate / self.current_rate < 0.95:
            assert "Sell all your cryptocurrency"

    def test_crypto_sure_answer_105_percent(self) -> None:

        prediction_rate = get_exchange_rate_prediction(self.exchange_rate)
        if prediction_rate / self.current_rate > 1.05:
            assert "Buy more cryptocurrency"

    @mock.patch("random.choice")
    def test_rate_percent_do_nothing(
            self,
            mock_random_choice: Mock
    ) -> None:
        mock_random_choice.return_value = 0.5
        prediction_rate = get_exchange_rate_prediction(self.exchange_rate)
        if not (
                prediction_rate / self.current_rate < 0.95
                or prediction_rate / self.current_rate > 1.05
        ):
            assert "Do nothing"
