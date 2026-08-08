import pytest
from unittest import mock
from .main import get_exchange_rate_prediction, cryptocurrency_action


@pytest.mark.parametrize(
    "exchange_rate, mock_choice, mock_random, expected_result",
    [
        (100, "increase", 0.5, round(100 / 0.5, 2)),
        (100, "decrease", 0.2, round(100 * 0.2, 2)),
    ],
    ids=[
        "increase_case",
        "decrease_case",
    ]
)
def test_get_exchange_rate_prediction(
        exchange_rate: int,
        mock_choice: str,
        mock_random: float,
        expected_result: float,
) -> None:
    with (mock.patch(
            "random.choice", return_value=mock_choice
    ), mock.patch(
        "random.random", return_value=mock_random
    )):
        result = get_exchange_rate_prediction(exchange_rate)

        assert result == expected_result, (f"Expected {expected_result}, "
                                           f"but it turned out {result}")


@pytest.mark.parametrize(
    "current_rate,prediction_rate,expected_result",
    [
        (100, 200, "Buy more cryptocurrency"),
        (100, 10, "Sell all your cryptocurrency"),
        (100, 99, "Do nothing"),
        (100, 101, "Do nothing"),
        (100, 95, "Do nothing"),
        (100, 105, "Do nothing"),
    ],
    ids=[
        "increase_case",
        "decrease_case",
        "normal_decrease_case",
        "normal_increase_case",
        "boundary_95_case",
        "boundary_105_case"
    ]
)
def test_cryptocurrency_action(
    current_rate: int,
    prediction_rate: int,
    expected_result: str
) -> None:
    with mock.patch(
            "app.main.get_exchange_rate_prediction",
            return_value=prediction_rate
    ):
        result = cryptocurrency_action(current_rate)

    assert result == expected_result, (f"Expected {expected_result}, "
                                       f"but it turned out {result}")
