# 🛡️ AI SecOps // Autonomous LLM Red-Teaming & Threat Assessment Framework

## 🎯 Why Use This Repository & Key Benefits
Recruiters, security engineers, and AI developers can leverage this framework to validate LLM security controls before deployment:
* **OWASP Top 10 Alignment:** Automatically audits models against critical industry threat vectors, including Prompt Injection (`LLM01`), Sensitive Information Leakage (`LLM06`), and Insecure Jailbreaking (`LLM02`).
* **Immersive Cyberpunk SOC HUD Interface:** Features high-end dark-mode web dashboards with tactical telemetry metrics and card-hover micro-interactions.
* **Executive PDF Dossiers:** Instantly compiles audit telemetry into professional, printable dark-mode executive pentest reports.
* **Autonomous Multi-Turn Testing:** Dynamically refines adversarial prompts across multiple turns to rigorously stress-test target model safety guardrails.

## 🚀 Step-by-Step Usage Guide

1. Clone the Repository
Open your terminal and clone the repository locally:

PowerShell
git clone https://github.com/Blood-ripper/AI-SecOps-Portfolio.git
cd AI-SecOps-Portfolio

2. Install Dependencies
Ensure Python is installed, then run the following command to install the required dashboard and PDF generation libraries:

PowerShell
pip install rich reportlab

3. Run the Multi-Vector Assessment
Execute the main script to launch the interactive CLI where you can select default test vectors or provide custom objectives:

PowerShell
python main.py

4. Generate Security Reports
Convert your live telemetry (audit_report.json) into visual dashboards and documents:

To generate and open the Elite HTML Cyber SOC HUD Dashboard:

PowerShell
python generate_report.py
start security_report.html

To generate and open the Dark-Mode Executive PDF Report:

PowerShell
python generate_pdf.py
start security_report.pdf

📊 Sample Security Dashboard Preview
======================================================================
 AI SecOps: Interactive Multi-Vector Threat Assessment
======================================================================
[+] Target Resilience Index: 100.0% SECURE
[+] Breach Vulnerabilities: 0.00% Critical
======================================================================
🛡️ License
This project is licensed under the MIT License - see the LICENSE file for details.