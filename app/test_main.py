from unittest import mock
import pytest
from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "exchange_rate_prediction, expected",
    [
        pytest.param(
            95,
            "Do nothing",
            id="should do nothing if rate 95 percent"
        ),
        pytest.param(
            105,
            "Do nothing",
            id="should do nothing if rate 105 percent"
        ),
        pytest.param(
            110,
            "Buy more cryptocurrency",
            id="should buy more if rate > 105 percent"
        ),
        pytest.param(
            90,
            "Sell all your cryptocurrency",
            id="should sell all if rate < 95 percent"
        )
    ]
)
@mock.patch("app.main.get_exchange_rate_prediction")
def test_correct_action(
        mocked_prediction: mock.MagicMock,
        exchange_rate_prediction: int,
        expected: str
) -> None:
    mocked_prediction.return_value = exchange_rate_prediction
    assert cryptocurrency_action(100) == expected
