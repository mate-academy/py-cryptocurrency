from pytest import fixture, mark
from unittest import mock

from app.main import cryptocurrency_action


@fixture()
def mocked_prediction() -> None:
    with (
        mock.patch("app.main.get_exchange_rate_prediction")
        as mocked_test_prediction
    ):

        yield mocked_test_prediction


@mark.parametrize(
    "predicted_rate,expected_decision",
    [
        (106, "Buy more cryptocurrency"),
        (94, "Sell all your cryptocurrency"),
        (105, "Do nothing"),
        (95, "Do nothing")
    ]
)
def test_if_function_works_correctly_with_different_rate(
        mocked_prediction: mock,
        predicted_rate: int,
        expected_decision: int
) -> None:
    mocked_prediction.return_value = predicted_rate
    decision = cryptocurrency_action(100)
    assert decision == expected_decision
