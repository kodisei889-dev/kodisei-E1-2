파이썬의 실행
python main.py

명령어를 사용하면 에러로 실행이 안되는 현상 발견

확인 해보니

py main.py로 실행하면 실행 됨.

왜 그런가?

Windows의 앱 실행 별칭이 켜져 있음
Microsoft Store 연동이 잡혀 있음
실제 Python 경로가 PATH에 앞쪽으로 안 잡혀 있음
이라고 하는데,

설정창이 막혀 있어서 사용자가 못 고쳐서 방법을 알아봄

현재 PowerShell 창에서만 python을 py처럼 쓰기
설정창이 막혀 있어도 현재 창 한정 임시 우회는 가능합니다.

Set-Alias python py

하면, 실제로 python --version 했을 때, 버전이 나타나고
python main.py 도 정상 실행 확인
py main.py도 정상 실행 확인

원래 상태도 되돌리려면

Remove-Item Alias:python

하게 되면 python은 실행 안됨.

where.exe 로 나온 경로로
& "실제-python.exe-전체경로" main.py를 실행하면 안되고,

& "C:\Users\사용자이름\AppData\Local\Microsoft\WindowsApps\python.exe" main.py

py -0p 로 나온 경로로
& "실제-python.exe-전체경로" main.py를 실행하면 실행된다.

 & "C:\Users\사용자이름\AppData\Roaming\uv\python\cpython-3.15.2-windows-x86_64-none\python.exe" main.py

여기서 자세히 경로를 보면 python.exe가 WindowsApps 폴더안에 있는 것을 확인할 수 있다.
python이 WindowsApps 쪽 별칭/스토어 연결 파일로 잡혀 있다는 뜻

시험을 위해 파이썬 단어를 외울 겸 set-alias python py 해준다.

where.exe를 통해서만 python의 연결 경로로 제대로 인식이 잡혀 있는지 알 수 있다.
단, where로 해서는 안된다. where의 경우도 윈도우앱에 잡혀 있는 경우가 있어서 .exe까지 적어주는 걸 권장한다.

1) 머지 진행하고 나가기
기본 메시지 그대로 써도 되면:

Esc 누르기
:wq 입력
Enter
이렇게 하면 저장하고 종료되고, merge commit이 완료됩니다.

2) 그냥 편집기만 강제로 나가기
Esc
:q!
Enter
다만 이 경우는 머지 처리 의도에 따라 결과가 헷갈릴 수 있어서,
지금은 보통 :wq가 가장 안전합니다.

브런치 만들기
git branch feature-readme

브런치 이동하기
git checkout feature-readme

위 두줄을 한 줄로 하면,

git checkout -b feature-readme

readme 파일 수정 후

파일 저장
git add readme.md

코밋
git commit -m "README 기능 설명 보완"

main으로 돌아가기
git checkout main

병합하기
git merge feature-readme

깃허브에 올리기
git push origin main

결과 확인
브런치 확인
git branch
로그 확인 [병합내용 나옴]
git log --oneline --graph --all
깃 상태확인
git status

머지 자체를 취소하고 싶다면
git merge --abort

브랜치 작업이 끝난 후 feature 브랜치를 지우려면,
git branch -d feature-readme

만약, 같은 이름의 브런치가 있는데 생성하면,
fatal: a branch named 'feature-readme' already exists
라고 메세지가 뜸
그럴땐 그냥 이동 하면 됨
git checkout feature-readme

또, 수정 중인 파일 때문에 이동이 안될 수가 있음
그럴 땐 보통:
먼저 커밋하거나
변경사항을 정리한 뒤 이동해야 합니다.

git log 화면 안에 있으면:
q
를 눌러서 나온다.

def init(self, question, choices, answer, hint=""):
def __init__(self, question: str, choices: Sequence[str], answer: int, hint: str = ""):

자동 호출 여부
__init__는 인스턴스를 만들 때 자동 호출된다: class C: def init(self, x): self.x = x c = C(10) # => __init__가 자동으로 실행되어 c.x == 10
반면 init은 그냥 일반 메서드: class C: def init(self, x): self.x = x c = C() # init는 자동 호출 안됨 c.init(10) # 직접 호출해야 동작
이름의 의미
__init__처럼 앞뒤로 두 개 이상의 밑줄(dunder, double underscore)을 갖는 이름은 파이썬에서 특별한 의미(스페셜 메서드)를 가지며 인터프리터가 특정 시점에 호출합니다(초기화, 표현, 비교 등).
단, 앞만 ''이고 뒤에 ''가 없으면 이름 맹글링(name mangling)이 발생할 수 있음(클래스 내부 private 흉내). __init__은 dunder 패턴이라 맹글링 대상 아님.
타입 힌트(annotations)의 차이
def init(self, question: str, choices: Sequence[str], answer: int, hint: str = "")
이는 단지 문서화와 정적 검사용입니다. 런타임에서 파이썬이 자동으로 타입을 체크하거나 변환하지 않습니다.
타입 힌트를 활용하려면 mypy 같은 도구로 정적 검사하거나, 런타임 검사 라이브러리(예: typeguard, pydantic)를 사용해야 합니다.
Sequence[str]를 쓰려면 from collections.abc import Sequence (또는 from typing import Sequence, Python 버전에 따라 선택).
기본값과 반환값
__init__은 반환값이 없어야 합니다(정상적으로는 None). 관습적으로 반환 타입 표기는 -> None으로 씁니다: def init(...) -> None:
일반 메서드 init는 원하는 값을 반환할 수 있습니다(return 사용 가능).
__new__와의 관계(간단히)
객체 생성 과정: __new__가 새 인스턴스를 만들고, 만들어진 인스턴스에 대해 __init__가 초기화를 수행합니다. 따라서 __init__는 인스턴스가 이미 만들어진 이후 호출되는 "초기화자"입니다.
예시로 비교
자동 초기화되는 init:
class Q1:
def init(self, text):
self.text = text

q = Q1("문제")  # 생성 시 text가 설정됨

