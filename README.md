# Jogo da Velha com IA Minimax

Jogo da velha para duas pessoas no mesmo computador: uma pessoa joga contra uma IA que escolhe as jogadas usando o algoritmo **minimax**. A interface gráfica é feita com Pygame.

Este projeto demonstra fundamentos de Python, separação entre regras do jogo e interface, e busca adversarial em uma árvore de estados. É um bom projeto de portfólio para estágio ou início de carreira, especialmente se você conseguir explicar as decisões do minimax e evoluir o projeto com testes e melhorias de experiência.

## Funcionalidades

- Escolha jogar como X ou O.
- A IA considera as possibilidades futuras e joga de forma ótima; com jogo perfeito dos dois lados, a partida termina em empate.
- O jogo identifica vitórias e empates e permite iniciar uma nova partida.
- Regras do jogo e interface ficam em módulos separados.

## Requisitos

- Python 3.9 ou superior
- Pygame 2.5 ou superior

## Como executar

Clone o repositório e entre na pasta do projeto. Em seguida, crie e ative um ambiente virtual:

```bash
python -m venv .venv
source .venv/bin/activate
```

No Windows PowerShell, ative o ambiente com:

```powershell
.venv\Scripts\Activate.ps1
```

Instale o projeto e inicie o jogo:

```bash
python -m pip install -e .
python -m tic_tac_toe
```

Também é possível executar o comando instalado:

```bash
tic-tac-toe
```

## Como funciona o minimax

O algoritmo percorre recursivamente as jogadas possíveis até chegar a um estado final. Ele atribui valor `1` à vitória de X, `-1` à vitória de O e `0` ao empate. X escolhe a jogada que maximiza o resultado; O escolhe a que minimiza. Como o tabuleiro tem apenas nove casas, a árvore completa pode ser avaliada sem heurísticas ou poda alfa-beta.

## Estrutura do projeto

```text
.
├── README.md
├── pyproject.toml
└── src/
    └── tic_tac_toe/
        ├── __init__.py
        ├── __main__.py
        ├── ai.py       # busca minimax
        ├── game.py     # estado e regras
        └── gui.py      # interface Pygame
```

## Próximas melhorias

- Adicionar testes automatizados para regras, estados finais e escolhas da IA.
- Melhorar a interação do mouse e incluir uma opção de reinício durante a partida.
- Adicionar captura de tela ou GIF da aplicação ao README.
- Implementar poda alfa-beta e comparar a quantidade de estados avaliados.

## Licença

Nenhuma licença foi definida. Adicione um arquivo `LICENSE` antes de redistribuir o projeto como software de código aberto.
