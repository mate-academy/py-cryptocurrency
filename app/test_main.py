from unittest import mock

import pytest

from app.main import cryptocurrency_action


@pytest.fixture()
def mocked_get_exchange_rate_prediction() -> mock.Mock:
    with mock.patch("app.main.get_exchange_rate_prediction") as mocked_data:
        yield mocked_data


@pytest.mark.parametrize(
    "rate_prediction,cryptocurrency,expected_data",
    [
        pytest.param(
            100, 0.94, "Buy more cryptocurrency",
        ),
        pytest.param(
            94, 100, "Sell all your cryptocurrency",
        ),
        pytest.param(
            21, 20, "Do nothing",
        ),
        pytest.param(
            19, 20, "Do nothing",
        ),
    ]
)
def test_cryptocurrency_action(
        mocked_get_exchange_rate_prediction: mock.Mock,
        rate_prediction: int,
        cryptocurrency: float,
        expected_data: str
) -> None:
    mocked_get_exchange_rate_prediction.return_value = rate_prediction
    assert cryptocurrency_action(cryptocurrency) == expected_data