수동 초기화하는 init:
class Q2:
def init(self, text):
self.text = text

q = Q2()       # q.text 없음
q.init("문제")  # 직접 호출해야 text가 설정됨

타입 힌트 사용 예시(Sequence 필요 import)
from collections.abc import Sequence
class Quiz:
def init(self, question: str, choices: Sequence[str], answer: int, hint: str = "") -> None:
...

Sequence는 "순서가 있는 시퀀스(열)"에 대한 추상 인터페이스(abstract base class)입니다. 리스트(list), 튜플(tuple), 문자열(str), range 등 인덱스 접근과 길이 측정을 지원하는 자료형들을 포괄합니다.

위치: collections.abc.Sequence (또는 typing.Sequence)
정의: Sequence는 len()과 getitem()을 최소한으로 제공하면 Sequence의 조건을 만족합니다. 즉, 길이를 알 수 있고 인덱스로 접근 가능한 객체라면 Sequence로 간주됩니다.
Sequence가 제공하는 편의 메서드(ABC가 구현해줌)
contains(self, x) (in 연산)
iter(self)
reversed(self)
index(value)
count(value) 이런 메서드는 실제 하위 클래스가 최소 메서드만 구현하면 ABC가 자동으로 제공합니다.

언제 list를 쓸지, 언제 Sequence(또는 Iterable 등)를 쓸지 결정하는 기준
만약 함수가 반드시 list여야 하고(예: 함수 내부에서 append/pop 등 리스트 전용 메서드를 쓸 때), 호출자에게 list를 요구하고 싶다면 choices: list[str] 로 명시하라.
함수가 리스트나 튜플 모두 허용해도 되고, 단지 순회(반복)만 필요하면 Iterable[T]가 더 적절하다(제너레이터도 허용).
함수가 인덱스 접근과 len()을 사용하지만 변경은 하지 않으면 Sequence[T]가 적절하다.
외부에서 문자열(str)을 실수로 넘기는 것을 막고 싶다면 추가 검사를 하라(문자열은 Sequence이지만 의도한 컬렉션이 아님).
Quiz의 choices에 대해 권장
보통 "선택지 목록"은 순서가 있고 길이(4)가 고정이므로 list[str]를 요구하면 명확합니다.
만약 호출자가 tuple도 쓰길 허용하려면 Sequence[str]를 쓰되, 문자열("abcd")가 들어오는 것을 차단하는 검사를 추가하세요.

함수 시그니처에 적는 "매개변수: 타입"은 기본적으로 문서(문서화)와 정적 검사기(mypy 등)를 위한 힌트입니다. 파이썬 인터프리터가 자동으로 입력값의 타입을 강제하지는 않습니다.
즉, 타입 힌트를 적어도 아무 타입이나 넣으면 함수는 실행됩니다(런타임에서 오류가 나지 않음). 타입 힌트만으로는 타입 강제가 되지 않습니다.

파이썬은 동적 타이핑(dynamically typed) 언어입니다. 변수는 런타임에 타입이 정해지고, 인터프리터는 타입 주석을 무시합니다(주석이 아니라 애노테이션이긴 하지만 기본 동작은 무시).
타입 힌트는 "이 함수는 이렇게 기대합니다"라는 계약을 표현하는 문서와 같고, 정적 분석 도구가 이를 읽어 코드의 잠재적 버그를 잡아줍니다. 하지만 런타임 비용과 유연성을 이유로 인터프리터가 자동으로 검사하지 않는 설계입니다.

간단한 예로 차이 보여주기

타입 힌트만: (검사 없음)
def f(x: int) -> None:
print(x)

f("문자열")  # 오류 없이 실행. 인터프리터는 타입 힌트를 강제하지 않음

런타임 검사(타입가드 사용):
from typeguard import typechecked

@typechecked
def f(x: int) -> None:
print(x)

f("문자열")  # TypeError: type of argument "x" must be int; got str instead

권장 관행

클래스 인스턴스의 초기화는 __init__에 둔다(사용자들이 기대함).
타입 힌트를 추가하면 가독성/정적 검사에 도움. 하지만 런타임 검사도 원하면 명시적으로 isinstance 검사하거나 타입 검사 도구 사용.
init 내부에서 입력 검증/정리(예: strip())를 해두면 객체가 항상 유효한 상태를 유지하게 할 수 있음.
일반 메서드는 의미 있는 이름을 사용(init 같은 이름은 혼동을 줄 수 있음) — 예: initialize()로 명시적 의도를 주거나, 그냥 __init__에서 처리.

if not isinstance(question, str) or not question.strip():
raise ValueError("문제는 비어 있을 수 없습니다.")

목적
question이 문자열인지 확인하고(타입 검사), 공백을 제거했을 때 빈 문자열이 아닌지 확인(내용 검사)합니다.
빈 문제(또는 타입이 잘못된 입력)를 방지해 객체가 항상 유효한 상태가 되게 합니다(방어적 프로그래밍).
순서(안전성)
isinstance 검사(타입 검사)를 먼저 두는 이유: question이 문자열이 아닐 경우 .strip()을 호출하면 AttributeError 발생. 논리 연산자(or)는 좌측이 True이면 우측을 평가하지 않는 단락 평가(short-circuit)를 하므로, "not isinstance(...)"을 앞에 두면 안전하게 동작합니다.
예외 타입
코드에서는 ValueError를 사용. 타입 문제는 TypeError가 더 적합하며, 값(공백 등) 문제는 ValueError가 적합합니다. (둘을 분리하면 더 명확)

개선방향:
타입 검사
        if not isinstance(question, str):
            raise TypeError("question must be a str")
        question = question.strip()
        if not question:
            raise ValueError("문제는 비어 있을 수 없습니다.")


if not isinstance(choices, list) or len(choices) != 4:
raise ValueError("선택지는 반드시 4개여야 합니다.")

