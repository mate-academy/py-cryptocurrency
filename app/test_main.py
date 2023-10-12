import pytest
from unittest import mock
from app.main import cryptocurrency_action
from typing import Union


@pytest.mark.parametrize("data, prediction, result", [
    (1, 1.99, "Buy more cryptocurrency"),
    (-1, -7.63, "Buy more cryptocurrency"),
    (3.5, 32.56, "Buy more cryptocurrency"),
    (-1, -0.94, "Sell all your cryptocurrency"),
    (5, 3.95, "Sell all your cryptocurrency"),
    (350, 243.78, "Sell all your cryptocurrency"),
    (3.5, 3.32, "Do nothing"),
    (350, 367.5, "Do nothing"),
])
def test_cryptocurrency_action(
        data: Union[int, float],
        prediction: float,
        result: str
) -> None:
    with (mock.patch("app.main.get_exchange_rate_prediction")
          as mock_prediction):
        mock_prediction.return_value = prediction
        assert cryptocurrency_action(data) == result


@pytest.mark.parametrize("data", [
    "str",
    ["list"],
    {"dict": ""}
])
def test_cryptocurrency_action_type_error_string(data: any) -> None:
    with pytest.raises(TypeError):
        cryptocurrency_action(data)
