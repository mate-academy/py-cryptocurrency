import pytest

from unittest import mock

from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "exchange_rate,prediction,expected_response",
    [
        pytest.param(
            100, 120, "Buy more cryptocurrency",
            id="Should return 'Buy more cryptocurrency'"
        ),
        pytest.param(
            100, 80, "Sell all your cryptocurrency",
            id="Should return 'Sell all your cryptocurrency'"
        ),
        pytest.param(
            100, 105, "Do nothing",
            id="Should return 'Do nothing'"
        ),
        pytest.param(
            100, 95, "Do nothing",
            id="Should return 'Do nothing'"
        )
    ]
)
@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action(
        mocked_get_exchange_rate_prediction: mock.MagicMock,
        exchange_rate: int | float,
        prediction: float,
        expected_response: str
) -> None:
    mocked_get_exchange_rate_prediction.return_value = prediction
    assert cryptocurrency_action(exchange_rate) == expected_response
