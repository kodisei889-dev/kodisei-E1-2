# 나의 파이썬 & Git 학습 기록

## 목차

1. 파이썬 실행 환경과 명령어 문제 해결
2. Git 브랜치 생성 및 병합
3. 파이썬 클래스와 `__init__`
4. 타입 힌트와 Sequence
5. 입력값 검증과 방어적 프로그래밍
6. 조건문 작성 원칙
7. 반복문 작성 원칙
8. raise, return, break, continue의 차이
9. 함수 자체를 인자로 전달하기
10. enumerate()의 활용
11. strip()의 활용
12. classmethod와 cls의 의미
13. pathlib와 파일 경로 관리
14. `__name__ == "__main__"`의 의미
15. with 문과 파일 관리
16. 딕셔너리 get()과 중첩 함수
17. JSON 데이터 읽기와 저장하기
18. print()와 input()의 차이

---

# 1. 파이썬 실행 환경과 명령어 문제 해결

## 1-1. 파이썬 실행 문제 발견

파이썬 프로그램을 실행하기 위해 다음 명령어를 사용했다.

```powershell
python main.py
```

그런데 명령어를 실행하면 오류가 발생하면서 프로그램이 실행되지 않는 현상을 발견했다.

반면 다음 명령어를 사용하면 정상적으로 실행되었다.

```powershell
py main.py
```

처음에는 두 명령어가 같은 기능을 하는 것으로 생각했지만, 실제로는 파이썬 실행 파일을 찾는 경로와 연결 방식에 차이가 있을 수 있다는 사실을 알게 되었다.

## 1-2. 문제가 발생하는 원인

확인한 결과, 다음과 같은 원인이 있을 수 있었다.

- Windows의 앱 실행 별칭이 활성화되어 있다.
- Microsoft Store와 연결된 Python 실행 별칭이 잡혀 있다.
- 실제 Python 실행 파일의 경로가 PATH 환경 변수에서 우선적으로 잡히지 않는다.

특히 WindowsApps 폴더에 있는 python.exe가 실제 파이썬 실행 파일이 아니라 Microsoft Store와 연결된 실행 별칭으로 작동할 수 있다는 점을 알게 되었다.

## 1-3. PowerShell에서 임시로 해결하는 방법

설정창이 제한되어 있어 Windows의 앱 실행 별칭을 직접 변경할 수 없었다.

그래서 현재 PowerShell 창에서만 `python`을 `py`처럼 사용하도록 임시 별칭을 설정했다.

```powershell
Set-Alias python py
```

이 명령어를 실행한 뒤 다음과 같이 확인했다.

```powershell
python --version
```

정상적으로 파이썬 버전이 출력되었다.

이후 다음 두 명령어 모두 정상적으로 실행되는 것을 확인했다.

```powershell
python main.py
py main.py
```

이 방법은 Windows 설정 자체를 변경하는 것이 아니라 현재 열려 있는 PowerShell 세션에만 적용되는 임시 해결 방법이다.

## 1-4. 원래 상태로 되돌리는 방법

설정한 별칭을 제거하려면 다음 명령어를 사용한다.

```powershell
Remove-Item Alias:python
```

이후 `python` 명령어는 다시 기존 실행 경로를 따르게 된다.

실제로 별칭을 제거한 뒤 `python`이 정상 실행되지 않는 것도 확인했다.

## 1-5. Python 실행 파일의 실제 경로 확인

파이썬이 어떤 실행 파일을 통해 실행되는지 확인하는 방법도 공부했다.

먼저 다음 명령어를 사용한다.

```powershell
where.exe python
```

여기서 중요한 점은 `where`가 아니라 `where.exe`라고 정확하게 입력하는 것이다.

PowerShell에서는 `where`라는 이름이 다른 명령어의 별칭으로 사용될 수 있기 때문에 실행 파일을 정확하게 지정하는 것이 좋다.

또한 `where.exe`를 사용해 확인한 경로가 실제 Python 실행 파일인지 주의해서 살펴봐야 한다.

예를 들어 다음과 같은 경로가 나올 수 있다.

```text
C:\Users\사용자이름\AppData\Local\Microsoft\WindowsApps\python.exe
```

이 경로를 확인하면 Python이 WindowsApps의 실행 별칭 또는 Microsoft Store 연결을 통해 잡혀 있을 가능성이 있다는 것을 알 수 있다.

한편 다음 명령어로 등록된 Python 설치 경로를 확인할 수 있다.

```powershell
py -0p
```

이 명령어를 통해 실제 Python 인터프리터의 설치 경로를 확인할 수 있다.

예를 들어 다음과 같은 경로가 나올 수 있다.

```text
C:\Users\사용자이름\AppData\Roaming\uv\python\cpython-3.15.2-windows-x86_64-none\python.exe
```

실제 실행 파일의 전체 경로를 알고 있다면 다음과 같이 직접 실행할 수도 있다.

```powershell
& "C:\Users\사용자이름\AppData\Roaming\uv\python\cpython-3.15.2-windows-x86_64-none\python.exe" main.py
```

반대로 WindowsApps 경로에 있는 실행 별칭을 직접 사용하면 기대한 대로 실행되지 않을 수 있다.

```powershell
& "C:\Users\사용자이름\AppData\Local\Microsoft\WindowsApps\python.exe" main.py
```

따라서 실행 파일을 확인할 때는 `where.exe python`과 `py -0p`의 결과를 구분해서 살펴보는 것이 중요하다는 점을 배웠다.

### 핵심 정리

- `python main.py`: PATH와 실행 별칭의 영향을 받는다.
- `py main.py`: Python Launcher를 통해 실행한다.
- `Set-Alias python py`: 현재 PowerShell 창에서만 임시로 별칭을 설정한다.
- `Remove-Item Alias:python`: 설정한 별칭을 제거한다.
- `where.exe python`: 명령어 검색 경로를 확인한다.
- `py -0p`: 등록된 Python 인터프리터 경로를 확인한다.

이번 문제를 해결하면서 프로그램 실행 오류가 반드시 코드 자체의 문제에서 발생하는 것은 아니라는 사실을 알게 되었다. 실행 환경과 경로 설정도 함께 확인해야 한다는 점을 이해했다.

---

# 2. Git 브랜치 생성 및 병합

Git을 사용하면서 브랜치를 생성하고, 작업한 내용을 다른 브랜치에 병합하는 과정을 실습했다.

## 2-1. 브랜치 생성

먼저 새로운 브랜치를 생성했다.

```bash
git branch feature-readme
```

이 명령어는 `feature-readme`라는 브랜치를 생성하지만, 현재 작업 위치를 해당 브랜치로 변경하지는 않는다.

## 2-2. 브랜치 이동

생성한 브랜치로 이동하려면 다음 명령어를 사용한다.

```bash
git checkout feature-readme
```

브랜치를 생성하면서 동시에 이동하려면 두 명령어를 한 줄로 사용할 수 있다.

```bash
git checkout -b feature-readme
```

이 명령어는 브랜치 생성과 이동을 동시에 처리한다.

## 2-3. 브랜치에서 파일 수정 및 커밋

`feature-readme` 브랜치로 이동한 다음 README 파일을 수정했다.

파일을 수정하고 저장한 뒤 Git에 변경 내용을 추가했다.

```bash
git add readme.md
```

이후 커밋을 진행했다.

```bash
git commit -m "README 기능 설명 보완"
```

이렇게 하면 수정한 README 파일의 내용이 현재 브랜치에 기록된다.

## 2-4. main 브랜치로 이동

작업을 마친 뒤 원래 브랜치인 main으로 돌아갔다.

```bash
git checkout main
```

## 2-5. 브랜치 병합

feature-readme 브랜치에서 작업한 내용을 main 브랜치에 병합했다.

```bash
git merge feature-readme
```

이 명령어는 현재 위치한 브랜치에 지정한 브랜치의 변경 사항을 병합한다.

따라서 main 브랜치에 있는 상태에서 실행해야 main에 feature-readme의 작업 내용이 반영된다.

## 2-6. GitHub에 올리기

병합한 내용을 GitHub의 원격 저장소에 업로드했다.

```bash
git push origin main
```

여기서 `origin`은 원격 저장소의 이름이고, `main`은 업로드할 브랜치다.

## 2-7. 작업 결과 확인

브랜치 목록 확인:

```bash
git branch
```

전체 커밋 로그 확인:

```bash
git log --oneline --graph --all
```

Git 상태 확인:

```bash
git status
```

특히 `git log --oneline --graph --all`을 사용하면 브랜치의 분기와 병합 과정을 그래프 형태로 확인할 수 있다는 점을 알게 되었다.

## 2-8. 병합 취소

