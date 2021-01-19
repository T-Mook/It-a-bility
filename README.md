# 목표
* '타닥 탁!'하고 무언가 되면-화면에 보여지면 코딩하는 것 같아 보이고 좋겠다 싶은 것들을 직접 간단한 모듈로 구현해봅시다.

# 사용
1. 이용하고자 하는 모듈 폴더로 이동
1. 가상환경 설치 (하단 참고)
1. `python run.py`

# 환경설정
## 가상환경 (각 하위 폴더에서 합니다)
> 예시. `ChartingIsDone/` 폴더 내
1. 설치
   * python -m venv .venv
1. 가상환경 실행
   * (Mac OS) `. .venv/bin/activate`
   * (Window) `.venv/Scripts` 폴더 내 `activate` 실행
1. 필요 라이브러리 설치
   * `python -m pip install -r requirements.txt`
1. 신규 라이브러리 설치 후 저장
   * `pip freeze > requirements.txt`
## Git
```
git config commit.template .github/GIT_COMMIT_TEMPLATE
```