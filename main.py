import json
import random
from pathlib import Path


class SafeExit(Exception):
    """입력 중 Ctrl+C, EOF 발생 시 안전 종료를 위한 예외"""
    pass


class Quiz:
    def __init__(self, question, choices, answer):
        if not isinstance(question, str):
            raise ValueError("문제는 문자열이어야 합니다.")

        question = question.strip()

        if not question:
            raise ValueError("문제는 비어 있을 수 없습니다.")

        if not isinstance(choices, list) or len(choices) != 4:
            raise ValueError("선택지는 반드시 4개여야 합니다.")

        cleaned_choices = []
        for choice in choices:
            if not isinstance(choice, str) or not choice.strip():
                raise ValueError("선택지는 비어 있을 수 없습니다.")
            cleaned_choices.append(choice.strip())

        if not isinstance(answer, int) or not (1 <= answer <= 4):
            raise ValueError("정답은 1~4 사이의 번호여야 합니다.")

        self.question = question
        self.choices = cleaned_choices
        self.answer = answer

    def display(self):
        print(f"\n문제: {self.question}")
        for i, choice in enumerate(self.choices, start=1):
            print(f"{i}. {choice}")

    def is_correct(self, user_answer):
        return self.answer == user_answer

    def to_dict(self):
        return {
            "question": self.question,
            "choices": self.choices,
            "answer": self.answer
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            data["question"],
            data["choices"],
            data["answer"]
        )


