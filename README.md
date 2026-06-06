# Conexion-API-Andrea-Nova-2

## 📋 Descripción del Programa

Este proyecto es una aplicación Python que se conecta a la **API de Google Gemini** para realizar consultas de inteligencia artificial. El programa utiliza el modelo `gemini-2.5-flash` para generar respuestas inteligentes basadas en prompts específicos.

### Características principales:
- Conexión segura a la API de Google Gemini mediante clave de API
- Manejo de variables de entorno para proteger datos sensibles
- Gestión de errores robusta
- Consultas personalizables a través del modelo de IA más reciente

---

## 🚀 Pasos para Ejecutar el Programa

### 1. **Clonar el repositorio** 
```bash
git clone <URL_DEL_REPOSITORIO>
cd Conexion-API-Andrea-Nova-2
```

### 2. **Crear un ambiente virtual** 
```bash
# En Windows
python -m venv venv
venv\Scripts\activate

# En Mac/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. **Instalar las dependencias**
```bash
pip install -r requirements.txt
```

### 4. **Configurar la clave API de Gemini**
- Ve a [Google AI Studio](https://aistudio.google.com/app/apikeys)
- Crea o copia tu clave de API de Google Gemini
- Crea un archivo `.env` en la raíz del proyecto
- Agrega la siguiente línea al archivo `.env`:
```
GEMINI_API_KEY=tu_clave_api_aqui
```

### 5. **Ejecutar el programa**
```bash
python app_gemini.py
```

El programa debería ejecutarse y mostrar la respuesta de Gemini en la consola.

### 6. **Resultados esperados**

Confirmación de la conexion

<img width="1103" height="168" alt="image" src="https://github.com/user-attachments/assets/55b652b7-05b7-4a17-9737-4db3c3e7503d" />


Respuesta de la pregunta realizada, este caso la pregunta fue " Presentate y dime un chiste" a lo que el script responde: 

<img width="1571" height="711" alt="image" src="https://github.com/user-attachments/assets/16adfbaf-683c-433e-888f-0ab0a4f50e8e" />


El programa debería ejecutarse y mostrar la respuesta de Gemini en la consola.

---

## 📦 Archivos Principales

| Archivo | Descripción |
|---------|-------------|
| `app_gemini.py` | Aplicación principal que conecta con la API de Gemini |
| `requirements.txt` | Dependencias del proyecto |
| `.env` | Variables de entorno (no incluir en Git) |
| `.gitignore` | Archivos ignorados por Git |

---

## ⚙️ Requisitos Previos

- Python 3.8 o superior
- Una cuenta de Google con acceso a Google AI Studio
- Conexión a internet

---

## 🔒 Seguridad

⚠️ **Importante:** Nunca compartas tu archivo `.env` ni publiques tu `GEMINI_API_KEY` en repositorios públicos. El archivo `.env` está incluido en `.gitignore` para proteger tus credenciales.

---

## 🐛 Solución de Problemas

### Error: "ModuleNotFoundError: No module named 'google'"
- Asegúrate de haber activado el ambiente virtual
- Reinstala las dependencias: `pip install -r requirements.txt`

### Error: "GEMINI_API_KEY no encontrada"
- Verifica que el archivo `.env` existe en la raíz del proyecto
- Confirma que contiene la línea correcta con tu clave API

### Error de conexión a la API
- Verifica tu conexión a internet
- Comprueba que tu clave API es válida en [Google AI Studio](https://aistudio.google.com/app/apikeys)
