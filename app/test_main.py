import pytest
from unittest import mock
from app.main import cryptocurrency_action


@pytest.fixture()
def mocked_prediction() -> mock.MagicMock:
    with mock.patch(
        "app.main.get_exchange_rate_prediction"
    ) as mocked_test_prediction:
        mocked_test_prediction.return_value = 100
        yield mocked_test_prediction


def test_prediction_was_called(mocked_prediction: mock) -> None:
    cryptocurrency_action(100)
    mocked_prediction.assert_called()


@pytest.mark.parametrize(
    "current_rate, expected_result",
    [
        pytest.param(95.3, "Do nothing"),
        pytest.param(95, "Buy more cryptocurrency"),
        pytest.param(106, "Sell all your cryptocurrency"),
        pytest.param(105.1, "Do nothing"),
        pytest.param(100 / 1.05, "Do nothing"),
        pytest.param(100 / 0.95, "Do nothing"),
    ],
)
def test_action_is_correct(
    mocked_prediction: int | float,
    current_rate: int | float,
    expected_result: str,
) -> None:
    assert cryptocurrency_action(current_rate) == expected_result
