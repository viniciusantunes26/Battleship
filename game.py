import random
from typing import List, Tuple

# Singleton para Controle do Jogo
class Game:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Game, cls).__new__(cls)
            cls._instance.players = []
            cls._instance.winner = None
        return cls._instance

    def add_player(self, player):
        self.players.append(player)

    def set_winner(self, player):
        self.winner = player

    def reset(self):
        self.players = []
        self.winner = None

# Estratégia de Ataque
class AttackStrategy:
    def attack(self, opponent_board):
        pass

class HumanAttack(AttackStrategy):
    def attack(self, opponent_board):
        pos = input("Escolha uma posição para atacar (ex: 1A): ").upper()
        return opponent_board.receive_attack(pos)

class BotAttack(AttackStrategy):
    def attack(self, opponent_board):
        pos = f"{random.randint(1, 5)}{random.choice('ABCDE')}"
        print(f"Bot ataca na posição: {pos}")
        return opponent_board.receive_attack(pos)

# Jogador e Fábrica de Jogadores
class Player:
    def __init__(self, name, attack_strategy, is_bot=False):
        self.name = name
        self.attack_strategy = attack_strategy
        self.is_bot = is_bot
        self.board = Board()

    def place_ship(self):
        if self.is_bot:
            # Escolha aleatória para o bot
            pos = f"{random.randint(1, 5)}{random.choice('ABCDE')}"
            self.board.place_ship(pos)
        else:
            while True:
                pos = input(f"{self.name}, escolha a posição para colocar seu navio (ex: 1A): ").upper()
                if self.board.place_ship(pos):
                    break
                print("Posição inválida ou já ocupada. Escolha novamente.")

    def attack(self, opponent):
        return self.attack_strategy.attack(opponent.board)

class PlayerFactory:
    @staticmethod
    def create_player(name, is_bot=False):
        if is_bot:
            return Player(name, BotAttack(), is_bot=True)
        return Player(name, HumanAttack())

# Tabuleiro e Notificação de Ataques
class Board:
    def __init__(self):
        self.grid = [["~" for _ in range(5)] for _ in range(5)]
        self.ship_position = None

    def display(self):
        print("   A B C D E")
        for i, row in enumerate(self.grid):
            print(f"{i+1} ", " ".join(row))

    def place_ship(self, pos: str):
        row, col = self._parse_position(pos)
        if row is not None and col is not None and self.ship_position is None:
            self.ship_position = pos
            return True
        return False

    def receive_attack(self, pos: str) -> bool:
        row, col = self._parse_position(pos)
        if row is not None and col is not None:
            if pos == self.ship_position:
                self.grid[row][col] = "O"
                print("Acerto! O navio foi atingido.")
                return True
            else:
                self.grid[row][col] = "X"
                print("Água! Não há navio nesta posição.")
                return False
        print("Posição inválida.")
        return False

    def _parse_position(self, pos: str) -> Tuple[int, int]:
        try:
            row = int(pos[0]) - 1
            col = ord(pos[1]) - ord("A")
            if 0 <= row < 5 and 0 <= col < 5:
                return row, col
        except (IndexError, ValueError):
            pass
        return None, None

# Template Method para o Jogo
class BattleShipGame:
    def setup(self):
        self.game = Game()
        self.game.reset()  # Reinicia o estado do jogo ao iniciar uma nova partida
        mode = input("Escolha o modo de jogo (1 - Player vs Player, 2 - Player vs Bot): ")
        player1 = PlayerFactory.create_player("Jogador 1")
        player2 = PlayerFactory.create_player("Bot" if mode == "2" else "Jogador 2", is_bot=(mode == "2"))
        
        self.game.add_player(player1)
        self.game.add_player(player2)

        print("\nColocando navios no tabuleiro:")
        for player in self.game.players:
            player.place_ship()

    def play(self):
        while not self.game.winner:
            for player in self.game.players:
                print(f"\n{player.name}'s Turn")
                opponent = self.game.players[1] if player == self.game.players[0] else self.game.players[0]
                
                if player.attack(opponent):
                    self.game.set_winner(player)
                    break

                print(f"Tabuleiro de {opponent.name}:")
                opponent.board.display()

    def end_game(self):
        if self.game.winner:
            print(f"\n{self.game.winner.name} venceu a batalha naval!")
        else:
            print("\nO jogo terminou em empate.")

    def run(self):
        self.setup()
        self.play()
        self.end_game()

# Executa o jogo
if __name__ == "__main__":
    while True:
        game = BattleShipGame()
        game.run()
        if input("\nDeseja jogar novamente? (s/n): ").lower() != "s":
            break
