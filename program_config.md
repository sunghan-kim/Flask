# 프로그램 설정

- 프로그램들은 일종의 설정 및 구성을 필요
- `Flask` 객체의 `config` 속성을 통해 설정값 변경 및 설정 가능
- `config`는 실제로는 dictionary의 서브 클래스이며, 다른 dictionary처럼 다음과 같이 수정 가능

```python
app = Flask(__name__)
app.config['DEBUG'] = True
```

<br>

## 다양한 프로그램 설정 방법

```python
app = Flask(__name__)
app.config.from_object('yourapplication.default_settings')
app.config.from_envvar('YOURAPPLICATION_SETTINGS')
```

<br>

- 어플리케이션은 환경 변수(`envvar`)에 의해 지정된 구성 파일을 기반으로 설정할 수 있다.

```python
app.config.from_envvar('YOURAPPLICATION_SETTINGS')
```

<br>

- Flask 어플리케이션 설정을 위해 클래스들을 사용할 수 있다.

```python
app.config.from_object('module_name.DevelopmentConfig')
```

```python
class DevelopmentConfig(BaseConfig):
  DEBUG = True
  TESTING = True
```
