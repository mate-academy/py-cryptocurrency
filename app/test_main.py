import pytest

from app.main import cryptocurrency_action
from unittest import mock


class Test():
    @pytest.mark.parametrize(
        "test_cripto,test_what_need_do",
        [
            [1.06, "Buy more cryptocurrency"],
            [0.94, "Sell all your cryptocurrency"]
        ]
    )
    def test_should_(
            self,
            test_cripto,
            test_what_need_do
    ) -> None:
        assert cryptocurrency_action(test_cripto) == test_what_need_do