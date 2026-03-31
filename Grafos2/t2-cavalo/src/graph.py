from __future__ import annotations

from pathlib import Path


class Graph:
    def __init__(self, vertices: int) -> None:
        if vertices < 0:
            raise ValueError("O numero de vertices deve ser nao negativo.")
        self._v = vertices
        self._e = 0
        self._adj = [[] for _ in range(vertices)]

    @property
    def v(self) -> int:
        return self._v

    @property
    def e(self) -> int:
        return self._e

    def _validate_vertex(self, vertex: int) -> None:
        if vertex < 0 or vertex >= self._v:
            raise ValueError(f"Vertice invalido: {vertex}")

    def add_edge(self, v: int, w: int) -> None:
        self._validate_vertex(v)
        self._validate_vertex(w)

        # Insercao no inicio para reproduzir a ordem de iteracao
        # tipica usada na representacao do algs4.
        self._adj[v].insert(0, w)
        self._adj[w].insert(0, v)
        self._e += 1

    def adj(self, vertex: int) -> list[int]:
        self._validate_vertex(vertex)
        return self._adj[vertex]

    @classmethod
    def from_algs4_file(cls, file_path: str | Path) -> "Graph":
        path = Path(file_path)
        lines = [
            line.strip()
            for line in path.read_text(encoding="utf-8").splitlines()
            if line.strip()
        ]

        if len(lines) < 2:
            raise ValueError("Arquivo de entrada invalido.")

        vertices = int(lines[0])
        expected_edges = int(lines[1])
        graph = cls(vertices)

        edge_lines = lines[2:]
        if len(edge_lines) != expected_edges:
            raise ValueError(
                "Quantidade de arestas informada nao corresponde ao arquivo."
            )

        for edge_line in edge_lines:
            v_str, w_str = edge_line.split()
            graph.add_edge(int(v_str), int(w_str))

        return graph

    def adjacency_list_as_text(self) -> str:
        lines = []
        for vertex in range(self._v):
            neighbors = " ".join(str(neighbor) for neighbor in self._adj[vertex])
            lines.append(f"{vertex}: {neighbors}".rstrip())
        return "\n".join(lines)
