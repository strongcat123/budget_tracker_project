"""my_package/subclass.py와 utils.py 모듈을 검증하는 테스트 모듈입니다."""

from my_package.subclass import Income, Expense
from my_package.utils import calculate_totals, get_category_distribution


def test_income_subclass_initialization_and_summary():
    """Income 자식 클래스의 인스턴스 생성 및 메서드를 검증합니다."""
    inc = Income(
        amount=500000.0,
        category="용돈",
        date="2026-06-13",
        description="부모님 용돈",
        source="부모님",
    )
    assert inc.amount == 500000.0
    assert inc.source == "부모님"
    assert "[수입]" in inc.get_summary()
    assert inc.to_dict()["type"] == "income"


def test_expense_subclass_initialization_and_summary():
    """Expense 자식 클래스의 인스턴스 생성 및 메서드를 검증합니다."""
    exp = Expense(
        amount=15000.0,
        category="외식비",
        date="2026-06-13",
        description="저녁 삼겹살",
        payment_method="카드",
    )
    assert exp.amount == 15000.0
    assert exp.payment_method == "카드"
    assert "[지출]" in exp.get_summary()
    assert exp.to_dict()["type"] == "expense"


def test_utils_calculate_totals_success():
    """calculate_totals 도우미 함수의 정상 연산 로직을 검증합니다."""
    transactions = [
        Income(
            amount=20000.0,
            category="부업",
            date="2026-06-13",
            source="블로그",
        ),
        Expense(
            amount=5000.0,
            category="식비",
            date="2026-06-13",
            payment_method="카드",
        ),
        Expense(
            amount=15000.0,
            category="식비",
            date="2026-06-13",
            payment_method="현금",
        ),
    ]
    total_inc, total_exp, balance = calculate_totals(transactions)
    assert total_inc == 20000.0
    assert total_exp == 20000.0
    assert balance == 0.0


def test_utils_get_category_distribution_success():
    """get_category_distribution 도우미 함수의 정상 연산 로직을 검증합니다."""
    transactions = [
        Expense(
            amount=5000.0,
            category="식비",
            date="2026-06-13",
            payment_method="카드",
        ),
        Expense(
            amount=3000.0,
            category="교통비",
            date="2026-06-13",
            payment_method="카드",
        ),
        Expense(
            amount=12000.0,
            category="식비",
            date="2026-06-13",
            payment_method="현금",
        ),
    ]
    dist = get_category_distribution(transactions)
    assert dist["식비"] == 17000.0
    assert dist["교통비"] == 3000.0


def test_utils_calculate_totals_with_empty_list_returns_zeros():
    """빈 리스트가 들어왔을 때 calculate_totals가 0을 반환하는지 검증합니다."""
    empty_list = []
    total_inc, total_exp, balance = calculate_totals(empty_list)
    assert total_inc == 0.0
    assert total_exp == 0.0
    assert balance == 0.0


def test_utils_get_category_distribution_with_empty_list_returns_empty():
    """빈 리스트가 들어왔을 때 카테고리 지출 분포가 빈 사전을 반환하는지 검증합니다."""
    empty_list = []
    dist = get_category_distribution(empty_list)
    assert dist == {}