병합 진행 중 아직 병합 커밋이 완료되지 않은 상태라면 다음 명령어로 병합을 취소할 수 있다.

```bash
git merge --abort
```

## 2-9. 작업이 끝난 브랜치 삭제

브랜치 작업이 끝났다면 다음 명령어로 삭제할 수 있다.

```bash
git branch -d feature-readme
```

`-d`는 병합이 완료된 브랜치를 안전하게 삭제할 때 사용하는 옵션이다.

## 2-10. 이미 존재하는 브랜치를 생성하려고 할 때

같은 이름의 브랜치가 이미 존재하는데 다시 생성하려고 하면 다음 오류가 발생한다.

```text
fatal: a branch named 'feature-readme' already exists
```

이 경우에는 새로 생성할 필요 없이 기존 브랜치로 이동하면 된다.

```bash
git checkout feature-readme
```

## 2-11. 수정 중인 파일 때문에 브랜치 이동이 안 되는 경우

작업 중인 파일에 변경 사항이 남아 있으면 브랜치 이동이 제한될 수 있다.

이럴 때는 다음과 같이 처리할 수 있다.

- 변경 사항을 먼저 커밋한다.
- 변경 사항을 정리한 뒤 이동한다.

작업 내용을 저장하거나 정리하지 않은 상태에서 무작정 브랜치를 이동하려고 하면 문제가 발생할 수 있다는 점을 알게 되었다.

## 2-12. Git 편집기에서 빠져나오기

Git 병합 과정에서 편집기가 열릴 수 있다.

이때 기본 커밋 메시지를 그대로 사용해 병합을 완료하려면 다음 순서로 진행한다.

1. `Esc`를 누른다.
2. `:wq`를 입력한다.
3. Enter를 누른다.

이렇게 하면 내용을 저장하고 편집기를 종료하며, 병합 커밋이 완료된다.

반대로 편집기만 강제로 종료하려면 다음 명령어를 사용한다.

1. `Esc`를 누른다.
2. `:q!`를 입력한다.
3. Enter를 누른다.

다만 이 경우에는 저장하지 않고 종료하기 때문에 병합 처리 의도에 따라 결과가 달라질 수 있다.

일반적으로 병합 커밋 메시지를 그대로 사용하려는 상황에서는 `:wq`가 적절하다.

## 2-13. Git 로그 화면에서 빠져나오기

`git log` 명령어를 실행하면 로그 화면에 들어갈 수 있다.

이 화면에서 빠져나오려면 다음 키를 누른다.

```text
q
```

### 핵심 정리

| 명령어 | 기능 |
|---|---|
| `git branch 이름` | 브랜치 생성 |
| `git checkout 이름` | 브랜치 이동 |
| `git checkout -b 이름` | 생성과 이동 동시 수행 |
| `git add 파일명` | 변경 파일 스테이징 |
| `git commit -m "메시지"` | 커밋 |
| `git merge 이름` | 브랜치 병합 |
| `git push origin main` | 원격 저장소에 업로드 |
| `git branch` | 브랜치 확인 |
| `git log --oneline --graph --all` | 커밋 그래프 확인 |
| `git status` | 현재 상태 확인 |
| `git merge --abort` | 진행 중인 병합 취소 |
| `git branch -d 이름` | 병합된 브랜치 삭제 |

---

# 3. 파이썬 클래스와 __init__

파이썬 클래스를 공부하면서 가장 먼저 이해해야 할 부분은 `__init__`의 역할이었다.

## 3-1. init과 __init__의 차이

다음 두 코드는 이름이 비슷하지만 동작이 다르다.

일반 메서드인 init:

```python
class C:
    def init(self, x):
        self.x = x

c = C()
c.init(10)
```

이 경우 `init()`은 일반 메서드이기 때문에 객체를 생성한다고 자동으로 호출되지 않는다.

직접 `c.init(10)`을 실행해야 동작한다.

반면 특별 메서드인 `__init__`은 다음과 같다.

```python
class C:
    def __init__(self, x):
        self.x = x

c = C(10)
```

객체를 생성할 때 `__init__`이 자동으로 호출되어 `self.x`에 10이 저장된다.

즉, 클래스의 인스턴스를 생성할 때 자동으로 초기화 작업을 수행하려면 `__init__`을 사용해야 한다.

## 3-2. Dunder 메서드의 의미

`__init__`처럼 앞뒤에 밑줄 두 개가 붙은 이름을 Dunder(Double Underscore)라고 한다.

이러한 이름은 파이썬에서 특별한 의미를 가진다.

대표적인 역할은 다음과 같다.

- 초기화
- 객체 표현
- 객체 비교
- 연산자 동작

파이썬 인터프리터는 특정 상황에서 이러한 특별 메서드를 호출한다.

참고로 이름 앞에만 밑줄 두 개가 있고 뒤에는 밑줄 두 개가 없는 경우에는 클래스 내부에서 이름 맹글링(Name Mangling)이 발생할 수 있다.

예를 들어 `__value`와 같은 이름은 클래스 내부에서 이름이 변환될 수 있다.

하지만 `__init__`은 앞뒤에 밑줄 두 개가 있는 Dunder 패턴이므로 이름 맹글링의 대상이 아니다.

## 3-3. __new__와 __init__의 관계

객체 생성 과정에는 `__new__`와 `__init__`이 관여한다.

- `__new__`: 새로운 인스턴스를 생성한다.
- `__init__`: 생성된 인스턴스를 초기화한다.

즉, `__new__`가 객체를 만들고, 만들어진 객체에 대해 `__init__`이 초기화 작업을 수행한다.

따라서 `__init__`은 이미 만들어진 인스턴스를 초기화하는 역할을 한다.

## 3-4. __init__의 반환값

`__init__`은 반환값이 없어야 한다.

일반적으로 반환 타입을 다음과 같이 표시한다.

```python
def __init__(self, question: str) -> None:
    self.question = question
```

`None`을 반환하는 것이 정상적인 사용 방식이다.

반면 일반 메서드인 `init()`은 `return`을 사용해 원하는 값을 반환할 수 있다.

## 3-5. Quiz 클래스에 적용하기

퀴즈 프로그램을 만들면서 다음과 같은 클래스 구조를 공부했다.

```python
from collections.abc import Sequence

class Quiz:
    def __init__(
        self,
        question: str,
        choices: Sequence[str],
        answer: int,
        hint: str = ""
    ) -> None:
        self.question = question
        self.choices = choices
        self.answer = answer
        self.hint = hint
```

여기서 각 매개변수의 의미는 다음과 같다.

- `self`: 현재 생성된 인스턴스를 가리킨다.
- `question`: 문제 문자열이다.
- `choices`: 선택지들을 담은 시퀀스다.
- `answer`: 정답 번호다.
- `hint`: 선택적인 힌트 문자열이며 기본값은 빈 문자열이다.

클래스의 인스턴스를 만들 때 전달한 값이 `__init__`을 통해 각 인스턴스 속성에 저장된다.

---

# 4. 타입 힌트와 Sequence

## 4-1. 타입 힌트란?

함수나 메서드의 매개변수와 반환값에 타입 정보를 표시하는 것을 타입 힌트(Type Hint)라고 한다. 이러한 타입 정보는 애너테이션(Annotation) 문법을 활용하여 작성한다.

예를 들어 다음과 같이 작성한다.

```python
def add(a: int, b: int) -> int:
    return a + b
```

여기서 의미는 다음과 같다.

- `a: int`: a는 정수로 사용하기를 기대한다.
- `b: int`: b는 정수로 사용하기를 기대한다.
- `-> int`: 반환값은 정수로 사용하기를 기대한다.

엄밀하게 구분하면 애너테이션은 타입 외의 다양한 정보도 표시할 수 있는 문법이고, 타입 힌트는 그중 타입 정보를 표현하는 용도다.

하지만 타입 힌트를 작성했다고 해서 파이썬이 실제 입력값의 타입을 자동으로 검사하거나 변환하지는 않는다.

## 4-2. 타입 힌트만으로는 타입이 강제되지 않는다

다음 코드를 살펴보자.

```python
def f(x: int) -> None:
    print(x)

f("문자열")
```

타입 힌트에는 정수라고 표시했지만 문자열을 전달해도 파이썬은 기본적으로 실행을 허용한다.

즉, 타입 힌트는 문서화와 정적 검사를 위한 정보이지, 런타임에서 타입을 강제하는 기능은 아니다.

파이썬은 동적 타이핑(Dynamically Typed) 언어이기 때문이다.

## 4-3. 타입 힌트를 활용하는 방법

타입 힌트를 실제로 활용하려면 별도의 도구를 사용할 수 있다.

