#!/usr/bin/env python3
"""Point d'entrée IvoirLLM Guard."""
import argparse
import sys


def cmd_run(args):
    print("[run] Lancement des tests — à implémenter (Phase 3)")
    # TODO: charger data/prompts.json, appeler src/runner.py


def cmd_analyze(args):
    print("[analyze] Analyse des résultats — à implémenter (Phase 4)")
    # TODO: lire reports/raw_*.json, générer reports/report.md


def main():
    parser = argparse.ArgumentParser(
        prog="ivoirllm-guard",
        description="Suite de tests de sécurité pour LLM (contexte ivoirien).",
    )
    sub = parser.add_subparsers(dest="command", required=True)

    p_run = sub.add_parser("run", help="Lancer les tests sur le modèle")
    p_run.set_defaults(func=cmd_run)

    p_analyze = sub.add_parser("analyze", help="Analyser les résultats et générer le rapport")
    p_analyze.set_defaults(func=cmd_analyze)

    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
