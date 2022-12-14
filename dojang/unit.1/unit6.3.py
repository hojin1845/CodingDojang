#unit.6.3.
#지금까지 변수를 만들 때 10, 'Hello, world!' 등의 값을 직접 할당해줌 
#하지만 이렇게 하면 고정된 값만 사용할 수 있음 
#그럼 매번 다른 값을 변수에 할당하려면 어떻게 해야 할까?

#input 함수의 결과를 변수에 할당하기
#input함수의 결과를 변수 x에 할당함
#Hello world!를 입력한 뒤 엔터키를 누름

#변수 x에 입력한 문자열이 저장됨
#x의 값을 출력해보면 방금 입력한 'Hello world'가 나옴

#여기서 한 가지 불편한 점은 input함수가 실행된 다음에는 아무내용이 없어서 입력을 을 받는 상태인지 출력이 없는 상태인지 알 수가 없다는 점

#input 함수의 결과를 변수에 할당하기
#input괄호 안에 문자열을 지정해주면 됨

#실행 해보면 '문자열을 입력하세요:'처럼 안내 문구가 먼저 나옴
#문자열을 입력한 뒤 엔터키를 누르면 입력한 그대로 출력
#이 문자열은 스크립트 파일 사용자에게 입력받는 값의 용도를 미리 알려줄때 사용
#다른말로는 프롬프트 라고 부름/(파이썬 프롬프트 >>>와 같은 의미

#두 숫자의 합 구하기 
#조금 응용해서 두 개를 입력받는 뒤에 두 숫자의 합을 구해보자
#IDLE의 소스 코드 편집 창에입력

#소스 코드를 실행하면 '첫번째 숫자를 입력하세요.'가 출력
#10을 입력하고 엔터 키를 누름 
#'두 번째 숫자를 입력하세요:'가 출력되면 20을 입력하고 엔터 키를 누름

#10 + 20의 결과는 30이 나와야되는데 1020이 나옴
#이런 결과는 input에서 입력받은 값은 항상 문자열 형태이기 때문임
#10과20은 겉보기엔 숫자이지만 실제로는 문자열이므로 10과20을 +로 연결하며 1020이 나오게됨
#input의 결과를 변수의 저장한 뒤 type을 사용해보면 input의 결과가 문자열이라는 것을 알 수 있음
