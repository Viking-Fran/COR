from chatbot import qa_chain

test_queries = [
    "¿Cuáles son los tres pilares fundamentales para el éxito de un proyecto?",
    "¿Qué técnica se utiliza para mantener el enfoque en las tareas?",
]
    


for query in test_queries:
    print(f"Pregunta: {query}")
    response = qa_chain({"query": query})
    answer = response['result']
    source_docs = response['source_documents']
    
    print(f"Respuesta: {answer}")
    print("Documentos fuente:")
    for doc in source_docs:
        print(f"- {doc.page_content[:100]}...")  # Print first 100 characters of each source document
    print()  