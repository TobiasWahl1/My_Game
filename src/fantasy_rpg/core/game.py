class Game:
    def __init__(self):
        self.running = True

    def run(self):
        print("Fantasy RPG started!")

        while self.running:
            command = input("> ")

            if command == "quit":
                self.running = False
                print("Game closed.")