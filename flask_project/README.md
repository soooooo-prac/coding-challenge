# 📝 Flask Todo Web App

Python과 Flask를 이용한 간단한 웹 기반 할 일 관리 앱입니다.  
CLI에서 시작한 프로젝트를 웹으로 확장하면서 웹 개발의 흐름을 익혔습니다.

---

## ✨ 주요 기능

- 할 일 항목 추가 / 삭제 / 완료 체크 ✅
- 완료 항목은 회색 처리 + 줄 긋기
- JSON 파일로 영구 저장 (서버 껐다 켜도 유지)
- Bootstrap 적용으로 깔끔한 UI
- 템플릿 상속으로 유지보수 쉬운 구조

---

## 🖥️ 실행 방법

```bash
# 가상환경 생성 (선택)
python -m venv venv
source venv/bin/activate  # 윈도우는 venv\Scripts\activate

# 필수 패키지 설치
pip install flask

# 앱 실행
python app.py