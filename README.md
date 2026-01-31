# Chatbot with LangGraph & Streamlit

An intelligent conversational chatbot built using **LangGraph** for graph-based conversation flow management and **Streamlit** for a user-friendly web interface. Powered by OpenAI's GPT models.

## Features

- 💬 Real-time conversational AI
- 📊 Graph-based conversation management with LangGraph
- 💾 In-memory message history with checkpointing
- 🎨 Clean and intuitive Streamlit UI
- 🔌 OpenAI GPT integration
- 📱 Responsive web interface

## Prerequisites

- Python 3.9+
# Chatbot with LangGraph & Streamlit

An intelligent conversational chatbot built using **LangGraph** for graph-based conversation flow management and **Streamlit** for a user-friendly web interface. Powered by OpenAI's GPT models.

**Live demo:** https://langgraphmanish.streamlit.app/

## Features

- Real-time conversational AI
- Graph-based conversation management with LangGraph
- In-memory message checkpointing
- Streamlit web UI for quick interaction

## Prerequisites

- Python 3.9+
- OpenAI API Key
- Git

## Installation

1. Clone the repository:
```bash
git clone https://github.com/manish324saini/Chatbot_LangGrapg.git
cd Chatbot_LangGrapg
```

2. (Optional) Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Configure API keys (locally):
Create a `.env` file in the project root with your keys (this file is ignored by git):
```
OPENAI_API_KEY=your-openai-api-key
HUGGINGFACEHUB_API_TOKEN=your-hf-token (optional)
```

## Running Locally

Start the Streamlit app:
```bash
streamlit run streamlit.py
```

Open http://localhost:8501 in your browser.

## Project Structure

```
├── streamlit.py          # Main Streamlit app (entrypoint)
├── chatbot_graph.py      # LangGraph chatbot configuration and graph
├── requirements.txt      # Python dependencies
├── .env                  # Local environment variables (ignored)
├── .gitignore            # Git ignore rules
├── .streamlit/           # Streamlit config and secrets template
└── README.md             # This file
```

## How It Works

- `chatbot_graph.py`: defines the `ChatState`, builds a LangGraph `StateGraph`, and integrates the `ChatOpenAI` model. The code loads `OPENAI_API_KEY` from environment variables or Streamlit secrets and handles missing keys gracefully.
- `streamlit.py`: Streamlit UI, manages session state for message history, validates that `OPENAI_API_KEY` is configured, and invokes the chatbot graph to get responses.

## Deployment (Streamlit Cloud)

1. Go to https://share.streamlit.io/ and sign in with GitHub.
2. Click **New app** and provide:
   - Repository: `manish324saini/Chatbot_LangGrapg`
   - Branch: `main`
   - Main file path: `streamlit.py`
3. Click **Deploy**.

### Add secrets on Streamlit Cloud
After deployment, open the app settings (⋮) → **Secrets** and add:
```toml
OPENAI_API_KEY = "your-openai-key"
HUGGINGFACEHUB_API_TOKEN = "your-hf-token"  # optional
```
Save — the app will restart and pick up the secrets.

## Security Notes

- Do NOT commit your `.env` file or API keys to GitHub. The repository already has `.env` removed from commits and `.gitignore` configured to ignore it.
- If you accidentally committed secrets, rotate them immediately (OpenAI/Hugging Face) and remove them from the git history.

## Troubleshooting

- If you see an error about `OPENAI_API_KEY` missing, add the key to Streamlit Secrets or your local `.env` and restart the app.
- If `langgraph` module errors occur, ensure your local file is named `chatbot_graph.py` (not `langgraph.py`).

## Contributing

Open issues or PRs in the GitHub repository: https://github.com/manish324saini/Chatbot_LangGrapg

## License

MIT

---

Deployed app: https://langgraphmanish.streamlit.app/

### API Key Issues
- Ensure `OPENAI_API_KEY` is set in your `.env` file
- Check that your API key is valid and has available credits
- Never commit `.env` to version control

### Streamlit Connection Issues
- Make sure Streamlit is installed: `pip install streamlit`
- Try running with: `python -m streamlit run streamlit.py`

## License

This project is open source and available under the MIT License.

## Support

For issues or questions, please open an issue on GitHub: https://github.com/manish324saini/Chatbot_LangGrapg/issues

## Author

Created with ❤️ for intelligent conversational AI

---

**Live Demo**: Check the deployed app on Streamlit Cloud after deployment!
