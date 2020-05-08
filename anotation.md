# anotation

- `before_first_request`
  - 웹 application 기동 이후 가장 처음에 들어오는 HTTP 요청에서만 실행
  - 인자를 전달할 수 없음


- `before_request`
  - HTTP 요청이 들어올 때마다 실행
  - 인자를 전달할 수 없음


- `after_request`
  - HTTP 요청이 끝나고 브라우저에 응답하기 전에 실행


- `teardown_request`
  - HTTP 요청 결과가 브라우저에 응답한 다음 실행


- `teardown_appcontext`
  - HTTP 요청이 완전히 완료되면 실행
