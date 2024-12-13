
# Testes do Jogo de Batalha Naval

## Descrição

Este projeto inclui uma suíte de testes automatizados para garantir o funcionamento correto das funcionalidades principais do jogo de Batalha Naval. Os testes foram desenvolvidos utilizando o módulo integrado do Python, `unittest`.

Os testes são simples e cobrem as funcionalidades mais importantes do jogo, garantindo confiabilidade e fácil manutenção.

## Funcionalidades Testadas

Os testes cobrem as seguintes áreas do sistema:

### 1. **Posicionar navio no tabuleiro**
   - **Objetivos**:
     - Garantir que um navio pode ser posicionado em uma posição válida.
     - Impedir que o mesmo navio seja posicionado na mesma posição novamente.
     - Verificar o comportamento ao tentar posicionar um navio em uma posição inválida (fora do tabuleiro).

### 2. **Realizar ataques no tabuleiro**
   - **Objetivos**:
     - Verificar o comportamento em ataques bem-sucedidos (acerto).
     - Verificar o comportamento em ataques malsucedidos (erro).
     - Garantir que ataques em posições inválidas não causem erros.

### 3. **Criação de jogadores com o Factory Method**
   - **Objetivos**:
     - Garantir que jogadores humanos e bots são criados corretamente.
     - Verificar as propriedades atribuídas aos jogadores.

## Como Executar os Testes

### Pré-requisitos

Certifique-se de ter o **Python 3.x** instalado no seu sistema.

### Passos para executar os testes

1. **Certifique-se de que o projeto está configurado corretamente.**
   - Salve o código principal do jogo em um arquivo (por exemplo, `game.py`).
   - Salve os testes em outro arquivo (por exemplo, `test_game.py`).

2. **Execute os testes usando o módulo `unittest`:**

   ```bash
   python -m unittest tests.py
   ```

3. **Interpretação dos resultados:**
   - Se todos os testes passarem, você verá uma saída como esta:
     ```
     ...
     ----------------------------------------------------------------------
     Ran 3 tests in 0.003s

     OK
     ```
   - Caso algum teste falhe, você verá detalhes sobre a falha, incluindo o nome do teste e o motivo.

## Estrutura dos Testes

Os testes estão organizados no arquivo `test_game.py` com os seguintes métodos:

| Método                 | Funcionalidade                       | Descrição                                                                 |
|------------------------|---------------------------------------|---------------------------------------------------------------------------|
| `test_place_ship`      | Posicionar navios                    | Testa se o posicionamento de navios no tabuleiro funciona corretamente.   |
| `test_receive_attack`  | Realizar ataques                     | Testa a lógica de ataques no tabuleiro, incluindo acertos e erros.        |
| `test_player_factory`  | Criação de jogadores                 | Testa a criação de jogadores usando o padrão Factory Method.              |

Desenvolvido por:
- Matheus Paes de Camargo Vieira
- Vinícius Antunes Silva
