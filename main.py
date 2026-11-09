class QuizGame:
    def __init__(self):
        self.running = True

    def show_menu(self):
        print("\n=== Quiz Game ===")
        print("1. Play Quiz")
        print("2. Add Quiz")
        print("3. Quiz List")
        print("4. Show High Score")
        print("5. Exit")

    def play_quiz_screen(self):
        print("\n[Play Quiz Screen]")
        input("Press Enter to return to menu...")

    def add_quiz_screen(self):
        print("\n[Add Quiz Screen]")
        input("Press Enter to return to menu...")

    def quiz_list_screen(self):
        print("\n[Quiz List Screen]")
        input("Press Enter to return to menu...")

    def show_high_score_screen(self):
        print("\n[High Score Screen]")
        input("Press Enter to return to menu...")

    def exit_program(self):
        print("\nExiting program. Goodbye!")
        self.running = False

    def handle_menu(self, choice):
        if choice == "1":
            self.play_quiz_screen()
        elif choice == "2":
            self.add_quiz_screen()
        elif choice == "3":
            self.quiz_list_screen()
        elif choice == "4":
            self.show_high_score_screen()
        elif choice == "5":
            self.exit_program()
        else:
            print("\nInvalid input. Please enter a number from 1 to 5.")

    def run(self):
        while self.running:
            self.show_menu()
            choice = input("Select menu number: ")
            self.handle_menu(choice)


if __name__ == "__main__":
    game = QuizGame()
    game.run()