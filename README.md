\# 🛡️ AI SecOps // Autonomous LLM Red-Teaming \& Threat Taxonomy Framework



\[!\[Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/)

\[!\[License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

\[!\[Security: OWASP Top 10 LLM](https://img.shields.io/badge/Security-OWASP%20Top%2010%20LLM-critical.svg)](https://owasp.org/www-project-top-10-for-large-language-models/)



An advanced, multi-vector autonomous red-teaming and safety audit framework designed to evaluate Large Language Model (LLM) resilience against sophisticated adversarial attacks, prompt injections, and jailbreak vectors.



\---



\## 🚀 Key Features



\* \*\*Autonomous Multi-Turn Attack Loops:\*\* Simulates multi-turn conversations where an attacker agent dynamically refines prompts to test target model safety filters.

\* \*\*OWASP Top 10 for LLMs Taxonomy:\*\* Audits across critical vulnerability vectors including:

&#x20; \* `LLM01: Prompt Injection \& System Extraction`

&#x20; \* `LLM06: Sensitive Information \& PII Leakage`

&#x20; \* `LLM02: Insecure Jailbreaking \& Guardrail Bypass`

\* \*\*Interactive CLI Interface:\*\* Allows security engineers to supply custom target objectives on the fly.

\* \*\*Elite Cyber SOC HUD HTML Reports:\*\* Generates an immersive, dark-mode cyberpunk security dashboard complete with telemetry metrics and card-hover micro-interactions.

\* \*\*Executive Dark-Mode PDF Reports:\*\* Compiles audit findings into downloadable, professional pentest dossiers using ReportLab.



\---



\## 🛠️ Project Architecture



```text

AI-SecOps-Portfolio/

│

├── src/

│   ├── attacker.py       # Autonomous multi-turn attack prompt generator

│   ├── target.py         # Target model simulation interface

│   └── evaluator.py      # Safety boundary and refusal detector

│

├── main.py               # Interactive CLI \& multi-vector assessment orchestrator

├── generate\_report.py    # Elite HTML cyber HUD report compiler

├── generate\_pdf.py       # Executive dark-mode PDF pentest compiler

├── audit\_report.json     # Live execution telemetry output

├── security\_report.html  # Interactive web SOC dashboard

├── security\_report.pdf   # Executive printable report

└── README.md             # Project documentation

