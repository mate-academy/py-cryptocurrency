import pytest
from pytest_mock import MockerFixture

from app import main


@pytest.mark.parametrize(
    "current_rate,prediction,expected",
    [
        (100, 106, "Buy more cryptocurrency"),      # > 5%
        (100, 105, "Do nothing"),                   # рівно +5%
        (100, 104.99, "Do nothing"),                # трохи менше +5%

        (100, 94, "Sell all your cryptocurrency"),  # < -5%
        (100, 95, "Do nothing"),                    # рівно -5%
        (100, 95.01, "Do nothing"),                 # трохи більше -5%

        (100, 100, "Do nothing"),                   # без змін
    ],
)
def test_cryptocurrency_action(
    mocker: MockerFixture,
    current_rate: float,
    prediction: float,
    expected: str,
) -> None:
    mocker.patch(
        "app.main.get_exchange_rate_prediction",
        return_value=prediction,
    )

    assert main.cryptocurrency_action(current_rate) == expected
