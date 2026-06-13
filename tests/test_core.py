"""my_package/core.py의 Transaction 클래스를 검증하는 테스트 모듈입니다."""

import pytest
from my_package.core import Transaction


def test_transaction_initialization_success():
    """정상적인 수치로 Transaction 인스턴스가 생성되는지 검증합니다."""
    t = Transaction(
        amount=10000.0,
        category="식비",
        date="2026-06-13",
        description="점심식사",
    )
    assert t.amount == 10000.0
    assert t.category == "식비"
    assert t.date == "2026-06-13"
    assert t.description == "점심식사"
    assert t.get_summary() == "[2026-06-13] 식비: 10000.0 (점심식사)"


def test_transaction_to_dict_success():
    """Transaction 객체가 딕셔너리로 정상 변환되는지 검증합니다."""
    t = Transaction(amount=5000.0, category="식비", date="2026-06-13")
    res = t.to_dict()
    assert res["amount"] == 5000.0
    assert res["category"] == "식비"
    assert res["date"] == "2026-06-13"


def test_transaction_negative_amount_raises_value_error():
    """음수 금액이 입력되었을 때 ValueError가 발생하는지 검증합니다."""
    with pytest.raises(ValueError):
        Transaction(amount=-500.0, category="식비", date="2026-06-13")


def test_transaction_invalid_amount_type_raises_type_error():
    """숫자가 아닌 타입의 금액이 입력되었을 때 TypeError를 검증합니다."""
    with pytest.raises(TypeError):
        Transaction(
            amount="만원",  # type: ignore
            category="식비",
            date="2026-06-13",
        )


def test_transaction_invalid_date_format_raises_value_error():
    """잘못된 형식의 날짜가 입력되었을 때 ValueError를 검증합니다."""
    with pytest.raises(ValueError):
        Transaction(amount=1000.0, category="식비", date="2026/06/13")