목적
choices가 리스트 타입인지 확인하고, 길이가 정확히 4인지 확인합니다. 설계상 4지선다 고정이므로 꼭 필요합니다.
순서(안전성)
리스트인지 확인한 뒤 len()을 호출하면 안전. 만약 choices가 None 같은 다른 타입이면 len() 호출 전 isinstance 검사로 보호해야 오류를 피할 수 있습니다.
개선
"list" 대신 "Sequence"나 "Iterable"을 허용하면 더 유연. 다만 문자열(str)은 Sequence라서 별도 처리 필요.

cleaned_choices = []
for choice in choices:
if not isinstance(choice, str) or not choice.strip():
raise ValueError("선택지는 비어 있을 수 없습니다.")
cleaned_choices.append(choice.strip())

목적
각 선택지가 문자열인지, 공백만으로 이루어지지 않았는지 검사합니다. 또한 strip()로 앞뒤 공백을 제거해 정리(clean)된 값을 저장합니다.
순서(안전성)
choice가 문자열인지 먼저 확인한 뒤 strip()를 호출하도록 되어 있어 안전합니다.
고려사항
동일한 검사(타입+비어있지 않음)를 for문으로 처리했지만 any()/all() 또는 리스트/제너레이터 표현으로 더 간단히 표현할 수 있습니다.
중복된 선택지나 지나치게 긴 선택지 같은 추가 검증을 할 수 있습니다.

if not isinstance(answer, int) or not (1 <= answer <= 4):
raise ValueError("정답은 1~4 사이의 번호여야 합니다.")

목적
정답이 정수인지, 그리고 1~4 범위인지 확인합니다.
설계적 주의
코드가 1-based 인덱스(1~4)를 사용하고 있음을 명시합니다. 파이썬 관습(리스트 인덱스)은 0-based이므로 혼동 주의.
타입 검사와 범위 검사 분리(예: TypeError vs ValueError)하면 더 명확.

if not isinstance(hint, str):
raise ValueError("힌트는 문자열이어야 합니다.")

목적
hint가 문자열인지 확인(기본값이 ""이므로 대부분 문제 없음). 이후 hint.strip()을 호출하므로 타입 검사가 필요합니다.
개선
hint는 선택사항이므로 None 허용을 고려하거나, 타입 검사 대신 str(hint)로 변환하는 방법도 있음.
속성 할당
self.question = question.strip()
self.choices = cleaned_choices
self.answer = answer
self.hint = hint.strip()

목적
검증된(정리된) 데이터를 인스턴스 변수로 저장. strip()는 앞뒤 공백 제거, cleaned_choices는 이미 strip된 항목들.

조건문(분기문) 작성의 일반 원칙(법칙) — 실전 팁과 예시 아래는 조건문을 읽기 쉽고 안전하게, 버그 없이 쓰기 위한 규칙들입니다.
먼저 실패 케이스를 빨리 처리하라 (Guard clauses / Fail-fast)
함수 맨 앞에서 잘못된 입력을 검사해 바로 raise/return 한다. 복잡한 중첩을 피할 수 있음.
예: if not valid: raise ValueError(...)

타입검사는 그 값을 실제로 사용하기 전에 하라
.strip(), len(), indexing 등 특정 타입에만 동작하는 연산을 수행하기 전에 isinstance로 확인.
안전한 순서: isinstance 검사 -> 실제 연산 수행

논리 연산의 단락평가(short-circuit)를 이해하고 활용하라
A and B: A가 False이면 B는 평가되지 않음.
A or B: A가 True이면 B는 평가되지 않음.
이를 이용해 안전한 조건문 순서를 구성한다(첫번째 검사로 대상을 제한).

조건은 가능한 한 간단하게 유지하라
복잡한 boolean 표현식은 변수로 분해하거나 의미있는 이름을 붙여라.
예: is_str = isinstance(x, str) is_not_empty = bool(x.strip()) if is_str else False if not (is_str and is_not_empty): raise ...

긍정 형태를 우선하라(가능하면)
if not ...와 같은 부정형 조건은 읽기 어렵다. 가능하면 긍정형으로 바꿔 가독성을 높임.
예: if question.strip(): ... 대신 if not question.strip(): raise ... (이건 예외 케이스라서 괜찮음)

예외 타입을 적절히 사용하라
타입 오류에는 TypeError, 값 오류에는 ValueError 등 표준 예외를 사용하면 디버깅이 쉬움.

의미 있는 에러 메시지를 제공하라
어떤 값이 잘못되었는지, 어떤 조건을 만족해야 하는지를 명확히 적는다.

중복을 피하고 재사용 가능한 검사로 묶어라
같은 검사 로직을 여러 곳에서 쓰면 함수로 분리. (예: validate_nonempty_str(x, name))

가능한 경우 표준 함수(all, any)을 활용하라
반복적 검사(for-loop) 대신 any/all + 제너레이터를 쓰면 코드가 간결해짐.
예: if any(not isinstance(c, str) or not c.strip() for c in choices): raise ...

사이드 이펙트가 있는 조건은 주의하라
조건 안에서 값을 변경하거나 I/O를 하면 읽기 어렵고 버그를 유발할 수 있음.


반복문(루프) 작성의 일반 원칙(법칙) — 실전 팁과 예시 반복문은 잘 쓰면 깔끔하지만, 잘못 쓰면 성능/버그 원인이 됩니다.
가능한 경우 for-in을 사용하라 (파이썬스러운 방식)
for item in iterable: ... 대신 range(len(iterable))로 인덱싱하는 스타일을 지양 (단, 인덱스가 필요하면 enumerate 사용)

인덱스가 필요하면 enumerate 사용
for i, item in enumerate(seq): ... — 인덱스와 값 모두 필요할 때 안전하고 가독성 좋음.

여러 시퀀스를 동시에 순회하려면 zip 사용
for a, b in zip(list1, list2): ...

리스트를 순회하면서 수정하지 마라
for item in lst: lst.remove(item) — 예측 불가능한 버그 유발. 대신 새로운 리스트에 결과를 수집하거나 리스트 컴프리헨션 사용.

