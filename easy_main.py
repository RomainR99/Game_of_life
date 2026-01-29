import numpy as np
import time
import os

# ----------------------------
# PARAMÈTRES DU JEU
# ----------------------------
GRID_SIZE = 7
SLEEP_TIME = 0.8

# ----------------------------
# GRILLE INITIALE (7x7)
# 0 = cellule morte
# 1 = cellule vivante
# ----------------------------
frame = np.array([
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 1, 0, 0, 0],
    [0, 1, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 0],
])

# ----------------------------
# CALCUL DES VOISINS
# ----------------------------
def count_neighbors(padded_grid, row, col):
    """
    Calcule le nombre de voisins vivants pour la cellule (row, col)
    dans la matrice avec padding.
    """
    return (
        padded_grid[row - 1, col - 1] + padded_grid[row - 1, col] + padded_grid[row - 1, col + 1] +
        padded_grid[row,     col - 1]                             + padded_grid[row,     col + 1] +
        padded_grid[row + 1, col - 1] + padded_grid[row + 1, col] + padded_grid[row + 1, col + 1]
    )

# ----------------------------
# CALCUL DE LA GÉNÉRATION SUIVANTE
# ----------------------------
def next_generation(grid):
    """
    Calcule la génération suivante selon les règles du Jeu de la Vie
    """
    # Ajout d'une bordure de zéros (zero padding)
    padded_grid = np.pad(grid, pad_width=1, mode='constant', constant_values=0)

    # Nouvelle grille vide
    new_grid = np.zeros_like(grid)

    # Parcours de la zone utile
    for row in range(1, GRID_SIZE + 1):
        for col in range(1, GRID_SIZE + 1):
            neighbors = count_neighbors(padded_grid, row, col)
            cell = padded_grid[row, col]

            # Règles du jeu de la vie
            if cell == 1 and (neighbors == 2 or neighbors == 3):
                new_grid[row - 1, col - 1] = 1
            elif cell == 0 and neighbors == 3:
                new_grid[row - 1, col - 1] = 1
            else:
                new_grid[row - 1, col - 1] = 0

    return new_grid

# ----------------------------
# AFFICHAGE DANS LE TERMINAL
# ----------------------------
def display(grid):
    """
    Affiche la grille dans le terminal
    os.system : Effacer le terminal avant chaque affichage
    pour donner l'illusion d'une animation.
    """
    os.system('cls' if os.name == 'nt' else 'clear')
    for row in grid:
        print(" ".join("█" if cell == 1 else "·" for cell in row))

# ----------------------------
# BOUCLE PRINCIPALE
# ----------------------------
generation = 0

while True:
    print(f"Génération : {generation}")
    display(frame)

    # Condition d'arrêt : plus aucune cellule vivante
    if np.sum(frame) == 0:
        print("\n💀 Plus aucune cellule vivante. Fin de la simulation.")
        break

    frame = next_generation(frame)
    generation += 1
    time.sleep(SLEEP_TIME)