대표적으로 다음과 같은 방법이 있다.

- mypy: 정적 타입 검사
- pyright: 정적 타입 검사
- typeguard: 런타임 타입 검사
- pydantic: 데이터 검증과 변환 등에 활용

예를 들어 typeguard를 사용하면 다음과 같이 작성할 수 있다.

```python
from typeguard import typechecked

@typechecked
def f(x: int) -> None:
    print(x)

f("문자열")
```

이 경우 타입이 맞지 않으면 다음과 같은 형태의 오류가 발생한다.

```text
TypeError: type of argument "x" must be int; got str instead
```

따라서 일반적으로는 타입 힌트와 정적 검사 도구를 함께 사용하고, 외부 입력을 받는 부분에서는 별도의 런타임 검사를 적용하는 것이 좋다는 점을 알게 되었다.

## 4-4. Sequence란?

`Sequence`는 순서가 있는 시퀀스에 대한 추상 인터페이스(Abstract Base Class)다.

다음과 같이 가져올 수 있다.

```python
from collections.abc import Sequence
```

또는 다음과 같이 사용할 수도 있다.

```python
from typing import Sequence
```

Sequence는 길이를 확인하고 인덱스로 접근할 수 있는 자료형을 포괄한다.

대표적인 자료형은 다음과 같다.

- list
- tuple
- str
- range
- bytes
- bytearray
- memoryview
- Sequence 인터페이스를 구현한 자료형

## 4-5. Sequence의 기본 조건

Sequence는 기본적으로 다음 기능을 지원한다.

```python
len(value)
value[index]
```

즉, 길이를 알 수 있고 인덱스를 통해 요소에 접근할 수 있는 것이 핵심이다.

Sequence의 추상 기본 클래스가 제공하는 편의 메서드도 있다.

- `__contains__`: in 연산
- `__iter__`: 반복자 생성
- `__reversed__`: 역순 반복
- `index(value)`: 값의 위치 확인
- `count(value)`: 특정 값의 개수 확인

이러한 기능은 하위 클래스가 필요한 최소 메서드를 구현하면 ABC가 제공하는 방식으로 사용할 수 있다.

## 4-6. list, Sequence, Iterable의 차이

함수에서 어떤 자료형을 요구할 것인지 결정하는 기준도 공부했다.

**list를 사용하는 경우**

함수 내부에서 반드시 리스트 전용 기능을 사용해야 한다면 `list[str]`로 명시하는 것이 좋다.

예를 들어 다음과 같은 기능이 필요할 때다.

```python
choices.append("새로운 선택지")
choices.pop()
```

**Iterable을 사용하는 경우**

리스트나 튜플뿐만 아니라 제너레이터도 허용하고 싶고, 단순히 순회만 하면 된다면 `Iterable[T]`가 적절하다.

**Sequence를 사용하는 경우**

인덱스 접근과 `len()`을 사용하지만 데이터를 변경하지 않는다면 `Sequence[T]`가 적절하다.

## 4-7. Sequence 사용 시 주의사항

중요하게 알아야 할 점은 문자열도 Sequence라는 것이다.

```python
choices: Sequence[str]
```

이렇게 작성하면 `"abcd"`와 같은 문자열도 Sequence[str]로 간주될 수 있다.

따라서 선택지 목록을 받아야 하는 상황에서 문자열 하나가 잘못 전달되는 것을 방지하려면 별도의 검사가 필요하다.

## 4-8. Quiz의 choices에는 무엇이 적절할까?

퀴즈 프로그램의 선택지는 순서가 있고, 보통 4개로 고정되어 있다.

따라서 다음 두 가지 설계가 가능하다.

```python
choices: list[str]
```

리스트만 허용하고 싶을 때 사용한다.

```python
choices: Sequence[str]
```

리스트와 튜플 등을 모두 허용하고 싶을 때 사용한다.

다만 Sequence를 사용한다면 문자열 하나가 전달되는 상황을 별도로 막아야 한다.

### 핵심 정리

| 자료형 | 적절한 사용 상황 |
|---|---|
| `list[T]` | 리스트만 허용하고 변경 작업도 필요할 때 |
| `Sequence[T]` | 길이와 인덱스 접근이 필요하고 수정하지 않을 때 |
| `Iterable[T]` | 단순히 순회만 하면 될 때 |

## 4-9. 함수와 메서드에서 self의 사용

파이썬에서 모든 함수에 `self`를 붙여야 하는 것은 아니다.

`self`는 클래스 내부의 인스턴스 메서드에서 현재 객체 자신을 참조하기 위해 사용하는 매개변수다.

함수의 종류와 사용 목적에 따라 `self`의 필요 여부가 달라진다.

### ① 일반 함수

클래스 외부에서 정의하는 일반 함수에는 `self`가 필요하지 않다.

```python
def add(a: int, b: int) -> int:
    return a + b

print(add(10, 20))
```

실행 결과:

```text
30
```

일반 함수는 객체에 소속되지 않으므로 `self`를 전달할 필요가 없다.

### ② 인스턴스 메서드

클래스 내부에서 정의하고 객체의 데이터를 다루는 메서드다.

일반적으로 첫 번째 매개변수에 `self`를 작성한다.

```python
class Quiz:
    def __init__(self, question):
        self.question = question

    def show_question(self):
        print(self.question)

quiz = Quiz("파이썬이란?")
quiz.show_question()
```

실행 결과:

```text
파이썬이란?
```

여기서 `self`는 현재 메서드를 호출한 객체 자신을 의미한다.

예를 들어 다음과 같이 사용할 수 있다.

- `self.question`: 현재 객체가 가지고 있는 question 변수에 접근한다.
- `self.show_question()`: 현재 객체의 다른 메서드를 호출한다.

인스턴스 메서드를 호출하면 파이썬이 해당 인스턴스를 첫 번째 인자로 자동 전달한다.

따라서 다음과 같이 작성한다.

```python
def show_question(self):
    print(self.question)
```

호출할 때는 다음과 같이 사용한다.

```python
quiz.show_question()
```

호출할 때 `self`를 직접 전달하지 않아도 된다.

### ③ 정적 메서드(@staticmethod)

클래스 내부에 정의하지만 객체의 데이터인 `self`를 사용하지 않는 메서드다.

이때는 `self`를 작성하지 않아도 된다.

```python
class Quiz:
    @staticmethod
    def abab(i: int, j: str) -> None:
        ab = i * j
        print(ab)

quiz = Quiz()
quiz.abab(1, "안녕")
```

실행 결과:

```text
안녕
```

`@staticmethod`를 사용하면 인스턴스가 첫 번째 인자로 자동 전달되지 않는다.

따라서 객체의 상태에 의존하지 않는 독립적인 기능을 클래스 내부에 구성할 때 사용할 수 있다.

### ④ 일반 메서드와 정적 메서드의 차이

| 구분 | 인스턴스 메서드 | 정적 메서드 |
|---|---|---|
| 선언 방식 | `def 함수(self):` | `@staticmethod` + `def 함수():` |
| self 필요 여부 | 필요 | 불필요 |
| 인스턴스 정보 접근 | 가능 | 직접 접근 불가능 |
| 인스턴스 자동 전달 | O | X |
| 주요 용도 | 객체의 데이터와 기능 처리 | 객체 상태와 관계없는 기능 처리 |

### ⑤ self를 사용해야 하는 경우

다음과 같이 구분하면 이해하기 쉽다.

- `self.question`처럼 객체가 가진 변수에 접근해야 한다면 `self`를 사용한다.
- 객체의 상태를 변경하거나 객체의 다른 메서드를 호출한다면 일반적으로 `self`를 사용한다.
- 객체의 데이터와 관계없이 독립적인 기능을 수행한다면 `@staticmethod`를 고려한다.
- 클래스와도 관계없는 독립적인 기능이라면 일반 함수를 사용한다.

추가로 `self`는 파이썬의 예약어가 아니다. 관례적으로 사용하는 이름이다.

기술적으로 다른 이름을 사용할 수도 있지만, 특별한 이유가 없다면 `self`라고 작성하는 것이 일반적이다.

### ⑥ self를 작성하지 않았을 때 발생하는 오류

클래스 내부에 다음과 같이 메서드를 작성했다고 가정한다.

```python
class Quiz:
    def abab(i: int, j: str):
        ab = i * j
        print(ab)

    def __init__(self):
        self.abab(1, "안녕")
```

이때 `self.abab(1, "안녕")`으로 호출하면 오류가 발생한다.

```text
TypeError: Quiz.abab() takes 2 positional arguments but 3 were given
```

그 이유는 인스턴스 메서드를 호출할 때 파이썬이 인스턴스 자신을 첫 번째 인자로 자동 전달하기 때문이다.

