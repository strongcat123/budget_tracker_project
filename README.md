# Budget Tracker (가계부 및 예산 추적기)

본 패키지는 금융 거래 데이터를 객체지향 설계를 활용해 체계적으로 관리하고, 수입/지출 통계 및 월간 요약을 제공하는 파이썬 라이브러리입니다.

---

## 1. 프로젝트 개요
- **소프트웨어 공학 원칙 적용**: 모듈성, 가독성, DRY(Don't Repeat Yourself) 원칙을 준수하여 설계되었습니다.
- **객체지향 상속 설계**: 공통 비즈니스 로직을 지닌 부모 클래스(`Transaction`)를 정의하고, 이를 상속하는 자식 클래스(`Income`, `Expense`)로 상속 계층을 완벽히 구현하였습니다.
- **안정성 검증**: 정적 분석 도구(`pycodestyle`)를 활용해 PEP 8 코딩 표준 규격을 준수하고, 단위 테스트 프레임워크(`pytest`)를 통해 예외 상황 및 정상 연산 로직을 철저히 검증했습니다.

---

## 2. 설치 방법
가상환경을 활성화한 후, 프로젝트 루트 디렉터리에서 아래 명령어를 실행하여 로컬 패키지로 설치할 수 있습니다.
```bash
pip install .
```

---

## 3. 빠른 시작 (Quick Start)
설치를 완료한 후 아래 예제 코드를 즉시 복사하여 가계부 패키지의 핵심 기능을 수행해 볼 수 있습니다.
```Python
from my_package import Income, Expense, calculate_totals, get_category_distribution

# 1. 수입 및 지출 내역 생성
transactions = [
    Income(amount=3000000.0, category="급여", date="2026-06-01", description="6월 기본급", source="회사"),
    Income(amount=100000.0, category="부업", date="2026-06-13", description="외주 개발", source="크몽"),
    Expense(amount=12000.0, category="식비", date="2026-06-13", description="점심 돈까스", payment_method="카드"),
    Expense(amount=3500.0, category="교통비", date="2026-06-13", description="버스 요금", payment_method="카드"),
    Expense(amount=45000.0, category="쇼핑", date="2026-06-13", description="여름 셔츠", payment_method="카드"),
    Expense(amount=8000.0, category="식비", date="2026-06-13", description="아메리카노", payment_method="현금")
]

# 2. 거래 내역 요약 출력
print("=== 거래 내역 리포트 ===")
for tx in transactions:
    print(tx.get_summary())

# 3. 전체 합계 통계 연산
total_inc, total_exp, balance = calculate_totals(transactions)
print("\n=== 금융 종합 통계 ===")
print(f"총 수입: {total_inc:,.1f}원")
print(f"총 지출: {total_exp:,.1f}원")
print(f"순 잔액: {balance:,.1f}원")

# 4. 카테고리별 지출 분포 분석
distribution = get_category_distribution(transactions)
print("\n=== 카테고리별 지출 분포 ===")
for category, amount in distribution.items():
    print(f"- {category}: {amount:,.1f}원")

```

---

## 4. 주요 기능 설명

1. 거래 유효성 검증: 거래 금액이 양수인지 검사하고, 일자 데이터의 YYYY-MM-DD 포맷 일치 여부를 객체 생성 단계에서 엄격히 검증합니다.
2. 다형성 정보 반환: 공통 요약 인터페이스(get_summary()) 및 딕셔너리 변환 인터페이스(to_dict())가 각 수입/지출 내역에 맞춰 다형성 있게 특화된 문자열을 출력합니다.
3. 금융 지표 계산: 복잡한 거래 리스트가 들어와도 수입과 지출의 구분 유형을 판단하여 총 수입, 총 지출, 최종 순 금액을 오차 없이 일괄 연산해 냅니다.
4. 지출 분포 통계: 축적된 대량의 거래 정보에서 수입은 제외하고 실제 지출의 카테고리 분포만 선별하여 누적 계산된 통계를 도출해 냅니다.

---

## 5. 테스트 실행 방법
본 패키지는 pytest 프레임워크를 기반으로 모든 검증을 자동 수행합니다. 아래 명령어로 테스트를 가동할 수 있습니다.
```bash
python -m pytest
```

---

## 6. 작성자 정보

이름: 박재현
학번: 202620863
