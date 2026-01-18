from unittest import mock

import pytest

from app.main import cryptocurrency_action


@pytest.fixture()
def mocked_rate() -> None:
    with mock.patch("app.main.get_exchange_rate_prediction") as mocked_rate:
        yield mocked_rate


def test_function_has_been_called(mocked_rate: mock) -> None:
    mocked_rate.return_value = 14
    cryptocurrency_action(7)
    mocked_rate.assert_called_once()


@pytest.mark.parametrize(
    "return_values, awaited_results",
    [
        pytest.param(
            95,
            "Do nothing",
            id="should return Do nothing if in range 95% - 105%"
        ),
        pytest.param(
            105,
            "Do nothing",
            id="should return Do nothing if in range 95% - 105%"
        ),
        pytest.param(
            107,
            "Buy more cryptocurrency",
            id="should return Buy if > 105%"
        ),
        pytest.param(
            93,
            "Sell all your cryptocurrency",
            id="should return Sell if in < 95%"
        )
    ]
)
def test_should_return_right_value(
        mocked_rate: callable,
        return_values: int,
        awaited_results: str
) -> None:
    mocked_rate.return_value = return_values
    result = cryptocurrency_action(100)
    assert result == awaited_results
