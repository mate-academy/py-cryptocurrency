import pytest
from unittest import mock


from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "mock_result,expected_result",
    [
        pytest.param(
            0.95, "Do nothing",
            id="Should do nothing if prediction rate is 0.95"
        ),
        pytest.param(
            1.05, "Do nothing",
            id="Should do nothing if prediction rate is 1.05"
        ),
        pytest.param(
            0.9, "Sell all your cryptocurrency",
            id="Should sell if prediction rate is under 0.95"
        ),
        pytest.param(
            1.1, "Buy more cryptocurrency",
            id="Should buy if prediction rate is above 1.05"
        ),
    ]
)
def test_cryptocurrency_action_should_return_correct_action(
        mock_result: float,
        expected_result: str) -> None:
    with mock.patch("app.main.get_exchange_rate_prediction") as mocked_get_rt:
        mocked_get_rt.return_value = mock_result
        assert cryptocurrency_action(1) == expected_result
