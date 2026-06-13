"""my_package/subclass.py와 utils.py 모듈을 검증하는 테스트 모듈입니다."""

from my_package.subclass import Income, Expense
from my_package.utils import calculate_totals, get_category_distribution


def test_income_and_expense_subclasses():
    """Income과 Expense 자식 클래스의 인스턴스 생성 및 메서드를 검증합니다."""
    # 1. 수입 객체 생성 및 검증
    inc = Income(amount=500000.0, category="용돈", date="2026-06-13", description="부모님 용돈", source="부모님")
    assert inc.amount == 500000.0
    assert inc.source == "부모님"
    assert "[수입]" in inc.get_summary()
    assert inc.to_dict()["type"] == "income"

    # 2. 지출 객체 생성 및 검증
    exp = Expense(amount=15000.0, category="외식비", date="2026-06-13", description="저녁 삼겹살", payment_method="카드")
    assert exp.amount == 15000.0
    assert exp.payment_method == "카드"
    assert "[지출]" in exp.get_summary()
    assert exp.to_dict()["type"] == "expense"


def test_utils_calculation():
    """calculate_totals 및 get_category_distribution 함수를 검증합니다."""
    # 테스트용 모의 거래 데이터 리스트 생성
    transactions = [
        Income(amount=20000.0, category="부업", date="2026-06-13", source="블로그"),
        Expense(amount=5000.0, category="식비", date="2026-06-13", payment_method="카드"),
        Expense(amount=3000.0, category="교통비", date="2026-06-13", payment_method="카드"),
        Expense(amount=12000.0, category="식비", date="2026-06-13", payment_method="현금"),
    ]

    # 1. 총액 계산 도우미 함수 검증 (총수입 20,000 / 총지출 20,000 / 잔액 0)
    total_inc, total_exp, balance = calculate_totals(transactions)
    assert total_inc == 20000.0
    assert total_exp == 20000.0
    assert balance == 0.0

    # 2. 카테고리별 분배 검증 (식비 5,000 + 12,000 = 17,000 / 교통비 3,000)
    dist = get_category_distribution(transactions)
    assert dist["식비"] == 17000.0
    assert dist["교통비"] == 3000.0
    assert "부업" not in dist  # 수입 카테고리는 제외되어야 함


def test_utils_edge_cases_with_empty_input():
    """빈 거래 목록이 입력되었을 때 올바르게 대처하는지 엣지 케이스를 검증합니다."""
    empty_list = []

    # 1. 빈 목록의 합계 연산 검증 (0.0, 0.0, 0.0 예상)
    total_inc, total_exp, balance = calculate_totals(empty_list)
    assert total_inc == 0.0
    assert total_exp == 0.0
    assert balance == 0.0

    # 2. 빈 목록의 카테고리 분포 검증 (빈 딕셔너리 {} 예상)
    dist = get_category_distribution(empty_list)
    assert dist == {}
