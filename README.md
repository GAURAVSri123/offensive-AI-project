# offensive-AI-project
## 🚀 Offensive AI Simulation Framework

### *AI-Powered Generation & Simulation of MITRE ATT&CK Technique Pseudocode Using Local LLMs*

A research-grade cybersecurity tool that uses:

* **MITRE ATT&CK dataset (Enterprise)**
* **Local LLaMA model via Ollama**
* **Secure pseudocode generation**
* **Command sanitization**
* **Behavior simulation**
* **Automated analysis & charts**

This framework demonstrates how Large Language Models can be used to **generate structured, safe pseudocode for cyber-attack techniques**, while enforcing strict safety controls.

---

## 📌 Features

### ✅ 1. Automated MITRE ATT&CK Extraction

Loads and processes 800+ techniques directly from the **enterprise-attack.json** STIX dataset.

### ✅ 2. Pseudocode Generation (Local LLM)

Uses **Ollama + LLaMA 3.2** to generate clean, readable, structured pseudocode for each technique.

### ✅ 3. Safety-First Sanitizer

Replaces any risky patterns (`sudo`, `rm -rf`, `curl`, `wget`, `ssh`, etc.) with:

```
[SIMULATED]
```

### ✅ 4. Behavior Simulator

Interprets LLM outputs into:

* Steps
* Actions
* Timestamps

No real commands are executed.

### ✅ 5. Automated Pipeline

A single script:

```
python3 pipeline.py
```

Runs the entire workflow end-to-end.

### ✅ 6. Result Analysis

`analyze_results.py` generates:

* Summary statistics
* Charts (PNG)
* Steps distribution
* Sanitized commands distribution
* Simulated action frequency

Perfect for reporting and academic demonstration.

---

## 🧠 System Architecture

```
            ┌─────────────────────┐
            │ MITRE ATT&CK STIX   │
            │ enterprise-attack.json
            └──────────┬──────────┘
                       │
                       ▼
           ┌───────────────────────┐
           │  load_attack.py       │
           │ Loads + extracts data │
           └──────────┬────────────┘
                      │
                      ▼
        ┌──────────────────────────────┐
        │  simplify.py                  │
        │ Clean structured technique    │
        └──────────┬───────────────────┘
                   │
                   ▼
       ┌─────────────────────────────┐
       │ prompt_builder.py           │
       │ Builds safe structured prompt│
       └──────────┬──────────────────┘
                  │
                  ▼
  ┌──────────────────────────────────────────┐
  │ generate_llm_code.py                     │
  │ Calls Ollama → Sanitizes output          │
  │ Produces pseudocode + safe version       │
  └──────────┬───────────────────────────────┘
             │
             ▼
   ┌──────────────────────────┐
   │ simulator.py             │
   │ Parses + simulates steps │
   └───────┬──────────────────┘
           │
           ▼
   ┌──────────────────────────┐
   │ pipeline.py              │
   │ Full end-to-end process  │
   └───────┬──────────────────┘
           │
           ▼
   ┌──────────────────────────┐
   │ results.jsonl            │
   │ All outputs logged       │
   └──────────────────────────┘
```

---

## 🛠️ Installation

### 1️⃣ Clone repo

```
git clone https://github.com/yourusername/offensive-ai-simulation.git
cd offensive-ai-simulation
```

### 2️⃣ Create environment

```
python3 -m venv mitre_env
source mitre_env/bin/activate
```

### 3️⃣ Install dependencies

```
pip install mitreattack-python requests tqdm matplotlib reportlab
```

### 4️⃣ Install Ollama

```
curl -fsSL https://ollama.com/install.sh | sh
```

### 5️⃣ Pull LLaMA model

```
ollama pull llama3.2
```

---

## ▶️ Usage

## Run complete pipeline

```
python3 pipeline.py
```

### Output stored in:

```
results.jsonl
```

---

# 📊 Analyze Results

```
python3 analyze_results.py
```

Generates:

* `steps_distribution.png`
* `simulated_actions.png`
* `sanitized_distribution.png`

---

## 📁 Project Structure

```
offensive_ai_project/
│
├── enterprise-attack.json    # MITRE dataset
├── load_attack.py            # Loads ATT&CK techniques
├── simplify.py               # Extracts important fields
├── prompt_builder.py         # Builds safe prompt
├── generate_llm_code.py      # Calls LLM + sanitizes
├── simulator.py              # Simulates pseudocode
├── pipeline.py               # Full pipeline
├── analyze_results.py        # Charts + metrics
└── results.jsonl             # Output log
```

---

## 🔐 Safety Disclaimer

This project:

* **Does NOT generate real malware.**
* **Does NOT execute dangerous commands.**
* **Uses sanitization + simulation to ensure safety.**
* Is strictly for:
  🧪 academic research,
  🛡️ cybersecurity education,
  🔍 AI behavior analysis.

You are responsible for using it ethically.

---

## 📚 References 

* MITRE ATT&CK: [https://attack.mitre.org/](https://attack.mitre.org/)
* mitreattack-python library
* CAPEC Database
* Ollama Documentation
* Meta LLaMA Model

---

## 🚧 Future Improvements

* Add multi-model comparison (LLaMA, Mistral, Qwen)
* Add richer simulation engine
* Convert outputs into a mini dataset
* Add web dashboard for analysis
