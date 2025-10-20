# CountNumbersText

Ein kleines Python‑Programm, das die Anzahl der Wörter in einer Textdatei zählt. Standardmäßig liest es `data/sample.txt` und schreibt das Ergebnis zusätzlich nach `data/output.txt`.

## Voraussetzungen
- Python 3.10+ installiert.
- Windows: Falls `python` den Microsoft Store öffnet, nutze `py` oder deaktiviere die App‑Ausführungsaliase in den Einstellungen.

## Installation (Windows Schnellstart)
- Python installieren: `winget install Python.Python.3.12`

## Ausführen
- Standard (liest `data/sample.txt`, schreibt `data/output.txt`):
  - `py .\\src\\count_numbers_text\\main.py`
- Mit eigener Eingabedatei:
  - `py .\\src\\count_numbers_text\\main.py .\\data\\sample.txt`
- Mit eigener Ausgabedatei:
  - `py .\\src\\count_numbers_text\\main.py -o .\\data\\mein_output.txt`

Alternativ als Modul ausführen:
- PowerShell: `$env:PYTHONPATH = (Resolve-Path .\\src)`
- Dann: `python -m count_numbers_text.main`

## Beispielausgabe
- Für die mitgelieferte Datei `data/sample.txt` lautet die Ausgabe:
  - `Word count: 23`
  - und wird zusätzlich in `data/output.txt` gespeichert.

## Projektstruktur
- `data/sample.txt` – Beispieltext
- `data/output.txt` – Ergebnisdatei (wird beim Ausführen erzeugt/überschrieben)
- `src/count_numbers_text/main.py` – Skript zum Zählen
- `.gitignore` – Ignorierregeln für OS/IDE, Node & Python

