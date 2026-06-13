"""my_package 배포를 위한 라이브러리 빌드 사양서입니다."""

from setuptools import setup, find_packages

setup(
    name="my_package",
    version="0.1.0",
    author="홍길동",
    author_email="gildong@example.com",
    description="객체지향 설계 기반 가계부 및 예산 추적기 패키지",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="markdown",
    packages=find_packages(),
    install_requires=[],  # 파이썬 기본 표준 라이브러리만 사용하므로 비워둡니다.
    python_requires=">=3.8",
)