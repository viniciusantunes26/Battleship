import unittest
from typing import Tuple
from game import Board, PlayerFactory

class TestBattleShipGame(unittest.TestCase):
    def setUp(self):
        """Configuração inicial para os testes."""
        self.board = Board()
        self.player_human = PlayerFactory.create_player("Human")
        self.player_bot = PlayerFactory.create_player("Bot", is_bot=True)

    def test_place_ship(self):
        """Teste para posicionar um navio no tabuleiro."""
        self.assertTrue(self.board.place_ship("1A"))
        self.assertFalse(self.board.place_ship("1A"))  # Não deve permitir posicionar outro navio na mesma posição
        self.assertFalse(self.board.place_ship("6F"))  # Posição inválida

    def test_receive_attack(self):
        """Teste para ataques no tabuleiro."""
        self.board.place_ship("3C")
        self.assertTrue(self.board.receive_attack("3C"))  # Acerto no navio
        self.assertFalse(self.board.receive_attack("1A"))  # Tiro na água
        self.assertFalse(self.board.receive_attack("6F"))  # Ataque inválido

    def test_player_factory(self):
        """Teste para criação de jogadores usando o Factory Method."""
        self.assertEqual(self.player_human.name, "Human")
        self.assertFalse(self.player_human.is_bot)
        self.assertEqual(self.player_bot.name, "Bot")
        self.assertTrue(self.player_bot.is_bot)

if __name__ == "__main__":
    unittest.main()