실제로는 다음과 같이 전달되는 것과 같다.

```python
abab(self, 1, "안녕")
```

하지만 기존 함수는 `i`, `j` 두 개의 매개변수만 정의했기 때문에 세 개의 인자를 전달받아 오류가 발생한다.

이 문제를 해결하는 방법은 두 가지다.

**방법 1. self 추가하기**

```python
class Quiz:
    def abab(self, i: int, j: str):
        ab = i * j
        print(ab)

    def __init__(self):
        self.abab(1, "안녕")
```

**방법 2. @staticmethod 사용하기**

```python
class Quiz:
    @staticmethod
    def abab(i: int, j: str):
        ab = i * j
        print(ab)

    def __init__(self):
        self.abab(1, "안녕")
```

두 방법 모두 정상적으로 실행된다.

다만 `abab()` 함수가 `self`를 전혀 사용하지 않기 때문에 정적 메서드로 작성하는 방법도 적절하다.

### 핵심 정리

- 모든 함수에 `self`를 붙이는 것은 아니다.
- 일반 함수에는 `self`가 필요하지 않다.
- 인스턴스 메서드는 첫 번째 매개변수에 일반적으로 `self`를 사용한다.
- `@staticmethod`를 사용하면 `self` 없이 클래스 내부에 메서드를 작성할 수 있다.
- 인스턴스 메서드를 호출하면 파이썬이 인스턴스 자신을 첫 번째 인자로 자동 전달한다.
- `self`는 예약어가 아니라 관례적으로 사용하는 이름이다.

이번 내용을 통해 타입 힌트는 타입 정보를 표시하는 기능이고, `self`는 클래스의 인스턴스를 참조하는 기능이라는 점을 구분해서 이해하게 되었다.

# 5. 입력값 검증과 방어적 프로그래밍

클래스에 데이터를 저장하기 전에 입력값이 올바른지 확인하는 과정이 중요하다는 것을 배웠다.

이를 방어적 프로그래밍(Defensive Programming)이라고 이해했다.

객체가 생성된 이후에는 항상 유효한 상태를 유지하도록 입력값을 검증하는 것이다.

## 5-1. 문제 문자열 검사

```python
if not isinstance(question, str) or not question.strip():
    raise ValueError("문제는 비어 있을 수 없습니다.")
```

이 코드는 두 가지를 확인한다.

1. question이 문자열인지 검사한다.
2. 앞뒤 공백을 제거했을 때 빈 문자열인지 검사한다.

따라서 다음과 같은 입력을 방지할 수 있다.

```python
question = ""
question = "     "
question = 123
```

## 5-2. isinstance 검사를 먼저 하는 이유

문자열이 아닌 값에 `.strip()`을 사용하면 오류가 발생할 수 있다.

예를 들어 정수에는 문자열 메서드인 `.strip()`이 존재하지 않는다.

따라서 타입 검사를 먼저 해야 한다.

```python
if not isinstance(question, str) or not question.strip():
```

여기에는 단락 평가(Short-circuit)라는 개념도 적용되어 있다.

`or`는 왼쪽 조건이 True이면 오른쪽 조건을 평가하지 않는다.

따라서 question이 문자열이 아니라면 오른쪽의 `strip()`은 실행되지 않는다.

## 5-3. 예외 타입을 구분하기

타입이 잘못된 경우에는 `TypeError`를 사용하는 것이 적절하고, 값 자체가 잘못된 경우에는 `ValueError`를 사용하는 것이 더 명확하다.

따라서 다음과 같이 분리할 수 있다.

```python
if not isinstance(question, str):
    raise TypeError("question must be a str")

question = question.strip()

if not question:
    raise ValueError("문제는 비어 있을 수 없습니다.")
```

이렇게 하면 타입 오류와 값 오류를 구분할 수 있다.

## 5-4. 선택지 개수 검사

```python
if not isinstance(choices, list) or len(choices) != 4:
    raise ValueError("선택지는 반드시 4개여야 합니다.")
```

이 코드는 다음 두 가지를 검사한다.

- choices가 리스트인지 확인한다.
- 선택지 개수가 정확하게 4개인지 확인한다.

우리 퀴즈 프로그램은 4지선다 형식으로 설계했기 때문에 필요한 검사다.

리스트인지 먼저 검사하고 `len()`을 호출하는 이유도 안전성 때문이다.

만약 choices가 None이라면 `len(None)`에서 오류가 발생하기 때문이다.

다만 list 대신 Sequence나 Iterable을 허용하면 더 유연한 구조로 만들 수 있다. 이때 문자열도 Sequence라는 점은 별도로 고려해야 한다.

## 5-5. 각 선택지 검사 및 정리

```python
cleaned_choices = []

for choice in choices:
    if not isinstance(choice, str) or not choice.strip():
        raise ValueError("선택지는 비어 있을 수 없습니다.")

    cleaned_choices.append(choice.strip())
```

각 선택지가 문자열인지 확인하고, 공백만으로 이루어져 있지 않은지 검사한다.

이후 `.strip()`을 사용해 앞뒤 공백을 제거한 값을 새로운 리스트에 저장한다.

이렇게 하면 입력된 데이터를 그대로 저장하는 것이 아니라 정리된 데이터를 저장할 수 있다.

예를 들어 다음과 같은 입력이 들어왔다고 가정한다.

```python
choices = [" 사과 ", " 바나나 ", " 체리 ", " 포도 "]
```

정리된 결과는 다음과 같다.

```python
["사과", "바나나", "체리", "포도"]
```

또한 이 검사는 다음과 같이 간결하게 작성할 수도 있다.

```python
if any(
    not isinstance(choice, str) or not choice.strip()
    for choice in choices
):
    raise ValueError("선택지는 비어 있을 수 없습니다.")
```

`any()`를 사용하면 하나라도 잘못된 선택지가 있는지 확인할 수 있다.

추가적으로 다음과 같은 검증도 고려할 수 있다.

- 중복된 선택지가 있는지 확인
- 지나치게 긴 선택지가 있는지 확인

## 5-6. 정답 번호 검사

```python
if not isinstance(answer, int) or not (1 <= answer <= 4):
    raise ValueError("정답은 1~4 사이의 번호여야 합니다.")
```

이 코드는 정답이 정수인지, 그리고 1부터 4 사이의 범위인지 검사한다.

여기서 중요한 점은 우리 프로그램이 1부터 시작하는 번호 체계를 사용한다는 것이다.

이를 1-based 인덱스라고 한다.

반면 파이썬 리스트의 인덱스는 기본적으로 0부터 시작하는 0-based 방식이다.

따라서 정답 번호를 리스트 인덱스로 사용할 때는 혼동하지 않도록 주의해야 한다.

또한 파이썬에서는 bool이 int의 하위 타입이기 때문에 `isinstance(True, int)`가 True가 될 수 있다는 점도 기억해야 한다. 정수만 허용하려면 추가 검사가 필요하다.

## 5-7. 힌트 타입 검사

```python
if not isinstance(hint, str):
    raise ValueError("힌트는 문자열이어야 합니다.")
```

hint가 문자열인지 확인한다.

기본값이 빈 문자열이기 때문에 대부분 정상적으로 처리되지만, 외부에서 잘못된 타입을 전달할 가능성도 있으므로 검사가 필요하다.

이후 `.strip()`을 호출하므로 타입 검사를 먼저 하는 것이 안전하다.

hint가 선택사항이므로 None도 허용할 것인지 설계 단계에서 고려할 수 있다.

또한 타입 검사를 하지 않고 `str(hint)`로 변환하는 방법도 있지만, 이 경우 잘못된 입력을 조용히 문자열로 바꾸게 되므로 의도에 맞게 선택해야 한다.

## 5-8. 검증한 데이터 저장하기

```python
self.question = question.strip()
self.choices = cleaned_choices
self.answer = answer
self.hint = hint.strip()
```

모든 검증이 끝난 데이터를 인스턴스 속성에 저장한다.

여기서 `self`는 현재 생성된 인스턴스를 가리키는 참조다.

- `self.question`: 앞뒤 공백이 제거된 문제
- `self.choices`: 정리된 선택지 리스트
- `self.answer`: 검증된 정답 번호
- `self.hint`: 앞뒤 공백이 제거된 힌트

이렇게 하면 객체 내부에 저장되는 데이터가 일정한 규칙을 따르게 된다.

## 5-9. Quiz 클래스의 전체 구조

위에서 공부한 내용을 하나로 합치면 다음과 같다.

