import pytest
from unittest import mock
from app.main import cryptocurrency_action


@pytest.fixture()
def mocked_rate() -> mock.MagicMock:
    with mock.patch("app.main.get_exchange_rate_prediction") as mocked_rate:
        yield mocked_rate


def test_rate_prediction_is_called(mocked_rate: mock.MagicMock) -> None:
    mocked_rate.return_value = 1.00
    cryptocurrency_action(1.00)
    mocked_rate.assert_called_once_with(1.00)


@pytest.mark.parametrize(
    "current_rate,predicted_rate,expected_result",
    [
        (2.00, 1, "Sell all your cryptocurrency"),
        (100.00, 80.00, "Sell all your cryptocurrency"),
        (1500, 5.00, "Sell all your cryptocurrency"),
        (1.00, 1.05, "Do nothing"),
        (5, 10, "Buy more cryptocurrency"),
        (1.00, 2.00, "Buy more cryptocurrency"),
        (0.5, 100, "Buy more cryptocurrency"),
        (8, 10, "Buy more cryptocurrency"),
        (20, 19, "Do nothing"),
        (155.55, 155.55, "Do nothing")
    ]
)
def test_func_get_correct_advise(
    mocked_rate: mock.MagicMock,
    current_rate: float | int,
    predicted_rate: float | int,
    expected_result: str
) -> None:
    mocked_rate.return_value = predicted_rate
    assert cryptocurrency_action(current_rate) == expected_result
