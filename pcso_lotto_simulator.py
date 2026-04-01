# PCSO LOTTO SIMULATOR - FINAL POLISHED VERSION
import random
from typing import List

class PCSOLottoSimulator:
    def __init__(self):
        self.GAME_OPTIONS = {
            "6/42": {"max_num": 42, "name": "6/42 Grand Lotto"},
            "6/45": {"max_num": 45, "name": "6/45 Mega Lotto"},
            "6/49": {"max_num": 49, "name": "6/49 Super Lotto"},
            "6/55": {"max_num": 55, "name": "6/55 Grand Lotto"}
        }

    def select_game(self) -> str:
        print("\n=== PCSO LOTTO GAME SELECTION ===")
        for idx, game in enumerate(self.GAME_OPTIONS.keys(), 1):
            print(f"{idx}. {game} - {self.GAME_OPTIONS[game]['name']}")
        
        while True:
            try:
                choice = int(input("\nSelect game (1-{}): ".format(len(self.GAME_OPTIONS))))
                if 1 <= choice <= len(self.GAME_OPTIONS):
                    return list(self.GAME_OPTIONS.keys())[choice - 1]
                else:
                    print(f"Pick 1-{len(self.GAME_OPTIONS)}!")
            except ValueError:
                print("Enter a NUMBER only!")

    def generate_ticket(self, game_type: str) -> List[int]:
        max_num = self.GAME_OPTIONS[game_type]["max_num"]
        numbers = random.sample(range(1, max_num + 1), 6)
        numbers.sort()
        return numbers

    def run_simulator(self):
        print("===== PCSO LOTTO SIMULATOR =====")
        print("Your personal lotto machine - built exactly how we talked about!")
        selected_game = self.select_game()
        ticket = self.generate_ticket(selected_game)
        print(f"\nYour {selected_game} Ticket: {ticket}")

if __name__ == "__main__":
    simulator = PCSOLottoSimulator()
    simulator.run_simulator()
  