```python
from collections.abc import Sequence


class Quiz:
    def __init__(
        self,
        question: str,
        choices: Sequence[str],
        answer: int,
        hint: str = ""
    ) -> None:

        # 문제 타입 검사
        if not isinstance(question, str):
            raise TypeError("question must be a str")

        question = question.strip()

        if not question:
            raise ValueError("문제는 비어 있을 수 없습니다.")

        # 선택지 타입 및 개수 검사
        if isinstance(choices, (str, bytes)) or not isinstance(choices, Sequence):
            raise TypeError("choices는 시퀀스여야 합니다.")

        if len(choices) != 4:
            raise ValueError("선택지는 반드시 4개여야 합니다.")

        # 선택지 내용 검사 및 정리
        cleaned_choices = []

        for choice in choices:
            if not isinstance(choice, str) or not choice.strip():
                raise ValueError("선택지는 비어 있을 수 없습니다.")

            cleaned_choices.append(choice.strip())

        # 정답 검사
        if isinstance(answer, bool) or not isinstance(answer, int):
            raise TypeError("정답은 정수여야 합니다.")

        if not 1 <= answer <= 4:
            raise ValueError("정답은 1~4 사이의 번호여야 합니다.")

        # 힌트 검사
        if not isinstance(hint, str):
            raise TypeError("힌트는 문자열이어야 합니다.")

        # 검증된 데이터 저장
        self.question = question
        self.choices = cleaned_choices
        self.answer = answer
        self.hint = hint.strip()
```

이 코드는 입력 검증과 데이터 정리 과정을 이해하기 위한 통합 예제다.

## 5-10. 정상적으로 객체 생성하기

```python
q = Quiz(
    "가장 큰 수는?",
    ["1", "2", "3", "4"],
    4,
    "힌트 예시"
)

print(q.question)
print(q.choices)
print(q.answer)
print(q.hint)
```

출력 결과:

```text
가장 큰 수는?
['1', '2', '3', '4']
4
힌트 예시
```

## 5-11. 예외 처리하기

```python
try:
    q = Quiz("", ["a", "b", "c", "d"], 1)

except ValueError as e:
    print("오류:", e)
```

빈 문자열을 전달했기 때문에 ValueError가 발생하고, except에서 해당 오류를 처리한다.

---

# 6. 조건문 작성 원칙

조건문을 작성할 때는 단순히 실행 여부를 결정하는 것뿐만 아니라 가독성과 안전성을 함께 고려해야 한다는 점을 배웠다.

## 6-1. 실패 케이스를 먼저 처리하기

이를 Guard Clause 또는 Fail-fast라고 한다.

잘못된 입력이 들어오면 함수의 초반에서 바로 예외를 발생시키거나 반환한다.

```python
if not valid:
    raise ValueError("잘못된 입력입니다.")
```

이렇게 하면 여러 조건문이 중첩되는 것을 줄일 수 있다.

## 6-2. 타입 검사는 실제 사용 전에 하기

다음과 같은 연산을 하기 전에 타입을 확인하는 것이 좋다.

- `.strip()`
- `len()`
- 인덱스 접근
- 특정 자료형의 메서드 호출

안전한 순서는 다음과 같다.

```text
타입 검사
    ↓
값 검사
    ↓
실제 연산 수행
```

## 6-3. 단락 평가 이해하기

논리 연산자에는 단락 평가가 적용된다.

`and`의 경우:

```python
A and B
```

A가 False이면 B를 평가하지 않는다.

`or`의 경우:

```python
A or B
```

A가 True이면 B를 평가하지 않는다.

이를 이용하면 안전한 조건문을 작성할 수 있다.

## 6-4. 조건을 간단하게 유지하기

복잡한 Boolean 표현식은 변수로 분리하는 것이 좋다.

예를 들어 다음과 같이 작성할 수 있다.

```python
is_str = isinstance(x, str)
is_not_empty = bool(x.strip()) if is_str else False

if not (is_str and is_not_empty):
    raise ValueError("잘못된 값입니다.")
```

조건에 의미 있는 이름을 붙이면 코드를 이해하기 쉬워진다.

## 6-5. 긍정 형태 우선하기

가능하면 긍정 형태로 조건을 작성하는 것이 가독성에 도움이 된다.

다만 잘못된 입력을 빠르게 처리하는 Guard Clause에서는 다음과 같은 부정형도 적절하다.

```python
if not question.strip():
    raise ValueError("문제는 비어 있을 수 없습니다.")
```

## 6-6. 예외 타입 적절하게 사용하기

- `TypeError`: 자료형이 잘못된 경우
- `ValueError`: 자료형은 맞지만 값이 잘못된 경우
- `IOError` 또는 관련 파일 예외: 파일 입출력 과정의 문제

적절한 예외 타입을 사용하면 디버깅이 쉬워진다.

## 6-7. 의미 있는 에러 메시지 작성하기

단순히 오류가 발생했다는 메시지보다는 어떤 값이 잘못되었는지, 어떤 조건을 만족해야 하는지 알려주는 것이 좋다.

```python
raise ValueError("선택지는 반드시 4개여야 합니다.")
```

## 6-8. 중복 검사 로직 재사용하기

같은 검사를 여러 곳에서 반복한다면 별도의 함수로 분리할 수 있다.

예를 들어 다음과 같다.

```python
def validate_nonempty_str(value, name):
    if not isinstance(value, str):
        raise TypeError(f"{name}은 문자열이어야 합니다.")

    if not value.strip():
        raise ValueError(f"{name}은 비어 있을 수 없습니다.")
```

## 6-9. any()와 all() 활용하기

반복적인 검사는 `any()`와 `all()`을 활용하면 간결해질 수 있다.

```python
if any(
    not isinstance(c, str) or not c.strip()
    for c in choices
):
    raise ValueError("잘못된 선택지가 있습니다.")
```

## 6-10. 조건문 안에서 부작용 주의하기

조건문 안에서 값을 변경하거나 파일 입출력 등의 작업을 수행하면 코드를 이해하기 어려워질 수 있다.

따라서 조건 판단과 실제 작업을 가능한 한 분리하는 것이 좋다.

---

# 7. 반복문 작성 원칙

반복문은 데이터를 처리할 때 매우 중요하지만 잘못 사용하면 버그나 성능 문제를 일으킬 수 있다.

## 7-1. 가능한 경우 for-in 사용하기

파이썬에서는 다음과 같은 방식이 일반적으로 권장된다.

```python
for item in iterable:
    print(item)
```

반면 다음과 같이 인덱스로 접근하는 방식은 꼭 필요한 경우가 아니라면 지양한다.

```python
for i in range(len(iterable)):
    print(iterable[i])
```

## 7-2. 인덱스가 필요하면 enumerate 사용하기

인덱스와 값을 동시에 사용해야 한다면 `enumerate()`가 적절하다.

```python
for i, item in enumerate(seq):
    print(i, item)
```

## 7-3. 여러 시퀀스를 동시에 순회하려면 zip 사용하기

```python
for a, b in zip(list1, list2):
    print(a, b)
```

두 개 이상의 시퀀스를 같은 순서로 처리할 때 사용할 수 있다.

## 7-4. 리스트를 순회하면서 수정하지 않기

다음과 같은 코드는 주의해야 한다.

```python
for item in lst:
    lst.remove(item)
```

반복하는 도중 리스트의 크기나 위치가 바뀌면서 예상하지 못한 동작이 발생할 수 있다.

대신 새로운 리스트에 결과를 수집하거나 리스트 컴프리헨션을 사용하는 것이 좋다.

## 7-5. any()와 all() 활용하기

`any()`는 조건을 만족하는 항목이 하나라도 있으면 True를 반환한다.

`all()`은 모든 항목이 조건을 만족해야 True를 반환한다.

두 함수 모두 조건을 만족하거나 만족하지 않는 결과가 확정되면 더 이상 평가하지 않는 단락 평가를 활용한다.

## 7-6. break와 continue 남발하지 않기

두 명령어는 반복문의 흐름을 변경한다.

필요한 경우에는 유용하지만 지나치게 사용하면 코드 흐름을 파악하기 어려워진다.

## 7-7. 시간복잡도 고려하기

중첩 반복문은 입력 크기에 따라 O(n²)의 시간복잡도를 가질 수 있다.

따라서 데이터가 많아지는 상황에서는 반복문의 구조와 실행 횟수를 고려해야 한다.

## 7-8. 제너레이터 식 활용하기

큰 리스트를 새로 만들 필요가 없다면 제너레이터 식을 사용할 수 있다.

```python
(x for x in iterable)
```

필요한 값을 하나씩 생성하기 때문에 불필요한 메모리 사용을 줄일 수 있다.

## 7-9. while은 조건이 명확할 때 사용하기

반복 횟수가 정해져 있다면 for가 일반적으로 더 안전하다.