반복문으로 검사할 때는 any()/all() 고려
any(...) : 조건을 만족하는 것이 하나라도 있으면 True (단락평가로 성능 좋음)
all(...) : 모든 원소가 조건을 만족해야 True

break/continue는 필요한 경우에만, 남발하지 마라
루프 흐름을 갑자기 바꾸므로 가독성 저하 가능.

루프의 시간복잡성을 고려하라
중첩 루프는 O(n^2) 될 수 있으니 큰 입력에서는 주의.

제너레이터 식을 활용해 메모리 절약
큰 리스트를 만들 필요가 없을 때는 (x for x in ...) 사용.

while은 조건이 명확할 때(상태 변화가 필요한 경우)만 사용
반복 횟수가 정해져 있으면 for가 안전.

루프에 입력 검증을 포함하지 마라(검증은 먼저)
입력검증을 루프 내부에 넣으면 루프가 중복되고 읽기 어려워짐. 검증은 앞에서 처리.

raise: 오류(예외)를 발생시킬 때 — 호출자에게 “이건 정상 흐름이 아니다”라고 알려야 할 때.
return: 함수(또는 메서드)를 정상적으로 끝내고 값을 돌려줄 때(또는 더 이상 처리할 필요가 없을 때).
break: 현재 루프(가장 안쪽 루프)를 즉시 종료할 때.
continue: 현재 반복의 남은 부분을 건너뛰고 다음 반복으로 넘어갈 때.

raise (예외 발생)
언제 사용하나
함수/메서드의 계약(contract)이 위반되었을 때(잘못된 인자 타입/값 등). 예: __init__에서 잘못된 인자일 때.
프로그램이 정상 흐름으로 복구할 수 없는 에러가 발생했을 때(파일 읽기 실패, 외부 API 에러 등).
호출자에게 처리 책임을 넘겨야 할 때(하위 레이어에서 상위 레이어로 에러 전달).
규칙/권장
예외는 예외적인 상황에 사용. 흔한 흐름 제어용으로 남발하지 말 것(성능·가독성 문제).
구체적인 예외 타입(TypeError, ValueError, IOError 등) 사용. 필요하면 커스텀 예외 정의.
에러 메시지는 문제와 기대값을 명확히 하라.
예외를 발생시키면 해당 함수는 즉시 종료되고 호출자로 전파된다(try/except로 잡을 수 있음).
예시 def set_age(age): if not isinstance(age, int): raise TypeError("age는 정수여야 합니다") if age < 0: raise ValueError("age는 음수일 수 없습니다") ...
return (함수 종료 및 값 반환)
언제 사용하나
정상적인 결과를 반환할 때.
더 이상 처리할 필요가 없고 함수에서 즉시 빠져나가고 싶을 때(guard clause / early return).
"못 찾음"이나 "처리 불필요"를 나타내기 위해 None이나 sentinel 값을 반환할 수 있음(설계에 따라).
규칙/권장
함수는 가능한 한 하나의 의미 있는 타입을 반환하도록 설계. None/값/예외를 같은 상황에서 혼용하는 것은 혼란을 초래.
잘못된 입력은 보통 raise로 처리(프로그램 오류), 찾을 수 없음 등 정상 흐름의 일부라면 return None이나 Optional 반환을 사용.
함수 초반에 유효성 검사 후 early return(guard clause)을 쓰면 중첩을 줄여 가독성 개선.
예시 def find_user(users, name): for u in users: if u.name == name: return u return None # 못 찾음은 None으로 표현
break / continue (루프 제어)
break: 루프 즉시 종료

현재 루프만 빠져나감(중첩 루프의 바깥 루프는 그대로 진행).
"찾았다"처럼 더 이상 루프를 돌 필요 없을 때 사용.
continue: 현재 반복의 남은 부분을 건너뛰고 다음 반복으로 진행

주로 유효성 검사에서 조건이 맞지 않으면 건너뛰고 싶을 때.
규칙/권장

break/continue는 루프의 흐름을 간단하게 만들 때 유용하지만 남발하면 읽기 어려워짐.
인덱스가 필요하면 enumerate 사용. 여러 시퀀스는 zip 사용.
루프에서 값을 찾았을 때 break 후 플래그를 검사하는 대신, 파이썬의 for-else 패턴을 고려: for x in seq: if cond(x): break else: # break로 빠져나오지 않은 경우(=못 찾음)

continue 예시
for item in items:
if not valid(item):
continue
process(item)

break + for-else 예시 (못 찾았을 때 처리)
for x in items:
if is_target(x):
print("찾음:", x)
break
else:
print("못 찾음")

중첩 루프에서 즉시 전체 탈출이 필요할 때

방법 1: 플래그 사용
found = False
for a in A:
for b in B:
if cond(a,b):
found = True
break
if found:
break

방법 2: 예외를 사용해 탈출(권장하지는 않음 — 하지만 여러 레벨을 한 번에 탈출할 때 실용적)
class Found(Exception): pass
try:
for a in A:
for b in B:
if cond(a,b):
raise Found(a,b)
except Found as e:
a,b = e.args

위의 예외 방식은 제어 흐름의 명확성을 해칠 수 있으니 문서화하고 신중히 사용.

raise vs return 선택 가이드라인
잘못된 인자(프로그래머 실수): raise(TypeError/ValueError)
예: 함수가 필수 인자가 없거나 타입이 맞지 않을 때.
요청은 정상이지만 결과가 없을 수 있음(검색 함수 등): return None 혹은 Optional 타입
예: find()가 못 찾는 것은 오류가 아닐 수 있음.
외부 시스템 실패(파일, 네트워크): raise(예외)
호출자가 복구/재시도/로그를 할 필요가 있음.
성능이 중요한 핫 루프에서 흔한 상태 분기에는 예외를 쓰지 말 것(예외는 비용이 큼).
기타 주의사항
finally 블록은 예외 발생/return와 관계없이 실행됨. return을 finally에 쓰면 반환값/예외를 덮어쓸 수 있으므로 주의. try: return 1 finally: return 2 # 예외/원래 반환을 덮어쓴다 — 피하자
API 설계 시 예외 사용 규칙을 문서화하라(어떤 상황에서 어떤 예외를 던지는지).
단위 테스트: 예외 케이스와 정상 케이스(early return 포함)를 모두 테스트하라.
짧은 예제 모음
유효성 검사에서 raise (guard clause)
def create_quiz(question, choices):
if not isinstance(question, str):
raise TypeError("question은 문자열")
if not choices:
raise ValueError("choices가 필요")
# 이후 정상 처리 및 return

