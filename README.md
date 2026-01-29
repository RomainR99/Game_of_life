# Jeu de la Vie (Conway)

Simulation du **Jeu de la Vie** de Conway en Python.

---

## Fichiers principaux

### `easy_main.py` — Version terminal (la plus claire)

- **Lance le jeu dans le terminal** : grille 7×7, affichage avec `█` / `·`, animation par rafraîchissement du terminal.
- Code **autonome**, **lisible** et **pédagogique** : tout est dans un seul fichier (règles, voisinage, boucle).
- Idéal pour comprendre le fonctionnement et pour faire tourner une démo rapide en ligne de commande.

```bash
python easy_main.py
```

### `main.py` — Version interface (générée par IA)

- **Refactorisation pour l’interface Streamlit** : fonctions réutilisables (`next_generation`, `count_neighbors`) qui acceptent une grille de taille quelconque.
- Code **généré par IA** pour servir de moteur au jeu dans l’app graphique (`app.py`), pas prévu pour être exécuté directement.

---

## Interface graphique (Streamlit)

- **`app.py`** : interface web avec grille 600×600, motif « dragon » (courbe du dragon), bouton *Lancer le jeu de la vie*.
- **`grid.py`** : grille 600×600 et génération du dragon.

**Lancer l’app :**

```bash
source venv/bin/activate
pip install -r requirements.txt
streamlit run app.py
```

Ou, avec le script fourni :

```bash
./run.sh
```

---

## Dépendances

- **`easy_main.py`** : `numpy`
- **Streamlit** : `numpy`, `streamlit` (voir `requirements.txt`)
