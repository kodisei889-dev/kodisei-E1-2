
import json
import random
from pathlib import Path
from datetime import datetime


class SafeExit(Exception):
    """입력 중 Ctrl+C, EOF 발생 시 안전 종료"""
    pass


class Quiz:
    def __init__(self, question, choices, answer, hint=""):
        if not isinstance(question, str) or not question.strip():
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

        if not isinstance(hint, str):
            raise ValueError("힌트는 문자열이어야 합니다.")

        self.question = question.strip()
        self.choices = cleaned_choices
        self.answer = answer
        self.hint = hint.strip()

    def display(self):
        print(f"\n문제: {self.question}")

        for i, choice in enumerate(self.choices, start=1):
            print(f"{i}. {choice}")

    def show_hint(self):
        if self.hint:
            print(f"\n[힌트] {self.hint}")
        else:
            print("\n등록된 힌트가 없습니다.")

    def is_correct(self, user_answer):
        return self.answer == user_answer

    def to_dict(self):
        return {
            "question": self.question,
            "choices": self.choices,
            "answer": self.answer,
            "hint": self.hint
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            data["question"],
            data["choices"],
            data["answer"],
            data.get("hint", "")
        )


class QuizGame:
    def __init__(self):
        self.state_file = Path(__file__).resolve().with_name("state.json")

        self.quizzes = []
        self.best_score = None
        self.history = []

        self.load_state()

    def get_default_quizzes(self):
        return [
            Quiz(
                "파이썬에서 변수를 만들 때 사용하는 대입 연산자는?",
                ["==", "=", ":=", "!="],
                2,
                "변수에 값을 저장할 때 사용하는 기호입니다."
            ),
            Quiz(
                "리스트의 길이를 구하는 함수는?",
                ["count", "size", "len", "length"],
                3,
                "세 글자로 이루어진 내장 함수입니다."
            ),
            Quiz(
                "조건문에 사용하는 키워드는?",
                ["for", "while", "if", "def"],
                3,
                "만약 ~라면이라는 의미를 가진 영어 단어입니다."
            ),
            Quiz(
                "반복문에서 많이 사용하는 키워드 중 하나는?",
                ["for", "if", "return", "class"],
                1,
                "특정 횟수만큼 반복할 때 자주 사용합니다."
            ),
            Quiz(
                "함수를 정의할 때 사용하는 키워드는?",
                ["import", "return", "def", "class"],
                3,
                "define의 줄임말입니다."
            ),
            Quiz(
                "파이썬 실행을 위한 명령어는? 파일은 main.py 이다.",
                ["run main.py", "python main.py",
                 "pyth main.py", "execute main.py"],
                2,
                "파이썬 인터프리터를 실행할 때 사용하는 명령어입니다."
            ),
            Quiz(
                "원격 저장소 주소를 보고 싶으면?",
                ["git status", "git branch",
                 "git remote -v", "git log"],
                3,
                "원격 저장소를 의미하는 Git 명령어를 사용합니다."
            )
        ]

    def load_state(self):
        if not self.state_file.exists():
            print("state.json 파일이 없어 기본 퀴즈를 사용합니다.")
            self.quizzes = self.get_default_quizzes()
            self.save_state()
            return

        try:
            with open(self.state_file, "r", encoding="utf-8") as file:
                data = json.load(file)

            if not isinstance(data, dict):
                raise ValueError("저장 데이터 형식이 올바르지 않습니다.")

            raw_quizzes = data.get("quizzes", [])

            if not isinstance(raw_quizzes, list):
                raise ValueError("quizzes 항목이 올바르지 않습니다.")

            loaded_quizzes = []

            for item in raw_quizzes:
                if not isinstance(item, dict):
                    raise ValueError("퀴즈 데이터 형식이 올바르지 않습니다.")

                if "question" not in item or "choices" not in item or "answer" not in item:
                    raise ValueError("퀴즈 데이터 항목이 부족합니다.")

                loaded_quizzes.append(Quiz.from_dict(item))

            self.quizzes = loaded_quizzes

            score = data.get("best_score", data.get("high_score"))

            if score is None:
                self.best_score = None
            elif isinstance(score, int) and not isinstance(score, bool) and score >= 0:
                self.best_score = score
            else:
                raise ValueError("최고 점수 데이터가 올바르지 않습니다.")

            self.history = data.get("history", [])

            if not isinstance(self.history, list):
                raise ValueError("점수 기록 데이터가 올바르지 않습니다.")

            # 기존 state.json도 새 형식으로 저장
            self.save_state()

        except (json.JSONDecodeError, OSError, ValueError,
                KeyError, TypeError, AttributeError) as e:

            print("state.json 파일이 손상되었습니다.")
            print(f"오류 내용: {e}")
            print("기본 퀴즈 데이터로 복구합니다.")

            self.quizzes = self.get_default_quizzes()
            self.best_score = None
            self.history = []

            self.save_state()

    def save_state(self):
        data = {
            "quizzes": [quiz.to_dict() for quiz in self.quizzes],
            "best_score": self.best_score,
            "history": self.history
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
            print("\n입력이 중단되었습니다. 저장 후 종료합니다.")
            raise SafeExit

    def input_nonempty(self, prompt):
        while True:
            text = self.safe_input(prompt).strip()

            if not text:
                print("빈 입력은 허용되지 않습니다.")
                continue

            return text

    def input_int(self, prompt, min_value, max_value):
        while True:
            text = self.safe_input(prompt).strip()

            try:
                number = int(text)

            except ValueError:
                print("숫자를 입력하세요.")
                continue

            if not min_value <= number <= max_value:
                print(f"{min_value}부터 {max_value} 사이의 숫자를 입력하세요.")
                continue

            return number

    def show_menu(self):
        print("\n===== 퀴즈 게임 =====")
        print("1. 퀴즈 풀기")
        print("2. 퀴즈 추가")
        print("3. 퀴즈 목록 보기")
        print("4. 최고 점수 확인")
        print("5. 퀴즈 삭제")
        print("6. 점수 기록 히스토리")
        print("0. 종료")

    # 1. 문제 수 선택 기능
    def select_question_count(self):
        total = len(self.quizzes)

        if total == 0:
            print("등록된 퀴즈가 없습니다.")
            return 0

        print("\n===== 문제 수 선택 =====")
        print(f"등록된 전체 문제 수: {total}")
        print("0. 전체 문제 풀기")

        count = self.input_int(
            f"풀 문제 수를 선택하세요 (0~{total}): ",
            0,
            total
        )

        if count == 0:
            return total

        return count

    # 2. 퀴즈 풀기 및 힌트 기능
    def play_quiz(self):
        if not self.quizzes:
            print("등록된 퀴즈가 없습니다.")
            return

        question_count = self.select_question_count()

        if question_count == 0:
            return

        random_quizzes = self.quizzes[:]
        random.shuffle(random_quizzes)

        selected_quizzes = random_quizzes[:question_count]

        score = 0
        hint_penalty = 0
        total = len(selected_quizzes)

        print("\n퀴즈를 시작합니다.")
        print("힌트를 사용하면 해당 문제의 획득 점수가 1점 차감됩니다.")

        for idx, quiz in enumerate(selected_quizzes, start=1):
            print(f"\n[{idx}/{total}]")
            quiz.display()

            used_hint = False

            while True:
                print("\n0. 힌트 보기")
                print("1~4. 정답 선택")

                answer = self.input_int(
                    "입력하세요: ",
                    0,
                    4
                )

                if answer == 0:
                    if not used_hint:
                        quiz.show_hint()
                        used_hint = True
                        hint_penalty += 1
                    else:
                        print("이미 이 문제의 힌트를 사용했습니다.")

                    continue
                
                if quiz.is_correct(answer):
                    print("정답입니다!")
                    score += 1

                else:
                    print(f"오답입니다. 정답은 {quiz.answer}번입니다.")

                # 힌트를 사용했다면 정답 여부와 관계없이 1점 차감
                if used_hint:
                    score -= 1
                    print("힌트 사용으로 1점 차감되었습니다.")

                break

        print("\n===== 결과 =====")
        print(f"총 문제 수: {total}")
        print(f"획득 점수: {score} / {total}")
        print(f"힌트 사용 횟수: {hint_penalty}")

        # 4. 점수 기록 히스토리
        record = {
            "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "total_questions": total,
            "score": score,
            "hint_used": hint_penalty
        }

        self.history.append(record)

        # 최고 점수 갱신
        if self.best_score is None or score > self.best_score:
            self.best_score = score
            print("최고 점수를 갱신했습니다!")

        self.save_state()

    # 퀴즈 추가 기능
    def add_quiz(self):
        print("\n===== 퀴즈 추가 =====")

        question = self.input_nonempty("문제를 입력하세요: ")

        choices = []

        for i in range(1, 5):
            choice = self.input_nonempty(
                f"{i}번 선택지를 입력하세요: "
            )
            choices.append(choice)

        answer = self.input_int(
            "정답 번호를 입력하세요 (1~4): ",
            1,
            4
        )

        hint = self.safe_input(
            "힌트를 입력하세요 (없으면 Enter): "
        ).strip()

        try:
            new_quiz = Quiz(question, choices, answer, hint)

            self.quizzes.append(new_quiz)

            if self.save_state():
                print("퀴즈가 저장되었습니다.")

        except ValueError as e:
            print(f"퀴즈 추가 실패: {e}")

    # 퀴즈 목록 보기
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
            print(f"  힌트: {quiz.hint if quiz.hint else '없음'}")

    # 3. 퀴즈 삭제 기능
    def delete_quiz(self):
        if not self.quizzes:
            print("삭제할 퀴즈가 없습니다.")
            return

        print("\n===== 퀴즈 삭제 =====")

        for idx, quiz in enumerate(self.quizzes, start=1):
            print(f"{idx}. {quiz.question}")

        print("0. 취소")

        number = self.input_int(
            f"삭제할 퀴즈 번호를 선택하세요 (0~{len(self.quizzes)}): ",
            0,
            len(self.quizzes)
        )

        if number == 0:
            print("삭제를 취소했습니다.")
            return

        quiz = self.quizzes[number - 1]

        confirm = self.safe_input(
            f"'{quiz.question}' 문제를 삭제할까요? (y/n): "
        ).strip().lower()

        if confirm == "y":
            deleted_quiz = self.quizzes.pop(number - 1)

            if self.save_state():
                print("퀴즈가 삭제되었습니다.")
            else:
                self.quizzes.insert(number - 1, deleted_quiz)
                print("저장 실패로 삭제를 취소했습니다.")

        else:
            print("삭제를 취소했습니다.")

    # 최고 점수 확인
    def show_best_score(self):
        print("\n===== 최고 점수 =====")

        if self.best_score is None:
            print("아직 퀴즈를 푼 기록이 없습니다.")

        else:
            print(f"최고 점수: {self.best_score}")

    # 4. 점수 기록 히스토리 확인
    def show_history(self):
        print("\n===== 점수 기록 히스토리 =====")

        if not self.history:
            print("아직 점수 기록이 없습니다.")
            return

        for idx, record in enumerate(self.history, start=1):
            print(f"\n[{idx}번째 기록]")
            print(f"날짜 및 시간: {record['date']}")
            print(f"푼 문제 수: {record['total_questions']}")
            print(f"획득 점수: {record['score']}")
            print(f"힌트 사용 횟수: {record.get('hint_used', 0)}")

        print("\n===== 전체 통계 =====")

        total_games = len(self.history)
        total_score = sum(r["score"] for r in self.history)

        print(f"총 게임 횟수: {total_games}")
        print(f"누적 획득 점수: {total_score}")

    def run(self):
        try:
            while True:
                self.show_menu()

                menu = self.input_int(
                    "메뉴 번호를 선택하세요: ",
                    0,
                    6
                )

                if menu == 1:
                    self.play_quiz()

                elif menu == 2:
                    self.add_quiz()

                elif menu == 3:
                    self.show_quiz_list()

                elif menu == 4:
                    self.show_best_score()

                elif menu == 5:
                    self.delete_quiz()

                elif menu == 6:
                    self.show_history()

                elif menu == 0:
                    self.save_state()
                    print("프로그램을 종료합니다.")
                    break

        except SafeExit:
            self.save_state()
            print("안전하게 종료되었습니다.")


if __name__ == "__main__":
    game = QuizGame()
    game.run()


class QuizGame:
    def run(self): ...
def main():
    game = QuizGame()
    game.run()

if __name__ == "__main__":
    main()