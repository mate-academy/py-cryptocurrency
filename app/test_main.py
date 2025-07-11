import pytest
from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "current_rate, mock_rate, result",
    [
        (100, 106, "Buy more cryptocurrency"),
        (100, 94, "Sell all your cryptocurrency"),
        (100, 104.9, "Do nothing"),
        (100, 95, "Do nothing"),
        (100, 105, "Do nothing"),
    ],
    ids=[
        "buy",
        "sell",
        "not buy and sell",
        "not buy and sell",
        "not buy and sell"
    ]
)
def test_for_cryptocurrency_action(current_rate: int,
                                   mock_rate: int,
                                   result: str,
                                   monkeypatch: pytest.MonkeyPatch
                                   ) -> None:
    def mock_get_exchange(*args, **kwargs) -> int:
        return mock_rate
    (monkeypatch.setattr
     ("app.main.get_exchange_rate_prediction", mock_get_exchange))
    assert cryptocurrency_action(current_rate) == result


"""Also method with mock.patch"""
# from unittest import mock
# def test_for_cryptocurrency_action(current_rate: int,
#                                    mock_rate: int,
#                                    result: str
#                                    ) -> None:
#     with (mock.patch("app.main.get_exchange_rate_prediction")
#           as mock_prediction):
#         mock_prediction.return_value = mock_rate
#         assert cryptocurrency_action(current_rate) == result
