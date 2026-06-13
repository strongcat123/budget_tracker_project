"""가계부 데이터 연산 및 통계 생성을 지원하는 도우미 함수 모듈입니다."""

from typing import List, Dict, Tuple
from my_package.core import Transaction


def calculate_totals(
    transactions: List[Transaction],
) -> Tuple[float, float, float]:
    """주어진 거래 목록에서 총 수입, 총 지출, 순 잔액을 계산합니다.

    :param transactions: 거래 객체들의 리스트
    :return: (총 수입, 총 지출, 순 잔액) 형태의 튜플

    >>> from my_package.subclass import Income, Expense
    >>> txs = [
    ...     Income(5000.0, "용돈", "2026-06-13"),
    ...     Expense(2000.0, "식비", "2026-06-13")
    ... ]
    >>> calculate_totals(txs)
    (5000.0, 2000.0, 3000.0)
    """
    total_income = 0.0
    total_expense = 0.0

    for tx in transactions:
        tx_dict = tx.to_dict()
        tx_type = tx_dict.get("type", "unknown")

        if tx_type == "income":
            total_income += tx.amount
        elif tx_type == "expense":
            total_expense += tx.amount

    net_balance = total_income - total_expense
    return total_income, total_expense, net_balance


def get_category_distribution(
    transactions: List[Transaction],
) -> Dict[str, float]:
    """주어진 거래 목록의 카테고리별 지출 분포를 계산합니다.

    지출만 합산하여 카테고리별 분배 딕셔너리를 반환합니다.

    :param transactions: 거래 객체들의 리스트
    :return: 카테고리명을 키로, 지출 합계를 값으로 하는 딕셔너리

    >>> from my_package.subclass import Expense
    >>> txs = [
    ...     Expense(1500.0, "식비", "2026-06-13"),
    ...     Expense(3000.0, "교통비", "2026-06-13")
    ... ]
    >>> get_category_distribution(txs)
    {'식비': 1500.0, '교통비': 3000.0}
    """
    distribution: Dict[str, float] = {}

    for tx in transactions:
        tx_dict = tx.to_dict()
        if tx_dict.get("type") == "expense":
            category = tx.category
            current_val = distribution.get(category, 0.0)
            distribution[category] = current_val + tx.amount

    return distribution