반면 특정 상태가 바뀔 때까지 반복해야 하는 경우에는 while이 적절하다.

## 7-10. 입력 검증은 반복문 전에 처리하기

반복문 내부에 입력 검증을 넣으면 같은 검사가 반복되고 코드가 복잡해질 수 있다.

따라서 가능하면 반복문을 실행하기 전에 입력값을 검증하는 것이 좋다.

---

# 8. raise, return, break, continue의 차이

네 가지 명령어는 모두 실행 흐름에 영향을 주지만 역할이 서로 다르다.

## 8-1. raise: 예외 발생

`raise`는 정상적인 실행 흐름이 아니라는 사실을 호출자에게 알릴 때 사용한다.

### 사용하는 상황

- 잘못된 인자 타입이 전달된 경우
- 잘못된 값이 전달된 경우
- 파일 읽기 실패
- 외부 API 오류
- 호출자에게 오류 처리를 넘겨야 하는 경우

예를 들어 다음과 같다.

```python
def set_age(age):
    if not isinstance(age, int):
        raise TypeError("age는 정수여야 합니다.")

    if age < 0:
        raise ValueError("age는 음수일 수 없습니다.")
```

### 사용 원칙

- 예외적인 상황에 사용한다.
- 일반적인 흐름 제어용으로 남발하지 않는다.
- 구체적인 예외 타입을 사용한다.
- 오류 메시지는 문제와 기대값을 명확하게 표현한다.

예외가 발생하면 해당 함수의 실행은 즉시 중단되고 호출자에게 전달된다.

호출자는 try/except로 예외를 처리할 수 있다.

## 8-2. return: 함수 종료 및 값 반환

`return`은 함수를 정상적으로 종료하고 결과를 반환할 때 사용한다.

또한 더 이상 처리할 필요가 없을 때 함수에서 빠져나오는 용도로 사용할 수 있다.

이를 Early Return이라고 한다.

예를 들어 검색 함수는 다음과 같이 작성할 수 있다.

```python
def find_user(users, name):
    for user in users:
        if user.name == name:
            return user

    return None
```

사용자를 찾으면 해당 객체를 반환하고, 찾지 못하면 None을 반환한다.

### 사용 원칙

- 정상적인 결과를 반환할 때 사용한다.
- 더 이상 처리할 필요가 없다면 조기에 반환할 수 있다.
- 반환 타입을 가능한 한 일관되게 유지한다.
- 잘못된 입력은 일반적으로 raise로 처리한다.
- 찾을 수 없는 상황이 정상적인 경우라면 None이나 Optional 반환을 고려한다.

같은 상황에서 None, 값, 예외를 혼용하면 호출자가 결과를 이해하기 어려워질 수 있다.

## 8-3. break: 반복문 즉시 종료

`break`는 현재 실행 중인 가장 안쪽 반복문을 즉시 종료한다.

예를 들어 원하는 값을 찾았다면 더 이상 반복할 필요가 없으므로 사용할 수 있다.

중첩 반복문에서 break를 사용하면 가장 안쪽 반복문만 종료된다.

## 8-4. continue: 현재 반복 건너뛰기

`continue`는 현재 반복의 남은 부분을 실행하지 않고 다음 반복으로 넘어간다.

예를 들어 유효하지 않은 항목을 건너뛸 때 사용할 수 있다.

```python
for item in items:
    if not valid(item):
        continue

    process(item)
```

유효하지 않은 항목은 처리하지 않고 다음 항목으로 이동한다.

## 8-5. break와 for-else

파이썬에는 `for-else`라는 문법이 있다.

반복문이 break로 종료되지 않고 정상적으로 끝났을 때 else 블록이 실행된다.

```python
for x in items:
    if is_target(x):
        print("찾음:", x)
        break
else:
    print("못 찾음")
```

이 코드는 플래그를 별도로 만들지 않고도 검색 결과를 처리할 수 있다.

## 8-6. 중첩 반복문에서 전체 탈출하기

중첩 반복문에서 가장 안쪽 반복문뿐만 아니라 바깥쪽 반복문까지 빠져나오고 싶을 수 있다.

### 방법 1. 플래그 사용

```python
found = False

for a in A:
    for b in B:
        if cond(a, b):
            found = True
            break

    if found:
        break
```

안쪽 반복문에서 값을 찾으면 found를 True로 변경하고, 바깥쪽 반복문에서도 해당 값을 확인해 종료한다.

### 방법 2. 예외 사용

```python
class Found(Exception):
    pass

try:
    for a in A:
        for b in B:
            if cond(a, b):
                raise Found(a, b)

except Found as e:
    a, b = e.args
```

사용자 정의 예외를 발생시켜 여러 단계의 반복문을 한 번에 빠져나오는 방법이다.

다만 일반적인 반복문 제어에 예외를 사용하는 것은 제어 흐름을 복잡하게 만들 수 있으므로 신중하게 사용해야 한다.

## 8-7. raise와 return 선택 기준

| 상황 | 적절한 방법 |
|---|---|
| 잘못된 인자 타입 | raise TypeError |
| 잘못된 인자 값 | raise ValueError |
| 검색 결과 발견 | return 결과 |
| 검색 결과 없음 | return None 또는 Optional |
| 외부 시스템 실패 | raise |
| 정상적으로 함수 종료 | return |
| 반복문 즉시 종료 | break |
| 현재 반복 건너뛰기 | continue |

## 8-8. 추가 주의사항: finally

`finally` 블록은 예외 발생 여부나 return 여부와 관계없이 실행된다.

따라서 다음과 같은 코드는 주의해야 한다.

```python
def example():
    try:
        return 1
    finally:
        return 2
```

이 경우 finally 안의 return이 원래 반환값을 덮어쓴다.

또한 원래 발생하려던 예외도 덮어쓸 수 있다.

따라서 finally 블록 안에 return을 작성하는 것은 피하는 것이 좋다.

API를 설계할 때는 어떤 상황에서 어떤 예외가 발생하는지 문서화하고, 단위 테스트에서도 정상 상황과 예외 상황을 모두 확인해야 한다.

## 8-9. 실전 예제 모음

### 입력 검증에서 raise 사용

```python
def create_quiz(question, choices):
    if not isinstance(question, str):
        raise TypeError("question은 문자열이어야 합니다.")

    if not choices:
        raise ValueError("choices가 필요합니다.")

    # 이후 정상 처리 및 return
```

### 검색 함수에서 return 사용

```python
def search(nums, target):
    for n in nums:
        if n == target:
            return n

    return None
```

### 유효하지 않은 항목 건너뛰기

```python
for item in items:
    if not is_valid(item):
        continue

    handle(item)
```

### 중첩 반복문에서 첫 번째 발견 시 종료

```python
found = None

for a in A:
    for b in B:
        if cond(a, b):
            found = (a, b)
            break

    if found is not None:
        break

if found is None:
    print("못 찾음")
```

---

# 9. 함수 자체를 인자로 전달하기

파이썬에서는 함수 이름 자체가 해당 함수를 가리키는 값이다.

따라서 함수를 다른 함수의 인자로 전달할 수 있다.

## 9-1. 기본 개념

```python
def twice(x):
    return x * 2


def apply(func, value):
    return func(value)


print(apply(twice, 5))
```

출력 결과:

```text
10
```

여기서 `twice`라는 함수 자체를 `apply()`에 전달했다.

`apply()` 내부에서는 전달받은 함수의 이름인 `func`를 사용해 호출한다.

## 9-2. 함수 호출 방법

함수를 인자로 전달받았다면 일반 함수처럼 호출하면 된다.

```python
def caller(f):
    return f(1, 2)
```

즉, 함수 자체를 전달할 때는 괄호를 붙이지 않고, 실제로 실행할 때는 괄호를 붙인다.

```python
caller(my_function)
```

이 개념은 콜백 함수나 함수형 프로그래밍을 이해하는 데도 중요한 기초가 된다.

---

# 10. enumerate()의 활용

`enumerate()`는 반복 가능한 객체를 순회하면서 인덱스와 값을 함께 얻을 수 있도록 해주는 파이썬 내장 함수다.

## 10-1. 기본 사용법

```python
choices = ["사과", "바나나", "체리"]

for index, choice in enumerate(choices):
    print(index, choice)
```

기본적으로 인덱스는 0부터 시작한다.

## 10-2. 시작 번호 지정하기

퀴즈 프로그램처럼 선택지를 1번부터 표시하고 싶다면 다음과 같이 작성한다.

```python
for index, choice in enumerate(choices, start=1):
    print(index, choice)
```

이렇게 하면 1부터 시작하는 번호를 얻을 수 있다.

