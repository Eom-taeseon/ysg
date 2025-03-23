import os
import subprocess
from datetime import datetime
import shutil
import sys

def main():
    print("===== Streamlit 애플리케이션 실행기 (.exe 버전) =====")

    # log 디렉토리 생성
    log_dir = "log"
    if not os.path.exists(log_dir):
        print("log 디렉토리가 없습니다. 새로 생성합니다.")
        os.makedirs(log_dir)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    log_file = os.path.join(log_dir, f"streamlit_{timestamp}.log")
    print(f"로그 파일: {log_file}")

    # requirements.txt 존재 확인
    if not os.path.exists("requirements.txt"):
        print("[오류] requirements.txt 파일이 없습니다.")
        sys.exit(1)

    print("필요한 패키지를 설치합니다...")
    subprocess.run(["pip", "install", "-r", "requirements.txt"], check=True)

    if not os.path.exists("main.py"):
        print("[오류] main.py 파일이 없습니다.")
        sys.exit(1)

    print("Streamlit 앱 실행 중... (로그 저장 중)")
    with open(log_file, "w") as log:
        subprocess.run(["streamlit", "run", "main.py"], stdout=log, stderr=subprocess.STDOUT)

if __name__ == "__main__":
    main()
