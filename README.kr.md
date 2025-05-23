# K-Logger 🇰🇷

한국 개발자를 위한 간편하고 깔끔한 Python 로깅 유틸리티

[![PyPI version](https://badge.fury.io/py/k-logger.svg)](https://badge.fury.io/py/k-logger)
[![Python Support](https://img.shields.io/pypi/pyversions/k-logger.svg)](https://pypi.org/project/k-logger/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## 특징

- 🕐 **한국 시간대 자동 적용** - 모든 시간이 자동으로 한국 시간(KST)으로 표시
- 🔤 **축약된 로그 레벨** - 깔끔한 한 글자 로그 레벨 표시 (D, I, W, E, C)
- 🎨 **유연한 포맷팅** - 필요에 따라 파일 정보 표시 여부 선택 가능
- ⚡ **간편한 설정** - 별도 설정 없이 바로 사용 가능
- 🐍 **순수 Python** - 시스템 의존성 없음
- 📦 **가벼운 용량** - 최소한의 의존성 (`loguru`와 `pytz`만 필요)
- 🖱️ **IDE 친화적** - VSCode 등 최신 IDE에서 클릭 가능한 파일 경로 (형식: `file.py:line`)

## 설치

```bash
pip install k-logger
```

## 빠른 시작

```python
from k_logger import get_logger

logger = get_logger()

logger.info("애플리케이션 시작")
logger.warning("경고 메시지")
logger.error("에러 발생")
```

출력:
```
I 05-23 14:30:15 | example.py:5 - 애플리케이션 시작
W 05-23 14:30:15 | example.py:6 - 경고 메시지
E 05-23 14:30:15 | example.py:7 - 에러 발생
```

> 💡 **Pro tip**: VSCode나 최신 IDE에서 `example.py:5`를 클릭하면 해당 코드 라인으로 바로 이동할 수 있습니다!

## 사용법

### 기본 사용법

K-Logger는 import하면 자동으로 기본 설정으로 초기화됩니다:

```python
from k_logger import get_logger

logger = get_logger()
logger.info("안녕하세요!")
```

### 커스텀 설정

`setup_korean_logger()`를 사용하여 로거 동작을 커스터마이징할 수 있습니다:

```python
from k_logger import setup_korean_logger

# 디버그 메시지 표시 및 파일 정보 포함
logger = setup_korean_logger(level="DEBUG", show_file_info=True)

logger.debug("디버그 메시지")
logger.info("정보 메시지")
logger.warning("경고 메시지")
logger.error("에러 메시지")
logger.critical("치명적 메시지")
```

### 간단한 포맷

파일 정보 없이 더 깔끔한 출력을 원한다면:

```python
from k_logger import setup_korean_logger

# 파일 정보 없는 간단한 포맷
logger = setup_korean_logger(level="INFO", show_file_info=False)

logger.info("깔끔한 로그 출력")  # I 05-23 14:30:15 - 깔끔한 로그 출력
```

## 로그 레벨

| 레벨     | 축약 | 설명 |
|----------|------|------|
| DEBUG    | D    | 디버깅을 위한 상세 정보 |
| INFO     | I    | 일반적인 정보성 메시지 |
| WARNING  | W    | 경고 메시지 |
| ERROR    | E    | 에러 메시지 |
| CRITICAL | C    | 치명적 문제 |

## API 문서

### `setup_korean_logger(level="INFO", show_file_info=True)`

한국 시간대를 지원하는 로거 인스턴스를 설정하고 반환합니다.

**매개변수:**
- `level` (str): 로깅 레벨 ("DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL")
- `show_file_info` (bool): 로그에 파일 경로와 라인 번호 포함 여부

**반환값:**
- `loguru.Logger`: 설정된 로거 인스턴스

### `get_logger()`

현재 로거 인스턴스를 가져옵니다. 설정되지 않은 경우 자동 설정된 기본 로거를 반환합니다.

**반환값:**
- `loguru.Logger`: 현재 로거 인스턴스

## 예제

### 기존 프로젝트와 통합

```python
# myapp.py
from k_logger import get_logger

logger = get_logger()

def process_data(data):
    logger.debug(f"{len(data)}개 항목 처리 중")
    try:
        # 데이터 처리
        result = data.upper()
        logger.info("데이터 처리 성공")
        return result
    except Exception as e:
        logger.error(f"데이터 처리 실패: {e}")
        raise
```

### 멀티 모듈 애플리케이션

```python
# config.py
from k_logger import setup_korean_logger

# 애플리케이션 시작 시 한 번만 설정
logger = setup_korean_logger(level="DEBUG", show_file_info=True)

# other_module.py
from k_logger import get_logger

logger = get_logger()  # 동일한 설정된 인스턴스를 가져옴
logger.info("다른 모듈에서 로거 사용")
```

## 요구사항

- Python 3.7+
- `loguru` >= 0.6.0
- `pytz` >= 2021.1

## 기여하기

기여는 언제나 환영합니다! Pull Request를 보내주세요.

1. 저장소를 Fork합니다
2. Feature 브랜치를 생성합니다 (`git checkout -b feature/AmazingFeature`)
3. 변경사항을 커밋합니다 (`git commit -m 'Add some AmazingFeature'`)
4. 브랜치에 Push합니다 (`git push origin feature/AmazingFeature`)
5. Pull Request를 생성합니다

## 라이선스

이 프로젝트는 MIT 라이선스 하에 배포됩니다 - 자세한 내용은 [LICENSE](LICENSE) 파일을 참조하세요.

## 저자

- **june-oh** - [GitHub](https://github.com/june-oh)

## 변경사항

### v1.0.0 (2025-05-23)
- 첫 정식 릴리즈
- 한국 시간대 지원
- 축약된 로그 레벨
- 커스터마이징 가능한 포맷팅 옵션
- IDE 친화적 클릭 가능한 파일 경로

## 감사의 말

- [loguru](https://github.com/Delgan/loguru) - Python 로깅을 (놀랍도록) 간단하게
- [pytz](https://github.com/stub42/pytz) - Python을 위한 세계 시간대 정의 