## 10-3. enumerate가 반환하는 값 확인하기

```python
list(enumerate(choices, start=1))
```

결과:

```python
[
    (1, "사과"),
    (2, "바나나"),
    (3, "체리")
]
```

즉, enumerate는 순서대로 `(인덱스, 값)` 형태의 튜플을 생성하는 반복자를 반환한다.

## 10-4. 왜 enumerate를 사용하는가?

반복문에서 다음과 같이 작성할 수도 있다.

```python
for i in range(len(choices)):
    print(i + 1, choices[i])
```

하지만 enumerate를 사용하면 인덱스와 값을 동시에 가져올 수 있어 코드가 더 간결하고 읽기 쉽다.

---

# 11. strip()의 활용

`strip()`은 파이썬 문자열의 앞뒤에 있는 불필요한 문자를 제거하는 메서드다.

기본적으로 앞뒤 공백 문자를 제거한다.

```python
text = "   Hello Python   "

print(text.strip())
```

출력 결과:

```text
Hello Python
```

중요한 점은 `strip()`이 문자열의 양끝만 처리한다는 것이다.

문자열 중간에 있는 공백은 제거하지 않는다.

예를 들어 다음과 같다.

```python
text = "Hello   Python"

print(text.strip())
```

출력 결과:

```text
Hello   Python
```

따라서 입력값의 앞뒤 공백을 제거하고 싶을 때 유용하다.

퀴즈 프로그램에서는 문제, 선택지, 힌트 등을 저장하기 전에 `strip()`을 사용해 불필요한 공백을 제거했다.

---

# 12. classmethod와 cls의 의미

클래스 메서드에서 `cls`를 사용하는 이유를 공부했다.

## 12-1. cls란?

`cls`는 클래스 자체를 가리키는 매개변수다.

일반 인스턴스 메서드에서 `self`가 현재 객체를 가리키는 것처럼, 클래스 메서드에서는 `cls`가 호출된 클래스를 가리킨다.

```python
class Quiz:
    @classmethod
    def from_dict(cls, data):
        return cls(...)
```

## 12-2. 왜 cls를 사용하는가?

클래스 메서드는 상속 관계에서도 유용하다.

예를 들어 Quiz 클래스를 상속받은 SubQuiz가 있다고 가정한다.

```python
class Quiz:
    @classmethod
    def from_dict(cls, data):
        return cls(...)
```

다음과 같이 호출하면 된다.

```python
SubQuiz.from_dict(data)
```

이때 cls는 Quiz가 아니라 SubQuiz를 가리킨다.

따라서 `cls(...)`를 실행하면 SubQuiz의 인스턴스를 생성할 수 있다.

## 12-3. staticmethod와의 차이

`@staticmethod`를 사용하면 클래스 정보를 자동으로 전달받지 않는다.

따라서 호출된 클래스에 따라 다른 인스턴스를 생성하는 등의 상속 친화적인 동작을 구현하기에는 classmethod가 더 적합하다.

---

# 13. pathlib와 파일 경로 관리

파이썬에서 파일 경로를 다룰 때 `pathlib` 모듈을 사용할 수 있다는 점을 공부했다.

다음 코드를 살펴보자.

```python
self.state_file = Path(__file__).resolve().with_name("state.json")
```

이 코드는 현재 파이썬 파일이 있는 위치를 기준으로 `state.json` 파일의 경로를 만든다.

## 13-1. Path(__file__)

`__file__`은 현재 파이썬 파일의 경로를 나타낸다.

예를 들어 다음과 같다고 가정한다.

```text
project/quiz.py
```

다음 코드를 실행하면 Path 객체가 만들어진다.

```python
Path(__file__)
```

결과:

```text
Path("project/quiz.py")
```

## 13-2. resolve()

```python
Path(__file__).resolve()
```

`resolve()`는 경로를 절대 경로로 변환한다.

예를 들어 다음과 같이 바뀔 수 있다.

```text
/home/user/project/quiz.py
```

## 13-3. with_name()

```python
Path(__file__).resolve().with_name("state.json")
```

`with_name()`은 기존 경로의 파일 이름을 새로운 이름으로 바꾼다.

예를 들어 다음과 같다.

```text
기존:
 /home/user/project/quiz.py

변경:
 /home/user/project/state.json
```

따라서 최종적으로 다음 경로가 만들어진다.

```python
self.state_file = Path("/home/user/project/state.json")
```

즉, 현재 실행 위치에 영향을 받지 않고 파이썬 파일이 있는 폴더를 기준으로 상태 파일을 관리할 수 있다는 점을 이해했다.

---

# 14. __name__ == "__main__"의 의미

파이썬 파일의 아래 코드를 공부했다.

```python
if __name__ == "__main__":
    game = QuizGame()
    game.run()
```

이 코드는 해당 파이썬 파일을 직접 실행했을 때만 내부 코드가 실행되도록 하는 역할을 한다.

## 14-1. 직접 실행하는 경우

예를 들어 다음과 같이 실행한다.

```bash
python a.py
```

이때 a.py의 `__name__` 값은 `"__main__"`이 된다.

따라서 조건문 안의 코드가 실행된다.

## 14-2. 다른 파일에서 import 하는 경우

다른 파이썬 파일에서 다음과 같이 작성했다고 가정한다.

```python
import a
```

이 경우 a.py는 직접 실행된 것이 아니라 다른 파일에 의해 불러와진 것이다.

따라서 a.py의 `__name__` 값은 `"a"`가 된다.

그러므로 다음 조건은 False가 된다.

```python
if __name__ == "__main__":
```

결과적으로 조건문 내부의 코드는 실행되지 않는다.

다만 조건문 바깥에 작성된 코드는 모듈을 불러오는 과정에서 실행될 수 있다.

## 14-3. 비유로 이해하기

파이썬 파일을 하나의 집이라고 생각하면 된다.

`if __name__ == "__main__":`은 직접 문을 열고 집에 들어왔을 때만 전등을 켜는 장치와 같다.

다른 사람이 창문으로 집 안을 들여다보는 것처럼 import만 했다면 전등은 켜지지 않는다.

## 14-4. 실습 예제

a.py:

```python
print("모듈 로드 됨")

if __name__ == "__main__":
    print("직접 실행 중!")
```

직접 실행:

```bash
python a.py
```

출력:

```text
모듈 로드 됨
직접 실행 중!
```

다른 파일에서 import:

```python
import a
```

출력:

```text
모듈 로드 됨
```

직접 실행 중!이라는 문구는 출력되지 않는다.

이러한 구조를 사용하면 다른 파일에서 모듈을 불러올 때 불필요한 프로그램 실행을 방지할 수 있다.

---

# 15. with 문과 파일 관리

파일을 열고 작업한 다음 자동으로 정리하는 방법을 공부했다.

```python
with open(...) as file:
    ...
```

각 요소의 의미는 다음과 같다.

- `with`: 작업이 끝난 후 자원을 자동으로 정리하도록 하는 문법
- `open(...)`: 파일을 여는 함수
- `as file`: 열린 파일 객체에 file이라는 이름을 붙인다.

가장 중요한 점은 with 블록이 끝나면 파일이 자동으로 닫힌다는 것이다.

따라서 파일을 열고 닫는 작업을 직접 관리하는 부담을 줄일 수 있다.

---

# 16. 딕셔너리 get()과 중첩 함수

프로그램의 상태 데이터를 불러오는 과정에서 다음과 같은 코드를 공부했다.

```python
score = data.get("best_score", data.get("high_score"))
```

이 코드는 딕셔너리에서 `best_score`를 먼저 확인하고, 해당 키가 없으면 `high_score`를 가져오는 구조다.

## 16-1. get()의 기본 구조

```python
딕셔너리.get("찾을 키", "없을 때 사용할 값")
```

첫 번째 인자로 전달한 키가 존재하면 해당 값을 반환한다.

키가 없으면 두 번째 인자로 전달한 기본값을 반환한다.

## 16-2. best_score가 있는 경우

```python
data = {
    "best_score": 100,
    "high_score": 80
}

score = data.get("best_score", data.get("high_score"))

print(score)
```

출력:

```text
100
```

`best_score`가 존재하기 때문에 100을 가져온다.

## 16-3. best_score가 없는 경우

```python
data = {
    "high_score": 80
}

score = data.get("best_score", data.get("high_score"))

print(score)
```

출력:

```text
80
```

`best_score`가 없으므로 `high_score`의 값인 80을 가져온다.

## 16-4. 두 키 모두 없는 경우

```python
data = {}

score = data.get("best_score", data.get("high_score"))

print(score)
```

출력:

```text
None
```

두 키가 모두 존재하지 않기 때문에 None이 반환된다.

