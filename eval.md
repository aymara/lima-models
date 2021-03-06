## Evaluation on Universal Dependencies 2.6 corpora collection

| Sofware | Version |
| --- | --- |
| Lima commit hash | [91bdeab](https://github.com/aymara/lima/commit/91bdeab356d6e9dc1766da47509a8aa747d0f70e) |
| Lima models | v0.1.5 |
| UDPipe | v1.2.0 |
| UDPipe models | 2.5-191206 |
| UDify commit hash | [c277ade](https://github.com/Hyperparticle/udify/commit/c277adea9295b05772e3b508d05ce13aea8bde03) |

[Download link](https://github.com/aymara/lima-models/releases/tag/v0.1.5-beta)

| Language | Code | Language | Code | Language | Code | Language | Code |
| --- | --- | --- | --- | --- | --- | --- | --- |
| [Afrikaans](#Afrikaans-AfriBooms) | afr | [Albanian](#Albanian-TSA) | sqi | [Arabic](#Arabic-PADT) | ara | [Armenian](#Armenian-ArmTDP) | hye |
| [Basque](#Basque-BDT) | eus | [Belarusian](#Belarusian-HSE) | bel | [Breton](#Breton-KEB) | bre | [Bulgarian](#Bulgarian-BTB) | bul |
| [Catalan](#Catalan-AnCora) | cat | [Chinese](#Chinese-GSD) | zho | [Chinese](#Chinese-GSDSimp) | zho-simp | [Classical_Chinese](#Classical_Chinese-Kyoto) | lzh |
| [Coptic](#Coptic-Scriptorium) | cop | [Croatian](#Croatian-SET) | hrv | [Czech](#Czech-PDT) | ces | [Danish](#Danish-DDT) | dan |
| [Dutch](#Dutch-LassySmall) | nld | [English](#English-EWT) | eng | [Estonian](#Estonian-EDT) | est | [Finnish](#Finnish-TDT) | fin |
| [French](#French-Sequoia) | fra | [Galician](#Galician-CTG) | glg | [German](#German-HDT) | deu | [Greek](#Greek-GDT) | ell |
| [Hebrew](#Hebrew-HTB) | heb | [Hindi](#Hindi-HDTB) | hin | [Hungarian](#Hungarian-Szeged) | hun | [Indonesian](#Indonesian-GSD) | ind |
| [Irish](#Irish-IDT) | gle | [Italian](#Italian-ISDT) | ita | [Japanese](#Japanese-GSD) | jpn | [Kazakh](#Kazakh-KTB) | kaz |
| [Korean](#Korean-Kaist) | kor | [Kurmanji](#Kurmanji-MG) | kmr | [Latin](#Latin-PROIEL) | lat | [Latvian](#Latvian-LVTB) | lav |
| [Lithuanian](#Lithuanian-ALKSNIS) | lit | [Maltese](#Maltese-MUDT) | mlt | [Marathi](#Marathi-UFAL) | mar | [Naija](#Naija-NSC) | pcm |
| [North_Sami](#North_Sami-Giella) | sme | [Norwegian](#Norwegian-Bokmaal) | nob | [Norwegian](#Norwegian-Nynorsk) | nno | [Old_Church_Slavonic](#Old_Church_Slavonic-PROIEL) | chu |
| [Old_French](#Old_French-SRCMF) | fro | [Old_Russian](#Old_Russian-TOROT) | orv | [Persian](#Persian-Seraji) | fas | [Polish](#Polish-PDB) | pol |
| [Portuguese](#Portuguese-GSD) | por | [Romanian](#Romanian-Nonstandard) | ron | [Russian](#Russian-SynTagRus) | rus | [Scottish_Gaelic](#Scottish_Gaelic-ARCOSG) | gla |
| [Serbian](#Serbian-SET) | srp | [Slovak](#Slovak-SNK) | slk | [Slovenian](#Slovenian-SSJ) | slv | [Spanish](#Spanish-AnCora) | spa |
| [Swedish](#Swedish-Talbanken) | swe | [Tamil](#Tamil-TTB) | tam | [Telugu](#Telugu-MTG) | tel | [Thai](#Thai-PUD) | tha |
| [Turkish](#Turkish-IMST) | tur | [Ukrainian](#Ukrainian-IU) | ukr | [Urdu](#Urdu-UDTB) | urd | [Uyghur](#Uyghur-UDT) | uig |
| [Vietnamese](#Vietnamese-VTB) | vie | [Welsh](#Welsh-CCG) | cym | [Wolof](#Wolof-WTB) | wol  | |

### Average
| Tool | Mode | Tokens | Sentences | Words | UPOS | UFeats | Lemmas | UAS | LAS | Speed |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lima | raw | 98 | 86 | 96 | 88 | 77 | 85 | 75 | 69 | 337 |
| lima | gold-tok | 100 | 100 | 100 | 92 | 81 | 89 | 82 | 75 | 349 |
| udpipe | raw | 99 | 88 | 98 | 92 | 89 | 92 | 77 | 71 | 2302 |
| udpipe | gold-tok | 100 | 100 | 100 | 94 | 90 | 94 | 81 | 75 | 2761 |
| udify | gold-tok | 100 | 100 | 100 | 89 | 81 | 87 | 82 | 74 | 91 |

### Afrikaans-AfriBooms
Download link: [lima-deep-models-afr-afrikaans_0.1.5_all.deb](https://github.com/aymara/lima-models/releases/download/v0.1.5-beta/lima-deep-models-afr-afrikaans_0.1.5_all.deb)
| Tool | Mode | Tokens | Sentences | Words | UPOS | UFeats | Lemmas | UAS | LAS | Speed |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lima | raw | 99.96 | 99.65 | 99.96 | 96.78 | 77.85 | 96.31 | 85.93 | 82.34 | 349 |
| lima | gold-tok | 100 | 100 | 100 | 96.8 | 77.87 | 96.33 | 86.07 | 82.44 | 371 |
| udpipe | raw | 99.82 | 98.25 | 99.82 | 95.18 | 94.82 | 96.55 | 82.06 | 78.03 | 2516 |
| udpipe | gold-tok | 100 | 100 | 100 | 95.3 | 94.92 | **96.69** | 82.5 | 78.43 | **3355** |
| udify | gold-tok | 100 | 100 | 100 | **97.62** | **96.73** | 95.29 | **87.32** | **83.79** | 104 |

### Albanian-TSA
Download link: [lima-deep-models-sqi-albanian_0.1.5_all.deb](https://github.com/aymara/lima-models/releases/download/v0.1.5-beta/lima-deep-models-sqi-albanian_0.1.5_all.deb)
| Tool | Mode | Tokens | Sentences | Words | UPOS | UFeats | Lemmas | UAS | LAS | Speed |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lima | raw | 99.51 | 100 | 99.51 | 83.65 | 32.27 | 46.06 | 89.08 | 77.89 | 106 |
| lima | gold-tok | 100 | 100 | 100 | **84.16** | **32.32** | 46.53 | **89.59** | **78.2** | **132** |
| udify | gold-tok | 100 | 100 | 100 | 81.67 | 29.5 | **55.86** | 88.61 | 75.6 | 61 |

### Arabic-PADT
Download link: [lima-deep-models-ara-arabic_0.1.5_all.deb](https://github.com/aymara/lima-models/releases/download/v0.1.5-beta/lima-deep-models-ara-arabic_0.1.5_all.deb)
| Tool | Mode | Tokens | Sentences | Words | UPOS | UFeats | Lemmas | UAS | LAS | Speed |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lima | raw | 99.95 | 83.84 | 79.3 | 74.34 | 66.7 | 67.02 | 54.14 | 50.56 | 403 |
| lima | gold-tok | 100 | 100 | 100 | **94.72** | 83.85 | 80.92 | 84.96 | 79.5 | 418 |
| udpipe | raw | 99.98 | 82.09 | 94.58 | 88.53 | 84.16 | 88.46 | 72.71 | 67.77 | **2174** |
| udpipe | gold-tok | 100 | 100 | 100 | 93.7 | 89.17 | **92.9** | 82.04 | 76.32 | **2174** |
| udify | gold-tok | 100 | 100 | 100 | 94.31 | **91.98** | 71.85 | **87.65** | **82.49** | 67 |

### Armenian-ArmTDP
Download link: [lima-deep-models-hye-armenian_0.1.5_all.deb](https://github.com/aymara/lima-models/releases/download/v0.1.5-beta/lima-deep-models-hye-armenian_0.1.5_all.deb)
| Tool | Mode | Tokens | Sentences | Words | UPOS | UFeats | Lemmas | UAS | LAS | Speed |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lima | raw | 99.88 | 96.61 | 97.84 | 92.65 | 82.48 | 90.65 | 77.77 | 70.6 | 191 |
| lima | gold-tok | 100 | 100 | 100 | **94.6** | 84.11 | **92.51** | 81.42 | **73.79** | 204 |
| udpipe | raw | 99.92 | 97.85 | 99.34 | 91.99 | 84.66 | 91.83 | 75.62 | 68.5 | 1722 |
| udpipe | gold-tok | 100 | 100 | 100 | 92.49 | **85.15** | 92.41 | 76.93 | 69.71 | **2583** |
| udify | gold-tok | 100 | 100 | 100 | 91.79 | 75.84 | 85.39 | **82.66** | 73.64 | 86 |

### Basque-BDT
Download link: [lima-deep-models-eus-basque_0.1.5_all.deb](https://github.com/aymara/lima-models/releases/download/v0.1.5-beta/lima-deep-models-eus-basque_0.1.5_all.deb)
| Tool | Mode | Tokens | Sentences | Words | UPOS | UFeats | Lemmas | UAS | LAS | Speed |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lima | raw | 99.97 | 99.67 | 99.97 | 95.15 | 83.09 | 92.97 | 82.99 | 77.92 | 346 |
| lima | gold-tok | 100 | 100 | 100 | 95.18 | 83.11 | 92.99 | 83.04 | 77.97 | 353 |
| udpipe | raw | 99.94 | 99.83 | 99.94 | 92.32 | 87.33 | 93.54 | 75.02 | 69.91 | 2708 |
| udpipe | gold-tok | 100 | 100 | 100 | 92.37 | 87.38 | **93.57** | 75.09 | 69.97 | **3047** |
| udify | gold-tok | 100 | 100 | 100 | **95.52** | **87.69** | 91.53 | **84.79** | **80.9** | 104 |

### Belarusian-HSE
Download link: [lima-deep-models-bel-belarusian_0.1.5_all.deb](https://github.com/aymara/lima-models/releases/download/v0.1.5-beta/lima-deep-models-bel-belarusian_0.1.5_all.deb)
| Tool | Mode | Tokens | Sentences | Words | UPOS | UFeats | Lemmas | UAS | LAS | Speed |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lima | raw | 99.85 | 77.83 | 99.85 | 93.32 | 64.15 | 76.49 | 63.33 | 57.07 | 275 |
| lima | gold-tok | 100 | 100 | 100 | 93.56 | 65.13 | 76.76 | 67.19 | 60.75 | 287 |
| udpipe | raw | 99.84 | 78.7 | 99.84 | 84.29 | 65.3 | 75.02 | 58.57 | 52.85 | 1812 |
| udpipe | gold-tok | 100 | 100 | 100 | 84.42 | 65.37 | 75.16 | 59.48 | 53.76 | **2718** |
| udify | gold-tok | 100 | 100 | 100 | **97.22** | **87.45** | **79.83** | **85.69** | **81.77** | 73 |

### Breton-KEB
Download link: [lima-deep-models-bre-breton_0.1.5_all.deb](https://github.com/aymara/lima-models/releases/download/v0.1.5-beta/lima-deep-models-bre-breton_0.1.5_all.deb)
| Tool | Mode | Tokens | Sentences | Words | UPOS | UFeats | Lemmas | UAS | LAS | Speed |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lima | raw | 86.56 | 86.96 | 86.27 | 69.89 | 40.04 | 51.14 | 45.86 | 31.46 | 674 |
| lima | gold-tok | 100 | 100 | 100 | **78.55** | 44.97 | **55.65** | 61.56 | **41.48** | **709** |
| udify | gold-tok | 100 | 100 | 100 | 62.75 | **46.43** | 48.44 | **63.25** | 38.98 | 94 |

### Bulgarian-BTB
Download link: [lima-deep-models-bul-bulgarian_0.1.5_all.deb](https://github.com/aymara/lima-models/releases/download/v0.1.5-beta/lima-deep-models-bul-bulgarian_0.1.5_all.deb)
| Tool | Mode | Tokens | Sentences | Words | UPOS | UFeats | Lemmas | UAS | LAS | Speed |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lima | raw | 99.88 | 93.4 | 99.88 | 98.72 | 90.87 | 94.29 | 91.13 | 87.43 | 276 |
| lima | gold-tok | 100 | 100 | 100 | 98.85 | 91 | 94.4 | 92.21 | 88.49 | 281 |
| udpipe | raw | 99.91 | 94.17 | 99.91 | 97.62 | 95.4 | 94.6 | 89.09 | 84.99 | 1966 |
| udpipe | gold-tok | 100 | 100 | 100 | 97.79 | 95.55 | **94.72** | 89.98 | 85.81 | **2621** |
| udify | gold-tok | 100 | 100 | 100 | **98.95** | **95.84** | 94.35 | **95.56** | **92.47** | 100 |

### Catalan-AnCora
Download link: [lima-deep-models-cat-catalan_0.1.5_all.deb](https://github.com/aymara/lima-models/releases/download/v0.1.5-beta/lima-deep-models-cat-catalan_0.1.5_all.deb)
| Tool | Mode | Tokens | Sentences | Words | UPOS | UFeats | Lemmas | UAS | LAS | Speed |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lima | raw | 99.98 | 99.51 | 99.73 | 98.44 | 93.01 | 96.52 | 91.12 | 88.24 | 386 |
| lima | gold-tok | 100 | 100 | 100 | 98.68 | 93.17 | 96.71 | 91.68 | 88.75 | 389 |
| udpipe | raw | 99.98 | 99.43 | 99.98 | 98.11 | 97.67 | 98.15 | 89.01 | 85.91 | 2227 |
| udpipe | gold-tok | 100 | 100 | 100 | 98.14 | **97.7** | **98.18** | 89.08 | 85.98 | **3047** |
| udify | gold-tok | 100 | 100 | 100 | **98.7** | 93.11 | 97.72 | **92.99** | **91.02** | 90 |

### Chinese-GSD
Download link: [lima-deep-models-zho-chinese_0.1.5_all.deb](https://github.com/aymara/lima-models/releases/download/v0.1.5-beta/lima-deep-models-zho-chinese_0.1.5_all.deb)
| Tool | Mode | Tokens | Sentences | Words | UPOS | UFeats | Lemmas | UAS | LAS | Speed |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lima | raw | 91.46 | 97.39 | 91.46 | 87.62 | 85.88 | 88.64 | 70.95 | 67.73 | 290 |
| lima | gold-tok | 100 | 100 | 100 | **95.32** | 94.29 | 96.47 | **82.75** | **78.5** | 295 |
| udpipe | raw | 90.27 | 99.1 | 90.27 | 84.13 | 89.05 | 90.26 | 61.6 | 57.81 | **3003** |
| udpipe | gold-tok | 100 | 100 | 100 | 92.15 | 98.73 | **99.99** | 74.38 | 69.48 | **3003** |
| udify | gold-tok | 100 | 100 | 100 | 94.99 | **98.95** | 99.98 | 79.67 | 67.32 | 97 |

### Chinese-GSDSimp
Download link: [lima-deep-models-zho-simp-chinese_0.1.5_all.deb](https://github.com/aymara/lima-models/releases/download/v0.1.5-beta/lima-deep-models-zho-simp-chinese_0.1.5_all.deb)
| Tool | Mode | Tokens | Sentences | Words | UPOS | UFeats | Lemmas | UAS | LAS | Speed |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lima | raw | 92.12 | 97.01 | 92.12 | 88.13 | 86.52 | 90.54 | 71.39 | 67.72 | 296 |
| lima | gold-tok | 100 | 100 | 100 | **95.46** | 94.28 | 97.91 | **82.84** | **78.35** | 301 |
| udpipe | raw | 90.29 | 99.1 | 90.29 | 84.21 | 89.01 | 90.28 | 62.58 | 58.73 | 3003 |
| udpipe | gold-tok | 100 | 100 | 100 | 92.01 | 98.58 | **99.99** | 74.11 | 69 | **4004** |
| udify | gold-tok | 100 | 100 | 100 | 93.76 | **98.74** | 99.91 | 77.81 | 64.89 | 97 |

### Classical\_Chinese-Kyoto
Download link: [lima-deep-models-lzh-classical\_chinese_0.1.5_all.deb](https://github.com/aymara/lima-models/releases/download/v0.1.5-beta/lima-deep-models-lzh-classical\_chinese_0.1.5_all.deb)
| Tool | Mode | Tokens | Sentences | Words | UPOS | UFeats | Lemmas | UAS | LAS | Speed |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lima | raw | 99.21 | 41.52 | 99.21 | 89.11 | 77.88 | 95.58 | 68.6 | 62.19 | 510 |
| lima | gold-tok | 100 | 100 | 100 | 91.85 | 79.28 | 96.13 | 80.73 | 74.06 | 535 |
| udpipe | raw | 99.49 | 40.48 | 99.49 | 89.66 | 92.1 | 99.46 | 68.34 | 62.29 | 5281 |
| udpipe | gold-tok | 100 | 100 | 100 | **91.9** | **93.64** | **99.97** | **80.98** | **74.65** | **10562** |
| udify | gold-tok | 100 | 100 | 100 | 59.15 | 67.67 | 98.21 | 54.09 | 34.07 | 67 |

### Coptic-Scriptorium
Download link: [lima-deep-models-cop-coptic_0.1.5_all.deb](https://github.com/aymara/lima-models/releases/download/v0.1.5-beta/lima-deep-models-cop-coptic_0.1.5_all.deb)
| Tool | Mode | Tokens | Sentences | Words | UPOS | UFeats | Lemmas | UAS | LAS | Speed |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lima | raw | 99.8 | 20.85 | 23.4 | 20.74 | 19.66 | 21.93 | 1.55 | 1.43 | 395 |
| lima | gold-tok | 100 | 100 | 100 | 87.74 | 67.78 | 76.27 | 78.37 | 70.36 | 415 |
| udpipe | raw | 100 | 27.69 | 70.72 | 67.1 | 50.19 | 68.7 | 43.82 | 41.8 | **2593** |
| udpipe | gold-tok | 100 | 100 | 100 | **94.02** | **70.5** | **95.98** | **85.33** | **80.39** | **2593** |
| udify | gold-tok | 100 | 100 | 100 | 27.47 | 57.7 | 64.3 | 29.81 | 11.01 | 100 |

### Croatian-SET
Download link: [lima-deep-models-hrv-croatian_0.1.5_all.deb](https://github.com/aymara/lima-models/releases/download/v0.1.5-beta/lima-deep-models-hrv-croatian_0.1.5_all.deb)
| Tool | Mode | Tokens | Sentences | Words | UPOS | UFeats | Lemmas | UAS | LAS | Speed |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lima | raw | 99.92 | 94.55 | 99.92 | 97.67 | 81.47 | 91.28 | 87.75 | 82.42 | 320 |
| lima | gold-tok | 100 | 100 | 100 | **97.78** | 81.57 | 91.38 | 88.26 | 82.89 | 332 |
| udpipe | raw | 99.95 | 94.41 | 99.95 | 96.42 | 90.89 | 95.26 | 83.8 | 77.87 | 2205 |
| udpipe | gold-tok | 100 | 100 | 100 | 96.49 | **91.03** | 95.33 | 84.25 | 78.29 | **2426** |
| udify | gold-tok | 100 | 100 | 100 | 97.64 | 87.47 | **96.03** | **95.31** | **91.43** | 100 |

### Czech-PDT
Download link: [lima-deep-models-ces-czech_0.1.5_all.deb](https://github.com/aymara/lima-models/releases/download/v0.1.5-beta/lima-deep-models-ces-czech_0.1.5_all.deb)
| Tool | Mode | Tokens | Sentences | Words | UPOS | UFeats | Lemmas | UAS | LAS | Speed |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lima | raw | 99.95 | 93.37 | 99.87 | 98.85 | 84.78 | 94.36 | 91.67 | 88.68 | 338 |
| lima | gold-tok | 100 | 100 | 100 | 98.99 | 84.93 | 94.46 | 92.47 | 89.45 | 341 |
| udpipe | raw | 99.93 | 93.35 | 99.93 | 98.22 | 92.42 | 97.83 | 87.03 | 83.37 | 1831 |
| udpipe | gold-tok | 100 | 100 | 100 | 98.33 | 92.54 | 97.91 | 87.76 | 84.07 | **2450** |
| udify | gold-tok | 100 | 100 | 100 | **99.15** | **96.64** | **98.68** | **94.74** | **92.11** | 96 |

### Danish-DDT
Download link: [lima-deep-models-dan-danish_0.1.5_all.deb](https://github.com/aymara/lima-models/releases/download/v0.1.5-beta/lima-deep-models-dan-danish_0.1.5_all.deb)
| Tool | Mode | Tokens | Sentences | Words | UPOS | UFeats | Lemmas | UAS | LAS | Speed |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lima | raw | 99.84 | 89.72 | 99.84 | 96.86 | 92.71 | 95.57 | 83.08 | 79.7 | 222 |
| lima | gold-tok | 100 | 100 | 100 | 97.03 | 92.9 | **95.68** | 84.2 | 80.73 | 231 |
| udpipe | raw | 99.81 | 89.78 | 99.81 | 95.43 | 94.84 | 94.74 | 79.34 | 75.95 | 2506 |
| udpipe | gold-tok | 100 | 100 | 100 | 95.63 | 95.02 | 94.89 | 80.2 | 76.78 | **3341** |
| udify | gold-tok | 100 | 100 | 100 | **97.62** | **95.13** | 94.88 | **87.93** | **84.58** | 91 |

### Dutch-LassySmall
Download link: [lima-deep-models-nld-dutch_0.1.5_all.deb](https://github.com/aymara/lima-models/releases/download/v0.1.5-beta/lima-deep-models-nld-dutch_0.1.5_all.deb)
| Tool | Mode | Tokens | Sentences | Words | UPOS | UFeats | Lemmas | UAS | LAS | Speed |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lima | raw | 99.68 | 74.27 | 99.68 | 94.95 | 92.65 | 95.73 | 82.82 | 78.32 | 250 |
| lima | gold-tok | 100 | 100 | 100 | 95.38 | 93.43 | **96.22** | 87.11 | 82.29 | 250 |
| udpipe | raw | 99.83 | 75.4 | 99.83 | 94.07 | 93.69 | 95.46 | 79.01 | 75.01 | **2889** |
| udpipe | gold-tok | 100 | 100 | 100 | 94.25 | 94.15 | 95.73 | 82.36 | 77.95 | **2889** |
| udify | gold-tok | 100 | 100 | 100 | **96.1** | **96.08** | 95.66 | **92.85** | **89.51** | 92 |

### English-EWT
Download link: [lima-deep-models-eng-english_0.1.5_all.deb](https://github.com/aymara/lima-models/releases/download/v0.1.5-beta/lima-deep-models-eng-english_0.1.5_all.deb)
| Tool | Mode | Tokens | Sentences | Words | UPOS | UFeats | Lemmas | UAS | LAS | Speed |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lima | raw | 98.85 | 85.14 | 98.85 | 94.89 | 90.81 | 94.17 | 85.15 | 82.06 | 245 |
| lima | gold-tok | 100 | 100 | 100 | 95.95 | 91.86 | 95.09 | 87.91 | 84.65 | 254 |
| udpipe | raw | 98.9 | 86.92 | 98.9 | 93.34 | 94.3 | 95.45 | 81.83 | 78.64 | 1793 |
| udpipe | gold-tok | 100 | 100 | 100 | 94.43 | 95.37 | 96.41 | 84.4 | 81.08 | **2281** |
| udify | gold-tok | 100 | 100 | 100 | **96.29** | **96.19** | **97.39** | **91.12** | **88.53** | 92 |

### Estonian-EDT
Download link: [lima-deep-models-est-estonian_0.1.5_all.deb](https://github.com/aymara/lima-models/releases/download/v0.1.5-beta/lima-deep-models-est-estonian_0.1.5_all.deb)
| Tool | Mode | Tokens | Sentences | Words | UPOS | UFeats | Lemmas | UAS | LAS | Speed |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lima | raw | 99.94 | 89.42 | 99.94 | 97.02 | 90.09 | 94.11 | 85.29 | 81.93 | 236 |
| lima | gold-tok | 100 | 100 | 100 | 97.15 | 90.18 | **94.23** | 86.49 | 83.08 | 238 |
| udpipe | raw | 99.96 | 91.56 | 99.96 | 95.61 | 93.41 | 90.58 | 79.55 | 75.78 | 1865 |
| udpipe | gold-tok | 100 | 100 | 100 | 95.71 | 93.48 | 90.64 | 80.33 | 76.53 | **2552** |
| udify | gold-tok | 100 | 100 | 100 | **97.52** | **95.04** | 88.12 | **89.72** | **86.88** | 96 |

### Finnish-TDT
Download link: [lima-deep-models-fin-finnish_0.1.5_all.deb](https://github.com/aymara/lima-models/releases/download/v0.1.5-beta/lima-deep-models-fin-finnish_0.1.5_all.deb)
| Tool | Mode | Tokens | Sentences | Words | UPOS | UFeats | Lemmas | UAS | LAS | Speed |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lima | raw | 99.71 | 90.35 | 99.65 | 96.81 | 91.28 | 92.5 | 87.77 | 85.04 | 257 |
| lima | gold-tok | 100 | 100 | 100 | **97.14** | 91.52 | **92.8** | **89.12** | **86.34** | 267 |
| udpipe | raw | 99.71 | 88.64 | 99.7 | 94.27 | 92 | 86.88 | 80.49 | 76.85 | 2634 |
| udpipe | gold-tok | 100 | 100 | 100 | 94.7 | **92.38** | 87.2 | 81.78 | 78.07 | **3010** |
| udify | gold-tok | 100 | 100 | 100 | 94.33 | 90.47 | 84.02 | 86.32 | 81.78 | 93 |

### French-Sequoia
Download link: [lima-deep-models-fra-french_0.1.5_all.deb](https://github.com/aymara/lima-models/releases/download/v0.1.5-beta/lima-deep-models-fra-french_0.1.5_all.deb)
| Tool | Mode | Tokens | Sentences | Words | UPOS | UFeats | Lemmas | UAS | LAS | Speed |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lima | raw | 99.69 | 84.22 | 97.94 | 96.06 | 89.28 | 94.91 | 85.09 | 82.4 | 291 |
| lima | gold-tok | 100 | 100 | 100 | **98.25** | 91.33 | 96.91 | 89.1 | 86.48 | 300 |
| udpipe | raw | 99.79 | 87.5 | 99.09 | 96.1 | 94.93 | 96.93 | 84.85 | 82.09 | **3349** |
| udpipe | gold-tok | 100 | 100 | 100 | 97.08 | **95.84** | **97.82** | 86.83 | 84.13 | **3349** |
| udify | gold-tok | 100 | 100 | 100 | 97.93 | 89.41 | 97.24 | **92.07** | **89.22** | 86 |

### Galician-CTG
Download link: [lima-deep-models-glg-galician_0.1.5_all.deb](https://github.com/aymara/lima-models/releases/download/v0.1.5-beta/lima-deep-models-glg-galician_0.1.5_all.deb)
| Tool | Mode | Tokens | Sentences | Words | UPOS | UFeats | Lemmas | UAS | LAS | Speed |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lima | raw | 99.86 | 95.76 | 96.42 | 92.82 | 96.18 | 92.86 | 76.02 | 72.43 | 563 |
| lima | gold-tok | 100 | 100 | 100 | 96.51 | 99.76 | 96.5 | 82.93 | 78.97 | 585 |
| udpipe | raw | 99.9 | 97.22 | 99.22 | 96.29 | 99.01 | 96.2 | 79.26 | 76.22 | 2703 |
| udpipe | gold-tok | 100 | 100 | 100 | **97.03** | **99.79** | 96.94 | 80.84 | 77.69 | **3717** |
| udify | gold-tok | 100 | 100 | 100 | 96.64 | 97.51 | **97.36** | **84.83** | **81** | 96 |

### German-HDT
Download link: [lima-deep-models-deu-german_0.1.5_all.deb](https://github.com/aymara/lima-models/releases/download/v0.1.5-beta/lima-deep-models-deu-german_0.1.5_all.deb)
| Tool | Mode | Tokens | Sentences | Words | UPOS | UFeats | Lemmas | UAS | LAS | Speed |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lima | raw | 100 | 95.67 | 100 | 90.56 | 32.77 | 74.61 | 88.09 | 81.31 | 299 |
| lima | gold-tok | 100 | 100 | 100 | 90.58 | 32.78 | 74.61 | 88.49 | 81.69 | 312 |
| udpipe | raw | 99.92 | 92.59 | 99.92 | 97.85 | 91.38 | 94.53 | 93.97 | 92.26 | 1576 |
| udpipe | gold-tok | 100 | 100 | 100 | **97.93** | **91.48** | **94.61** | **94.61** | **92.91** | **2065** |
| udify | gold-tok | 100 | 100 | 100 | 91.1 | 33.14 | 74.74 | 90.5 | 85.21 | 106 |

### Greek-GDT
Download link: [lima-deep-models-ell-greek_0.1.5_all.deb](https://github.com/aymara/lima-models/releases/download/v0.1.5-beta/lima-deep-models-ell-greek_0.1.5_all.deb)
| Tool | Mode | Tokens | Sentences | Words | UPOS | UFeats | Lemmas | UAS | LAS | Speed |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lima | raw | 99.88 | 90.21 | 96.33 | 93.76 | 84.48 | 90.69 | 84.65 | 81.11 | 315 |
| lima | gold-tok | 100 | 100 | 100 | **97.48** | 89.06 | 94.41 | 89.59 | 86.62 | 332 |
| udpipe | raw | 99.88 | 90.19 | 99.87 | 95.68 | 90.29 | 94.63 | 86.52 | 83.05 | **2668** |
| udpipe | gold-tok | 100 | 100 | 100 | 95.86 | 90.47 | **94.72** | 87.16 | 83.68 | **2668** |
| udify | gold-tok | 100 | 100 | 100 | 94.07 | **93.16** | 90.1 | **94.32** | **92.13** | 88 |

### Hebrew-HTB
Download link: [lima-deep-models-heb-hebrew_0.1.5_all.deb](https://github.com/aymara/lima-models/releases/download/v0.1.5-beta/lima-deep-models-heb-hebrew_0.1.5_all.deb)
| Tool | Mode | Tokens | Sentences | Words | UPOS | UFeats | Lemmas | UAS | LAS | Speed |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lima | raw | 99.98 | 100 | 57.8 | 54.93 | 42.36 | 53.19 | 33.93 | 31.51 | 375 |
| lima | gold-tok | 100 | 100 | 100 | 96.78 | 81.28 | 88.28 | 87.47 | 83.88 | 386 |
| udpipe | raw | 99.94 | 99.39 | 85.04 | 80.5 | 78.7 | 81.58 | 61.69 | 58.3 | 2047 |
| udpipe | gold-tok | 100 | 100 | 100 | 94.9 | 92.66 | **95.42** | 83.59 | 79.58 | **2457** |
| udify | gold-tok | 100 | 100 | 100 | **96.9** | **93.34** | 94.79 | **91.71** | **88.14** | 94 |

### Hindi-HDTB
Download link: [lima-deep-models-hin-hindi_0.1.5_all.deb](https://github.com/aymara/lima-models/releases/download/v0.1.5-beta/lima-deep-models-hin-hindi_0.1.5_all.deb)
| Tool | Mode | Tokens | Sentences | Words | UPOS | UFeats | Lemmas | UAS | LAS | Speed |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lima | raw | 100 | 99.08 | 100 | 97.36 | 84.2 | 91.78 | 93.78 | 90.2 | 527 |
| lima | gold-tok | 100 | 100 | 100 | **97.38** | 84.21 | 91.78 | **93.87** | **90.29** | 536 |
| udpipe | raw | 100 | 98.9 | 100 | 95.87 | 90.38 | 98.06 | 91.26 | 87.17 | 738 |
| udpipe | gold-tok | 100 | 100 | 100 | 95.88 | 90.39 | 98.06 | 91.35 | 87.25 | **805** |
| udify | gold-tok | 100 | 100 | 100 | 97.3 | **92.85** | **98.52** | 93.06 | 89.18 | 105 |

### Hungarian-Szeged
Download link: [lima-deep-models-hun-hungarian_0.1.5_all.deb](https://github.com/aymara/lima-models/releases/download/v0.1.5-beta/lima-deep-models-hun-hungarian_0.1.5_all.deb)
| Tool | Mode | Tokens | Sentences | Words | UPOS | UFeats | Lemmas | UAS | LAS | Speed |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lima | raw | 99.87 | 95.49 | 99.87 | 94.12 | 85.19 | 82.87 | 77.9 | 71.71 | 284 |
| lima | gold-tok | 100 | 100 | 100 | 94.19 | 85.3 | 82.96 | 78.66 | 72.35 | 300 |
| udpipe | raw | 99.85 | 95.89 | 99.85 | 90.64 | 88.11 | 88.55 | 72.81 | 67.17 | **3483** |
| udpipe | gold-tok | 100 | 100 | 100 | 90.72 | **88.2** | 88.71 | 73.32 | 67.57 | **3483** |
| udify | gold-tok | 100 | 100 | 100 | **96.4** | 87.11 | **90.75** | **89.73** | **85.14** | 95 |

### Indonesian-GSD
Download link: [lima-deep-models-ind-indonesian_0.1.5_all.deb](https://github.com/aymara/lima-models/releases/download/v0.1.5-beta/lima-deep-models-ind-indonesian_0.1.5_all.deb)
| Tool | Mode | Tokens | Sentences | Words | UPOS | UFeats | Lemmas | UAS | LAS | Speed |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lima | raw | 100 | 93.13 | 100 | 93.25 | 89.69 | **98.9** | 82.57 | 75.26 | 319 |
| lima | gold-tok | 100 | 100 | 100 | 93.26 | 89.7 | **98.9** | 82.96 | 75.7 | 330 |
| udpipe | raw | 100 | 94.13 | 100 | 93.01 | 93.91 | 92.19 | 81.01 | 74.56 | **2945** |
| udpipe | gold-tok | 100 | 100 | 100 | 93.03 | **93.93** | 92.19 | 81.18 | 74.77 | 2356 |
| udify | gold-tok | 100 | 100 | 100 | **93.4** | 93.42 | 98.67 | **86.42** | **79.95** | 94 |

### Irish-IDT
Download link: [lima-deep-models-gle-irish_0.1.5_all.deb](https://github.com/aymara/lima-models/releases/download/v0.1.5-beta/lima-deep-models-gle-irish_0.1.5_all.deb)
| Tool | Mode | Tokens | Sentences | Words | UPOS | UFeats | Lemmas | UAS | LAS | Speed |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lima | raw | 99.63 | 97.59 | 99.63 | 89.17 | 58.42 | 83.94 | 75.68 | 62 | 284 |
| lima | gold-tok | 100 | 100 | 100 | 89.45 | 58.75 | 84.16 | 75.76 | 62.1 | 296 |
| udpipe | raw | 99.69 | 97.47 | 99.69 | 89.23 | 77.37 | 87.88 | 76.73 | 65.14 | **2527** |
| udpipe | gold-tok | 100 | 100 | 100 | 89.46 | **77.61** | **88.13** | 77.02 | **65.43** | **2527** |
| udify | gold-tok | 100 | 100 | 100 | **89.86** | 71.95 | 83.18 | **80.42** | 64.33 | 77 |

### Italian-ISDT
Download link: [lima-deep-models-ita-italian_0.1.5_all.deb](https://github.com/aymara/lima-models/releases/download/v0.1.5-beta/lima-deep-models-ita-italian_0.1.5_all.deb)
| Tool | Mode | Tokens | Sentences | Words | UPOS | UFeats | Lemmas | UAS | LAS | Speed |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lima | raw | 99.91 | 98.76 | 98.93 | 96.85 | 93.84 | 90.91 | 88.97 | 86.7 | 313 |
| lima | gold-tok | 100 | 100 | 100 | 97.94 | 94.9 | 91.8 | 91.21 | 88.96 | 330 |
| udpipe | raw | 99.93 | 98.76 | 99.84 | 97.18 | 97.1 | 97.37 | 88.78 | 86.21 | 1488 |
| udpipe | gold-tok | 100 | 100 | 100 | 97.35 | 97.25 | 97.51 | 89.14 | 86.61 | **1736** |
| udify | gold-tok | 100 | 100 | 100 | **98.54** | **97.99** | **97.92** | **95.51** | **93.74** | 91 |

### Japanese-GSD
Download link: [lima-deep-models-jpn-japanese_0.1.5_all.deb](https://github.com/aymara/lima-models/releases/download/v0.1.5-beta/lima-deep-models-jpn-japanese_0.1.5_all.deb)
| Tool | Mode | Tokens | Sentences | Words | UPOS | UFeats | Lemmas | UAS | LAS | Speed |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lima | raw | 85.48 | 94.3 | 85.48 | 80.61 | 84.98 | 80.72 | 64.57 | 59.6 | 371 |
| lima | gold-tok | 100 | 100 | 100 | 92.93 | **99.45** | 93.09 | 84.87 | 76.53 | 378 |
| udpipe | raw | 85.52 | 94.61 | 85.52 | 79.7 | 83.45 | 83.74 | 63.91 | 58.86 | **2607** |
| udpipe | gold-tok | 100 | 100 | 100 | 91.5 | 97.56 | 96.74 | 83.55 | 75.33 | **2607** |
| udify | gold-tok | 100 | 100 | 100 | **93.26** | 97.55 | **96.92** | **85.78** | **77.2** | 93 |

### Kazakh-KTB
Download link: [lima-deep-models-kaz-kazakh_0.1.5_all.deb](https://github.com/aymara/lima-models/releases/download/v0.1.5-beta/lima-deep-models-kaz-kazakh_0.1.5_all.deb)
| Tool | Mode | Tokens | Sentences | Words | UPOS | UFeats | Lemmas | UAS | LAS | Speed |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lima | raw | 93.72 | 90.86 | 94.82 | 82.34 | 61.42 | 66.63 | 68.87 | 59.08 | 63 |
| lima | gold-tok | 100 | 100 | 100 | **86.73** | 64.59 | 70.27 | **75.35** | **64.35** | 66 |
| udify | gold-tok | 100 | 100 | 100 | 85.62 | **66.25** | **77.74** | 74.43 | 63.55 | **87** |

### Korean-Kaist
Download link: [lima-deep-models-kor-korean_0.1.5_all.deb](https://github.com/aymara/lima-models/releases/download/v0.1.5-beta/lima-deep-models-kor-korean_0.1.5_all.deb)
| Tool | Mode | Tokens | Sentences | Words | UPOS | UFeats | Lemmas | UAS | LAS | Speed |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lima | raw | 100 | 100 | 100 | 94.24 | **100** | 87.74 | 86.81 | 84.02 | 316 |
| lima | gold-tok | 100 | 100 | 100 | 94.24 | **100** | 87.74 | 86.81 | 84.02 | 333 |
| udpipe | raw | 99.95 | 100 | 99.95 | 93.32 | 99.95 | 88.48 | 77.9 | 70.59 | 2182 |
| udpipe | gold-tok | 100 | 100 | 100 | 93.36 | **100** | **88.51** | 77.99 | 70.66 | **2364** |
| udify | gold-tok | 100 | 100 | 100 | **94.42** | 99.96 | 87.03 | **87.46** | **84.21** | 100 |

### Kurmanji-MG
Download link: [lima-deep-models-kmr-kurmanji_0.1.5_all.deb](https://github.com/aymara/lima-models/releases/download/v0.1.5-beta/lima-deep-models-kmr-kurmanji_0.1.5_all.deb)
| Tool | Mode | Tokens | Sentences | Words | UPOS | UFeats | Lemmas | UAS | LAS | Speed |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lima | raw | 97.14 | 90.61 | 96.81 | 62.99 | 37.73 | 53.23 | 36.07 | 20.4 | 87 |
| lima | gold-tok | 100 | 100 | 100 | **64.69** | **38.32** | 54.15 | **39.4** | **22.18** | 81 |
| udify | gold-tok | 100 | 100 | 100 | 60.57 | 38.13 | **58.76** | 35.49 | 20.17 | **100** |

### Latin-PROIEL
Download link: [lima-deep-models-lat-latin_0.1.5_all.deb](https://github.com/aymara/lima-models/releases/download/v0.1.5-beta/lima-deep-models-lat-latin_0.1.5_all.deb)
| Tool | Mode | Tokens | Sentences | Words | UPOS | UFeats | Lemmas | UAS | LAS | Speed |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lima | raw | 100 | 39.29 | 100 | 95.1 | 82.31 | 93.88 | 71.78 | 65.83 | 310 |
| lima | gold-tok | 100 | 100 | 100 | 95.47 | 83.15 | 94.22 | 80.8 | 74.75 | 277 |
| udpipe | raw | 99.87 | 36.81 | 99.87 | 94.52 | 86.69 | 94.52 | 65.94 | 60.11 | 1281 |
| udpipe | gold-tok | 100 | 100 | 100 | 94.71 | 87.19 | **94.68** | 73.36 | 67.31 | **1761** |
| udify | gold-tok | 100 | 100 | 100 | **96.93** | **89.69** | 92.42 | **84.63** | **79.87** | 89 |

### Latvian-LVTB
Download link: [lima-deep-models-lav-latvian_0.1.5_all.deb](https://github.com/aymara/lima-models/releases/download/v0.1.5-beta/lima-deep-models-lav-latvian_0.1.5_all.deb)
| Tool | Mode | Tokens | Sentences | Words | UPOS | UFeats | Lemmas | UAS | LAS | Speed |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lima | raw | 99.48 | 97.92 | 99.48 | 96.05 | 84.68 | 93.82 | 86.42 | 82.62 | 282 |
| lima | gold-tok | 100 | 100 | 100 | **96.42** | 84.99 | **94.14** | 87.26 | 83.33 | 299 |
| udpipe | raw | 99.33 | 98.74 | 99.33 | 93.48 | 89.55 | 92.72 | 78.77 | 74.25 | **2200** |
| udpipe | gold-tok | 100 | 100 | 100 | 94.05 | **90.1** | 93.26 | 79.71 | 75.08 | **2200** |
| udify | gold-tok | 100 | 100 | 100 | 96.29 | 84.33 | 92.12 | **89.82** | **85.07** | 93 |

### Lithuanian-ALKSNIS
Download link: [lima-deep-models-lit-lithuanian_0.1.5_all.deb](https://github.com/aymara/lima-models/releases/download/v0.1.5-beta/lima-deep-models-lit-lithuanian_0.1.5_all.deb)
| Tool | Mode | Tokens | Sentences | Words | UPOS | UFeats | Lemmas | UAS | LAS | Speed |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lima | raw | 99.72 | 87.7 | 99.72 | 94.99 | 79.35 | 90.42 | 78.07 | 69.82 | 239 |
| lima | gold-tok | 100 | 100 | 100 | **95.16** | 79.49 | **90.62** | **79.46** | **71.16** | 253 |
| udpipe | raw | 99.91 | 87.87 | 99.91 | 90.33 | 81.2 | 88.75 | 68.95 | 60.09 | **2712** |
| udpipe | gold-tok | 100 | 100 | 100 | 90.51 | **81.38** | 88.89 | 69.83 | 60.96 | **2712** |
| udify | gold-tok | 100 | 100 | 100 | 85.77 | 53.98 | 64.89 | 76.28 | 63.49 | 91 |

### Maltese-MUDT
Download link: [lima-deep-models-mlt-maltese_0.1.5_all.deb](https://github.com/aymara/lima-models/releases/download/v0.1.5-beta/lima-deep-models-mlt-maltese_0.1.5_all.deb)
| Tool | Mode | Tokens | Sentences | Words | UPOS | UFeats | Lemmas | UAS | LAS | Speed |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lima | raw | 99.81 | 82.34 | 99.81 | 90.68 | 99.81 | 99.81 | 73.73 | 65.22 | 499 |
| lima | gold-tok | 100 | 100 | 100 | 90.72 | **100** | **100** | 74.9 | 66.27 | 497 |
| udpipe | raw | 99.84 | 86.29 | 99.84 | 93.85 | 99.84 | 99.84 | 77.65 | 71.75 | **3691** |
| udpipe | gold-tok | 100 | 100 | 100 | **93.94** | **100** | **100** | 78.02 | 72.15 | **3691** |
| udify | gold-tok | 100 | 100 | 100 | 91.18 | 99.89 | **100** | **83.24** | **73.79** | 89 |

### Marathi-UFAL
Download link: [lima-deep-models-mar-marathi_0.1.5_all.deb](https://github.com/aymara/lima-models/releases/download/v0.1.5-beta/lima-deep-models-mar-marathi_0.1.5_all.deb)
| Tool | Mode | Tokens | Sentences | Words | UPOS | UFeats | Lemmas | UAS | LAS | Speed |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lima | raw | 96.77 | 86.36 | 86.15 | 65.31 | 43.2 | 67.34 | 47.27 | 33.29 | 68 |
| lima | gold-tok | 100 | 100 | 100 | 74.03 | 46.84 | 67.48 | 65.29 | 44.66 | 80 |
| udpipe | raw | 98.8 | 92.63 | 90.25 | 71.5 | 60.75 | 76.25 | 60.5 | 49.5 | **82** |
| udpipe | gold-tok | 100 | 100 | 100 | 77.67 | **63.35** | **76.46** | 68.45 | 54.85 | 22 |
| udify | gold-tok | 100 | 100 | 100 | **88.35** | 58.25 | 73.06 | **78.88** | **66.99** | 34 |

### Naija-NSC
Download link: [lima-deep-models-pcm-naija_0.1.5_all.deb](https://github.com/aymara/lima-models/releases/download/v0.1.5-beta/lima-deep-models-pcm-naija_0.1.5_all.deb)
| Tool | Mode | Tokens | Sentences | Words | UPOS | UFeats | Lemmas | UAS | LAS | Speed |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lima | raw | 85.85 | 0.27 | 85.85 | 83.14 | 76.97 | 78.81 | 58.27 | 54.58 | **448** |
| lima | gold-tok | 100 | 100 | 100 | **97.49** | **90.68** | **91.75** | **87.59** | **83.43** | 421 |
| udify | gold-tok | 100 | 100 | 100 | 53.67 | 58.04 | 90.66 | 49.47 | 33.71 | 93 |

### North\_Sami-Giella
Download link: [lima-deep-models-sme-north\_sami_0.1.5_all.deb](https://github.com/aymara/lima-models/releases/download/v0.1.5-beta/lima-deep-models-sme-north\_sami_0.1.5_all.deb)
| Tool | Mode | Tokens | Sentences | Words | UPOS | UFeats | Lemmas | UAS | LAS | Speed |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lima | raw | 99.8 | 99.65 | 99.8 | 86.54 | 76.16 | 77.06 | 68.06 | 59.82 | 360 |
| lima | gold-tok | 100 | 100 | 100 | 86.7 | 76.24 | 77.22 | 68.18 | 59.93 | 383 |
| udpipe | raw | 99.87 | 98.79 | 99.87 | 87.75 | 82.46 | 81.97 | 64.65 | 57.92 | **3337** |
| udpipe | gold-tok | 100 | 100 | 100 | 87.91 | 82.58 | **82.1** | 64.91 | 58.17 | **3337** |
| udify | gold-tok | 100 | 100 | 100 | **90.39** | **84.32** | 73.19 | **74.23** | **67.22** | 87 |

### Norwegian-Bokmaal
Download link: [lima-deep-models-nob-norwegian_0.1.5_all.deb](https://github.com/aymara/lima-models/releases/download/v0.1.5-beta/lima-deep-models-nob-norwegian_0.1.5_all.deb)
| Tool | Mode | Tokens | Sentences | Words | UPOS | UFeats | Lemmas | UAS | LAS | Speed |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lima | raw | 100 | 97.47 | 100 | 98.11 | 87.64 | 85.49 | 91 | 88.57 | 347 |
| lima | gold-tok | 100 | 100 | 100 | 98.12 | 87.64 | 85.5 | 91.27 | 88.78 | 358 |
| udpipe | raw | 99.98 | 96.45 | 99.98 | 96.62 | 95.37 | 96.93 | 87.18 | 84.36 | 2305 |
| udpipe | gold-tok | 100 | 100 | 100 | 96.71 | 95.41 | 96.95 | 87.54 | 84.73 | **2497** |
| udify | gold-tok | 100 | 100 | 100 | **98.21** | **96.37** | **97.58** | **91.85** | **90.05** | 101 |

### Norwegian-Nynorsk
Download link: [lima-deep-models-nno-norwegian_0.1.5_all.deb](https://github.com/aymara/lima-models/releases/download/v0.1.5-beta/lima-deep-models-nno-norwegian_0.1.5_all.deb)
| Tool | Mode | Tokens | Sentences | Words | UPOS | UFeats | Lemmas | UAS | LAS | Speed |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lima | raw | 99.91 | 93.68 | 99.91 | 10.92 | 38.89 | 54.38 | 9.38 | 2.81 | 286 |
| lima | gold-tok | 100 | 100 | 100 | 11.1 | 38.96 | 54.49 | 9.66 | 2.95 | 290 |
| udpipe | raw | 99.91 | 94.11 | 99.91 | 96.04 | 94.9 | 96.28 | 85.71 | 82.77 | 1770 |
| udpipe | gold-tok | 100 | 100 | 100 | 96.21 | 95.05 | 96.4 | 86.44 | 83.48 | **2252** |
| udify | gold-tok | 100 | 100 | 100 | **97.88** | **96.59** | **97.33** | **92.15** | **90.19** | 99 |

### Old\_Church\_Slavonic-PROIEL
Download link: [lima-deep-models-chu-old\_church\_slavonic_0.1.5_all.deb](https://github.com/aymara/lima-models/releases/download/v0.1.5-beta/lima-deep-models-chu-old\_church\_slavonic_0.1.5_all.deb)
| Tool | Mode | Tokens | Sentences | Words | UPOS | UFeats | Lemmas | UAS | LAS | Speed |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lima | raw | 100 | 38.04 | 100 | 94.43 | 76.85 | 91.65 | 73.37 | 67.88 | 291 |
| lima | gold-tok | 100 | 100 | 100 | **94.82** | 77.4 | **91.84** | **84.45** | **78.73** | 295 |
| udpipe | raw | 100 | 41.43 | 100 | 93.49 | 86.76 | 90.94 | 71.19 | 65.3 | 2508 |
| udpipe | gold-tok | 100 | 100 | 100 | 93.82 | **87.44** | 91.04 | 79.53 | 73.22 | **3344** |
| udify | gold-tok | 100 | 100 | 100 | 80.17 | 69.8 | 68.08 | 70.34 | 60.29 | 82 |

### Old\_French-SRCMF
Download link: [lima-deep-models-fro-old\_french_0.1.5_all.deb](https://github.com/aymara/lima-models/releases/download/v0.1.5-beta/lima-deep-models-fro-old\_french_0.1.5_all.deb)
| Tool | Mode | Tokens | Sentences | Words | UPOS | UFeats | Lemmas | UAS | LAS | Speed |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lima | raw | 100 | 76.15 | 100 | 90.33 | 87.3 | **100** | 87.24 | 81.34 | 409 |
| lima | gold-tok | 100 | 100 | 100 | 90.68 | 87.56 | **100** | 89.2 | 83.26 | 506 |
| udpipe | raw | 99.91 | 100 | 99.91 | 89.91 | 96.03 | 99.91 | 85.65 | 79.02 | **2893** |
| udpipe | gold-tok | 100 | 100 | 100 | 89.99 | 96.11 | **100** | 85.72 | 79.09 | **2893** |
| udify | gold-tok | 100 | 100 | 100 | **91.51** | **96.99** | **100** | **92** | **86.65** | 85 |

### Old\_Russian-TOROT
Download link: [lima-deep-models-orv-old\_russian_0.1.5_all.deb](https://github.com/aymara/lima-models/releases/download/v0.1.5-beta/lima-deep-models-orv-old\_russian_0.1.5_all.deb)
| Tool | Mode | Tokens | Sentences | Words | UPOS | UFeats | Lemmas | UAS | LAS | Speed |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lima | raw | 100 | 26.11 | 100 | 90.71 | 71.37 | 82.84 | 65.75 | 58.81 | 291 |
| lima | gold-tok | 100 | 100 | 100 | **91.48** | 72.49 | **83.55** | **78.33** | **70.9** | 275 |
| udpipe | raw | 100 | 29.6 | 100 | 89.86 | 81.84 | 81.16 | 63.85 | 56.92 | 1396 |
| udpipe | gold-tok | 100 | 100 | 100 | 90.46 | **82.52** | 81.31 | 73.44 | 65.88 | **1707** |
| udify | gold-tok | 100 | 100 | 100 | 69.87 | 52.93 | 39.98 | 60.49 | 48.34 | 82 |

### Persian-Seraji
Download link: [lima-deep-models-fas-persian_0.1.5_all.deb](https://github.com/aymara/lima-models/releases/download/v0.1.5-beta/lima-deep-models-fas-persian_0.1.5_all.deb)
| Tool | Mode | Tokens | Sentences | Words | UPOS | UFeats | Lemmas | UAS | LAS | Speed |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lima | raw | 99.98 | 99.25 | 99.06 | 96.67 | 86.98 | 96.18 | 87.12 | 83.01 | 368 |
| lima | gold-tok | 100 | 100 | 100 | **97.56** | 87.41 | **96.85** | 88.59 | 84.48 | 385 |
| udpipe | raw | 100 | 98.75 | 99.65 | 96.02 | 96.09 | 93.64 | 83.63 | 79.57 | **3205** |
| udpipe | gold-tok | 100 | 100 | 100 | 96.32 | **96.41** | 93.91 | 84.3 | 80.17 | 2671 |
| udify | gold-tok | 100 | 100 | 100 | 96.23 | 94.79 | 92.64 | **89.77** | **85.96** | 90 |

### Polish-PDB
Download link: [lima-deep-models-pol-polish_0.1.5_all.deb](https://github.com/aymara/lima-models/releases/download/v0.1.5-beta/lima-deep-models-pol-polish_0.1.5_all.deb)
| Tool | Mode | Tokens | Sentences | Words | UPOS | UFeats | Lemmas | UAS | LAS | Speed |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lima | raw | 99.86 | 96.7 | 98.72 | 97.39 | 84.85 | 94.97 | 88.4 | 85.69 | 296 |
| lima | gold-tok | 100 | 100 | 100 | **98.68** | 86.17 | 95.98 | **92.12** | **89.34** | 308 |
| udpipe | raw | 99.86 | 97.33 | 99.85 | 97.07 | 88.64 | 95.95 | 86.53 | 82.74 | 1769 |
| udpipe | gold-tok | 100 | 100 | 100 | 97.19 | **88.78** | **96.09** | 87.02 | 83.2 | **2401** |
| udify | gold-tok | 100 | 100 | 100 | 96.79 | 67.31 | 91.95 | 88.4 | 81.04 | 95 |

### Portuguese-GSD
Download link: [lima-deep-models-por-portuguese_0.1.5_all.deb](https://github.com/aymara/lima-models/releases/download/v0.1.5-beta/lima-deep-models-por-portuguese_0.1.5_all.deb)
| Tool | Mode | Tokens | Sentences | Words | UPOS | UFeats | Lemmas | UAS | LAS | Speed |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lima | raw | 99.93 | 96.63 | 96.71 | 94.57 | 93.39 | 96.08 | 86.72 | 84.52 | 316 |
| lima | gold-tok | 100 | 100 | 100 | **97.95** | 96.71 | **99.41** | 91.36 | **89.42** | 316 |
| udpipe | raw | 99.95 | 97.12 | 97.98 | 95.16 | 97.77 | 96.39 | 86.15 | 84.03 | 2253 |
| udpipe | gold-tok | 100 | 100 | 100 | 97.17 | **97.95** | 94.71 | 88.26 | 86.1 | **2867** |
| udify | gold-tok | 100 | 100 | 100 | 97.16 | 74.68 | 98.76 | **92.08** | 87.07 | 96 |

### Romanian-Nonstandard
Download link: [lima-deep-models-ron-romanian_0.1.5_all.deb](https://github.com/aymara/lima-models/releases/download/v0.1.5-beta/lima-deep-models-ron-romanian_0.1.5_all.deb)
| Tool | Mode | Tokens | Sentences | Words | UPOS | UFeats | Lemmas | UAS | LAS | Speed |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lima | raw | 98.98 | 96.92 | 98.98 | 95.56 | 61.03 | 91.55 | 86.72 | 81.32 | 387 |
| lima | gold-tok | 100 | 100 | 100 | **96.54** | 61.7 | 92.37 | 88.21 | 82.67 | 399 |
| udpipe | raw | 98.2 | 96.73 | 98.2 | 94.2 | 88.22 | 92.41 | 82.35 | 77.09 | 1908 |
| udpipe | gold-tok | 100 | 100 | 100 | 95.94 | **89.74** | **94.03** | 84.89 | 79.42 | **2099** |
| udify | gold-tok | 100 | 100 | 100 | 95.73 | 88.17 | 90.44 | **90.64** | **85.81** | 92 |

### Russian-SynTagRus
Download link: [lima-deep-models-rus-russian_0.1.5_all.deb](https://github.com/aymara/lima-models/releases/download/v0.1.5-beta/lima-deep-models-rus-russian_0.1.5_all.deb)
| Tool | Mode | Tokens | Sentences | Words | UPOS | UFeats | Lemmas | UAS | LAS | Speed |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lima | raw | 99.63 | 98.61 | 99.63 | 98.45 | 96.18 | 95.55 | 92.09 | 90.41 | 299 |
| lima | gold-tok | 100 | 100 | 100 | 98.8 | **96.5** | 95.81 | 92.7 | 91 | 301 |
| udpipe | raw | 99.6 | 98.8 | 99.6 | 97.78 | 93.55 | 96.55 | 87.62 | 85.01 | 1989 |
| udpipe | gold-tok | 100 | 100 | 100 | 98.16 | 93.87 | **96.9** | 88.34 | 85.68 | **2607** |
| udify | gold-tok | 100 | 100 | 100 | **98.87** | 96.19 | 94.71 | **94.59** | **92.88** | 103 |

### Scottish\_Gaelic-ARCOSG
Download link: [lima-deep-models-gla-scottish\_gaelic_0.1.5_all.deb](https://github.com/aymara/lima-models/releases/download/v0.1.5-beta/lima-deep-models-gla-scottish\_gaelic_0.1.5_all.deb)
| Tool | Mode | Tokens | Sentences | Words | UPOS | UFeats | Lemmas | UAS | LAS | Speed |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lima | raw | 99.7 | 50.92 | 99.7 | 86.99 | 69.6 | 91.36 | 70.56 | 61.64 | 393 |
| lima | gold-tok | 100 | 100 | 100 | 88.09 | 70.24 | 91.97 | 77.09 | 67.29 | 328 |
| udpipe | raw | 99.58 | 55.57 | 99.58 | 90.47 | 84.6 | 92.07 | 73.9 | 66.13 | 2004 |
| udpipe | gold-tok | 100 | 100 | 100 | **91.07** | **84.95** | **92.46** | **78.42** | **70.34** | **2505** |
| udify | gold-tok | 100 | 100 | 100 | 58.15 | 29.18 | 60.98 | 54.45 | 28.17 | 88 |

### Serbian-SET
Download link: [lima-deep-models-srp-serbian_0.1.5_all.deb](https://github.com/aymara/lima-models/releases/download/v0.1.5-beta/lima-deep-models-srp-serbian_0.1.5_all.deb)
| Tool | Mode | Tokens | Sentences | Words | UPOS | UFeats | Lemmas | UAS | LAS | Speed |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lima | raw | 99.96 | 94.63 | 99.96 | 97.98 | 80.46 | 94.99 | 89.49 | 84.25 | 262 |
| lima | gold-tok | 100 | 100 | 100 | **98.06** | 80.48 | 95.06 | 90.04 | 84.76 | 246 |
| udpipe | raw | 99.99 | 93 | 99.99 | 97.15 | 91.09 | 95.08 | 85.7 | 80.59 | **2855** |
| udpipe | gold-tok | 100 | 100 | 100 | 97.23 | **91.21** | 95.12 | 86.3 | 81.14 | **2855** |
| udify | gold-tok | 100 | 100 | 100 | 95.93 | 77.69 | **97.15** | **96.65** | **92.65** | 102 |

### Slovak-SNK
Download link: [lima-deep-models-slk-slovak_0.1.5_all.deb](https://github.com/aymara/lima-models/releases/download/v0.1.5-beta/lima-deep-models-slk-slovak_0.1.5_all.deb)
| Tool | Mode | Tokens | Sentences | Words | UPOS | UFeats | Lemmas | UAS | LAS | Speed |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lima | raw | 99.96 | 85.62 | 99.96 | 95.64 | 81.61 | 91.11 | 86.97 | 82.84 | 319 |
| lima | gold-tok | 100 | 100 | 100 | 95.68 | 81.79 | 91.14 | 88.88 | 84.66 | 335 |
| udpipe | raw | 100 | 85.28 | 100 | 92.93 | 80.34 | 86.56 | 80.95 | 75.97 | **2171** |
| udpipe | gold-tok | 100 | 100 | 100 | 93.06 | 80.53 | 86.61 | 82.46 | 77.45 | **2171** |
| udify | gold-tok | 100 | 100 | 100 | **97.08** | **89.21** | **94.3** | **96.05** | **93.3** | 97 |

### Slovenian-SSJ
Download link: [lima-deep-models-slv-slovenian_0.1.5_all.deb](https://github.com/aymara/lima-models/releases/download/v0.1.5-beta/lima-deep-models-slv-slovenian_0.1.5_all.deb)
| Tool | Mode | Tokens | Sentences | Words | UPOS | UFeats | Lemmas | UAS | LAS | Speed |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lima | raw | 98.5 | 66.67 | 98.5 | 96.82 | 84.88 | 94.81 | 84.33 | 82.14 | 311 |
| lima | gold-tok | 100 | 100 | 100 | 98.29 | 86.58 | 96.24 | 91.07 | 88.76 | 296 |
| udpipe | raw | 97.99 | 67.98 | 97.99 | 94.25 | 86.52 | 93.41 | 79.61 | 76.43 | **2011** |
| udpipe | gold-tok | 100 | 100 | 100 | 96.19 | 88.69 | 95.33 | 85.18 | 81.81 | **2011** |
| udify | gold-tok | 100 | 100 | 100 | **98.76** | **93.36** | **96.71** | **94.75** | **93.07** | 101 |

### Spanish-AnCora
Download link: [lima-deep-models-spa-spanish_0.1.5_all.deb](https://github.com/aymara/lima-models/releases/download/v0.1.5-beta/lima-deep-models-spa-spanish_0.1.5_all.deb)
| Tool | Mode | Tokens | Sentences | Words | UPOS | UFeats | Lemmas | UAS | LAS | Speed |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lima | raw | 99.96 | 97.88 | 99.44 | 93.37 | 87.31 | 87.5 | 80.33 | 70.71 | 450 |
| lima | gold-tok | 100 | 100 | 100 | 93.93 | 87.52 | 88.04 | 81.58 | 71.51 | 466 |
| udpipe | raw | 99.97 | 98.32 | 99.95 | 98.32 | 98.13 | 98.48 | 88.22 | 85.1 | 2024 |
| udpipe | gold-tok | 100 | 100 | 100 | **98.36** | **98.17** | **98.52** | 88.4 | 85.26 | **2769** |
| udify | gold-tok | 100 | 100 | 100 | 97.95 | 91.34 | 97.74 | **91.68** | **89.08** | 93 |

### Swedish-Talbanken
Download link: [lima-deep-models-swe-swedish_0.1.5_all.deb](https://github.com/aymara/lima-models/releases/download/v0.1.5-beta/lima-deep-models-swe-swedish_0.1.5_all.deb)
| Tool | Mode | Tokens | Sentences | Words | UPOS | UFeats | Lemmas | UAS | LAS | Speed |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lima | raw | 99.9 | 95.35 | 99.9 | 97.37 | 92.08 | 96.43 | 86.37 | 82.38 | 350 |
| lima | gold-tok | 100 | 100 | 100 | 97.45 | 92.12 | **96.51** | 86.86 | 82.89 | 338 |
| udpipe | raw | 99.89 | 96.13 | 99.89 | 95.59 | 94.46 | 95.38 | 82.49 | 78.56 | 2038 |
| udpipe | gold-tok | 100 | 100 | 100 | 95.7 | 94.54 | 95.45 | 82.87 | 78.89 | **2911** |
| udify | gold-tok | 100 | 100 | 100 | **98.2** | **95.92** | 96.29 | **92.06** | **89.24** | 104 |

### Tamil-TTB
Download link: [lima-deep-models-tam-tamil_0.1.5_all.deb](https://github.com/aymara/lima-models/releases/download/v0.1.5-beta/lima-deep-models-tam-tamil_0.1.5_all.deb)
| Tool | Mode | Tokens | Sentences | Words | UPOS | UFeats | Lemmas | UAS | LAS | Speed |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lima | raw | 99.58 | 96.3 | 85.31 | 73.78 | 63.9 | 75.85 | 48.1 | 41.01 | 148 |
| lima | gold-tok | 100 | 100 | 100 | 86.88 | 75.67 | **88.74** | 70.49 | 60.73 | 163 |
| udpipe | raw | 99.16 | 97.52 | 94.51 | 81.31 | 80.45 | 84.14 | 58.94 | 51.96 | **1989** |
| udpipe | gold-tok | 100 | 100 | 100 | 85.67 | **84.72** | 88.29 | 64.96 | 56.91 | **1989** |
| udify | gold-tok | 100 | 100 | 100 | **91.35** | 81 | 83.86 | **79.44** | **71.44** | 76 |

### Telugu-MTG
Download link: [lima-deep-models-tel-telugu_0.1.5_all.deb](https://github.com/aymara/lima-models/releases/download/v0.1.5-beta/lima-deep-models-tel-telugu_0.1.5_all.deb)
| Tool | Mode | Tokens | Sentences | Words | UPOS | UFeats | Lemmas | UAS | LAS | Speed |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lima | raw | 100 | 97.95 | 100 | 90.98 | 98.34 | **100** | 88.21 | 76.84 | 99 |
| lima | gold-tok | 100 | 100 | 100 | 91.12 | 98.34 | **100** | 88.35 | 77.12 | 124 |
| udpipe | raw | 99.58 | 96.62 | 99.58 | 90.3 | 98.48 | 99.58 | 87.12 | 75.76 | 721 |
| udpipe | gold-tok | 100 | 100 | 100 | 90.57 | 98.89 | **100** | 88.21 | 76.84 | **1442** |
| udify | gold-tok | 100 | 100 | 100 | **93.62** | **99.17** | **100** | **91.96** | **83.36** | 40 |

### Thai-PUD
Download link: [lima-deep-models-tha-thai_0.1.5_all.deb](https://github.com/aymara/lima-models/releases/download/v0.1.5-beta/lima-deep-models-tha-thai_0.1.5_all.deb)
| Tool | Mode | Tokens | Sentences | Words | UPOS | UFeats | Lemmas | UAS | LAS | Speed |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lima | raw | 91.51 | 62.75 | 91.51 | 83.42 | 86.47 | 91.51 | 71.94 | 67.5 | 761 |
| lima | gold-tok | 100 | 100 | 100 | **90.53** | **94.81** | **100** | **84.32** | **77.48** | **892** |
| udify | gold-tok | 100 | 100 | 100 | 56.54 | 69.64 | **100** | 48.64 | 25.71 | 95 |

### Turkish-IMST
Download link: [lima-deep-models-tur-turkish_0.1.5_all.deb](https://github.com/aymara/lima-models/releases/download/v0.1.5-beta/lima-deep-models-tur-turkish_0.1.5_all.deb)
| Tool | Mode | Tokens | Sentences | Words | UPOS | UFeats | Lemmas | UAS | LAS | Speed |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lima | raw | 99.92 | 96.23 | 96.5 | 90.28 | 76.03 | 91.39 | 62.9 | 54.58 | 313 |
| lima | gold-tok | 100 | 100 | 100 | 93.45 | 78.84 | **94.52** | 68.84 | 59.73 | 329 |
| udpipe | raw | 99.92 | 96.97 | 98.3 | 91.64 | 88.48 | 89.95 | 62.17 | 55.09 | **3343** |
| udpipe | gold-tok | 100 | 100 | 100 | 93.04 | **89.87** | 91.44 | 64.51 | 57.15 | **3343** |
| udify | gold-tok | 100 | 100 | 100 | **94.42** | 84.66 | 88.54 | **74.8** | **67.45** | 89 |

### Ukrainian-IU
Download link: [lima-deep-models-ukr-ukrainian_0.1.5_all.deb](https://github.com/aymara/lima-models/releases/download/v0.1.5-beta/lima-deep-models-ukr-ukrainian_0.1.5_all.deb)
| Tool | Mode | Tokens | Sentences | Words | UPOS | UFeats | Lemmas | UAS | LAS | Speed |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lima | raw | 99.65 | 93.18 | 99.63 | 97.01 | 82.15 | 93.83 | 84.52 | 81.37 | 280 |
| lima | gold-tok | 100 | 100 | 100 | 97.42 | 82.4 | 93.99 | 85.44 | 82.22 | 294 |
| udpipe | raw | 99.85 | 96.61 | 99.81 | 94.91 | 84.28 | 93.56 | 79.43 | 74.83 | 1712 |
| udpipe | gold-tok | 100 | 100 | 100 | 95.06 | 84.42 | 93.73 | 79.76 | 75.14 | **2445** |
| udify | gold-tok | 100 | 100 | 100 | **97.81** | **88.62** | **94.5** | **92.57** | **89.93** | 89 |

### Urdu-UDTB
Download link: [lima-deep-models-urd-urdu_0.1.5_all.deb](https://github.com/aymara/lima-models/releases/download/v0.1.5-beta/lima-deep-models-urd-urdu_0.1.5_all.deb)
| Tool | Mode | Tokens | Sentences | Words | UPOS | UFeats | Lemmas | UAS | LAS | Speed |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lima | raw | 99.97 | 98.6 | 99.97 | 93.3 | 75 | 93.99 | 85.53 | 78.48 | 424 |
| lima | gold-tok | 100 | 100 | 100 | 93.34 | 75.03 | 94 | 85.68 | **78.63** | 437 |
| udpipe | raw | 100 | 98.31 | 100 | 92.4 | 80.76 | 93.08 | 83.61 | 76.91 | **740** |
| udpipe | gold-tok | 100 | 100 | 100 | 92.41 | 80.76 | 93.07 | 83.73 | 77.01 | **740** |
| udify | gold-tok | 100 | 100 | 100 | **94.44** | **83.76** | **97.13** | **86.32** | 76.06 | 94 |

### Uyghur-UDT
Download link: [lima-deep-models-uig-uyghur_0.1.5_all.deb](https://github.com/aymara/lima-models/releases/download/v0.1.5-beta/lima-deep-models-uig-uyghur_0.1.5_all.deb)
| Tool | Mode | Tokens | Sentences | Words | UPOS | UFeats | Lemmas | UAS | LAS | Speed |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lima | raw | 99.67 | 81.67 | 99.67 | 85.47 | 73.03 | 90.23 | 69.41 | 54.32 | 354 |
| lima | gold-tok | 100 | 100 | 100 | 85.83 | 73.41 | 90.46 | 71.65 | 56.49 | 365 |
| udpipe | raw | 99.54 | 81.81 | 99.54 | 87.74 | 83.99 | 91.69 | 70.62 | 56.7 | 2582 |
| udpipe | gold-tok | 100 | 100 | 100 | **88.19** | **84.42** | **92.15** | **71.99** | **57.94** | **5165** |
| udify | gold-tok | 100 | 100 | 100 | 75.97 | 71.4 | 81.04 | 65.69 | 48.69 | 93 |

### Vietnamese-VTB
Download link: [lima-deep-models-vie-vietnamese_0.1.5_all.deb](https://github.com/aymara/lima-models/releases/download/v0.1.5-beta/lima-deep-models-vie-vietnamese_0.1.5_all.deb)
| Tool | Mode | Tokens | Sentences | Words | UPOS | UFeats | Lemmas | UAS | LAS | Speed |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lima | raw | 84.66 | 91.78 | 84.66 | 73.53 | 80.45 | 82.83 | 46.39 | 39.73 | 458 |
| lima | gold-tok | 100 | 100 | 100 | 85.29 | 95.37 | 97.41 | 64.81 | 54.39 | 513 |
| udpipe | raw | 85.37 | 93.46 | 85.37 | 76.36 | 85.02 | 84.53 | 45.79 | 40.6 | 2989 |
| udpipe | gold-tok | 100 | 100 | 100 | 87.59 | 99.5 | 98.91 | 62.58 | 54.45 | **3985** |
| udify | gold-tok | 100 | 100 | 100 | **91.32** | **99.6** | **99.18** | **73.79** | **65.57** | 109 |

### Welsh-CCG
Download link: [lima-deep-models-cym-welsh_0.1.5_all.deb](https://github.com/aymara/lima-models/releases/download/v0.1.5-beta/lima-deep-models-cym-welsh_0.1.5_all.deb)
| Tool | Mode | Tokens | Sentences | Words | UPOS | UFeats | Lemmas | UAS | LAS | Speed |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lima | raw | 99.91 | 97.78 | 99.35 | 90.45 | 77.32 | **63.27** | 76.01 | 63.24 | 715 |
| lima | gold-tok | 100 | 100 | 100 | **91.06** | **77.91** | **63.27** | **77.58** | **64.77** | **731** |
| udify | gold-tok | 100 | 100 | 100 | 68.62 | 42.55 | 48.69 | 69.07 | 42.59 | 101 |

### Wolof-WTB
Download link: [lima-deep-models-wol-wolof_0.1.5_all.deb](https://github.com/aymara/lima-models/releases/download/v0.1.5-beta/lima-deep-models-wol-wolof_0.1.5_all.deb)
| Tool | Mode | Tokens | Sentences | Words | UPOS | UFeats | Lemmas | UAS | LAS | Speed |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lima | raw | 99.91 | 92.32 | 98.31 | 89.83 | 80.62 | 72.28 | 74.9 | 66.41 | 701 |
| lima | gold-tok | 100 | 100 | 100 | 91.89 | 82.36 | 73.16 | 78.54 | 69.91 | 690 |
| udpipe | raw | 99.96 | 91.95 | 99.23 | 91.74 | 90.98 | 93.18 | 76.95 | 70.92 | 2601 |
| udpipe | gold-tok | 100 | 100 | 100 | **92.62** | **91.71** | **93.9** | **78.66** | **72.47** | **3468** |
| udify | gold-tok | 100 | 100 | 100 | 41.39 | 43 | 32 | 33.23 | 11.17 | 99 |

