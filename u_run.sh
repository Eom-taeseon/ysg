#!/bin/bash

echo "===== Streamlit 애플리케이션 실행 스크립트 ====="

# log 디렉토리 확인 및 생성
if [ ! -d "./log" ]; then
    echo "log 디렉토리가 없습니다. 새로 생성합니다."
    mkdir -p "./log"
fi

# 현재 날짜와 시간으로 로그 파일 이름 생성
TIMESTAMP=$(date +"%Y%m%d_%H%M%S")
LOG_FILE="./log/streamlit_${TIMESTAMP}.log"

echo "로그 파일이 다음 위치에 저장됩니다: ${LOG_FILE}"

# Python 설치 확인
if ! command -v python3 &> /dev/null; then
    echo "[오류] Python이 설치되어 있지 않습니다."
    echo "Python을 설치하려면 운영체제에 따라 다음 명령어를 사용하세요:"
    echo "  - Ubuntu/Debian: sudo apt-get install python3"
    echo "  - CentOS/RHEL: sudo yum install python3"
    echo "  - macOS: brew install python3"
    echo "설치 후 이 스크립트를 다시 실행해주세요."
    exit 1
fi

# Conda 설치 확인
if ! command -v conda &> /dev/null; then
    echo "[오류] Conda가 설치되어 있지 않습니다."
    echo "Conda를 설치하려면 https://docs.conda.io/en/latest/miniconda.html 에서 다운로드하세요."
    echo "설치 후 이 스크립트를 다시 실행해주세요."
    exit 1
fi

# 'ysg' 환경 존재 확인 및 없으면 생성
if ! conda env list | grep -q "ysg"; then
    echo "'ysg' Conda 환경이 없습니다. 새로 생성합니다."
    conda create -y -n ysg python=3.9
    if [ $? -ne 0 ]; then
        echo "[오류] 'ysg' 환경 생성에 실패했습니다."
        exit 1
    fi
fi

echo "Conda 환경 'ysg'를 활성화합니다..."
# source 명령어를 사용하여 conda 활성화
eval "$(conda shell.bash hook)"
conda activate ysg
if [ $? -ne 0 ]; then
    echo "[오류] Conda 환경 활성화에 실패했습니다."
    exit 1
fi

# requirements.txt 파일 존재 확인
if [ ! -f "requirements.txt" ]; then
    echo "[오류] requirements.txt 파일이 존재하지 않습니다."
    echo "필요한 패키지 목록이 있는 requirements.txt 파일을 확인해주세요."
    exit 1
fi

echo "필요한 패키지를 설치합니다..."
pip install -r requirements.txt
if [ $? -ne 0 ]; then
    echo "[오류] 패키지 설치에 실패했습니다."
    exit 1
fi

# main.py 파일 존재 확인
if [ ! -f "main.py" ]; then
    echo "[오류] main.py 파일이 존재하지 않습니다."
    echo "Streamlit 애플리케이션 파일(main.py)을 확인해주세요."
    exit 1
fi

echo "Streamlit 애플리케이션을 실행합니다..."
echo "로그는 ${LOG_FILE}에 저장됩니다."
streamlit run main.py > "${LOG_FILE}" 2>&1
if [ $? -ne 0 ]; then
    echo "[오류] Streamlit 애플리케이션 실행에 실패했습니다."
    echo "자세한 내용은 로그 파일을 확인하세요: ${LOG_FILE}"
    exit 1
fi

echo "애플리케이션이 종료되었습니다. 로그 파일: ${LOG_FILE}"
exit 0