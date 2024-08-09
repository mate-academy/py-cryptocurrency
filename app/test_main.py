from unittest import mock

import pytest

from app.main import cryptocurrency_action


@pytest.fixture()
def mock_get_exchange_rate_prediction() -> mock.Mock:
    with mock.patch(
            "app.main.get_exchange_rate_prediction"
    ) as mock_prediction:
        yield mock_prediction


@pytest.fixture()
def mock_random_choice() -> mock.Mock:
    with mock.patch("random.choice") as mock_choice:
        yield mock_choice


@pytest.mark.parametrize(
    "current_rate, prediction, expected_action",
    [
        (100, 106, "Buy more cryptocurrency"),
        (100, 94, "Sell all your cryptocurrency"),
        (100, 105, "Do nothing"),
        (100, 95, "Do nothing"),
        (100, 100, "Do nothing"),
    ]
)
def test_cryptocurrency_action(
        mock_get_exchange_rate_prediction: mock.Mock,
        mock_random_choice: mock.Mock,
        current_rate: float,
        prediction: float,
        expected_action: str
) -> None:
    if prediction > current_rate:
        choice_value = "increase"
    else:
        choice_value = "decrease"

    mock_random_choice.return_value = choice_value
    mock_get_exchange_rate_prediction.return_value = prediction

    assert cryptocurrency_action(current_rate) == expected_action
