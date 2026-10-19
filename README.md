

# Lokal AI-Assistent

En lokal AI-assistent, som kan besvare spørgsmål ud fra interne dokumenter (PDF, CSV, TXT).

- **IDE:** PyCharm
- **Version:** Python 3.12.2 via Miniconda3

---

## Forudsætninger

Hvis du ikke allerede har Anaconda/Miniconda installeret, kan du hente det direkte via terminalen:

**På Windows:**
```powershell
curl -O [https://repo.anaconda.com/archive/Anaconda3-2025.12-2-Windows-x86_64.exe](https://repo.anaconda.com/archive/Anaconda3-2025.12-2-Windows-x86_64.exe)

```

**På Linux:**

```bash
curl -O [https://repo.anaconda.com/archive/Anaconda3-2025.12-2-Linux-x86_64.sh](https://repo.anaconda.com/archive/Anaconda3-2025.12-2-Linux-x86_64.sh)

```

---

## Installation og Opsætning

### Trin 1: Installer AI-motoren (Ollama)

Da systemet kører lokalt, bruger den Ollama til at hente sprogmodellerne.

1. Download og installer Ollama via PowerShell:

```powershell
irm [https://ollama.com/install.ps1](https://ollama.com/install.ps1) | iex

```

2. Åbn din terminal (f.eks. Anaconda Prompt) og hent de to nødvendige modeller:

```bash
ollama pull llama3
ollama pull nomic-embed-text

```

---

### Trin 2: Opsæt Conda-miljøet

Programmet bruger Conda til at sikre den rigtige Python-version (3.12.2).

1. Opret et nyt dedikeret miljø:

```bash
conda create -n rag_lokal python=3.12.2 -y

```

2. Aktivér miljøet:

```bash
conda activate rag_lokal

```

---

### Trin 3: Installer projektets afhængigheder

Sørg for, at du står i den mappe, hvor projektfilerne ligger, og kør:

```bash
pip install -r requirements.txt

```

---

### Trin 4: Kør programmet

Du kan nu starte det lokale kommandolinje-interface:

```bash
python main.py

```

*(Alternativt kan du starte API-serveren med `uvicorn api:app --reload`)*

