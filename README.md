# AI Engineer Technical Challenge - COR Chatbot

## Contexto y Problema

Imagina que uno de nuestros clientes en COR, una agencia de publicidad, quiere un chatbot interno simple. Este chatbot debe poder responder preguntas sobre un documento específico que resume las mejores prácticas para la gestión de proyectos.

Tu tarea es crear un script en Python que reciba una pregunta del usuario y utilice el siguiente texto como base de conocimiento para encontrar y generar una respuesta.

## Texto de Conocimiento

```python
knowledge_base_text = """
El éxito de un proyecto en nuestra agencia depende de tres pilares fundamentales: la comunicación clara, la gestión del tiempo y la rentabilidad.

La comunicación clara se logra manteniendo reuniones de seguimiento semanales y utilizando el canal de Slack #proyectos-activos para actualizaciones diarias. Es crucial documentar todas las decisiones importantes en la plataforma de COR.

Para la gestión del tiempo, cada tarea debe ser estimada en horas antes de iniciar un sprint. Utilizamos la técnica Pomodoro para mantener el enfoque y registramos el tiempo de cada actividad en COR para asegurar que nos mantenemos dentro del presupuesto. El Project Manager es responsable de ajustar el cronograma si surgen desvíos.

La rentabilidad se monitorea constantemente a través del dashboard de COR. Cualquier proyecto que caiga por debajo del 20% de margen de ganancia requiere una revisión inmediata. Los costos inesperados deben ser aprobados por el cliente antes de ser incurridos para evitar sorpresas en la facturación.
"""
```

## Tareas

### 1. Configuración del Entorno
- Usando Python, prepara el entorno para utilizar la librería langchain
- Puedes asumir que las librerías necesarias (`langchain`, `langchain-openai`, etc.) están instaladas

### 2. Cargar y Dividir el Documento
- Carga el `knowledge_base_text` y divídelo en fragmentos (chunks) manejables para su procesamiento

### 3. Crear un "Retriever"
- Implementa un recuperador (retriever) simple que pueda encontrar los fragmentos de texto más relevantes para una pregunta dada
- Puedes usar un almacén de vectores en memoria (como FAISS o ChromaDB) y embeddings
- Puedes usar un modelo de OpenAI o uno open-source para los embeddings

### 4. Construir la Cadena de Q&A
Crea una cadena de Langchain (chain) que:
- Reciba una pregunta
- Use el retriever para obtener el contexto relevante
- Pase la pregunta y el contexto a un modelo de lenguaje (LLM) para generar una respuesta

### 5. Probar el Sistema
- Demuestra que el sistema funciona haciendo al menos dos preguntas relevantes al texto

## Estructura del Proyecto

```
Software-Engineer-AI-Challenge/
├── README.md
├── requirements.txt
├── chatbot.py
└── test_questions.py
```

## Instalación y Configuración

### Prerrequisitos
- Python 3.8 o superior
- pip (gestor de paquetes de Python)

### Instalación de Dependencias

```bash
pip install -r requirements.txt
```

### Variables de Entorno

Crea un archivo `.env` en la raíz del proyecto:

```bash
OPENAI_API_KEY=tu_api_key_aqui
```

## Uso

### Ejecutar el Chatbot

```bash
python chatbot.py
```

### Ejecutar las Pruebas

```bash
python test_questions.py
```

## Ejemplos de Preguntas para Probar

1. "¿Cuáles son los tres pilares fundamentales para el éxito de un proyecto?"
2. "¿Cómo se logra la comunicación clara en los proyectos?"
3. "¿Qué técnica se utiliza para mantener el enfoque en las tareas?"
4. "¿Cuál es el margen de ganancia mínimo requerido para los proyectos?"
5. "¿Quién es responsable de ajustar el cronograma si hay desvíos?"

## Criterios de Evaluación

- **Funcionalidad**: El chatbot debe responder correctamente a las preguntas basándose en el texto proporcionado
- **Arquitectura**: Uso apropiado de LangChain y sus componentes
- **Código**: Código limpio, bien documentado y siguiendo buenas prácticas de Python
- **Documentación**: README claro y completo
- **Pruebas**: Demostración de que el sistema funciona con ejemplos reales

## Tecnologías Sugeridas

- **LangChain**: Para construir la cadena de Q&A
- **OpenAI**: Para embeddings y LLM (alternativamente, modelos open-source)
- **FAISS/ChromaDB**: Para almacenamiento de vectores
- **Python**: Lenguaje de programación principal

## Notas Importantes

- El candidato puede usar modelos open-source como alternativa a OpenAI
- Se debe documentar cualquier decisión técnica importante
- El código debe ser ejecutable y funcional
- Se valorará la creatividad en la implementación y las mejoras adicionales

## Entrega

El candidato debe entregar:
1. Código fuente completo y funcional
2. README con instrucciones de instalación y uso
3. Ejemplos de ejecución con preguntas y respuestas
4. Cualquier documentación adicional relevante

---

**¡Buena suerte!** 🚀 