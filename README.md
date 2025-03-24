# 예시건 PoC

## 시작하기

### 설치 방법

1. 아래 명령어를 사용하여 저장소를 복제합니다:
```
git clone https://github.com/Eom-taeseon/ysg.git
```

2. 복제된 디렉토리로 이동합니다:
```
cd ysg
```

### 실행 방법

1. Conda 설치
   - [Anaconda](https://www.anaconda.com/download) 또는 [Miniconda](https://docs.conda.io/en/latest/miniconda.html) 다운로드 및 설치

2. Conda 환경 생성 및 활성화
   ```bash
   # Python 3.10 환경 생성
   conda create -n ysg python=3.10
   
   # 환경 활성화
   conda activate ysg
   ```

3. 필요한 패키지 설치
   ```bash
   pip install -r requirements.txt
   ```

4. 애플리케이션 실행
   ```bash
   streamlit run main.py
   ```

5. web버전 poc 실행
```
(ysg) C:\path\to\your\dir\ysg>streamlit run main.py

  You can now view your Streamlit app in your browser.

  Local URL: http://localhost:8501
  Network URL: http://192.168.75.64:8501 
```
- Network URL은 사내 LAN이 연결되어 있다면 개별적인 DEMO 버전 사용 가능합니다.

### 주요 기능
- 사업비 산정
- 종후자산 계산
- 종전 자산 평가

### 종료 방법
프로그램 실행 중 종료하고 싶을 때는 커맨드 창에서 `Ctrl+C`를 누르면 됩니다.