검색 함수: return으로 결과 또는 None 반환
def search(nums, target):
for n in nums:
if n == target:
return n
return None

유효하지 않은 항목은 건너뛰고 처리
for item in items:
if not is_valid(item):
continue
handle(item)

중첩 루프에서 즉시 탈출(예: 첫 발견 시 처리)
found = None
for a in A:
for b in B:
if cond(a,b):
found = (a,b)
break
if found:
break
if found is None:
print("못 찾음")

기본 개념 — 함수(참조)를 인자로 넘기기
함수 이름 자체가 그 함수를 가리키는 값이므로 그대로 인자로 넘기면 됩니다.
def twice(x):
return x * 2

def apply(func, value):
return func(value)

print(apply(twice, 5))  # 10


enumerate가 반환하는 값 직접 보기
list(enumerate(choices, start=1))  # -> [(1, '사과'), (2, '바나나'), (3, '체리')]


시그니처
def init(self, question, choices, answer, hint=""):
question: 문제 문자열
choices: 선택지들을 담은 리스트(여기서는 반드시 4개)
answer: 정답 번호(1~4)
hint: 선택적인 힌트 문자열(기본값은 빈 문자열)
질문 검사
if not isinstance(question, str) or not question.strip(): raise ValueError("문제는 비어 있을 수 없습니다.")
question이 문자열인지 확인하고, strip()으로 앞뒤 공백을 제거했을 때 비어있지 않은지 검사합니다.
공백만 들어오는 문자열도 빈 것으로 간주해서 예외를 던집니다.
이유: 빈문제나 비문자열 입력을 방지하기 위함.
선택지 리스트 검사
if not isinstance(choices, list) or len(choices) != 4: raise ValueError("선택지는 반드시 4개여야 합니다.")
choices가 리스트인지, 길이가 정확히 4인지 검사합니다.
퀴즈 형식을 고정(선택지 4개)하려는 설계입니다.
각 선택지 검사 및 정리
cleaned_choices = [] for choice in choices: if not isinstance(choice, str) or not choice.strip(): raise ValueError("선택지는 비어 있을 수 없습니다.") cleaned_choices.append(choice.strip())
각 선택지가 문자열인지, 공백만으로 이루어지지 않았는지 검사합니다.
strip()으로 앞뒤 공백을 제거한 값을 cleaned_choices에 저장합니다(데이터 정리).
이유: 저장 전 불필요한 공백 제거 및 빈 선택지 방지.
정답 검사
if not isinstance(answer, int) or not (1 <= answer <= 4): raise ValueError("정답은 1~4 사이의 번호여야 합니다.")
정답은 정수여야 하고 1~4 범위 내여야 합니다.
설계상 정답 인덱스를 1-based(1~4)로 사용합니다. (주의: Python 관습은 0-based인 경우가 많음)
힌트 타입 검사
if not isinstance(hint, str): raise ValueError("힌트는 문자열이어야 합니다.")
hint가 문자열인지 확인하고, 이후 strip()으로 공백을 제거해서 저장합니다.
속성 설정
self.question = question.strip()
self.choices = cleaned_choices
self.answer = answer
self.hint = hint.strip()
검증을 통과한(정리된) 값을 인스턴스 속성으로 저장합니다.
self 는 해당 인스턴스를 가리키는 참조입니다.
예제 사용법

정상 생성:
q = Quiz("가장 큰 수는?", ["1", "2", "3", "4"], 4, "힌트 예시")
print(q.question)   # "가장 큰 수는?"
print(q.choices)    # ["1","2","3","4"]
print(q.answer)     # 4
print(q.hint)       # "힌트 예시"

예외 처리:
try:
q = Quiz("", ["a","b","c","d"], 1)
except ValueError as e:
print("오류:", e)

if not isinstance(question, str) or not question.strip():
raise ValueError("문제는 비어 있을 수 없습니다.")

목적
question이 문자열인지 확인하고(타입 검사), 공백을 제거했을 때 빈 문자열이 아닌지 확인(내용 검사)합니다.
빈 문제(또는 타입이 잘못된 입력)를 방지해 객체가 항상 유효한 상태가 되게 합니다(방어적 프로그래밍).
순서(안전성)
isinstance 검사(타입 검사)를 먼저 두는 이유: question이 문자열이 아닐 경우 .strip()을 호출하면 AttributeError 발생. 논리 연산자(or)는 좌측이 True이면 우측을 평가하지 않는 단락 평가(short-circuit)를 하므로, "not isinstance(...)"을 앞에 두면 안전하게 동작합니다.
예외 타입
코드에서는 ValueError를 사용. 타입 문제는 TypeError가 더 적합하며, 값(공백 등) 문제는 ValueError가 적합합니다. (둘을 분리하면 더 명확)
조건 2
if not isinstance(choices, list) or len(choices) != 4:
raise ValueError("선택지는 반드시 4개여야 합니다.")

목적
choices가 리스트 타입인지 확인하고, 길이가 정확히 4인지 확인합니다. 설계상 4지선다 고정이므로 꼭 필요합니다.
순서(안전성)
리스트인지 확인한 뒤 len()을 호출하면 안전. 만약 choices가 None 같은 다른 타입이면 len() 호출 전 isinstance 검사로 보호해야 오류를 피할 수 있습니다.
개선
"list" 대신 "Sequence"나 "Iterable"을 허용하면 더 유연. 다만 문자열(str)은 Sequence라서 별도 처리 필요.
조건 3 (반복문 내 검사)
cleaned_choices = []
for choice in choices:
if not isinstance(choice, str) or not choice.strip():
raise ValueError("선택지는 비어 있을 수 없습니다.")
cleaned_choices.append(choice.strip())

