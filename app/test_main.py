import pytest
from unittest import mock

from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "predicted_rate,expected_result",
    [
        (1.06, "Buy more cryptocurrency"),
        (1.05, "Do nothing"),
        (0.95, "Do nothing"),
        (0.94, "Sell all your cryptocurrency"),
    ]
)
@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action(
        mocked_prediction: object,
        predicted_rate: int | float,
        expected_result: int | float
) -> None:
    mocked_prediction.return_value = predicted_rate
    assert cryptocurrency_action(1) == expected_result


@pytest.mark.parametrize(
    "rate",
    [
        pytest.param("", id="string"),
        pytest.param([], id="list"),
        pytest.param({}, id="dictionary")
    ]
)
def test_type_error_exception(rate: int | float) -> None:
    with pytest.raises(TypeError):
        assert cryptocurrency_action(rate)
