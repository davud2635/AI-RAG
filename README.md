# Lokal AI-Assistent

En lokal AI-assistent, som kan besvare spørgsmål ud fra interne dokumenter (PDF, CSV, TXT).

- **IDE:** PyCharm
- **Version:** Python 3.12.2 via Miniconda3

---

# Forudsætninger

Hvis du ikke allerede har Anaconda/Miniconda på Windows, kan du hente den med:

```powershell
curl -O https://repo.anaconda.com/archive/Anaconda3-2025.12-2-Windows-x86_64.exe
```

Hvis du ikke allerede har Anaconda/Miniconda på Linux, kan du hente den med:

```bash
curl -O https://repo.anaconda.com/archive/Anaconda3-2025.12-2-Linux-x86_64.sh
```

---

# Installation og Opsætning

## Trin 1: Installer AI-motoren (Ollama)

Da systemet kører lokalt, bruger vi Ollama til at hente sprogmodellerne.

1. Download og installer Ollama via PowerShell:

```powershell
irm https://ollama.com/install.ps1 | iex
```

2. Åbn din terminal (f.eks. Anaconda Prompt) og hent de to nødvendige modeller:

```bash
ollama pull llama3
ollama pull nomic-embed-text
```

---

## Trin 2: Opsæt Conda-miljøet

Vi bruger Conda til at sikre den rigtige Python-version (3.12.2).

1. Opret et nyt dedikeret miljø:

```bash
conda create -n rag_lokal python=3.12.2 -y
```

2. Aktivér miljøet:

```bash
conda activate rag_lokal
```

---

## Trin 3: Installer projektets afhængigheder

```bash
pip install -r requirements.txt
```

---

## Trin 4: Kør programmet

```bash
python main.py
```
