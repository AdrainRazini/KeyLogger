import base64

def decode_base64_string(b64_string):
    try:
        decoded_bytes = base64.b64decode(b64_string)
        return decoded_bytes.decode('utf-8')
    except Exception:
        # Se não conseguir decodificar, retorna a string original
        return b64_string

with open("log.txt", "r", encoding="utf-8") as f:
    for line in f:
        line = line.strip()
        # Ignora linhas em branco ou de cabeçalho
        if not line or line.startswith("Início do log") or line.startswith("Computador:"):
            print(line)
            continue
        
        # Tenta separar hora e tecla codificada
        if " - " in line:
            hora, tecla_b64 = line.split(" - ", 1)
            tecla = decode_base64_string(tecla_b64)
            print(f"{hora} - {tecla}")
        else:
            print(line)
