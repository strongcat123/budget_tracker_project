"""Transaction 클래스를 상속받아 수입과 지출 클래스를 정의하는 모듈입니다."""

from my_package.core import Transaction


class Income(Transaction):
    """수입 거래를 나타내는 클래스이며, Transaction 클래스를 상속받습니다.

    :ivar amount: 거래 금액
    :ivar category: 거래 카테고리 (예: 급여, 부업)
    :ivar date: YYYY-MM-DD 형식의 거래 일자
    :ivar description: 거래에 대한 추가 설명
    :ivar source: 수입원 (예: 회사, 크몽 등)
    """

    def __init__(
        self,
        amount: float,
        category: str,
        date: str,
        description: str = "",
        source: str = "기타",
    ):
        """Income 인스턴스를 초기화합니다.

        :param amount: 수입 금액
        :param category: 수입 카테고리
        :param date: YYYY-MM-DD 형식의 거래 일자
        :param description: 수입에 대한 추가 설명
        :param source: 수입원

        >>> inc = Income(3000000.0, "급여", "2026-06-01", "6월 월급", "회사")
        >>> inc.source
        '회사'
        """
        super().__init__(amount, category, date, description)
        self.source = str(source)

    def get_summary(self) -> str:
        """수입 내역의 요약 정보를 문자열로 반환합니다.

        :return: 포맷팅된 수입 요약 문자열

        >>> inc = Income(50000.0, "부업", "2026-06-13", "디자인", "크몽")
        >>> inc.get_summary()
        '[수입] [2026-06-13] 부업: 50000.0 (디자인) [수입원: 크몽]'
        """
        base_summary = super().get_summary()
        return f"[수입] {base_summary} [수입원: {self.source}]"

    def to_dict(self) -> dict:
        """수입 내역 정보를 딕셔너리 형태로 변환합니다.

        :return: 수입 데이터가 담긴 딕셔너리

        >>> inc = Income(10000.0, "장학금", "2026-06-13")
        >>> inc.to_dict()['source']
        '기타'
        """
        data = super().to_dict()
        data["source"] = self.source
        data["type"] = "income"
        return data


class Expense(Transaction):
    """지출 거래를 나타내는 클래스이며, Transaction 클래스를 상속받습니다.

    :ivar amount: 거래 금액
    :ivar category: 거래 카테고리 (예: 식비, 교통비)
    :ivar date: YYYY-MM-DD 형식의 거래 일자
    :ivar description: 거래에 대한 추가 설명
    :ivar payment_method: 결제 수단 (예: 신용카드, 현금)
    """

    def __init__(
        self,
        amount: float,
        category: str,
        date: str,
        description: str = "",
        payment_method: str = "카드",
    ):
        """Expense 인스턴스를 초기화합니다.

        :param amount: 지출 금액
        :param category: 지출 카테고리
        :param date: YYYY-MM-DD 형식의 거래 일자
        :param description: 지출에 대한 추가 설명
        :param payment_method: 결제 수단

        >>> exp = Expense(8500.0, "식비", "2026-06-13", "국밥", "카드")
        >>> exp.payment_method
        '카드'
        """
        super().__init__(amount, category, date, description)
        self.payment_method = str(payment_method)

    def get_summary(self) -> str:
        """지출 내역의 요약 정보를 문자열로 반환합니다.

        :return: 포맷팅된 지출 요약 문자열

        >>> exp = Expense(12000.0, "영화", "2026-06-13", "", "페이")
        >>> exp.get_summary()
        '[지출] [2026-06-13] 영화: 12000.0 [결제수단: 페이]'
        """
        base_summary = super().get_summary()
        return f"[지출] {base_summary} [결제수단: {self.payment_method}]"

    def to_dict(self) -> dict:
        """지출 내역 정보를 딕셔너리 형태로 변환합니다.

        :return: 지출 데이터가 담긴 딕셔너리

        >>> exp = Expense(1500.0, "교통비", "2026-06-13")
        >>> exp.to_dict()['payment_method']
        '카드'
        """
        data = super().to_dict()
        data["payment_method"] = self.payment_method
        data["type"] = "expense"
        return data
