## Installation

Use lima_models.py to install LIMA models to user's home directory (~/.lima). This script is the part of LIMA installation.

```bash
usage: lima_models.py [-h] [-i] [-l LANG] [-d DEST] [-s SELECT]

optional arguments:
  -h, --help            show this help message and exit
  -i, --info            print list of available languages and exit
  -l LANG, --lang LANG  language name or language code (example: 'english' or 'eng')
  -d DEST, --dest DEST  destination directory
  -s SELECT, --select SELECT
                        select particular models to install: tokenizer, morphosyntax, lemmatizer
                        (comma-separated list)
  ```
  
  To install English models to ~/.lima (default destination directory) use following command:
  
  ```bash
  $ lima_models.py -l english
  ```
  
  An average size of models for each language is 600Mb.
  
  To make ~/.lima directory visible to analyzeText update LIMA_RESOURCE environment variable:
  
 * temporarily
  ```bash
  $ LIMA_RESOURCES=~/.lima/resources/:$LIMA_RESOURCES analyzeText -l ud -p deepud --opts udlang:fra test.txt
  ```
  
 * permanently
  ```bash
  $ echo LIMA_RESOURCES=~/.local/share/lima/resources/:$LIMA_RESOURCES >> ~/.profile
  $ source ~/.profile
  ```
  
  ## Evaluation
  
  Evaluation tables for all models are in [eval.md](eval.md).
