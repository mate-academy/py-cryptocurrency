import pytest
from unittest import mock

from app.main import cryptocurrency_action


class TestPrediction:
    @pytest.mark.parametrize(
        "prediction, current, expected",
        [
            pytest.param(106, 100, "Buy more cryptocurrency"),
            pytest.param(105, 100, "Do nothing"),
            pytest.param(100, 100, "Do nothing"),
            pytest.param(95, 100, "Do nothing"),
            pytest.param(94, 100, "Sell all your cryptocurrency")
        ],
        ids=[
            "prediction coefficient > 1.05",
            "prediction coefficient = 1.05",
            "prediction coefficient = 1",
            "prediction coefficient = 0.95",
            "prediction coefficient < 0.95"
        ]
    )
    @mock.patch("app.main.get_exchange_rate_prediction")
    def test_cryptocurrency_action(
        self,
        mocked_rate_prediction: mock,
        prediction: int | float,
        current: int | float,
        expected: str
    ) -> None:
        mocked_rate_prediction.return_value = prediction

        assert cryptocurrency_action(current) == expected
