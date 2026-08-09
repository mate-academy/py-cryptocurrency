from unittest import mock

import pytest

from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "prediction_rate, current_rate,expected_result",
    [
        (112, 100, "Buy more cryptocurrency"),
        (91, 100, "Sell all your cryptocurrency"),
        (105, 100, "Do nothing"),
        (95, 100, "Do nothing"),

    ],
    ids=[
        "currency will grow up",
        "currency will fall down",
        "currency will remain unchanged",
        "currency will remain unchanged"
    ]
)
def test_changes_of_cryptocurrency(prediction_rate: float,
                                   current_rate: float,
                                   expected_result: str) -> None:
    with (
        mock.patch("app.main.get_exchange_rate_prediction") as mocked_func
    ):
        mocked_func.return_value = prediction_rate
        assert cryptocurrency_action(current_rate) == expected_result