class QuizGame:
    def __init__(self):
        self.state_file = Path(__file__).resolve().with_name("state.json")
        self.quizzes = []
        self.best_score = None
        self.load_state()

    def get_default_quizzes(self):
        return [
            Quiz(
                "파이썬에서 변수를 만들 때 사용하는 대입 연산자는?",
                ["==", "=", ":=", "!="],
                2
            ),
            Quiz(
                "리스트의 길이를 구하는 함수는?",
                ["count", "size", "len", "length"],
                3
            ),
            Quiz(
                "조건문에 사용하는 키워드는?",
                ["for", "while", "if", "def"],
                3
            ),
            Quiz(
                "반복문에서 많이 사용하는 키워드 중 하나는?",
                ["for", "if", "return", "class"],
                1
            ),
            Quiz(
                "함수를 정의할 때 사용하는 키워드는?",
                ["import", "return", "def", "class"],
                3
            ),
            Quiz(
                "파이썬 실행을 위한 명령어는? 파일은 main.py 이다.",
                ["run main.py", "python main.py", "pyth main.py", "execute main.py"],
                2
            ),
            Quiz(
                "원격 저장소 주소를 보고 싶으면?",
                ["git status", "git branch", "git remote -v", "git log"],
                3
            )
        ]

    def get_old_quiz_mapping(self):
        """
        예전 형식:
        {
          "question": "...",
          "answer": "문자열정답"
        }
        을 현재 형식으로 바꾸기 위한 매핑
        """
        return {
            "파이썬에서 변수를 만들 때 사용하는 대입 연산자는?": {
                "choices": ["==", "=", ":=", "!="],
                "answer_text": "=",
                "answer_number": 2
            },
            "리스트의 길이를 구하는 함수는?": {
                "choices": ["count", "size", "len", "length"],
                "answer_text": "len",
                "answer_number": 3
            },
            "조건문에 사용하는 키워드는?": {
                "choices": ["for", "while", "if", "def"],
                "answer_text": "if",
                "answer_number": 3
            },
            "반복문에서 많이 사용하는 키워드 중 하나는?": {
                "choices": ["for", "if", "return", "class"],
                "answer_text": "for",
                "answer_number": 1
            },
            "함수를 정의할 때 사용하는 키워드는?": {
                "choices": ["import", "return", "def", "class"],
                "answer_text": "def",
                "answer_number": 3
            },
            "파이썬 실행을 위한 명령어는? 파일은 main.py 이다.": {
                "choices": ["run main.py", "python main.py", "pyth main.py", "execute main.py"],
                "answer_text": "python main.py",
                "answer_number": 2
            },
            "원격 저장소 주소를 보고 싶으면?": {
                "choices": ["git status", "git branch", "git remote -v", "git log"],
                "answer_text": "git remote -v",
                "answer_number": 3
            }
        }

    def migrate_old_quiz(self, item):
        question = item.get("question")
        answer_text = item.get("answer")

        mapping = self.get_old_quiz_mapping()

        if question not in mapping:
            raise ValueError("알 수 없는 예전 퀴즈 형식입니다.")

        quiz_info = mapping[question]

        if answer_text != quiz_info["answer_text"]:
            raise ValueError("예전 퀴즈 정답이 예상과 다릅니다.")

        return Quiz(
            question,
            quiz_info["choices"],
            quiz_info["answer_number"]
        )

    def load_state(self):
        if not self.state_file.exists():
            print("state.json 파일이 없어 기본 퀴즈를 사용합니다.")
            self.quizzes = self.get_default_quizzes()
            self.best_score = None
            self.save_state()
            return

        try:
            with open(self.state_file, "r", encoding="utf-8") as file:
                data = json.load(file)

            if not isinstance(data, dict):
                raise ValueError("state.json의 최상위 구조가 올바르지 않습니다.")

            raw_quizzes = data.get("quizzes")
            if not isinstance(raw_quizzes, list):
                raise ValueError("quizzes 항목이 올바르지 않습니다.")

            loaded_quizzes = []
            for item in raw_quizzes:
                if (
                    isinstance(item, dict)
                    and "question" in item
                    and "choices" in item
                    and "answer" in item
                ):
                    loaded_quizzes.append(Quiz.from_dict(item))
                elif (
                    isinstance(item, dict)
                    and "question" in item
                    and "answer" in item
                    and "choices" not in item
                ):
                    loaded_quizzes.append(self.migrate_old_quiz(item))
                else:
                    raise ValueError("퀴즈 데이터 형식이 올바르지 않습니다.")

            self.quizzes = loaded_quizzes

            score = data.get("best_score", data.get("high_score"))
            if score is None:
                self.best_score = None
            elif isinstance(score, int) and score >= 0:
                self.best_score = score
            else:
                raise ValueError("점수 데이터 형식이 올바르지 않습니다.")

            # 예전 형식(high_score 또는 문자열 answer)이면 현재 형식으로 다시 저장
            self.save_state()

        except (json.JSONDecodeError, OSError, ValueError, KeyError, TypeError, AttributeError) as e:
            print("state.json 파일이 없거나 손상되었습니다.")
            print(f"오류 내용: {e}")
            print("기본 퀴즈 데이터로 복구합니다.")
            self.quizzes = self.get_default_quizzes()
            self.best_score = None
            self.save_state()

    def save_state(self):
        data = {
            "quizzes": [quiz.to_dict() for quiz in self.quizzes],
            "best_score": self.best_score
        }

        try:
            with open(self.state_file, "w", encoding="utf-8") as file:
                json.dump(data, file, ensure_ascii=False, indent=2)
            return True

        except OSError as e:
            print("state.json 저장 중 오류가 발생했습니다.")
            print(f"오류 내용: {e}")
            return False
    
    def safe_input(self, prompt):
        try:
            return input(prompt)
        except (KeyboardInterrupt, EOFError):
            print("\n입력이 중단되었습니다. 저장 후 안전하게 종료합니다.")
            raise SafeExit

    def input_nonempty(self, prompt):
        while True:
            text = self.safe_input(prompt).strip()
            if text == "":
                print("빈 입력은 허용되지 않습니다. 다시 입력하세요.")
                continue
            return text

    def input_int(self, prompt, min_value, max_value):
        while True:
            text = self.safe_input(prompt).strip()

            if text == "":
                print("빈 입력은 허용되지 않습니다. 다시 입력하세요.")
                continue

            try:
                number = int(text)
            except ValueError:
                print("숫자를 입력해야 합니다. 다시 입력하세요.")
                continue

            if number < min_value or number > max_value:
                print(f"{min_value}부터 {max_value} 사이의 숫자를 입력하세요.")
                continue

            return number

    def show_menu(self):
        print("\n===== 퀴즈 게임 =====")
        print("1. 퀴즈 풀기")
        print("2. 퀴즈 추가")
        print("3. 퀴즈 목록 보기")
        print("4. 최고 점수 확인")
        print("0. 종료")

    def play_quiz(self):
        if not self.quizzes:
            print("등록된 퀴즈가 없습니다.")
            return

        print("\n퀴즈를 시작합니다.")
        score = 0

        # 원본 퀴즈 목록은 유지하고, 복사본만 섞기
        random_quizzes = self.quizzes[:]
        random.shuffle(random_quizzes)

        total = len(random_quizzes)

        for idx, quiz in enumerate(random_quizzes, 1):
            print(f"\n[{idx}/{total}]")
            quiz.display()

            answer = self.input_int("정답 번호를 입력하세요 (1~4): ", 1, 4)

            if quiz.is_correct(answer):
                print("정답입니다!")
                score += 1
            else:
                print(f"오답입니다. 정답은 {quiz.answer}번입니다.")

        print("\n===== 결과 =====")
        print(f"총 점수: {score} / {total}")

        if self.best_score is None or score > self.best_score:
            self.best_score = score
            self.save_state()
            print("최고 점수를 갱신했습니다!")
        else:
            self.save_state()

    def add_quiz(self):
        print("\n새 퀴즈를 추가합니다.")

        question = self.input_nonempty("문제를 입력하세요: ")

        choices = []
        for i in range(1, 5):
            choice = self.input_nonempty(f"{i}번 선택지를 입력하세요: ")
            choices.append(choice)

        answer = self.input_int("정답 번호를 입력하세요 (1~4): ", 1, 4)

        try:
            new_quiz = Quiz(question, choices, answer)
            self.quizzes.append(new_quiz)
            self.save_state()
            print("퀴즈가 저장되었습니다.")
        except ValueError as e:
            print(f"퀴즈 추가 실패: {e}")

    def show_quiz_list(self):
        if not self.quizzes:
            print("등록된 퀴즈가 없습니다.")
            return

        print("\n===== 퀴즈 목록 =====")
        for idx, quiz in enumerate(self.quizzes, start=1):
            print(f"\n[{idx}] {quiz.question}")
            for i, choice in enumerate(quiz.choices, start=1):
                print(f"  {i}. {choice}")
            print(f"  정답 번호: {quiz.answer}")

    def show_best_score(self):
        print("\n===== 최고 점수 =====")
        if self.best_score is None:
            print("아직 퀴즈를 푼 기록이 없습니다.")
        else:
            print(f"최고 점수: {self.best_score}")

    def run(self):
        try:
            while True:
                self.show_menu()
                menu = self.input_int("메뉴 번호를 선택하세요: ", 0, 4)

                if menu == 1:
                    self.play_quiz()
                elif menu == 2:
                    self.add_quiz()
                elif menu == 3:
                    self.show_quiz_list()
                elif menu == 4:
                    self.show_best_score()
                elif menu == 0:
                    self.save_state()
                    print("프로그램을 종료합니다.")
                    break

        except SafeExit:
            try:
                self.save_state()
            except OSError:
                print("저장 중 오류가 발생했지만 프로그램은 종료합니다.")
            print("안전하게 종료되었습니다.")


if __name__ == "__main__":
    game = QuizGame()
    game.run()