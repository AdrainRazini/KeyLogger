import base64

input_file = "my_encoded.b64"

with open(input_file, "rb") as f:
    encoded_content = f.read()

decoded_content = base64.b64decode(encoded_content).decode('utf-8')

exec(decoded_content)
