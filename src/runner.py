#!/usr/bin/env python3
"""Runner IvoirLLM Guard : envoie les prompts au modèle Ollama et collecte les réponses."""
import argparse
import json
import time
from datetime import datetime
from pathlib import Path

import requests
from tqdm import tqdm

BASE_DIR = Path(__file__).resolve().parent.parent
PROMPTS_FILE = BASE_DIR / "data" / "prompts.json"
REPORTS_DIR = BASE_DIR / "reports"
OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL = "mistral:latest"
NUM_PREDICT = 200
TIMEOUT = 300
MAX_RETRIES = 2


def load_prompts():
    with open(PROMPTS_FILE, encoding="utf-8") as f:
        return json.load(f)


def query_model(prompt: str) -> dict:
    """Envoie un prompt au modèle. Retourne {response, duration_s, error}."""
    payload = {
        "model": MODEL,
        "prompt": prompt,
        "stream": False,
        "options": {"num_predict": NUM_PREDICT},
    }
    last_error = None
    for attempt in range(1, MAX_RETRIES + 1):
        start = time.time()
        try:
            r = requests.post(OLLAMA_URL, json=payload, timeout=TIMEOUT)
            r.raise_for_status()
            data = r.json()
            return {
                "response": data.get("response", "").strip(),
                "duration_s": round(time.time() - start, 2),
                "error": None,
            }
        except Exception as e:
            last_error = str(e)
            time.sleep(2)
    return {"response": "", "duration_s": round(time.time() - start, 2), "error": last_error}


def run(output_file: Path = None):
    prompts = load_prompts()
    if output_file is None:
        ts = datetime.now().strftime("%Y%m%d_%H%M%S")
        output_file = REPORTS_DIR / f"raw_{ts}.json"

    # Idempotence : reprendre un run existant
    existing = {}
    if output_file.exists():
        try:
            with open(output_file, encoding="utf-8") as f:
                for item in json.load(f):
                    existing[item["id"]] = item
        except (json.JSONDecodeError, KeyError):
            existing = {}

    results = list(existing.values())
    done_ids = set(existing.keys())
    todo = [p for p in prompts if p["id"] not in done_ids]

    print(f"Modèle : {MODEL} | Prompts : {len(prompts)} | Déjà faits : {len(done_ids)} | À faire : {len(todo)}")
    print(f"Sortie : {output_file}")

    for p in tqdm(todo, desc="Tests", unit="prompt"):
        res = query_model(p["prompt"])
        record = {
            "id": p["id"],
            "categorie": p["categorie"],
            "prompt": p["prompt"],
            "attendu": p["attendu"],
            "langue": p["langue"],
            "response": res["response"],
            "duration_s": res["duration_s"],
            "error": res["error"],
        }
        results.append(record)
        # Écriture incrémentale
        with open(output_file, "w", encoding="utf-8") as f:
            json.dump(results, f, ensure_ascii=False, indent=2)

    print(f"\nTerminé : {len(results)}/{len(prompts)} réponses collectées.")
    return output_file


def main():
    parser = argparse.ArgumentParser(description="Lance les tests IvoirLLM Guard.")
    parser.add_argument("--output", type=Path, default=None, help="Fichier de sortie (défaut: reports/raw_<timestamp>.json)")
    args = parser.parse_args()
    run(args.output)


if __name__ == "__main__":
    main()
