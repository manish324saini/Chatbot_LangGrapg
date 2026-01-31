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
- OpenAI API Key
- Git

## Installation

1. **Clone the repository:**
```bash
git clone https://github.com/manish324saini/Chatbot_LangGrapg.git
cd Chatbot_LangGrapg
```

2. **Create a virtual environment (optional but recommended):**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies:**
```bash
pip install -r requirements.txt
```

4. **Set up environment variables:**
Create a `.env` file in the root directory with your API keys:
```
OPENAI_API_KEY=your-openai-api-key-here
```

## Running Locally

Start the Streamlit app:
```bash
streamlit run streamlit.py
```

The app will open in your browser at `http://localhost:8501`

## Project Structure

```
├── streamlit.py          # Main Streamlit app
├── chatbot_graph.py      # LangGraph chatbot configuration
├── requirements.txt      # Python dependencies
├── .env                  # Environment variables (not committed)
├── .gitignore           # Git ignore rules
└── README.md            # This file
```

## How It Works

### Components

1. **chatbot_graph.py**: 
   - Defines the `ChatState` using TypedDict
   - Creates a LangGraph StateGraph with a single chat node
   - Integrates OpenAI's ChatOpenAI model
   - Uses InMemorySaver for conversation checkpointing

2. **streamlit.py**:
   - Provides the web UI with Streamlit
   - Manages conversation history in session state
   - Sends messages to the chatbot graph
   - Displays chat messages with proper formatting

## Deployment to Streamlit Cloud

1. **Push to GitHub** (already done):
   - Your code is at: https://github.com/manish324saini/Chatbot_LangGrapg

2. **Deploy on Streamlit Cloud**:
   - Go to https://share.streamlit.io/
   - Sign in with GitHub
   - Click "New app"
   - Select repository: `manish324saini/Chatbot_LangGrapg`
   - Select branch: `main`
   - Enter main file path: `streamlit.py`
   - Click "Deploy"

3. **Add Secrets**:
   - After deployment, go to app settings (⋮ menu)
   - Click "Secrets"
   - Add your environment variables:
   ```toml
   OPENAI_API_KEY = "your-openai-api-key"
   ```

## Configuration

### Environment Variables

- `OPENAI_API_KEY`: Your OpenAI API key (required)

### Streamlit Configuration

The app uses default Streamlit settings. To customize, create/edit `.streamlit/config.toml`.

## Requirements

See `requirements.txt` for all dependencies, including:
- `streamlit` - Web framework
- `langgraph` - Graph-based conversation management
- `langchain` - LLM framework
- `langchain-openai` - OpenAI integration
- `python-dotenv` - Environment variable management

## Troubleshooting

### ModuleNotFoundError for langgraph
Ensure the local file is named `chatbot_graph.py`, not `langgraph.py`, to avoid shadowing the langgraph package.

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
