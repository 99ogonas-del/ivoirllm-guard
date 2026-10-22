# IvoirLLM Guard

Suite de tests de sécurité pour modèles de langage (LLM) dans le contexte ivoirien.

## Objectif
Tester la résistance d'un LLM (via Ollama) face à des attaques par injection de prompt en français et en langues ivoiriennes (dioula, etc.).

## Prérequis
- Python 3.10+
- [Ollama](https://ollama.com) installé
- Modèle `mistral:latest` téléchargé (`ollama pull mistral:latest`)

## Installation
```bash
pip install -r requirements.txt
```

## Utilisation
```bash
# Lancer les tests
python run.py run

# Analyser les résultats
python run.py analyze
```

## Structure
- `data/prompts.json` — questions pièges (Phase 2)
- `src/runner.py` — envoi des prompts au modèle
- `src/analyze.py` — détection et rapport
- `reports/` — résultats bruts et rapport final
