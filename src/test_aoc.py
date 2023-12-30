#!/usr/bin/env python3

"""
Test for AOC Helper Functions.
"""

from aoc import bfs, bfs_paths, dfs, dfs_paths, get_neighbour


def test_get_neighbour():
    """Test get neighbour for point (0,0)."""

    # 4-neighbour NSWE
    V4 = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    n4 = list(get_neighbour(0, 0, 4))
    assert len(n4) == len(V4)
    assert all(n in V4 for n in n4)

    # 8-neighbour NW, N, NE, W, E, SW, S, SE
    V8 = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    n8 = list(get_neighbour(0, 0, 8))
    assert len(n8) == len(V8)
    assert all(n in V8 for n in n8)

    # 9-neighbour NW, N, NE, W, E, SW, S, SE
    V9 = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 0), (0, 1), (1, -1), (1, 0), (1, 1)]
    n9 = list(get_neighbour(0, 0, 9))
    assert len(n9) == len(V9)
    assert all(n in V9 for n in n9)


def test_bfs_dfs():
    graph = {
        "A": set(["B", "C"]),
        "B": set(["A", "D", "E"]),
        "C": set(["A", "F"]),
        "D": set(["B"]),
        "E": set(["B", "F"]),
        "F": set(["C", "E"]),
    }

    res = bfs(graph, "A")
    assert res == {"B", "C", "A", "F", "D", "E"}

    res = list(bfs_paths(graph, "A", "F"))
    for r in res:
        assert r in [["A", "C", "F"], ["A", "B", "E", "F"]]

    res = dfs(graph, "C")
    assert res == {"E", "D", "F", "A", "C", "B"}

    res = list(dfs_paths(graph, "C", "F"))
    for r in res:
        assert r in [["C", "F"], ["C", "A", "B", "E", "F"]]


# ------------------------------------------------------------------------------
