from unittest.mock import patch, Mock
from pytest import mark
from app.main import cryptocurrency_action


@mark.parametrize(
    "current_rate, prediction_rate, expected_result",
    [
        (10, 10.5, "Do nothing"),
        (10, 9.5, "Do nothing"),
        (10, 12, "Buy more cryptocurrency"),
        (10.7, 11.9, "Buy more cryptocurrency"),
        (10, 9, "Sell all your cryptocurrency"),
        (11.49, 9.54, "Sell all your cryptocurrency"),
    ]
)
@patch("app.main.get_exchange_rate_prediction")
def test_should_return_correct_string(
        mocked_prediction: Mock,
        current_rate: int | float,
        prediction_rate: int | float,
        expected_result: str
) -> None:
    mocked_prediction.return_value = prediction_rate
    assert cryptocurrency_action(current_rate) == expected_result


@patch("app.main.get_exchange_rate_prediction")
def test_rate_prediction_function_was_called(mocked_prediction: Mock) -> None:
    mocked_prediction.return_value = 11
    cryptocurrency_action(10)
    mocked_prediction.assert_called_once_with(10)