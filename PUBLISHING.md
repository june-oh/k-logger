# K-Logger 배포 가이드

## 사전 준비

1. PyPI 계정 생성: https://pypi.org/account/register/
2. API 토큰 생성: https://pypi.org/manage/account/token/

## 배포 단계

### 1. 필요한 도구 설치

```bash
pip install --upgrade pip setuptools wheel twine
```

### 2. 빌드

```bash
# 이전 빌드 파일 제거
rm -rf dist/ build/ *.egg-info

# 새로 빌드
python setup.py sdist bdist_wheel
```

### 3. 테스트 PyPI에 업로드 (선택사항)

```bash
# 테스트 PyPI에 업로드
twine upload --repository testpypi dist/*

# 테스트 설치
pip install --index-url https://test.pypi.org/simple/ --no-deps k-logger
```

### 4. 실제 PyPI에 업로드

```bash
twine upload dist/*
```

또는 API 토큰 사용:

```bash
twine upload -u __token__ -p <your-api-token> dist/*
```

### 5. 설치 확인

```bash
pip install k-logger
```

## GitHub 푸시

```bash
git push -u origin main
```

## 버전 업데이트

새 버전 릴리즈 시:

1. `setup.py`, `pyproject.toml`, `k_logger/__init__.py`에서 버전 번호 변경
2. `README.md`의 Changelog 업데이트
3. Git 태그 생성:
   ```bash
   git tag v0.1.0
   git push origin v0.1.0
   ``` 