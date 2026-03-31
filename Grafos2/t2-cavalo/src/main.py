from __future__ import annotations

import sys
from pathlib import Path

from bfs import BreadthFirstPaths
from cc import CC
from cycle import Cycle
from graph import Graph


def position_to_vertex(row: int, col: int, board_size: int = 3) -> int:
    return row * board_size + col


def default_input_path() -> Path:
    return Path(__file__).resolve().parents[1] / "dados" / "entrada.txt"


def print_components(components: list[list[int]]) -> None:
    print(f"Componentes conexas: {len(components)}")
    for index, component in enumerate(components):
        vertices = " ".join(str(vertex) for vertex in sorted(component))
        print(f"Vertices da componente {index}: {vertices}")


def print_shortest_distance(graph: Graph) -> None:
    source = position_to_vertex(0, 0)
    target = position_to_vertex(2, 2)
    bfs = BreadthFirstPaths(graph, source)

    print("Distancia minima entre (0,0) e (2,2):", end=" ")
    if bfs.has_path_to(target):
        print(bfs.dist_to(target))
        path = " ".join(str(vertex) for vertex in bfs.path_to(target))
        print(f"Um menor caminho encontrado: {path}")
    else:
        print("inexistente")


def print_cycle_analysis(graph: Graph) -> None:
    cycle_finder = Cycle(graph)
    has_cycle = cycle_finder.has_cycle()

    print(f"O grafo possui ciclo: {'Sim' if has_cycle else 'Nao'}")

    if has_cycle:
        cycle = " ".join(str(vertex) for vertex in cycle_finder.cycle())
        print(f"Um ciclo encontrado: {cycle}")


def print_complexity_analysis() -> None:
    print("Analise de complexidade:")
    print("Tempo total: O(V + E), considerando DFS para componentes, BFS para menor caminho e DFS para ciclo.")
    print("Espaco total: O(V + E), pela lista de adjacencia e estruturas auxiliares dos algoritmos.")


def main() -> None:
    input_path = Path(sys.argv[1]) if len(sys.argv) > 1 else default_input_path()
    graph = Graph.from_algs4_file(input_path)

    print("Lista de adjacencia:")
    print(graph.adjacency_list_as_text())

    cc = CC(graph)
    print_components(cc.components())
    print_shortest_distance(graph)
    print_cycle_analysis(graph)
    print_complexity_analysis()


if __name__ == "__main__":
    main()
