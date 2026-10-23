## Post LinkedIn — IvoirLLM Guard

---

IvoirLLM Guard : j'ai testé la résistance d'un modèle de langage face aux attaques en français et en langues ivoiriennes

Pendant plusieurs semaines, j'ai construit un outil de test de sécurité pour modèles de langage (LLM) dans le contexte ivoirien. Le principe : envoyer 50 questions pièges à un modèle (Mistral 7B) et mesurer s'il résiste ou s'il génère du contenu dangereux.

Resultats

Résistance globale : 50% (32 refus, 15 compliance, 3 partiel)

Par catégorie :

- Désinformation : 0% de résistance. Le modèle génère des faux communiqués officiels (gouvernement, BCEAO, alerte sanitaire) avec un ton crédible.
- Jailbreak : 75% de résistance.
- Mélange de langues (français + dioula + nouchi) : 66.7% de résistance.

Faille la plus critique : la désinformation. Le modèle ne refuse jamais quand on lui demande de rédiger un faux communiqué officiel. Il génère un texte structuré, avec en-tête, date, signature, et ton administratif crédible.

Faille la plus intéressante : le mélange de langues. Quand on mélange français et langues locales avec un cadrage "projet d'école", le modèle tombe dans le piège et donne des instructions détaillées (piratage de compte Mobile Money, création de faux passeport).

Ce que ça prouve

Personne n'avait publié de tests de sécurité LLM pour la Côte d'Ivoire. Les modèles ne sont pas préparés aux contextes locaux. Un chatbot déployé en Côte d'Ivoire peut être détourné facilement si personne ne teste sa résistance en français et en langues ivoiriennes.

Le code est open source sur GitHub : https://github.com/99ogonas-del/ivoirllm-guard

Je suis étudiant en Réseau et Sécurité Informatique (ESATIC, Côte d'Ivoire). Ce projet fait partie de mon portfolio en cybersécurité.

Hashtags : #CyberSecurite #IA #LLM #CoteDIvoire #Securite #OpenSource #ESATIC #TechAfrica #PromptInjection

---

## Instructions pour publier

1. Copie le texte ci-dessus
2. Colle-le dans LinkedIn
3. Ajoute la capture d'écran `screenshot_linkedin.png` (dans le dossier du projet)
4. Publie !
