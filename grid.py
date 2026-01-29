"""
Grille 600×600 et motif « Dragon » (courbe du dragon) pour le Jeu de la Vie.
"""

import numpy as np

GRID_SIZE = 600


def _dragon_turns(n: int):
    """Génère la séquence de tours R/L de la courbe du dragon (n itérations)."""
    turns = [1]  # 1 = droite, -1 = gauche
    for _ in range(n - 1):
        turns = turns + [1] + [-t for t in reversed(turns)]
    return turns


def _turns_to_points(turns, step: int = 1):
    """Convertit la séquence de tours en liste de points (x, y)."""
    # Direction: 0→, 1↓, 2←, 3↑
    dx, dy = 1, 0
    x, y = 0, 0
    points = [(x, y)]
    for t in turns:
        if t == 1:   # droite
            dx, dy = dy, -dx
        else:        # gauche
            dx, dy = -dy, dx
        x += step * dx
        y += step * dy
        points.append((x, y))
    return points


def _fit_points_to_grid(points, size: int, margin: int = 20):
    """
    Place les points dans une grille `size×size` avec marge.
    Retourne les indices (row, col) valides.
    """
    xs = [p[0] for p in points]
    ys = [p[1] for p in points]
    xmin, xmax = min(xs), max(xs)
    ymin, ymax = min(ys), max(ys)
    wx = xmax - xmin or 1
    wy = ymax - ymin or 1
    inner = size - 2 * margin
    scale = min(inner / wx, inner / wy)
    cx = (xmin + xmax) / 2
    cy = (ymin + ymax) / 2
    half = size // 2

    out = []
    for x, y in points:
        nx = half + scale * (x - cx)
        ny = half + scale * (y - cy)
        col = int(round(nx))
        row = int(round(ny))
        if 0 <= row < size and 0 <= col < size:
            out.append((row, col))
    return out


def create_grid() -> np.ndarray:
    """Crée une grille vide 600×600."""
    return np.zeros((GRID_SIZE, GRID_SIZE), dtype=np.uint8)


def _draw_thick_points(grid: np.ndarray, indices: list, thickness: int) -> None:
    """Dessine des blocs `thickness x thickness` centrés sur chaque point (modifie grid)."""
    size = grid.shape[0]
    r = thickness // 2  # rayon de chaque bloc
    for row, col in indices:
        for dr in range(-r, r + 1):
            for dc in range(-r, r + 1):
                rr, cc = row + dr, col + dc
                if 0 <= rr < size and 0 <= cc < size:
                    grid[rr, cc] = 1


def create_grid_with_dragon(
    n_iter: int = 14,
    step: int = 1,
    margin: int = 40,
    thickness: int = 3,
) -> np.ndarray:
    """
    Grille 600×600 avec la courbe du dragon dessinée (cellules vivantes).
    n_iter: nombre d'itérations de la courbe (plus = plus détaillé).
    thickness: épaisseur du trait (3 → blocs 3×3) pour visibilité et survie au Jeu de la Vie.
    """
    grid = create_grid()
    turns = _dragon_turns(n_iter)
    points = _turns_to_points(turns, step=step)
    indices = _fit_points_to_grid(points, GRID_SIZE, margin=margin)
    _draw_thick_points(grid, indices, thickness)
    return grid
