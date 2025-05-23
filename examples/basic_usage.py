"""
K-Logger Basic Usage Example
"""

from k_logger import setup_korean_logger, get_logger

# Method 1: Auto-setup (already done on import)
logger = get_logger()

logger.info("기본 설정으로 로깅")
logger.warning("경고 메시지")
logger.error("에러 메시지")

print("\n" + "="*50 + "\n")

# Method 2: Custom setup
logger = setup_korean_logger(level="DEBUG", show_file_info=True)

logger.debug("디버그 메시지")
logger.info("정보 메시지")
logger.warning("경고 메시지")
logger.error("에러 메시지")

print("\n" + "="*50 + "\n")

# Method 3: Minimal setup (no file info)
logger = setup_korean_logger(level="INFO", show_file_info=False)

logger.info("파일 정보 없는 로깅")
logger.warning("간단한 경고")
logger.error("간단한 에러") 