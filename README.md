# Batalha Naval

## Descrição do Jogo

Este é um jogo de Batalha Naval para terminal, desenvolvido em Python, que oferece dois modos de jogo:

1. **Player vs Player:** Dois jogadores humanos inserem as posições de seus navios e se alternam para tentar acertar a posição do navio do adversário.
2. **Player vs Bot:** Um jogador humano contra um bot que toma decisões aleatórias tanto para a colocação do navio quanto para os ataques.

O jogo ocorre em um tabuleiro 5x5, onde:

- `~` representa água não atacada.
- `X` representa um ataque na água (tiro na água, sem acertar navio).
- `O` representa um acerto no navio do oponente.

Cada jogador escolhe uma única posição para colocar seu navio (por exemplo, "1A" ou "3E"). O primeiro jogador a acertar o navio do adversário vence a partida.

Ao final de cada partida, é possível escolher se deseja jogar novamente. Caso decida por uma nova partida, todo o estado do jogo anterior é reiniciado.

## Design Patterns Utilizados

Este projeto foi desenvolvido utilizando o paradigma de Orientação a Objetos (POO) e incorporando vários Design Patterns:

1. **Singleton (Classe `Game`):**  
   Garante que exista apenas uma instância de estado do jogo, controlando jogadores e vencedor de forma centralizada.

2. **Factory Method (Classe `PlayerFactory`):**  
   Simplifica a criação de jogadores (humano ou bot) sem expor a lógica de criação no código cliente.

3. **Strategy (Classes `AttackStrategy`, `HumanAttack`, `BotAttack`):**  
   Define diferentes estratégias de ataque (jogador humano escolhe a posição, bot escolhe aleatoriamente), permitindo trocar o comportamento de ataque facilmente.

4. **Template Method (Classe `BattleShipGame`):**  
   Define o esqueleto do fluxo do jogo (`setup`, `play` e `end_game`), permitindo que detalhes sejam implementados em subclasses (caso o jogo seja estendido).

## Pré-Requisitos

- **Python 3.x**: É necessário ter o Python instalado (recomenda-se Python 3.7 ou superior).

Nenhuma outra dependência externa é necessária. O código utiliza apenas módulos internos da biblioteca padrão do Python.

## Instalação

1. **Clonar o Repositório (opcional):**
   ```bash
   git clone https://github.com/viniciusantunes26/Battleship.git
   ```
   Caso já possua o arquivo `.py` localmente, basta ir para o próximo passo.

2. **Entrar no diretório do projeto:**
   
3. **(Opcional) Criar um ambiente virtual:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # Linux/MacOS
   # ou
   venv\Scripts\activate  # Windows
   ```

4. **Não há dependências adicionais para instalar**. Apenas certifique-se de ter o Python instalado.

## Executando o Jogo

Para iniciar o jogo, execute:

```bash
python3 nome_do_arquivo.py
```

ou, caso esteja em um ambiente Windows e tenha apenas uma versão do Python instalada:

```bash
python nome_do_arquivo.py
```

Durante a execução, siga as instruções apresentadas no terminal:

- Selecione o modo de jogo: Player vs Player (1) ou Player vs Bot (2).
- Se for jogador humano, insira a posição do seu navio conforme solicitado.
- No modo humano, insira as posições para atacar (como "2C" ou "5A").
- Ao final da partida, escolha se deseja jogar novamente.