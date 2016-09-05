# KoreaBankChecker

## kbstar (국민은행)
### 현재 구현된 기능
1. 은행 계좌의 잔액 확인
2. Transaction Class


### 사용방법
1. KB은행 간편조회에 사용하는 계좌를 등록
2. Python3 설치
3. pip로 필요 패키지 & 의존성 모듈 설치
```
pip install -r requirements.txt
```
4. 환경변수 세팅
  ~/.bashrc 파일에
```
#ENV for BANK PY
export RESIDENTNUMBER=주민번호 뒤7자리
export BANKID=국민은행ID
export BANKPW=계좌비밀번호4자리
export ACCOUNTNUMBER=계좌번호
```
  이같은 형식으로 저장하면 새 쉘 실행시 바로적용된다.
  쉘을 재실행 하지 않고 바로 적용하기 위해서는
```
source ~/.bashrc
```
  명령어로 사용 가능.


### 추가예정기능
1. Django ORM에 Celery를 통해 비동기 방식(스케쥴러)으로 동작
  Payment가 이루어진 경우에는 django db인스턴스 객체 생성 후 db에 반영함.
  사용 조건은 다음과 같음
  * 무통장 입금 기한은 실행 시간부터 24시간 이내로 할 것
  * 무통장 계좌 번호와 금액 안내가 사용자 휴대폰으로 안내됨.
  * 등록된 유저가 마이페이지에서 결제 페이지로 들어갈 경우에 결제정보를 볼 수 있어야 함.