## 16-5. get() 안에 또 다른 get() 사용하기

위의 코드는 get() 안에 또 다른 get()을 넣은 중첩 구조다.

파이썬에서는 함수 중첩에 이론적으로 정해진 횟수 제한이 없다.

예를 들어 다음과 같이 3중 중첩도 가능하다.

```python
score = data.get(
    "best_score",
    data.get(
        "high_score",
        data.get("old_score", 0)
    )
)
```

실행 순서는 다음과 같다.

1. best_score가 있는지 확인한다.
2. 없으면 high_score를 확인한다.
3. 없으면 old_score를 확인한다.
4. 모두 없으면 0을 반환한다.

## 16-6. 여러 함수를 중첩하기

다음 코드를 살펴보자.

```python
print(str(len(data.get("quizzes", []))))
```

이 코드에는 여러 함수가 중첩되어 있다.

각 함수의 역할은 다음과 같다.

- `data.get("quizzes", [])`: quizzes 데이터를 가져온다.
- `len()`: 데이터의 길이를 확인한다.
- `str()`: 결과를 문자열로 변환한다.
- `print()`: 결과를 출력한다.

실행 순서는 가장 안쪽 함수부터 바깥쪽 함수 순서다.

```text
data.get("quizzes", [])
        ↓
len(결과)
        ↓
str(결과)
        ↓
print(결과)
```

## 16-7. 함수 중첩이 많을수록 좋은 것은 아니다

다음 코드는 실행할 수 있지만 중첩이 많아 한눈에 이해하기 어려울 수 있다.

```python
print(str(len(data.get("quizzes", []))))
```

이럴 때는 다음처럼 나누어 작성할 수 있다.

```python
quizzes = data.get("quizzes", [])
count = len(quizzes)
result = str(count)

print(result)
```

이렇게 작성하면 각 단계의 결과를 확인하기 쉽다.

### 내가 기억할 원칙

- 간단한 함수 중첩은 적극적으로 사용해도 좋다.
- 중첩이 깊어져 이해하기 어려우면 변수로 분리한다.
- 다른 사람이 코드를 봤을 때 실행 순서를 쉽게 파악할 수 있어야 한다.
- 코드가 실행되는 것도 중요하지만, 나중에 내가 다시 봤을 때 이해할 수 있는 것도 중요하다.

---

# 17. JSON 데이터 읽기와 저장하기

프로그램의 상태 데이터를 저장하고 불러오는 과정에서 JSON을 공부했다.

특히 `json.load()`와 `json.dump()`의 차이를 확실하게 구분해야 한다.

## 17-1. json.load()와 json.dump()의 차이

가장 중요한 차이는 데이터의 이동 방향이다.

| 구분 | json.load() | json.dump() |
|---|---|---|
| 기능 | JSON 파일 읽기 | JSON 파일 저장 |
| 방향 | JSON → Python | Python → JSON |
| 목적 | 데이터 불러오기 | 데이터 저장하기 |

쉽게 기억하면 다음과 같다.

- load = 불러오기
- dump = 내보내기

## 17-2. json.dump() 사용하기

퀴즈 프로그램의 상태를 저장하는 `save_state()` 함수에서 다음 코드를 사용할 수 있다.

```python
with open(self.state_file, "w", encoding="utf-8") as file:
    json.dump(data, file, ensure_ascii=False, indent=2)
```

각 부분의 의미를 정리했다.

**1. 파일 열기**

```python
open(self.state_file, "w", encoding="utf-8")
```

state.json 파일을 쓰기 모드로 연다.

`"w"`는 쓰기 모드이며, 기존 파일이 있다면 기존 내용을 덮어쓴다.

**2. 파일 객체 준비**

```python
as file
```

열린 파일 객체에 file이라는 이름을 붙인다.

**3. JSON으로 저장**

```python
json.dump(data, file, ensure_ascii=False, indent=2)
```

파이썬의 data 데이터를 JSON 형식으로 변환해서 파일에 기록한다.

여기서 옵션의 의미는 다음과 같다.

- `ensure_ascii=False`: 한글 등의 문자를 유니코드 이스케이프 형태로 바꾸지 않고 저장한다.
- `indent=2`: 들여쓰기를 2칸으로 설정해 JSON 파일을 보기 좋게 정리한다.

**4. 파일 닫기**

with 블록이 끝나면 파일이 자동으로 닫힌다.

## 17-3. json.loads()와 json.dumps()

추가로 `json.loads()`와 `json.dumps()`도 있다는 점을 배웠다.

이 두 함수는 파일이 아니라 JSON 문자열을 대상으로 작업한다.

| 함수 | 기능 |
|---|---|
| `json.load()` | 파일에서 JSON 데이터 읽기 |
| `json.dump()` | JSON 데이터를 파일에 저장 |
| `json.loads()` | JSON 문자열을 파이썬 데이터로 변환 |
| `json.dumps()` | 파이썬 데이터를 JSON 문자열로 변환 |

따라서 파일을 대상으로 하는지 문자열을 대상으로 하는지 구분해서 기억해야 한다.

---

# 18. print()와 input()의 차이

마지막으로 `print()`와 `input()`의 차이를 정리했다.

## 18-1. print()

```python
print("이름을 입력하세요:")
```

안내 문구를 화면에 출력하고 종료한다.

사용자의 입력을 기다리지 않는다.

## 18-2. input()

```python
input("이름을 입력하세요:")
```

안내 문구를 출력하고 사용자의 입력을 기다린다.

즉, input()은 입력 안내 문구를 직접 출력하는 기능도 포함하고 있다.

따라서 다음과 같이 작성하면 된다.

```python
name = input("이름을 입력하세요: ")
```

별도로 print()를 작성하지 않아도 안내 문구가 화면에 나타난다.

반면 다음과 같이 작성하면 안내 문구가 두 번 출력될 수 있다.

```python
print("이름을 입력하세요:")
name = input("이름을 입력하세요: ")
```

따라서 사용자 입력을 기다리는 상황에서는 input()에 안내 문구를 직접 전달하면 된다.

---

# 마무리: 이번 학습을 통해 이해한 내용

이번 공부를 통해 단순히 파이썬 문법을 외우는 것에서 벗어나 실제 프로그램을 만들 때 필요한 개념들을 하나씩 이해할 수 있었다.

특히 퀴즈 프로그램을 구현하면서 다음 내용을 중요하게 공부했다.

1. **실행 환경 관리**: Python과 py 명령어의 차이, PATH, Windows 실행 별칭을 이해했다.
2. **Git 활용**: 브랜치를 생성하고 이동하며, 작업 내용을 커밋하고 병합하는 과정을 익혔다.
3. **클래스와 객체**: `__init__`, `self`, `cls`, `__new__`의 역할을 이해했다.
4. **타입 힌트**: 타입 힌트는 자동으로 타입을 강제하는 기능이 아니며, 정적 검사와 런타임 검사를 구분해야 한다는 것을 배웠다.
5. **자료형과 인터페이스**: list, Sequence, Iterable의 차이와 적절한 사용 상황을 이해했다.
6. **입력값 검증**: 객체에 데이터를 저장하기 전에 타입과 값을 검사하고, 불필요한 공백을 제거하는 방법을 익혔다.
7. **조건문과 반복문**: 가독성과 안정성을 고려한 코드 작성 원칙을 공부했다.
8. **실행 흐름 제어**: raise, return, break, continue가 각각 어떤 상황에서 필요한지 구분할 수 있게 되었다.
9. **함수 활용**: 함수 자체를 인자로 전달하는 방법과 enumerate를 활용하는 방법을 배웠다.
10. **파일과 데이터 관리**: pathlib, with, JSON을 이용해 파일 경로와 데이터를 관리하는 방법을 익혔다.
11. **프로그램 실행 구조**: `__name__ == "__main__"`을 통해 직접 실행과 import의 차이를 이해했다.
12. **데이터 처리**: 딕셔너리의 get()과 함수 중첩을 활용해 데이터를 가져오고 처리하는 방법을 공부했다.
13. **사용자 입력**: print()와 input()의 역할을 구분하고 입력 안내를 효율적으로 작성하는 방법을 배웠다.

앞으로 코드를 작성할 때는 단순히 실행되는 코드만 만드는 것이 아니라, 입력값이 올바른지 확인하고, 예외 상황을 고려하며, 나중에 다시 읽어도 이해하기 쉬운 코드를 작성하는 것을 목표로 삼으려고 한다.

이번에 공부한 내용들을 실제 퀴즈 프로그램에 적용하면서 하나씩 익혀 나가고, 앞으로 더 복잡한 프로그램을 만들 때도 지금 배운 개념들을 기초로 활용하고 싶다.