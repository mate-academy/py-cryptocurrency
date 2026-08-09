from unittest import mock
from unittest.mock import MagicMock
from app.main import cryptocurrency_action


@mock.patch("app.main.get_exchange_rate_prediction")
def test_buy_more_cryptocurrency(mock_prediction: MagicMock) -> None:
    """
    Test that 'Buy more cryptocurrency' is returned
    when the prediction is > 5% higher.
    """
    # Current rate is 100, prediction is 106 (6% increase)
    mock_prediction.return_value = 106
    assert cryptocurrency_action(100) == "Buy more cryptocurrency"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_sell_all_cryptocurrency(mock_prediction: MagicMock) -> None:
    """
    Test that 'Sell all your cryptocurrency' is returned
    when the prediction is > 5% lower.
    """
    # Current rate is 100, prediction is 94 (6% decrease)
    mock_prediction.return_value = 94
    assert cryptocurrency_action(100) == "Sell all your cryptocurrency"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_do_nothing_on_upper_boundary(mock_prediction: MagicMock) -> None:
    """
    Test that 'Do nothing' is returned when the
    prediction is exactly 5% higher.
    """
    mock_prediction.return_value = 105
    assert cryptocurrency_action(100) == "Do nothing"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_do_nothing_on_lower_boundary(mock_prediction: MagicMock) -> None:
    """
    Test that 'Do nothing' is returned when the
    prediction is exactly 5% lower.
    """
    mock_prediction.return_value = 95
    assert cryptocurrency_action(100) == "Do nothing"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_do_nothing_with_no_change(mock_prediction: MagicMock) -> None:
    """
    Test that 'Do nothing' is returned when there
    is no predicted change.
    """
    mock_prediction.return_value = 100
    assert cryptocurrency_action(100) == "Do nothing"