목적
각 선택지가 문자열인지, 공백만으로 이루어지지 않았는지 검사합니다. 또한 strip()로 앞뒤 공백을 제거해 정리(clean)된 값을 저장합니다.
순서(안전성)
choice가 문자열인지 먼저 확인한 뒤 strip()를 호출하도록 되어 있어 안전합니다.
고려사항
동일한 검사(타입+비어있지 않음)를 for문으로 처리했지만 any()/all() 또는 리스트/제너레이터 표현으로 더 간단히 표현할 수 있습니다.
중복된 선택지나 지나치게 긴 선택지 같은 추가 검증을 할 수 있습니다.
조건 4
if not isinstance(answer, int) or not (1 <= answer <= 4):
raise ValueError("정답은 1~4 사이의 번호여야 합니다.")

목적
정답이 정수인지, 그리고 1~4 범위인지 확인합니다.
설계적 주의
코드가 1-based 인덱스(1~4)를 사용하고 있음을 명시합니다. 파이썬 관습(리스트 인덱스)은 0-based이므로 혼동 주의.
타입 검사와 범위 검사 분리(예: TypeError vs ValueError)하면 더 명확.
조건 5
if not isinstance(hint, str):
raise ValueError("힌트는 문자열이어야 합니다.")

목적
hint가 문자열인지 확인(기본값이 ""이므로 대부분 문제 없음). 이후 hint.strip()을 호출하므로 타입 검사가 필요합니다.
개선
hint는 선택사항이므로 None 허용을 고려하거나, 타입 검사 대신 str(hint)로 변환하는 방법도 있음.
속성 할당
self.question = question.strip()
self.choices = cleaned_choices
self.answer = answer
self.hint = hint.strip()

목적
검증된(정리된) 데이터를 인스턴스 변수로 저장. strip()는 앞뒤 공백 제거, cleaned_choices는 이미 strip된 항목들.

조건문(분기문) 작성의 일반 원칙(법칙) — 실전 팁과 예시 아래는 조건문을 읽기 쉽고 안전하게, 버그 없이 쓰기 위한 규칙들입니다.
먼저 실패 케이스를 빨리 처리하라 (Guard clauses / Fail-fast)
함수 맨 앞에서 잘못된 입력을 검사해 바로 raise/return 한다. 복잡한 중첩을 피할 수 있음.
예: if not valid: raise ValueError(...)
타입검사는 그 값을 실제로 사용하기 전에 하라
.strip(), len(), indexing 등 특정 타입에만 동작하는 연산을 수행하기 전에 isinstance로 확인.
안전한 순서: isinstance 검사 -> 실제 연산 수행
논리 연산의 단락평가(short-circuit)를 이해하고 활용하라
A and B: A가 False이면 B는 평가되지 않음.
A or B: A가 True이면 B는 평가되지 않음.
이를 이용해 안전한 조건문 순서를 구성한다(첫번째 검사로 대상을 제한).
조건은 가능한 한 간단하게 유지하라
복잡한 boolean 표현식은 변수로 분해하거나 의미있는 이름을 붙여라.
예: is_str = isinstance(x, str) is_not_empty = bool(x.strip()) if is_str else False if not (is_str and is_not_empty): raise ...
긍정 형태를 우선하라(가능하면)
if not ...와 같은 부정형 조건은 읽기 어렵다. 가능하면 긍정형으로 바꿔 가독성을 높임.
예: if question.strip(): ... 대신 if not question.strip(): raise ... (이건 예외 케이스라서 괜찮음)
예외 타입을 적절히 사용하라
타입 오류에는 TypeError, 값 오류에는 ValueError 등 표준 예외를 사용하면 디버깅이 쉬움.
의미 있는 에러 메시지를 제공하라
어떤 값이 잘못되었는지, 어떤 조건을 만족해야 하는지를 명확히 적는다.
중복을 피하고 재사용 가능한 검사로 묶어라
같은 검사 로직을 여러 곳에서 쓰면 함수로 분리. (예: validate_nonempty_str(x, name))
가능한 경우 표준 함수(all, any)을 활용하라
반복적 검사(for-loop) 대신 any/all + 제너레이터를 쓰면 코드가 간결해짐.
예: if any(not isinstance(c, str) or not c.strip() for c in choices): raise ...
사이드 이펙트가 있는 조건은 주의하라
조건 안에서 값을 변경하거나 I/O를 하면 읽기 어렵고 버그를 유발할 수 있음.
반복문(루프) 작성의 일반 원칙(법칙) — 실전 팁과 예시 반복문은 잘 쓰면 깔끔하지만, 잘못 쓰면 성능/버그 원인이 됩니다.
가능한 경우 for-in을 사용하라 (파이썬스러운 방식)
for item in iterable: ... 대신 range(len(iterable))로 인덱싱하는 스타일을 지양 (단, 인덱스가 필요하면 enumerate 사용)
인덱스가 필요하면 enumerate 사용
for i, item in enumerate(seq): ... — 인덱스와 값 모두 필요할 때 안전하고 가독성 좋음.
여러 시퀀스를 동시에 순회하려면 zip 사용
for a, b in zip(list1, list2): ...
리스트를 순회하면서 수정하지 마라
for item in lst: lst.remove(item) — 예측 불가능한 버그 유발. 대신 새로운 리스트에 결과를 수집하거나 리스트 컴프리헨션 사용.
반복문으로 검사할 때는 any()/all() 고려
any(...) : 조건을 만족하는 것이 하나라도 있으면 True (단락평가로 성능 좋음)
all(...) : 모든 원소가 조건을 만족해야 True
break/continue는 필요한 경우에만, 남발하지 마라
루프 흐름을 갑자기 바꾸므로 가독성 저하 가능.
루프의 시간복잡성을 고려하라
중첩 루프는 O(n^2) 될 수 있으니 큰 입력에서는 주의.
제너레이터 식을 활용해 메모리 절약
큰 리스트를 만들 필요가 없을 때는 (x for x in ...) 사용.
while은 조건이 명확할 때(상태 변화가 필요한 경우)만 사용
반복 횟수가 정해져 있으면 for가 안전.
루프에 입력 검증을 포함하지 마라(검증은 먼저)
입력검증을 루프 내부에 넣으면 루프가 중복되고 읽기 어려워짐. 검증은 앞에서 처리.

