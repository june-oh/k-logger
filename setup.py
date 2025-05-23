from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="k-logger",
    version="0.1.0",
    author="Your Name",  # 여기에 실제 이름을 넣으세요
    author_email="your.email@example.com",  # 여기에 실제 이메일을 넣으세요
    description="Korean-friendly logging utility with abbreviated levels and Korean timezone",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/k-logger",  # 여기에 실제 GitHub URL을 넣으세요
    project_urls={
        "Bug Tracker": "https://github.com/yourusername/k-logger/issues",
    },
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: System :: Logging",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    packages=find_packages(),
    python_requires=">=3.7",
    install_requires=[
        "loguru>=0.6.0",
        "pytz>=2021.1",
    ],
    extras_require={
        "dev": [
            "pytest>=6.0",
            "black",
            "flake8",
            "mypy",
        ],
    },
    keywords="logging, korean, timezone, kst, loguru, abbreviated, simple",
) 