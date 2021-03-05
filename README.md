# DjangoTodoList
Django Practice

임의로 만들어 본 Todo리스트 이며 AWS서버로 배포 한게 아닌
그냥 단순히 파일을 옮겨 AWS에서 개발 서버로 AWS DB에 단순 연결 한 파일입니다


Todo리스트로 게시판 형식 만듦

create, modify, delete 및 view 만듦

기존 DjangoPractice, DjangoDoc 참조하여 sign, login, logout 만듦

Django aws 연결

aws rds mysql 연결

python manage.py migrate 하면 자동으로 만들어준다... 참좋네

setting에 ALLOWED_HOST에 AWS주소 넣어줌

setting에 DATABASE에 mysql로 바꾸고, AWS_RDS 주소, 이름 등 넣어줌

리눅스에선  python3 manage.py runserver 0:8000 이렇게 해 줘야 돌아간다




### 해야 할 일

django model 연습

사용자 인증 auth 연습 or 사용법 등 찾아보기

UserForm과 같은 form으로 만드는거 

이 공부는 [DjangoReview](https://github.com/NGG-kang/DjangoReview)로 이어질 예정입니다
