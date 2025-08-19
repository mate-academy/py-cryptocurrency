from typing import Generator, Any
from unittest import mock

import pytest

from app.main import cryptocurrency_action


@pytest.fixture(autouse=True)
def mocking_rate_prediction(
    request: pytest.FixtureRequest,
) -> Generator[mock.MagicMock, None, None]:
    mocked_value = getattr(request, "param", 1)
    with mock.patch(
        "app.main.get_exchange_rate_prediction"
    ) as mocked_prediction:
        mocked_prediction.return_value = mocked_value
        yield mocked_prediction


@pytest.mark.parametrize(
    "mocking_rate_prediction, current_rate, expected_result",
    [
        pytest.param(
            0,
            9999,
            "Sell all your cryptocurrency",
            id="should return Sell if currency will cost 0",
        ),
        pytest.param(
            5148.08,
            4438,
            "Buy more cryptocurrency",
            id="should return Buy if expected rate is 1.16",
        ),
        pytest.param(
            500,
            500,
            "Do nothing",
            id="should return Do nothing if expected rate is 1",
        ),
        pytest.param(
            -1,
            2131,
            "Sell all your cryptocurrency",
            id="should return Sell if expected rate is negative",
        ),
        pytest.param(
            2500,
            5000,
            "Sell all your cryptocurrency",
            id="should return Sell if expected rate is 0.5",
        ),
        pytest.param(
            315,
            300,
            "Do nothing",
            id="should return Do nothing if expected rate is 1.05",
        ),
        pytest.param(
            190,
            200,
            "Do nothing",
            id="should return Do nothing if expected rate is 0.95",
        ),
    ],
    indirect=["mocking_rate_prediction"],
)
def test_function_with_different_params(
    current_rate: int | float, expected_result: str
) -> None:
    assert cryptocurrency_action(current_rate) == expected_result


def test_should_call_rate_prediction_func(
    mocking_rate_prediction: mock.MagicMock,
) -> None:
    cryptocurrency_action(1)
    mocking_rate_prediction.assert_called_once()


def test_should_transfer_current_rate_to_prediction_func(
    mocking_rate_prediction: mock.MagicMock,
) -> None:
    cryptocurrency_action(0.5)
    mocking_rate_prediction.assert_called_once_with(0.5)


@pytest.mark.parametrize(
    "current_rate, exception",
    [
        pytest.param(
            0,
            ZeroDivisionError,
            id="should raise ZeroDivisionError if current_rate is 0",
        ),
        pytest.param(
            "1",
            TypeError,
            id="should raise TypeError if current_rate is string",
        ),
        pytest.param(
            None,
            TypeError,
            id="should raise TypeError if current_rate is None",
        ),
    ],
)
def test_should_raise_correct_exception(
    current_rate: Any, exception: type[Exception]
) -> None:
    with pytest.raises(exception):
        cryptocurrency_action(current_rate)
