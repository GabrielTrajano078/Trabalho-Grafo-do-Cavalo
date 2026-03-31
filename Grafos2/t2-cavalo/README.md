# T2 - Grafo do Cavalo em Tabuleiro 3x3

Projeto em Python que modela os movimentos de um cavalo em um tabuleiro de xadrez `3 x 3` como um grafo nao direcionado.

## Estrutura

```text
t2-cavalo/
├── README.md
├── dados/
│   └── entrada.txt
└── src/
    ├── bfs.py
    ├── cc.py
    ├── cycle.py
    ├── graph.py
    └── main.py
```

## Formato de entrada

O arquivo segue o formato `algs4`:

```text
V
E
v1 w1
v2 w2
...
```

Para este trabalho, a lista de arestas foi montada manualmente para o grafo do cavalo em um tabuleiro `3 x 3`.

## Como executar

Na raiz do projeto:

```bash
python3 src/main.py
```

Ou informando explicitamente o arquivo de entrada:

```bash
python3 src/main.py dados/entrada.txt
```

## Saidas do programa

O programa exibe:

- lista de adjacencia do grafo;
- componentes conexas;
- distancia minima entre `(0,0)` e `(2,2)`;
- existencia de ciclo;
- um ciclo encontrado;
- analise de complexidade de tempo e espaco.


Link explicação do trabalho:   https://youtu.be/vQ2MTKULzdg