init(self, question, choices, answer, hint="")
__init__(self, question: str, choices: Sequence[str], answer: int, hint: str = ""):

자동 호출 여부
__init__는 인스턴스를 만들 때 자동 호출된다: class C: def init(self, x): self.x = x c = C(10) # => __init__가 자동으로 실행되어 c.x == 10
반면 init은 그냥 일반 메서드: class C: def init(self, x): self.x = x c = C() # init는 자동 호출 안됨 c.init(10) # 직접 호출해야 동작
이름의 의미
__init__처럼 앞뒤로 두 개 이상의 밑줄(dunder, double underscore)을 갖는 이름은 파이썬에서 특별한 의미(스페셜 메서드)를 가지며 인터프리터가 특정 시점에 호출합니다(초기화, 표현, 비교 등).
단, 앞만 ''이고 뒤에 ''가 없으면 이름 맹글링(name mangling)이 발생할 수 있음(클래스 내부 private 흉내). __init__은 dunder 패턴이라 맹글링 대상 아님.
타입 힌트(annotations)의 차이
def init(self, question: str, choices: Sequence[str], answer: int, hint: str = "")
이는 단지 문서화와 정적 검사용입니다. 런타임에서 파이썬이 자동으로 타입을 체크하거나 변환하지 않습니다.
타입 힌트를 활용하려면 mypy 같은 도구로 정적 검사하거나, 런타임 검사 라이브러리(예: typeguard, pydantic)를 사용해야 합니다.
Sequence[str]를 쓰려면 from collections.abc import Sequence (또는 from typing import Sequence, Python 버전에 따라 선택).
기본값과 반환값
__init__은 반환값이 없어야 합니다(정상적으로는 None). 관습적으로 반환 타입 표기는 -> None으로 씁니다: def init(...) -> None:
일반 메서드 init는 원하는 값을 반환할 수 있습니다(return 사용 가능).
__new__와의 관계(간단히)
객체 생성 과정: __new__가 새 인스턴스를 만들고, 만들어진 인스턴스에 대해 __init__가 초기화를 수행합니다. 따라서 __init__는 인스턴스가 이미 만들어진 이후 호출되는 "초기화자"입니다.


        # 타입 검사
        if not isinstance(question, str):
            raise TypeError("question must be a str")
        question = question.strip()
        if not question:
            raise ValueError("문제는 비어 있을 수 없습니다.")

raise: 오류(예외)를 발생시킬 때 — 호출자에게 “이건 정상 흐름이 아니다”라고 알려야 할 때.
return: 함수(또는 메서드)를 정상적으로 끝내고 값을 돌려줄 때(또는 더 이상 처리할 필요가 없을 때).
break: 현재 루프(가장 안쪽 루프)를 즉시 종료할 때.
continue: 현재 반복의 남은 부분을 건너뛰고 다음 반복으로 넘어갈 때.
아래에서 언제, 왜 쓰는지 규칙과 주의사항, 실용 예제를 정리합니다.

raise (예외 발생)
언제 사용하나
함수/메서드의 계약(contract)이 위반되었을 때(잘못된 인자 타입/값 등). 예: __init__에서 잘못된 인자일 때.
프로그램이 정상 흐름으로 복구할 수 없는 에러가 발생했을 때(파일 읽기 실패, 외부 API 에러 등).
호출자에게 처리 책임을 넘겨야 할 때(하위 레이어에서 상위 레이어로 에러 전달).
규칙/권장
예외는 예외적인 상황에 사용. 흔한 흐름 제어용으로 남발하지 말 것(성능·가독성 문제).
구체적인 예외 타입(TypeError, ValueError, IOError 등) 사용. 필요하면 커스텀 예외 정의.
에러 메시지는 문제와 기대값을 명확히 하라.
예외를 발생시키면 해당 함수는 즉시 종료되고 호출자로 전파된다(try/except로 잡을 수 있음).
예시 def set_age(age): if not isinstance(age, int): raise TypeError("age는 정수여야 합니다") if age < 0: raise ValueError("age는 음수일 수 없습니다") ...
return (함수 종료 및 값 반환)
언제 사용하나
정상적인 결과를 반환할 때.
더 이상 처리할 필요가 없고 함수에서 즉시 빠져나가고 싶을 때(guard clause / early return).
"못 찾음"이나 "처리 불필요"를 나타내기 위해 None이나 sentinel 값을 반환할 수 있음(설계에 따라).
규칙/권장
함수는 가능한 한 하나의 의미 있는 타입을 반환하도록 설계. None/값/예외를 같은 상황에서 혼용하는 것은 혼란을 초래.
잘못된 입력은 보통 raise로 처리(프로그램 오류), 찾을 수 없음 등 정상 흐름의 일부라면 return None이나 Optional 반환을 사용.
함수 초반에 유효성 검사 후 early return(guard clause)을 쓰면 중첩을 줄여 가독성 개선.
예시 def find_user(users, name): for u in users: if u.name == name: return u return None # 못 찾음은 None으로 표현
break / continue (루프 제어)
break: 루프 즉시 종료

현재 루프만 빠져나감(중첩 루프의 바깥 루프는 그대로 진행).
"찾았다"처럼 더 이상 루프를 돌 필요 없을 때 사용.
continue: 현재 반복의 남은 부분을 건너뛰고 다음 반복으로 진행

주로 유효성 검사에서 조건이 맞지 않으면 건너뛰고 싶을 때.
규칙/권장

