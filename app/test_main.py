from app.main import cryptocurrency_action
from typing import Union
from _pytest.monkeypatch import MonkeyPatch


def test_buy_more_cryptocurrency(monkeypatch: MonkeyPatch) -> None:
    # Мок для get_exchange_rate_prediction
    def mock_prediction(current_rate: Union[int, float]) -> float:
        return current_rate * 1.10  # +10% від поточного курсу

    monkeypatch.setattr(
        "app.main.get_exchange_rate_prediction", mock_prediction
    )

    result = cryptocurrency_action(100)  # current_rate = 100
    assert result == "Buy more cryptocurrency", \
        "Expected to buy more cryptocurrency when rate increases >5%"


def test_sell_all_cryptocurrency(monkeypatch: MonkeyPatch) -> None:
    # Мок для get_exchange_rate_prediction
    def mock_prediction(current_rate: Union[int, float]) -> float:
        return current_rate * 0.90  # -10% від поточного курсу

    monkeypatch.setattr(
        "app.main.get_exchange_rate_prediction", mock_prediction
    )

    result = cryptocurrency_action(100)  # current_rate = 100
    assert result == "Sell all your cryptocurrency", \
        "Expected to sell all cryptocurrency when rate decreases >5%"


def test_do_nothing_high(monkeypatch: MonkeyPatch) -> None:
    # Мок для get_exchange_rate_prediction
    def mock_prediction(current_rate: Union[int, float]) -> float:
        return current_rate * 1.05  # рівно +5%

    monkeypatch.setattr(
        "app.main.get_exchange_rate_prediction", mock_prediction
    )

    result = cryptocurrency_action(100)  # current_rate = 100
    assert result == "Do nothing",\
        "Expected to do nothing when rate increases exactly by 5%"


def test_do_nothing_low(monkeypatch: MonkeyPatch) -> None:
    # Мок для get_exchange_rate_prediction
    def mock_prediction(current_rate: Union[int, float]) -> float:
        return current_rate * 0.95  # рівно -5%

    monkeypatch.setattr(
        "app.main.get_exchange_rate_prediction", mock_prediction
    )

    result = cryptocurrency_action(100)  # current_rate = 100
    assert result == "Do nothing", \
        "Expected to do nothing when rate decreases exactly by 5%"
