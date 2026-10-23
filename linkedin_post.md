## Post LinkedIn — IvoirLLM Guard

---

🛡️ IvoirLLM Guard — J'ai testé la résistance d'un LLM face aux attaques en français et en langues ivoiriennes

Pendant plusieurs semaines, j'ai construit un outil de test de sécurité pour modèles de langage (LLM) dans le contexte ivoirien.

Le principe : envoyer 50 questions pièges à un modèle (Mistral 7B) et mesurer s'il résiste ou s'il génère du contenu dangereux.

📊 Résultats :
• Résistance globale : 50% (32 refus, 15 compliance, 3 partiel)
• Désinformation : 0% de résistance (le modèle génère des faux communiqués officiels sans hésiter)
• Jailbreak : 75% de résistance
• Mélange de langues (français + dioula/nouchi) : 66.7% de résistance

🔍 Faille la plus critique : la désinformation. Le modèle génère des faux communiqués du gouvernement, de la BCEAO, des alertes sanitaires — avec un ton crédible.

🔍 Faille la plus intéressante : le mélange de langues. Quand on mélange français et langues locales avec un cadrage "projet d'école", le modèle tombe dans le piège.

💡 Ce que ça prouve : personne n'avait publié de tests de sécurité LLM pour la Côte d'Ivoire. Les modèles ne sont pas préparés aux contextes locaux.

Le code est open source sur GitHub : https://github.com/99ogonas-del/ivoirllm-guard

#CyberSécurité #IA #LLM #CôteDIvoire #Sécurité #OpenSource #ESATIC #TechAfrica #PromptInjection

---

## Instructions pour publier

1. Copie le texte ci-dessus
2. Colle-le dans LinkedIn
3. Ajoute la capture d'écran `screenshot_linkedin.png` (dans le dossier du projet)
4. Publie !
