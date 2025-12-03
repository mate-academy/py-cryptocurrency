import pytest
from app.main import cryptocurrency_action
from unittest import mock


@pytest.mark.parametrize(
    "current_rate, percent,expected",
    [
        (100, 106, "Buy more cryptocurrency"),
        (5768, 6748.56, "Buy more cryptocurrency"),
        (746, 701.24, "Sell all your cryptocurrency"),
        (736594, 611373.02, "Sell all your cryptocurrency"),
        (100, 105, "Do nothing"),
        (100, 95, "Do nothing")

    ]
)
def test_cryptocurrency_action(current_rate: int,
                               percent: int,
                               expected: str) -> None:
    with mock.patch("app.main.get_exchange_rate_prediction") as forecast:
        forecast.return_value = percent
        assert cryptocurrency_action(current_rate) == expected
