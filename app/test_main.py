import pytest
from unittest.mock import patch
from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "mocked_course, result",
    [
        (3, "Buy more cryptocurrency"),
        (1, "Sell all your cryptocurrency"),
        (2.1, "Do nothing"),
        (1.9, "Do nothing")
    ]
)
def test_cryptocurrency_action(mocked_course: int, result: str) -> None:
    with patch("app.main.get_exchange_rate_prediction",
               return_value=mocked_course):
        assert cryptocurrency_action(2) == result
