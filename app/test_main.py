from app.main import cryptocurrency_action

from pytest import fixture
from unittest.mock import patch, MagicMock


@fixture
def mock_get_prediction() -> MagicMock:
    with patch(
            "app.main.get_exchange_rate_prediction"
    ) as mocked_prediction:
        yield mocked_prediction


def test_get_prediction_should_be_called(
        mock_get_prediction: MagicMock
) -> None:
    mock_get_prediction.return_value = 0.95
    cryptocurrency_action(0.95)
    mock_get_prediction.assert_called_once_with(0.95)


def test_rate_95_percent_do_nothing(
        mock_get_prediction: MagicMock
) -> None:
    mock_get_prediction.return_value = 0.95
    assert cryptocurrency_action(1) == "Do nothing"


def test_rate_105_percent_do_nothing(
        mock_get_prediction: MagicMock
) -> None:
    mock_get_prediction.return_value = 1.05
    assert cryptocurrency_action(1) == "Do nothing"


def test_rate_106_percent_by_cryptocurrency(
        mock_get_prediction: MagicMock
) -> None:
    mock_get_prediction.return_value = 1.06
    assert cryptocurrency_action(1) == ("Buy more "
                                        "cryptocurrency")


def test_rate_94_percent_sell_cryptocurrency(
        mock_get_prediction: MagicMock
) -> None:
    mock_get_prediction.return_value = 0.94
    assert cryptocurrency_action(1) == ("Sell all your "
                                        "cryptocurrency")
