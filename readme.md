# 📚 Document Q&A with RAG (Retrieval Augmented Generation)

A lightweight, local-first document question-answering system built with Streamlit, Ollama, Sentence Transformers, and FAISS. Upload PDF documents and ask questions to get AI-powered answers based on the document content.

## ✨ Features

- **📄 PDF Document Processing**: Upload and process PDF documents with automatic text extraction
- **🔍 Semantic Search**: Use sentence transformers for intelligent document chunking and retrieval
- **🤖 Local LLM Integration**: Powered by Ollama for privacy-first AI responses
- **💬 RAG Architecture**: Retrieval Augmented Generation for accurate, context-aware answers
- **⚡ Fast Vector Search**: FAISS-based similarity search for efficient retrieval
- **🎨 Modern UI**: Clean, intuitive Streamlit interface
- **🔧 Configurable**: Adjustable chunk sizes, retrieval parameters, and model selection

## 🛠️ Tech Stack

- **Python 3.7+**: Core programming language
- **Streamlit**: Web framework for the interactive UI
- **Ollama**: Local LLM runtime (TinyLlama, Gemma, Llama2, Mistral, etc.)
- **Sentence Transformers**: For generating semantic embeddings (`all-MiniLM-L6-v2`)
- **FAISS**: Facebook AI Similarity Search for efficient vector search
- **PyPDF**: PDF text extraction

## 📋 Prerequisites

1. **Python 3.7+** installed
2. **Ollama** installed and running
   - Download from [ollama.ai](https://ollama.ai)
   - Install and start: `ollama serve`
   - Pull a model: `ollama pull tinyllama` (or `gemma:4b`, `llama2`, `mistral`)

## 🚀 Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/uday-codes69/LLM-Projects.git
   cd "LLM-Projects/Document-Q&A (RAG Lite)"
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
   
   **Note**: Make sure to use `-r` flag: `pip install -r requirements.txt`

3. **Verify Ollama is running**:
   ```bash
   curl http://localhost:11434/api/tags
   ```

4. **Pull required models** (optional, but recommended):
   ```bash
   ollama pull tinyllama
   ollama pull gemma:4b
   ```

## 💻 Usage

1. **Start Ollama** (if not already running):
   ```bash
   ollama serve
   ```

2. **Run the Streamlit application**:
   ```bash
   streamlit run app.py
   ```

3. **Use the application**:
   - Upload a PDF document using the file uploader
   - Click "Process Document" to extract and index the text
   - Enter your question in the text area
   - Click "Get Answer" to receive an AI-generated response based on the document

## 📁 Project Structure

```
Document-Q&A (RAG Lite)/
├── app.py              # Main Streamlit application and UI
├── ingest.py           # PDF text extraction module
├── retriever.py        # RAG retrieval with embeddings and FAISS
├── llm_clients.py      # Ollama API client for LLM calls
├── requirements.txt    # Python dependencies
└── README.md          # Project documentation
```

## 🔧 How It Works

### 1. Document Ingestion (`ingest.py`)
- Extracts text from uploaded PDF files
- Handles multi-page documents
- Error handling for corrupted or unreadable PDFs

### 2. Text Chunking (`retriever.py`)
- Splits documents into overlapping chunks (default: 500 words)
- Preserves context with configurable overlap (default: 50 words)
- Optimized for semantic search

### 3. Embedding & Indexing (`retriever.py`)
- Generates semantic embeddings using Sentence Transformers
- Builds FAISS index for fast similarity search
- Uses cosine similarity for relevance ranking

### 4. Retrieval (`retriever.py`)
- Searches for most relevant chunks based on query
- Returns top-k most similar document sections
- Configurable retrieval count

### 5. Answer Generation (`llm_clients.py`)
- Uses RAG (Retrieval Augmented Generation) approach
- Combines retrieved context with user question
- Generates answers using local Ollama LLM
- Ensures answers are grounded in document content

## ⚙️ Configuration

### Model Selection
Supported Ollama models:
- `tinyllama`: Fast, lightweight (recommended for quick testing)
- `gemma:4b`: Google's Gemma 4B model
- `llama2`: Meta's Llama 2
- `mistral`: Mistral AI model

To use a different model:
1. Pull it: `ollama pull <model-name>`
2. Select it from the dropdown in the app

### Chunking Parameters
- **Chunk Size**: Number of words per chunk (default: 500)
  - Smaller chunks: More precise retrieval, less context
  - Larger chunks: More context, potentially less precise
- **Overlap**: Words shared between chunks (default: 50)
  - Prevents context loss at chunk boundaries

### Retrieval Settings
- **Number of chunks**: How many document sections to use as context (default: 3)
  - More chunks: Richer context, potentially more noise
  - Fewer chunks: More focused, might miss relevant info

## 🎯 Key Features Explained

### RAG (Retrieval Augmented Generation)
Instead of asking the LLM to answer from memory, RAG:
1. Retrieves relevant document sections
2. Provides them as context to the LLM
3. Generates answers grounded in the actual document content

This approach:
- ✅ Reduces hallucinations
- ✅ Provides accurate, document-specific answers
- ✅ Allows citing source material
- ✅ Works with any document without fine-tuning

### Semantic Search
Uses sentence embeddings to find meaningfully similar text, not just keyword matches. This means:
- Finds relevant content even with different wording
- Understands context and intent
- More accurate than traditional keyword search

## 🐛 Troubleshooting

### "Error connecting to Ollama"
- Make sure Ollama is running: `ollama serve`
- Check if it's accessible: `curl http://localhost:11434/api/tags`
- Verify the model is pulled: `ollama list`

### "No relevant information found"
- Try rephrasing your question
- Increase the number of chunks to retrieve
- Check if the document was processed correctly

### Slow processing
- Use a smaller model (e.g., `tinyllama`)
- Reduce chunk size
- Process smaller documents first

### Memory issues
- Use `faiss-cpu` (already in requirements)
- Reduce chunk size
- Process documents one at a time

## 📝 Example Questions

After uploading a document, try asking:
- "What is this document about?"
- "Summarize the main points"
- "What are the key findings?"
- "Explain [specific topic from document]"
- "What does the document say about [topic]?"

## 🤝 Contributing

Contributions are welcome! To contribute:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is open source and available under the MIT License.

## 👤 Author

**Uday Thakur**
- GitHub: [@uday-codes69](https://github.com/uday-codes69)

## 🙏 Acknowledgments

- [Ollama](https://ollama.ai) for local LLM runtime
- [Streamlit](https://streamlit.io) for the web framework
- [Sentence Transformers](https://www.sbert.net/) for embeddings
- [FAISS](https://github.com/facebookresearch/faiss) for efficient similarity search
- The open-source AI community

## 🔮 Future Enhancements

- [ ] Support for multiple document formats (DOCX, TXT, etc.)
- [ ] Conversation history and follow-up questions
- [ ] Document metadata extraction
- [ ] Export conversation functionality
- [ ] Multi-document search
- [ ] Citation tracking (which chunk was used)
- [ ] Advanced chunking strategies (sentence-based, semantic)
- [ ] Support for images in PDFs (OCR)
- [ ] Batch processing multiple documents
- [ ] Persistent document storage

---

⭐ If you find this project useful, please consider giving it a star!
