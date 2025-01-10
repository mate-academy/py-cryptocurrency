import pytest
from unittest.mock import patch
from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "current_rate, projected_course, expected_result",
    [
        pytest.param(100, 150, "Buy more cryptocurrency",
                     id="Rate increased by more than 5%"),
        pytest.param(50, 25, "Sell all your cryptocurrency",
                     id="The rate fell by more than 5%"),
        pytest.param(40, 41, "Do nothing",
                     id="nothing"),
    ]
)
def test_cryptocurrency_action(current_rate: int,
                               projected_course: int,
                               expected_result: str) -> None:
    with patch("app.main.get_exchange_rate_prediction",
               return_value=projected_course):
        result = cryptocurrency_action(current_rate)
        assert result == expected_result
