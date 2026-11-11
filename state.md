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