break/continue는 루프의 흐름을 간단하게 만들 때 유용하지만 남발하면 읽기 어려워짐.
인덱스가 필요하면 enumerate 사용. 여러 시퀀스는 zip 사용.
루프에서 값을 찾았을 때 break 후 플래그를 검사하는 대신, 파이썬의 for-else 패턴을 고려: for x in seq: if cond(x): break else: # break로 빠져나오지 않은 경우(=못 찾음)



Sequence는 "순서가 있는 시퀀스(열)"에 대한 추상 인터페이스(abstract base class)입니다. 리스트(list), 튜플(tuple), 문자열(str), range 등 인덱스 접근과 길이 측정을 지원하는 자료형들을 포괄합니다.
무엇인지, 어떤 역할을 하나
위치: collections.abc.Sequence (또는 typing.Sequence)
정의: Sequence는 len()과 getitem()을 최소한으로 제공하면 Sequence의 조건을 만족합니다. 즉, 길이를 알 수 있고 인덱스로 접근 가능한 객체라면 Sequence로 간주됩니다.
Sequence가 제공하는 편의 메서드(ABC가 구현해줌)
contains(self, x) (in 연산)
iter(self)
reversed(self)
index(value)
count(value) 이런 메서드는 실제 하위 클래스가 최소 메서드만 구현하면 ABC가 자동으로 제공합니다.
Sequence에 속하는(대표적인) 타입들
list, tuple, str, range, bytes, bytearray, memoryview, collections.abc.Sequence 구현체 등
주의: str은 Sequence[str]로 간주됩니다(각 요소가 길이 1의 str). 따라서 "choices: Sequence[str]"라고 적으면 문자열 하나도 허용되는 것으로 해석될 수 있습니다.

함수 시그니처에 적는 "매개변수: 타입"은 기본적으로 문서(문서화)와 정적 검사기(mypy 등)를 위한 힌트입니다. 파이썬 인터프리터가 자동으로 입력값의 타입을 강제하지는 않습니다.
즉, 타입 힌트를 적어도 아무 타입이나 넣으면 함수는 실행됩니다(런타임에서 오류가 나지 않음). 타입 힌트만으로는 타입 강제가 되지 않습니다.
타입을 런타임에서 강제하려면 별도의 런타임 검사(직접 isinstance 검사, 데코레이터, 또는 typeguard/pydantic 같은 라이브러리)를 사용해야 합니다.
실무 권장: 기본은 타입 힌트 + 정적 검사(mypy, pyright)로 코드 품질 유지. 외부 경계(입력 파싱, API 엔드포인트 등)에서는 런타임 검사를 적용하면 안전합니다.
왜 타입 힌트만으로 강제되지 않을까?

파이썬은 동적 타이핑(dynamically typed) 언어입니다. 변수는 런타임에 타입이 정해지고, 인터프리터는 타입 주석을 무시합니다(주석이 아니라 애노테이션이긴 하지만 기본 동작은 무시).
타입 힌트는 "이 함수는 이렇게 기대합니다"라는 계약을 표현하는 문서와 같고, 정적 분석 도구가 이를 읽어 코드의 잠재적 버그를 잡아줍니다. 하지만 런타임 비용과 유연성을 이유로 인터프리터가 자동으로 검사하지 않는 설계입니다.


기본 개념 — 함수(참조)를 인자로 넘기기
함수 이름 자체가 그 함수를 가리키는 값이므로 그대로 인자로 넘기면 됩니다.
def twice(x):
return x * 2

def apply(func, value):
return func(value)

print(apply(twice, 5))  # 10

호출(사용) 방법
인자로 받은 함수는 일반 함수처럼 호출합니다: func(arg1, arg2) def caller(f): return f(1, 2)

strip()은 파이썬 문자열에서 앞뒤의 불필요한 문자(기본은 공백 문자)를 제거하는 메서드입니다. 주요 특징과 예시를 간단히 정리합니다.
strip()은 양끝만 처리(중간 공백은 제거 안 함).

enumerate(self.choices, start=1)
enumerate는 내장 함수로 "열거자" iterator를 반환합니다.
enumerate(choices, start=1)가 생성하는 값들은 순서대로 (1, "사과"), (2, "바나나"), (3, "체리")라는 튜플들입니다.

왜 cls를 쓰는가? (classmethod의 의미)
cls는 호출된 클래스(Quiz 또는 서브클래스)를 가리킵니다. 즉 SubQuiz.from_dict(...) 하면 cls는 SubQuiz가 되고 SubQuiz(...)를 호출하므로 서브클래스 인스턴스를 생성.
만약 @staticmethod로 만들면 클래스 정보를 못 써서 서브클래스 친화성이 떨어짐.

self.state_file = Path(__file__).resolve().with_name("state.json")
file 예: "project/quiz.py"
Path(file) -> Path("project/quiz.py")
.resolve() -> Path("/home/user/project/quiz.py")
.with_name("state.json") -> Path("/home/user/project/state.json")
self.state_file는 이제 Path("/home/user/project/state.json")

if __name__ == "__main__":
    game = QuizGame()
    game.run()

if name == "main": 안의 코드는 그 파일을 직접 실행(python 파일.py)할 때만 실행되고, 다른 파일에서 import 하면 실행되지 않습니다.
비유

파일이 집이라고 하면, if 블록은 “문을 열고 직접 들어왔을 때만 켜는 전등” 같은 겁니다. 다른 사람이 창문으로 들여다보기(import)만 하면 전등은 안 켭니다.
간단 예

file a.py:
print("모듈 로드 됨")
if name == "main":
print("직접 실행 중!")

콘솔에서:
python a.py
→ 출력: 모듈 로드 됨
직접 실행 중!

다른 파일에서 import:
import a
→ 출력: 모듈 로드 됨
(if 블록의 "직접 실행 중!"은 출력되지 않음)

with open(...) as file:
with: 작업이 끝난 후 자원 정리를 자동으로 처리하는 문법

open(...): 파일을 여는 함수

as file: 열린 파일 객체에 file이라는 이름을 붙이는 것