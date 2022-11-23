import pytest
from app.main import get_exchange_rate_prediction, cryptocurrency_action


class TestCryptoClass:
    @pytest.mark.parametrize(
        "current_rate,prediction_rate,action",
        [
            (1.4, 1.2, "Sell all your cryptocurrency"),
            (1.4, 1.6, "Buy more cryptocurrency"),
            (1.4, 1.4, "Do nothing"),
        ],
    )
    def test_matecoin(self, current_rate: int,
                      prediction_rate: int,
                      action: str) -> None:
        def mock_rate() -> None:

            mock_rate.predict = get_exchange_rate_prediction(prediction_rate)

            assert cryptocurrency_action(mock_rate.predict) == action
