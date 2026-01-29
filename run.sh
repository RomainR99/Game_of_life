#!/usr/bin/env bash
# Lancer l'app dans l'environnement virtuel

cd "$(dirname "$0")"

if [[ ! -d venv ]]; then
  python3 -m venv venv
fi

source venv/bin/activate
pip install -r requirements.txt
streamlit run app.py
