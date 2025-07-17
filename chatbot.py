# chatbot.py

from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_community.llms import OpenAI
from langchain.chains import RetrievalQA
from langchain.schema import Document
from langchain.text_splitter import RecursiveCharacterTextSplitter
from dotenv import load_dotenv
import os

# Carga .env con la API Key
load_dotenv()

# Texto base de conocimiento
knowledge_base_text = """
El éxito de un proyecto en nuestra agencia depende de tres pilares fundamentales: la comunicación clara, la gestión del tiempo y la rentabilidad.

La comunicación clara se logra manteniendo reuniones de seguimiento semanales y utilizando el canal de Slack #proyectos-activos para actualizaciones diarias. Es crucial documentar todas las decisiones importantes en la plataforma de COR.

Para la gestión del tiempo, cada tarea debe ser estimada en horas antes de iniciar un sprint. Utilizamos la técnica Pomodoro para mantener el enfoque y registramos el tiempo de cada actividad en COR para asegurar que nos mantenemos dentro del presupuesto. El Project Manager es responsable de ajustar el cronograma si surgen desvíos.

La rentabilidad se monitorea constantemente a través del dashboard de COR. Cualquier proyecto que caiga por debajo del 20% de margen de ganancia requiere una revisión inmediata. Los costos inesperados deben ser aprobados por el cliente antes de ser incurridos para evitar sorpresas en la facturación.
"""

# Dividir en chunks
text_splitter = RecursiveCharacterTextSplitter(chunk_size=300, chunk_overlap=50)
chunks = text_splitter.split_text(knowledge_base_text)
documents = [Document(page_content=chunk) for chunk in chunks]

# Creo embeddings y vectorstore
embedding = OpenAIEmbeddings()
vector_store = Chroma.from_documents(documents, embedding)
retriever = vector_store.as_retriever()

# Instanciar LLM y cadena QA
llm = OpenAI(temperature=0)
qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    retriever=retriever,
    return_source_documents=True
)

# Interfaz de consola
def main():
    print("🤖 COR Chatbot - Preguntame sobre gestión de proyectos.\n")
    while True:
        query = input("👉 Pregunta (o 'salir'): ")
        if query.lower() in ["exit", "salir", "quit"]:
            print("👋 Hasta la próxima!")
            break

        result = qa_chain({"query": query})
        print(f"\n✅ Respuesta:\n{result['result']}")
        print("\n📚 Fragmentos fuente:")
        for doc in result['source_documents']:
            print(f"- {doc.page_content[:80]}...")

if __name__ == "__main__":
    main()
