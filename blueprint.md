# blueprint

- 실제 서비스할 웹 서비스는 여러 Flask 응용프로그램(Application)으로 구성될 수 있다.
- 생성된 응용프로그램별로 다른 라우팅 규칙과 정적 파일/템플릿 폴더를 관리


- 블루프린트별 URL 규칙 설정
- 블루프린트별 URL 핸들러 설정 (before_request 등)
- 블루프린트별 정적 파일 및 템플릿 필터와 폴더 설정

```python
from flask import Blueprint
from imgdataservice.logger import Log

imgdataservice = Blueprint('imgdataservice', __name__, template_folder='../templates', static_folder='../static')
```
