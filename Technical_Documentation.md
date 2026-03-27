# DocuAi Technical Documentation 📚

DocuAi is an enterprise-grade **RAG (Retrieval-Augmented Generation)** chatbot application designed to turn static documents into interactive knowledge bases. It combines a premium React-based frontend with a powerful vector search engine and Cloud-LLM inference.

---

## 🏗️ System Architecture

```mermaid
graph TD
    User((User)) -->|Uploads PDF/TXT| Frontend[Reflex React Frontend]
    User -->|Asks Question| Frontend
    
    subgraph "Backend (Python)"
        Frontend -->|POST /_upload| API[FastAPI Handler]
        API -->|Parse & Chunk| LangChain[LangChain Pipeline]
        LangChain -->|Embeddings| MiniLM[MiniLM-L6-v2]
        MiniLM -->|Store Vectors| ChromaDB[(ChromaDB)]
        
        Frontend -->|Websocket /_event| RAG[Corrective RAG Logic]
        RAG -->|Semantic Search| ChromaDB
        RAG -->|Context Injection| Groq[Groq Cloud LLM]
        Groq -->|Generate Answer| RAG
    end
    
    subgraph "Infrastructure"
        Caddy[Caddy Reverse Proxy] -->|Port 7860| Frontend
        HuggingFace[Hugging Face Space] --> Docker[Docker Container]
    end
```

---

## 🛠️ Technology Stack

### 🎨 Frontend
- **Reflex:** Pure Python React framework for seamless full-stack state management.
- **Tailwind CSS:** Modern glassmorphism UI design.

### 🧠 AI Backend
- **LangChain:** Orchestrates document splitting and retrieval logic.
- **ChromaDB:** In-memory vector search database for document context.
- **HuggingFace MiniLM:** Local CPU-efficient embedding model.
- **Groq Llama 3.1:** High-speed cloud LLM for answer synthesis.

### 🚀 Infrastructure
- **Hugging Face Spaces:** 16GB free-tier hosting for high-performance ML workloads.
- **Docker:** Containerized for portability.
- **Caddy:** Reverse proxy for single-port WebSocket routing (7860).

---

## 🔒 Security & Deployment
- **CORS Restricted:** Backend only accepts traffic from authorized Hugging Face domains.
- **Environment Driven:** Keys are handled via secure environment secrets.
- **Rootless Container:** Runs as User 1000 for standard Linux security compliance.

---
**Live Application:** [DocuAi on Hugging Face](https://huggingface.co/spaces/Sikee18/DocuAi)
