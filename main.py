import json
import os


class Quiz:
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer

    def to_dict(self):
        return {
            "question": self.question,
            "answer": self.answer
        }

    @classmethod
    def from_dict(cls, data):
        return cls(data["question"], data["answer"])


class QuizGame:
    def __init__(self, state_file="state.json"):
        self.state_file = state_file
        self.quizzes = []
        self.high_score = 0
        self.load_state()

    def load_state(self):
        """state.json 파일에서 퀴즈와 최고 점수를 불러온다."""
        if not os.path.exists(self.state_file):
            self.create_default_state()
            return

        try:
            with open(self.state_file, "r", encoding="utf-8") as file:
                data = json.load(file)

            self.quizzes = [Quiz.from_dict(q) for q in data.get("quizzes", [])]
            self.high_score = data.get("high_score", 0)

            # 파일은 있는데 퀴즈가 비어 있으면 기본 퀴즈 채우기
            if len(self.quizzes) < 5:
                self.create_default_state()

        except (json.JSONDecodeError, KeyError):
            print("state.json 파일이 손상되어 기본 데이터로 다시 생성합니다.")
            self.create_default_state()

    def save_state(self):
        """현재 상태를 state.json 파일에 저장한다."""
        data = {
            "quizzes": [quiz.to_dict() for quiz in self.quizzes],
            "high_score": self.high_score
        }

        with open(self.state_file, "w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=2)

    def create_default_state(self):
        """기본 퀴즈 5개와 최고 점수 0으로 초기화한다."""
        self.quizzes = [
            Quiz("파이썬에서 변수를 만들 때 사용하는 대입 연산자는?", "="),
            Quiz("리스트의 길이를 구하는 함수는?", "len"),
            Quiz("조건문에 사용하는 키워드는?", "if"),
            Quiz("반복문에서 많이 사용하는 키워드 중 하나는?", "for"),
            Quiz("함수를 정의할 때 사용하는 키워드는?", "def")
        ]
        self.high_score = 0
        self.save_state()

    def show_menu(self):
        print("\n==== 파이썬 기초 퀴즈 게임 ====")
        print("1. 퀴즈 풀기")
        print("2. 퀴즈 추가")
        print("3. 퀴즈 목록")
        print("4. 최고 점수 확인")
        print("5. 종료")

    def play_quiz(self):
        if not self.quizzes:
            print("등록된 퀴즈가 없습니다.")
            return

        print("\n[퀴즈 풀기]")
        score = 0

        for index, quiz in enumerate(self.quizzes, start=1):
            print(f"\n문제 {index}: {quiz.question}")
            user_answer = input("정답 입력: ").strip()

            if user_answer.lower() == quiz.answer.lower():
                print("정답입니다!")
                score += 1
            else:
                print(f"오답입니다. 정답: {quiz.answer}")

        print(f"\n이번 점수: {score} / {len(self.quizzes)}")

        if score > self.high_score:
            self.high_score = score
            self.save_state()
            print("축하합니다! 최고 점수를 갱신했습니다.")
        else:
            print(f"현재 최고 점수: {self.high_score}")

    def add_quiz(self):
        print("\n[퀴즈 추가]")
        question = input("문제를 입력하세요: ").strip()
        answer = input("정답을 입력하세요: ").strip()

        if not question or not answer:
            print("문제와 정답은 비워둘 수 없습니다.")
            return

        self.quizzes.append(Quiz(question, answer))
        self.save_state()
        print("퀴즈가 추가되었습니다.")

    def list_quizzes(self):
        print("\n[퀴즈 목록]")
        if not self.quizzes:
            print("등록된 퀴즈가 없습니다.")
            return

        for index, quiz in enumerate(self.quizzes, start=1):
            print(f"{index}. 문제: {quiz.question} / 정답: {quiz.answer}")

    def show_high_score(self):
        print("\n[최고 점수 확인]")
        print(f"현재 최고 점수: {self.high_score}")

    def run(self):
        while True:
            self.show_menu()
            choice = input("번호를 선택하세요: ").strip()

            if choice == "1":
                self.play_quiz()
            elif choice == "2":
                self.add_quiz()
            elif choice == "3":
                self.list_quizzes()
            elif choice == "4":
                self.show_high_score()
            elif choice == "5":
                print("프로그램을 종료합니다.")
                break
            else:
                print("올바른 번호를 입력하세요.")


if __name__ == "__main__":
    game = QuizGame()
    game.run()