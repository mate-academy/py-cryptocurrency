import pytest

from unittest import mock

from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "predicted_rate,expected_result",
    [
        (95, "Do nothing"),
        (105, "Do nothing"),
        (106, "Buy more cryptocurrency"),
        (94, "Sell all your cryptocurrency"),
    ],
    ids=[
        "should do nothing if rate < current, but difference is not that much",
        "should do nothing if rate > current, but difference is not that much",
        "should buy if predicted exchange rate > current (more than 5%)",
        "should sell if predicted exchange rate < current (more than 5%)",
    ]
)
def test_cryptocurrency_action(
        predicted_rate: int,
        expected_result: str
) -> None:
    with (mock.patch("app.main.get_exchange_rate_prediction")
          as mocked_get_exchange_rate_prediction):
        mocked_get_exchange_rate_prediction.return_value = predicted_rate
        actual_result = cryptocurrency_action(100)

        assert expected_result == actual_result
