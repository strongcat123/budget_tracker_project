"""가계부 패키지의 핵심 부모 클래스인 Transaction 클래스를 정의하는 모듈입니다."""

from datetime import datetime


class Transaction:
    """금융 거래(수입 또는 지출)를 나타내는 부모 클래스입니다.

    :ivar amount: 거래 금액
    :ivar category: 거래 카테고리 (예: 식비, 월급)
    :ivar date: YYYY-MM-DD 형식의 거래 일자
    :ivar description: 거래에 대한 추가 설명 (선택 사항)
    """

    def __init__(self, amount: float, category: str, date: str, description: str = ""):
        """Transaction 인스턴스를 초기화합니다.

        :param amount: 거래 금액 (양수여야 합니다)
        :param category: 거래 카테고리
        :param date: YYYY-MM-DD 형식의 거래 일자
        :param description: 거래에 대한 추가 설명

        >>> t = Transaction(1000.0, "식비", "2026-06-13", "점심 식사")
        >>> t.amount
        1000.0
        """
        self._validate_amount(amount)
        self._validate_date(date)
        self.amount = float(amount)
        self.category = str(category)
        self.date = str(date)
        self.description = str(description)

    def _validate_amount(self, amount: float) -> None:
        """금액이 양수이며 숫자형 데이터인지 검증합니다.

        :param amount: 검증할 거래 금액
        :raises ValueError: 금액이 양수가 아닐 때 발생
        :raises TypeError: 금액이 숫자 형식이 아닐 때 발생
        """
        if not isinstance(amount, (int, float)):
            raise TypeError("Amount must be a number.")
        if amount <= 0:
            raise ValueError("Amount must be a positive number.")

    def _validate_date(self, date_str: str) -> None:
        """날짜 문자열이 YYYY-MM-DD 형식에 부합하는지 검증합니다.

        :param date_str: 검증할 날짜 문자열
        :raises ValueError: 날짜 형식이 올바르지 않을 때 발생
        """
        try:
            datetime.strptime(date_str, "%Y-%m-%d")
        except ValueError as exc:
            raise ValueError("Date must be in YYYY-MM-DD format.") from exc

    def get_summary(self) -> str:
        """거래 내역의 요약 정보를 문자열로 반환합니다.

        :return: 포맷팅된 요약 문자열

        >>> t = Transaction(1500.0, "교통비", "2026-06-13", "시내버스")
        >>> t.get_summary()
        '[2026-06-13] 교통비: 1500.0 (시내버스)'
        """
        desc_str = f" ({self.description})" if self.description else ""
        return f"[{self.date}] {self.category}: {self.amount}{desc_str}"

    def to_dict(self) -> dict:
        """거래 내역 정보를 딕셔너리 형태로 변환합니다.

        :return: 거래 데이터가 담긴 딕셔너리

        >>> t = Transaction(5000.0, "도서", "2026-06-13")
        >>> t.to_dict()
        {'amount': 5000.0, 'category': '도서', 'date': '2026-06-13', 'description': ''}
        """
        return {
            "amount": self.amount,
            "category": self.category,
            "date": self.date,
            "description": self.description,
        }