# Simulação do Problema dos Três Corpos

Este projeto é um trabalho de Conceitos de Linguagens de Programação que envolve a criação de um projeto utilizando duas linguagens de programação: C++ e Python. A simulação modela interações gravitacionais entre tres objetos celestes. A DLL em C++ realiza os cálculos físicos, enquanto o Python exibe os resultados visualmente. A comunicação entre as duas linguagens permite executar simulações e visualizar os dados gerados.

## Arquivos do Repositório

- **`gravity.cpp`**: Código C++ que implementa a simulação gravitacional e cria uma biblioteca compartilhada.
- **`threeBodyProblem.py`**: Código Python que utiliza a biblioteca compartilhada para executar a simulação e exibir a visualização gráfica com Pygame.
- **`Makefile`**: Arquivo de automação que define as regras para compilar a biblioteca compartilhada e executar o código Python.

## Dependências

### Pacotes Necessários

Para compilar o código C++ e executar o script Python, você precisará dos seguintes pacotes:

- **Para a biblioteca compartilhada C++**:
  - `g++`: Compilador C++.

- **Para o Python**:
  - `pygame`: Biblioteca para criação de jogos e gráficos.

### Instalação dos Pacotes

- **No Ubuntu/Debian**:
  ```sh
  sudo apt-get update
  sudo apt-get install g++ python3 python3-pygame

- **No MacOs**:
  ```sh
  brew install gcc
  pip3 install pygame

- **No Windows**:
    - Baixe e instale o MinGW para o compilador C++
    - Instale o Pygame usando pip:
  ```sh
  pip install pygame
  
## Compilação e Execução

### Compilação

Para compilar o código C++ e gerar a biblioteca compartilhada, execute:

    make

Isso criará um arquivo chamado `libthreebodyproblem.so` que será usado pelo script Python.

### Execução

Para executar o script Python e iniciar a simulação, execute:

    make run

### Limpeza

Para remover a biblioteca compartilhada gerada, execute:

    make clean

## Como Funciona

1. **Compilação**: O `Makefile` compila o código C++ em uma biblioteca compartilhada que é utilizada pelo script Python.
2. **Execução**: O script Python carrega a biblioteca compartilhada, inicializa os objetos da simulação, e atualiza a visualização dos objetos em órbita com o Pygame.
3. **Visualização**: A simulação é exibida em uma janela gráfica, mostrando o movimento dos corpos ao longo do tempo.
