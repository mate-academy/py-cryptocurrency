from app.main import cryptocurrency_action
import pytest
from unittest import mock


@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurency(mocked_crypto: int) -> None:
    cryptocurrency_action(100)
    mocked_crypto.assert_called_once()


def test_correct_value() -> None:
    with pytest.raises(TypeError):
        cryptocurrency_action("100")
