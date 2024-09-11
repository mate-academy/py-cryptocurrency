import pytest

from app.main import cryptocurrency_action

from unittest import mock


@pytest.fixture()
def mock_get_exchange_rate_prediction() -> None:
    with (mock.patch("app.main.get_exchange_rate_prediction")
          as mock_prediction):
        yield mock_prediction


def test_prediction_function_was_called(
        mock_get_exchange_rate_prediction: callable
) -> None:
    mock_get_exchange_rate_prediction.return_value = 5
    cryptocurrency_action(25)
    mock_get_exchange_rate_prediction.assert_called_once_with(25)


@pytest.mark.parametrize(
    "mock_rate,current_rate,result",
    [
        (106, 100, "Buy more cryptocurrency"),
        (105, 100, "Do nothing"),
        (100, 100, "Do nothing"),
        (95, 100, "Do nothing"),
        (94, 100, "Sell all your cryptocurrency"),
    ],
    ids=[
        "should return 'Buy more cryptocurrency' "
        "when prediction_rate / current_rate = 1.06",
        "should return 'Do nothing' "
        "when prediction_rate / current_rate = 1.05",
        "should return 'Do nothing' when prediction_rate / current_rate = 1",
        "should return 'Do nothing' "
        "when prediction_rate / current_rate = 0.95",
        "should return 'Sell all your cryptocurrency' "
        "when prediction_rate / current_rate = 0.94",
    ]
)
def test_all_possible_ratio(
        mock_rate: int | float,
        current_rate: int | float,
        result: str,
        mock_get_exchange_rate_prediction: callable
) -> None:
    mock_get_exchange_rate_prediction.return_value = mock_rate
    assert cryptocurrency_action(current_rate) == result
