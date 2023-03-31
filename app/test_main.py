import pytest


from unittest import mock


from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "prediction_rate,current_rate,exception_message",
    [
        pytest.param(
            1060,
            1000,
            "Buy more cryptocurrency"
        ),
        pytest.param(
            940,
            1000,
            "Sell all your cryptocurrency"
        ),
        pytest.param(
            950,
            1000,
            "Do nothing"
        ),
        pytest.param(
            1050,
            1000,
            "Do nothing"
        )
    ]
)
@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action_with_lower_rate(
        mocked_rate_prediction: callable,
        prediction_rate: float | int,
        current_rate: float | int,
        exception_message: str
) -> None:
    mocked_rate_prediction.return_value = prediction_rate
    assert cryptocurrency_action(current_rate) == exception_message
