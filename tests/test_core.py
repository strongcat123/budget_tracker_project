"""my_package/core.py의 Transaction 클래스를 검증하는 테스트 모듈입니다."""

import pytest
from my_package.core import Transaction


def test_transaction_initialization_success():
    """정상적인 수치로 Transaction 인스턴스가 올바르게 생성되는지 검증합니다."""
    t = Transaction(amount=10000.0, category="식비", date="2026-06-13", description="점심식사")
    assert t.amount == 10000.0
    assert t.category == "식비"
    assert t.date == "2026-06-13"
    assert t.description == "점심식사"
    assert t.get_summary() == "[2026-06-13] 식비: 10000.0 (점심식사)"


def test_transaction_invalid_inputs_raise_error():
    """음수 금액이나 숫자가 아닌 값이 입력되었을 때 올바르게 에러가 발생하는지 검증합니다."""
    # 1. 음수 금액 에러 검증 (ValueError 예상)
    with pytest.raises(ValueError):
        Transaction(amount=-500.0, category="식비", date="2026-06-13")

    # 2. 숫자가 아닌 타입 에러 검증 (TypeError 예상)
    with pytest.raises(TypeError):
        Transaction(amount="만원", category="식비", date="2026-06-13")  # type: ignore

    # 3. 잘못된 날짜 형식 에러 검증 (ValueError 예상)
    with pytest.raises(ValueError):
        Transaction(amount=1000.0, category="식비", date="2026/06/13")