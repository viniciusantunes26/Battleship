# Battleship

#### Requisitos Funcionais:

1. **Tabuleiro Simples**: O jogo usa um tabuleiro de 5x5 para cada jogador, representando o mar. 
2. **Navios**: Cada jogador possui 2 navios, cada um ocupando uma única posição no tabuleiro.
3. **Modo de Jogo**:
    - Jogador vs Jogador (PvP): Dois jogadores se alternam nos turnos.
    - Jogador vs Computador (PvE): O jogador joga contra.
4. **Sistema de Combate por Turnos**: Em cada turno, o jogador escolhe uma coordenada (como A1, B3, etc.) para tentar acertar um navio do adversário. O jogo informa se foi um acerto ou erro.
5. **Vitória**: O jogador vence quando todos os navios do oponente forem destruídos.

#### Requisitos Técnicos:

- O jogo deve ser implementado em C# ou qualquer outra linguagem simples de console.
- Não há necessidade de usar padrões complexos de design. A ênfase é na simplicidade.

#### Detalhes Específicos:

1. **Posicionamento de Navios**: No início do jogo, cada jogador posiciona seus 2 navios em coordenadas aleatórias no tabuleiro.
2. **Ação de Ataque**: Em cada turno, o jogador seleciona uma posição no tabuleiro do oponente para atacar.
    - **Acerto**: Se houver um navio nessa posição, ele será afundado.
    - **Erro**: Se não houver navio, o jogador simplesmente erra.
3. **Sem Salvamento de Progresso**: O jogo começa e termina em uma única sessão, sem a necessidade de salvar o progresso.

#### Requisitos Adicionais:

- O jogo começa com um menu simples: "Novo Jogo" ou "Sair".
- Instruções claras são mostradas no início para explicar como escolher coordenadas no tabuleiro.
