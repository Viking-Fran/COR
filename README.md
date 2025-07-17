# COR AI Chatbot – Technical Challenge

> A modern RAG-based conversational AI system built with LangChain, OpenAI, and ChromaDB

## Overview

This project implements a sophisticated chatbot solution for COR's AI Engineer position technical challenge. The system leverages **Retrieval-Augmented Generation (RAG)** architecture to provide contextually accurate responses about specific knowledge domains using state-of-the-art language models.

### Key Features

- **Semantic Search**: Advanced embedding-based document retrieval
- **Context-Aware Responses**: LLM-powered natural language generation
- **Modular Architecture**: Built with LangChain's composable components
- **Vector Storage**: Efficient similarity search using ChromaDB
- **Interactive Console**: Real-time conversational interface

## Technical Architecture

```
┌─────────────────┐    ┌──────────────────┐    ┌─────────────────┐
│   User Input    │───▶│  Embedding Model │───▶│  Vector Store   │
└─────────────────┘    └──────────────────┘    └─────────────────┘
                                                        │
┌─────────────────┐    ┌──────────────────┐    ┌─────────────────┐
│   AI Response   │◀───│   Language Model │◀───│   Retriever     │
└─────────────────┘    └──────────────────┘    └─────────────────┘
```

## Project Structure

```
AI-Challenge/
├── chatbot.py           # Main chatbot application
├── test_questions.py    # Automated testing suite
├── requirements.txt     # Project dependencies
├── .env.example         # Environment configuration template
├── .gitignore           # Git ignore patterns
└── README.md            # Project documentation
```

## Technology Stack

|     Component     |     Technology    |           Purpose           |
|-------------------|-------------------|-----------------------------|
| **Framework**     | LangChain         | AI application orchestration|
| **Language Model**| OpenAI GPT        | Natural language generation |
| **Embeddings**    | OpenAI Embeddings | Semantic text representation|
| **Vector Store**  | ChromaDB          | Efficient similarity search |
| **Runtime**       | Python 3.10+      | Application execution       |

## Quick Start

### Prerequisites

- Python 3.10 or higher
- OpenAI API key
- Git

### Installation

1. **Clone the repository**
  
   git clone https://github.com/Viking-Fran/COR.git
   cd AI-Challenge
   

2. **Set up virtual environment**
  
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   

3. **Install dependencies**
   
   pip install -r requirements.txt
   

4. **Configure environment**
   
   cp .env
   # Edit .env and add your OpenAI API key
   echo "OPENAI_API_KEY=your_api_key_here" > .env
   

## Usage

### Running the Chatbot


python chatbot.py


**Example interaction:**

🤖 COR Chatbot - Ask me about project management

👉 Question: What technique is used to maintain focus?
✅ Answer: The Pomodoro technique is used to maintain focus.

👉 Question: exit


### Running Tests


python test_questions.py


**Expected output:**

Question: What are the three fundamental pillars?
Answer: Clear communication, time management, and profitability.

Question: How is clear communication achieved?
Answer: Through regular meetings and transparent reporting.


## Sample Queries

The system can handle various types of questions about project management:

- **Fundamental Concepts**: "What are the three fundamental pillars for project success?"
- **Process Questions**: "How is clear communication achieved?"
- **Technical Details**: "What technique is used to maintain focus?"
- **Operational Queries**: "What is the minimum required margin?"
- **Responsibility Questions**: "Who adjusts the schedule if there are deviations?"

## Configuration

### Environment Variables

|     Variable     |          Description          | Required |
|------------------|-------------------------------|----------|
| `OPENAI_API_KEY` | OpenAI API authentication key |   Yes    |

### Dependencies

langchain
langchain-openai
langchain-community
chromadb
python-dotenv
openai


## Technical Implementation

### Core Components

- **Document Loader**: Processes and chunks knowledge base text
- **Embedding Model**: Converts text to vector representations
- **Vector Store**: Manages similarity search operations
- **Retriever**: Finds relevant context for user queries
- **LLM Chain**: Generates coherent responses using retrieved context

### Architecture Decisions

- **In-Memory Vector Store**: ChromaDB for fast prototyping and testing
- **Modular Design**: LangChain components for maintainability
- **Environment-Based Configuration**: Secure API key management
- **Console Interface**: Simple yet effective user interaction

## Development Notes

- Uses `langchain_community` and `langchain_openai` for compatibility
- Vector store instantiated with `Chroma.from_documents()` for simplicity
- Environment variables loaded via `python-dotenv`
- Comprehensive error handling for API interactions

## Author

**Francisco Draghi**  
*AI Engineer Technical Challenge for COR*

---

*Built with ❤️ for the COR AI team*