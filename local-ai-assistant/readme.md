# 🧠 Local AI Assistant

A modern, interactive web application for running Large Language Models (LLMs) locally using Ollama. Built with Streamlit, this application provides an intuitive interface to interact with local AI models with full control over inference parameters.

## ✨ Features

- **Local LLM Integration**: Seamlessly connect with Ollama API to run models locally without cloud dependencies
- **Multiple Model Support**: Switch between different models (TinyLlama, Gemma, etc.) on the fly
- **Advanced Inference Controls**: Fine-tune model behavior with comprehensive parameters:
  - **Temperature**: Control randomness and creativity (0.0 - 1.0)
  - **Top-P (Nucleus Sampling)**: Limit token selection to cumulative probability mass
  - **Top-K**: Restrict sampling to top K most likely tokens
  - **Min-P**: Stability parameter for more consistent outputs
  - **Max Tokens**: Control response length
- **Streaming Responses**: Real-time token streaming for better user experience
- **Clean UI/UX**: Modern, responsive interface built with Streamlit
- **Privacy-First**: All processing happens locally on your machine

## 🛠️ Tech Stack

- **Python 3.x**: Core programming language
- **Streamlit**: Web framework for building the interactive UI
- **Ollama**: Local LLM runtime and API
- **Requests**: HTTP library for API communication

## 📋 Prerequisites

Before running this application, ensure you have:

1. **Python 3.7+** installed on your system
2. **Ollama** installed and running locally
   - Download from [ollama.ai](https://ollama.ai)
   - Install and start the Ollama service
3. **Required Python packages** (see Installation)

## 🚀 Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/uday-codes69/LLM-Projects.git
   cd LLM-Projects/Local-Ai-Assistant
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Pull required Ollama models** (if not already installed):
   ```bash
   ollama pull tinyllama


4. **Verify Ollama is running**:
   ```bash
   curl http://localhost:11434/api/tags
   ```

## 💻 Usage

1. **Start the Streamlit application**:
   ```bash
   streamlit run app.py
   ```

2. **Access the application**:
   - The app will automatically open in your default browser
   - Default URL: `http://localhost:8501`

3. **Configure settings** (optional):
   - Use the sidebar to adjust model parameters
   - Select your preferred model from the dropdown
   - Fine-tune temperature, top-p, top-k, and other settings

4. **Interact with the AI**:
   - Type your question or prompt in the text area
   - Click "Generate Response" to get AI-generated output
   - Responses stream in real-time for better user experience

## 📁 Project Structure

```
Local-Ai-Assistant/
├── app.py              # Main Streamlit application and UI
├── llm_client.py       # Ollama API client with streaming support
├── prompts.py          # System prompts and prompt templates
├── requirements.txt    # Python dependencies
└── README.md          # Project documentation
```

## 🔧 Configuration

### Model Selection
Currently supported models:
- `tinyllama`: Lightweight, fast model for quick responses

To add more models:
1. Pull the model using Ollama: `ollama pull <model-name>`
2. Add it to the model dropdown in `app.py` (line 14)

### API Configuration
The Ollama API endpoint is configured in `llm_client.py`. By default, it connects to:
- URL: `http://localhost:11434/api/generate`

To use a remote Ollama instance, modify the `OLLAMA_URL` constant in `llm_client.py`.

## 🎯 Key Features Explained

### Temperature
Controls the randomness of the model's output. Lower values (0.0-0.3) produce more focused, deterministic responses, while higher values (0.7-1.0) generate more creative and diverse outputs.

### Top-P (Nucleus Sampling)
Limits token selection to the smallest set of tokens whose cumulative probability exceeds the threshold. Helps balance between diversity and coherence.

### Top-K
Restricts sampling to the top K most likely tokens. Lower values produce more focused outputs, while higher values allow more diversity.

### Min-P
A stability parameter that filters out tokens below a minimum probability threshold, ensuring more consistent and reliable outputs.

## 🤝 Contributing

Contributions are welcome! If you'd like to improve this project:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is open source and available under the MIT License.

## 👤 Author

**Uday Thakur**
- GitHub: [@uday-codes69](https://github.com/uday-codes69)

## 🙏 Acknowledgments

- [Ollama](https://ollama.ai) for providing an excellent local LLM runtime
- [Streamlit](https://streamlit.io) for the amazing web framework
- The open-source AI community for continuous innovation

## 🔮 Future Enhancements

- [ ] Conversation history and context management
- [ ] Support for more Ollama models
- [ ] Export conversation functionality
- [ ] Custom prompt templates
- [ ] Model performance metrics
- [ ] Multi-turn conversation support
- [ ] Dark mode theme

---

⭐ If you find this project useful, please consider giving it a star!
