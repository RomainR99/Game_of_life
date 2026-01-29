"""
Interface Streamlit pour le Jeu de la Vie — grille 600×600 avec dragon.

Lancer avec :  streamlit run app.py
"""

import time
import numpy as np
import streamlit as st

from grid import create_grid_with_dragon
from main import next_generation

# Config de la page
st.set_page_config(page_title="Jeu de la Vie — Dragon", layout="centered")

st.title("Jeu de la Vie")
st.caption("Grille 600×600 — motif initial : courbe du dragon")

# Grille initiale avec dragon (épaisseur 3 pour visibilité et survie)
if "grid" not in st.session_state:
    st.session_state.grid = create_grid_with_dragon(n_iter=14, margin=40, thickness=3)
    st.session_state.gen = 0


def grid_to_image(g: np.ndarray) -> np.ndarray:
    """Convertit la grille 0/1 en image RGB (fond blanc, cellules noires)."""
    h, w = g.shape
    img = np.ones((h, w, 3), dtype=np.uint8) * 255
    img[g == 1] = [0, 0, 0]
    return img


# Placeholder pour la grille et la métrique
ph = st.empty()


def run_simulation():
    grid = st.session_state.grid.copy()
    gen = 0
    max_gen = 3000
    dt = 0.08

    while True:
        with ph.container():
            img = grid_to_image(grid)
            st.image(img, use_container_width=True)
            st.metric("Génération", gen)

        if np.sum(grid) == 0:
            st.success("Plus aucune cellule vivante. Fin de la simulation.")
            break
        if gen >= max_gen:
            st.info(f"Arrêt après {max_gen} générations.")
            break

        grid = next_generation(grid)
        gen += 1
        time.sleep(dt)


# Affichage initial
with ph.container():
    img = grid_to_image(st.session_state.grid)
    st.image(img, use_container_width=True)
    st.metric("Génération", st.session_state.gen)

col1, col2 = st.columns(2)
with col1:
    if st.button("Lancer le jeu de la vie", type="primary"):
        run_simulation()
with col2:
    if st.button("Nouvelle grille (dragon)"):
        st.session_state.grid = create_grid_with_dragon(n_iter=14, margin=40, thickness=3)
        st.session_state.gen = 0
        st.rerun()
