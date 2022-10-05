import pytest
from unittest import mock
from app.main import cryptocurrency_action


class TestCryptocurrencyAction:
    @pytest.fixture()
    def mocked_rate(self) -> int:
        with mock.patch("app.main.get_exchange_rate_prediction") as mock_rate:
            yield mock_rate

    @pytest.mark.parametrize(
        "rate,predicted_rate,result",
        [
            pytest.param(100, 106, "Buy more cryptocurrency",
                         id="If 106% should Buy more"),
            pytest.param(100, 94, "Sell all your cryptocurrency",
                         id="If 94% should Sell all"),
            pytest.param(100, 105, "Do nothing",
                         id="If 105% should Do nothing"),
            pytest.param(100, 95, "Do nothing",
                         id="If 95% should Do nothing")
        ]
    )
    def test_cryptocurrency_action(
            self,
            mocked_rate: int,
            rate: int,
            predicted_rate: int,
            result: str
    ) -> None:
        mocked_rate.return_value = predicted_rate
        assert cryptocurrency_action(rate) == result


if __name__ == "__main__":
    pytest.main()
