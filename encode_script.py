import base64

input_file = "my.py"           # Seu script original
output_file = "my_encoded.b64" # Arquivo com o código codificado em base64

with open(input_file, "rb") as f:
    content = f.read()

encoded = base64.b64encode(content)

with open(output_file, "wb") as f:
    f.write(encoded)

print(f"Arquivo '{input_file}' codificado com sucesso em '{output_file}'")
