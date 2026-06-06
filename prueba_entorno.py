import requests
import sys
import os

def verificar_configuracion():
    print("Verificando configuración del entorno...")

    if hasattr(sys, 'real_prefix') or (hasattr(sys, 'base_prefix') and sys.base_prefix != sys.prefix):
        print("Entorno virtual detectado.")
    else:
        print("No se detectó entorno virtual.")

    try:
        respuesta = requests.get("https://www.google.com")
        if respuesta.status_code == 200:
            print("Conexión  exitosa.")
        else:
            print("No se pudo conectar.")
    except Exception as e:
        print(f"Error de conexión: {e}")

if __name__ == "__main__":    
    verificar_configuracion()