# Projeto de Estudo: KeyLogger com Base64 em Python

Este projeto é um estudo simples sobre:
- Captura de teclas pressionadas (KeyLogger) usando Python e `pynput`
- Armazenamento do log de teclas em Base64
- Scripts para codificar e decodificar arquivos Python em Base64
- Execução dinâmica de código codificado

---

## Estrutura do projeto
```
KeyLoger/ # Pasta principal
├── log.txt # Arquivo de log com teclas capturadas em Base64
├── decode_log.py # Script para decodificar log.txt e mostrar teclas legíveis
├── encode_script.py # Script para codificar um arquivo .py em Base64
├── run_encoded.py # Script para executar código Python codificado em Base64
├── my.py # Código Python original (ex: KeyLogger)
└── README.md # Este arquivo de documentação
```

---

## Bibliotecas

| Biblioteca  | Uso                                     | Instalação Necessária?                  |
| ----------- | --------------------------------------- | --------------------------------------- |
| `tkinter`   | Interface gráfica (GUI)                 | Não (já vem no Python)                  |
| `datetime`  | Data e hora                             | Não                                     |
| `socket`    | Rede / obter IP e hostname              | Não                                     |
| `threading` | Executar listener em thread separada    | Não                                     |
| `base64`    | Codificar e decodificar em Base64       | Não                                     |
| `pynput`    | Capturar eventos do teclado (keylogger) | **Sim, via pip** (`pip install pynput`) |


## Como usar
codigos do cmd 

== python decodificar_log.py
== python encode_script.py
== python run_encoded.py

### 1. Executar o KeyLogger

O script `my.py` é o programa principal que captura as teclas digitadas e salva no `log.txt` codificado em Base64.

```bash
python my.py


