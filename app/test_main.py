import pytest
from unittest import mock
from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "prediction_rate,current_rate,expected",
    [
        pytest.param(
            1, 1, "Do nothing",
            id="Should return 'Do nothing' if rates are equal"
        ),
        pytest.param(
            1.05, 1, "Do nothing",
            id="Should return 'Do nothing' if "
               "prediction rate no more than the current one by 5%"
        ),
        pytest.param(
            0.95, 1, "Do nothing",
            id="Should return 'Do nothing' if "
               "prediction rate no less than the current one by 5%"
        ),
        pytest.param(
            0.94, 1, "Sell all your cryptocurrency",
            id="Should return 'Sell all your cryptocurrency' if "
               "prediction rate less than the current one by 5%"
        ),
        pytest.param(
            1.06, 1, "Buy more cryptocurrency",
            id="Should return 'Buy more cryptocurrency' if "
               "prediction rate more than the current one by 5%"
        )
    ]
)
@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action(
        mocked_get_exchange_rate_prediction: mock.MagicMock,
        prediction_rate: float | int,
        current_rate: float | int,
        expected: str
) -> None:
    mocked_get_exchange_rate_prediction.return_value = prediction_rate
    assert cryptocurrency_action(current_rate) == expected
