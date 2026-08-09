import pytest

from unittest.mock import patch, MagicMock

from app.main import cryptocurrency_action


class TestCryptocurrencyAction:
    @pytest.mark.parametrize(
        "current_rate, prediction_rate, expected",
        [
            pytest.param(
                100, 50., "Sell all your cryptocurrency",
                id="should sell when rate decreases by more than 5%"
            ),
            pytest.param(
                100, 94., "Sell all your cryptocurrency",
                id="should sell when rate decreases slightly over threshold"
            ),
            pytest.param(
                100, 95., "Do nothing",
                id="should do nothing at exactly 5% decrease"
            ),
            pytest.param(
                100., 100., "Do nothing",
                id="should do nothing when rate is unchanged"
            ),
            pytest.param(
                100, 105., "Do nothing",
                id="should do nothing at exactly 5% increase"
            ),

            pytest.param(
                100, 106., "Buy more cryptocurrency",
                id="should buy when rate increases slightly over threshold"
            ),
            pytest.param(
                100, 150., "Buy more cryptocurrency",
                id="should buy when rate increases significantly"
            ),
        ]
    )
    def test_should_provide_prediction_correctly(
            self,
            mock_prediction: MagicMock,
            current_rate: int | float,
            prediction_rate: float,
            expected: str
    ) -> None:

        mock_rate_prediction = mock_prediction
        mock_rate_prediction.return_value = prediction_rate

        assert cryptocurrency_action(current_rate) == expected

    def test_should_call__get_exchange_rate_prediction__correctly(
            self,
            mock_prediction: MagicMock
    ) -> None:
        mock_rate_prediction = mock_prediction
        mock_rate_prediction.return_value = 99

        cryptocurrency_action(100)
        mock_rate_prediction.assert_called_once_with(100)

    @pytest.fixture()
    def mock_prediction(self) -> MagicMock:
        with (patch("app.main.get_exchange_rate_prediction")
              as mock_rate_prediction):

            yield mock_rate_prediction
