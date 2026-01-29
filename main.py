"""
Logique du Jeu de la Vie (grille de taille quelconque).
"""

import numpy as np


def count_neighbors(padded_grid: np.ndarray, row: int, col: int) -> int:
    """
    Calcule le nombre de voisins vivants pour la cellule (row, col)
    dans la matrice avec padding.
    """
    return int(
        padded_grid[row - 1, col - 1]
        + padded_grid[row - 1, col]
        + padded_grid[row - 1, col + 1]
        + padded_grid[row, col - 1]
        + padded_grid[row, col + 1]
        + padded_grid[row + 1, col - 1]
        + padded_grid[row + 1, col]
        + padded_grid[row + 1, col + 1]
    )


def next_generation(grid: np.ndarray) -> np.ndarray:
    """
    Calcule la génération suivante selon les règles du Jeu de la Vie.
    Fonctionne pour toute taille de grille.
    """
    padded = np.pad(grid, pad_width=1, mode="constant", constant_values=0)
    rows, cols = grid.shape
    new_grid = np.zeros_like(grid)

    for r in range(1, rows + 1):
        for c in range(1, cols + 1):
            n = count_neighbors(padded, r, c)
            cell = padded[r, c]
            if cell == 1 and n in (2, 3):
                new_grid[r - 1, c - 1] = 1
            elif cell == 0 and n == 3:
                new_grid[r - 1, c - 1] = 1

    return new_grid
