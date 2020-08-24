# lima-models

Models for Lima

## Installation

Use install_models.py to install LIMA models to user's home directory (~/.lima). This script is the part of LIMA installation.

```bash
usage: install_models.py [-h] -l LANG [-d DEST]

optional arguments:
  -h, --help            show this help message and exit
  -l LANG, --lang LANG  language name or language code (example: 'english' or
                        'eng'
  -d DEST, --dest DEST  destination directory
  ```
  
  To install English models to ~/.lima (default destination directory) use following command:
  
  ```bash
  install_models.py -l english
  ```
  
  An average size of models for each language is 600Mb.
  
  To make ~/.lima directory visible to analyzeText update LIMA_RESOURCE environment variable:
  
 * temporarily
  ```bash
  LIMA_RESOURCES=~/.lima/resources/:$LIMA_RESOURCES analyzeText -l ud -p deepud --opts udlang:fra test.txt
  ```
  
 * permanently
  ```bash
  echo LIMA_RESOURCES=~/.lima/resources/:$LIMA_RESOURCES >> ~/.profile
  source ~/.profile
  ```
  
  ## Evaluation
  
  Evaluation tables for all models are in [eval.md](eval.md).
