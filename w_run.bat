@echo off
chcp 65001 > nul
setlocal enabledelayedexpansion

echo ===== Streamlit 애플리케이션 실행 스크립트 =====

REM log 디렉토리 확인 및 생성
if not exist ".\log" (
    echo log 디렉토리가 없습니다. 새로 생성합니다.
    mkdir ".\log"
)

REM 현재 날짜와 시간으로 로그 파일 이름 생성
for /f "tokens=2 delims==" %%a in ('wmic OS Get localdatetime /value') do set "dt=%%a"
set "YYYY=%dt:~0,4%"
set "MM=%dt:~4,2%"
set "DD=%dt:~6,2%"
set "HH=%dt:~8,2%"
set "Min=%dt:~10,2%"
set "Sec=%dt:~12,2%"

set "LOG_FILE=.\log\streamlit_%YYYY%%MM%%DD%_%HH%%Min%%Sec%.log"

echo 로그 파일이 다음 위치에 저장됩니다: %LOG_FILE%

REM Python 설치 확인
python --version > nul 2>&1
if %ERRORLEVEL% NEQ 0 (
    echo [오류] Python이 설치되어 있지 않습니다.
    echo Python을 설치하려면 https://www.python.org/downloads/ 에서 다운로드하세요.
    echo 설치 후 이 스크립트를 다시 실행해주세요.
    goto :ERROR
)

REM Conda 설치 확인
conda --version > nul 2>&1
if %ERRORLEVEL% NEQ 0 (
    echo [오류] Conda가 설치되어 있지 않습니다.
    echo Conda를 설치하려면 https://docs.conda.io/en/latest/miniconda.html 에서 다운로드하세요.
    echo 설치 후 이 스크립트를 다시 실행해주세요.
    goto :ERROR
)

REM 'ysg' 환경 존재 확인 및 없으면 생성
conda env list | findstr "ysg" > nul
if %ERRORLEVEL% NEQ 0 (
    echo 'ysg' Conda 환경이 없습니다. 새로 생성합니다.
    conda create -y -n ysg python=3.10
    if %ERRORLEVEL% NEQ 0 (
        echo [오류] 'ysg' 환경 생성에 실패했습니다.
        goto :ERROR
    )
)

echo Conda 환경 'ysg'를 활성화합니다...
call conda activate ysg
if %ERRORLEVEL% NEQ 0 (
    echo [오류] Conda 환경 활성화에 실패했습니다.
    goto :ERROR
)

REM requirements.txt 파일 존재 확인
if not exist "requirements.txt" (
    echo [오류] requirements.txt 파일이 존재하지 않습니다.
    echo 필요한 패키지 목록이 있는 requirements.txt 파일을 확인해주세요.
    goto :ERROR
)

echo 필요한 패키지를 설치합니다...
call pip install -r requirements.txt
if %ERRORLEVEL% NEQ 0 (
    echo [오류] 패키지 설치에 실패했습니다.
    goto :ERROR
)

REM main.py 파일 존재 확인
if not exist "main.py" (
    echo [오류] main.py 파일이 존재하지 않습니다.
    echo Streamlit 애플리케이션 파일(main.py)을 확인해주세요.
    goto :ERROR
)

echo Streamlit 애플리케이션을 실행합니다...
echo 로그는 %LOG_FILE%에 저장됩니다.
streamlit run main.py > "%LOG_FILE%" 2>&1
if %ERRORLEVEL% NEQ 0 (
    echo [오류] Streamlit 애플리케이션 실행에 실패했습니다.
    echo 자세한 내용은 로그 파일을 확인하세요: %LOG_FILE%
    goto :ERROR
)

echo 애플리케이션이 종료되었습니다. 로그 파일: %LOG_FILE%
goto :END

:ERROR
echo 스크립트 실행 중 오류가 발생했습니다.
exit /b 1

:END
endlocal
exit /b 0