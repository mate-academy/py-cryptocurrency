from unittest import mock
import pytest
from typing import Union

from app.main import cryptocurrency_action


@pytest.fixture()
def get_predict_rate() -> mock.MagicMock:
    with (mock.patch("app.main.get_exchange_rate_prediction")
          as mocked_get_predict):
        yield mocked_get_predict


def test_predict_action(get_predict_rate: mock.MagicMock) -> None:
    get_predict_rate.return_value = 500
    cryptocurrency_action(500)
    get_predict_rate.assert_called_once_with(500)


@pytest.mark.parametrize(
    "predict_rate,  result",
    [
        (94, "Sell all your cryptocurrency"),
        (95, "Do nothing"),
        (100, "Do nothing"),
        (105, "Do nothing"),
        (106, "Buy more cryptocurrency"),
    ],
    ids=[
        "predict rate lower",
        "predict rate lower line",
        "rate does not change",
        "predict rate upper line",
        "predict rate upper",
    ]
)
def test_right_predict(get_predict_rate: mock.MagicMock,
                       predict_rate: Union[int, float],
                       result: str) -> None:
    get_predict_rate.return_value = predict_rate
    assert cryptocurrency_action(100) == result
