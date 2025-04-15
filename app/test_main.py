from app.main import cryptocurrency_action
from unittest import mock


@mock.patch("app.main.get_exchange_rate_prediction")
def test_rate_95_do_nothing(mock_prediction: any) -> None:
    mock_prediction.return_value = 15000
    assert cryptocurrency_action(14285.71) == "Do nothing"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_rate_105_do_nothing(mock_prediction: any) -> None:
    mock_prediction.return_value = 200
    assert cryptocurrency_action(190.48) == "Do nothing"
