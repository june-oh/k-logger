# K-Logger 🇰🇷

한국 개발자를 위한 간편하고 깔끔한 로깅 유틸리티

Korean-friendly logging utility with abbreviated levels and Korean timezone support.

## 특징 (Features)

- 🇰🇷 **한국 시간대 자동 적용** - Korean timezone (KST) automatically applied
- 📝 **축약된 로그 레벨** - Abbreviated log levels (I, W, E, D, C)
- 🎨 **깔끔한 포맷** - Clean and readable format
- ⚡ **간편한 설정** - Simple setup with sensible defaults
- 🔧 **유연한 커스터마이징** - Flexible customization options

## 설치 (Installation)

```bash
pip install k-logger
```

## 빠른 시작 (Quick Start)

```python
from k_logger import get_logger

logger = get_logger()

logger.info("안녕하세요!")
logger.warning("경고 메시지")
logger.error("에러 메시지")
```

출력 예시:
```
I 05-23 14:30:15 | example.py:5 - 안녕하세요!
W 05-23 14:30:15 | example.py:6 - 경고 메시지
E 05-23 14:30:15 | example.py:7 - 에러 메시지
```

## 사용법 (Usage)

### 기본 사용법

```python
from k_logger import setup_korean_logger, get_logger

# 자동 설정 (import 시 자동 실행됨)
logger = get_logger()
logger.info("기본 설정으로 로깅")
```

### 커스텀 설정

```python
from k_logger import setup_korean_logger

# 디버그 레벨, 파일 정보 포함
logger = setup_korean_logger(level="DEBUG", show_file_info=True)

logger.debug("디버그 메시지")
logger.info("정보 메시지")
logger.warning("경고 메시지")
logger.error("에러 메시지")
```

### 간단한 포맷 (파일 정보 제외)

```python
from k_logger import setup_korean_logger

# 파일 정보 없는 간단한 포맷
logger = setup_korean_logger(level="INFO", show_file_info=False)

logger.info("간단한 로깅")  # I 05-23 14:30:15 - 간단한 로깅
```

## API 문서 (API Documentation)

### `setup_korean_logger(level="INFO", show_file_info=True)`

한국 시간대와 축약된 로그 레벨을 사용하는 로거를 설정합니다.

**매개변수:**
- `level` (str): 로그 레벨 ("DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL")
- `show_file_info` (bool): 파일 경로와 라인 번호 표시 여부

**반환값:**
- `loguru.Logger`: 설정된 로거 인스턴스

### `get_logger()`

현재 로거 인스턴스를 반환합니다.

**반환값:**
- `loguru.Logger`: 현재 로거 인스턴스

## 로그 레벨 (Log Levels)

| 원본 레벨 | 축약 | 설명 |
|----------|------|------|
| DEBUG    | D    | 디버그 정보 |
| INFO     | I    | 일반 정보 |
| WARNING  | W    | 경고 메시지 |
| ERROR    | E    | 에러 메시지 |
| CRITICAL | C    | 치명적 에러 |

## 의존성 (Dependencies)

- `loguru>=0.6.0` - 강력한 로깅 라이브러리
- `pytz>=2021.1` - 시간대 처리

## 라이선스 (License)

MIT License

## 기여하기 (Contributing)

이슈나 Pull Request는 언제나 환영합니다!

Issues and Pull Requests are always welcome!

## 변경사항 (Changelog)

### v0.1.0
- 첫 번째 릴리스
- 한국 시간대 지원
- 축약된 로그 레벨
- 기본 설정 제공 