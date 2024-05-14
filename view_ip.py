import requests

def obtener_ip_publica():
    try:
        response = requests.get('https://api.ipify.org?format=json')
        response.raise_for_status()  # Verifica que la solicitud fue exitosa
        ip_info = response.json()
        return ip_info['ip']
    except requests.RequestException as e:
        return f"Error al obtener la IP: {e}"

if __name__ == "__main__":
    ip_publica = obtener_ip_publica()
    print(f"Tu dirección IP pública es: {ip_publica}")
