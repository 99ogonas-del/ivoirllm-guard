#!/usr/bin/env python3
"""Point d'entrée IvoirLLM Guard."""
import argparse
import sys
from pathlib import Path

# Ajouter src/ au path pour importer runner
sys.path.insert(0, str(Path(__file__).resolve().parent / "src"))
from runner import run as run_tests
from analyze import analyze as run_analyze


def cmd_run(args):
    output = Path(args.output) if args.output else None
    prompts = Path(args.prompts) if args.prompts else None
    run_tests(output, args.limit, prompts)


def cmd_analyze(args):
    input_path = Path(args.input) if args.input else None
    if input_path:
        run_analyze(input_path)
    else:
        run_analyze(None)


def main():
    parser = argparse.ArgumentParser(
        prog="ivoirllm-guard",
        description="Suite de tests de sécurité pour LLM (contexte ivoirien).",
    )
    sub = parser.add_subparsers(dest="command", required=True)

    p_run = sub.add_parser("run", help="Lancer les tests sur le modèle")
    p_run.add_argument("--output", default=None, help="Fichier de sortie (défaut: reports/raw_<timestamp>.json)")
    p_run.add_argument("--limit", type=int, default=None, help="Limiter à N prompts (pilote)")
    p_run.add_argument("--prompts", default=None, help="Fichier de prompts personnalisé")
    p_run.set_defaults(func=cmd_run)

    p_analyze = sub.add_parser("analyze", help="Analyser les résultats et générer le rapport")
    p_analyze.add_argument("--input", default=None, help="Fichier brut à analyser (défaut: le plus récent)")
    p_analyze.set_defaults(func=cmd_analyze)

    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
