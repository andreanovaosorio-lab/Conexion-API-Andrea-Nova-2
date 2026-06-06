import os
from google import genai
from dotenv import load_dotenv 

# Cargar variables de entorno desde el archivo .env
load_dotenv()

# Configurar la clave de API
clave_api = os.getenv("GEMINI_API_KEY")

cliente = genai.Client(api_key=clave_api) 

def ejecutar_consulta():
    print("Ejecutando consulta a Gemini...")
    try:
        respuesta = cliente.models.generate_content(
            model="gemini-2.5-flash",
            contents="Presentate y dime un chiste"
        )

        print("Respuesta de Gemini:", respuesta.text)

    except Exception as e:
        print(f"Error al ejecutar la consulta: {e}")

if __name__ == "__main__":
    ejecutar_consulta()