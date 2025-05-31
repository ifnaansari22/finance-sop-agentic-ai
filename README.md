
# Finance SOP Agentic AI

A collaborative, open-source platform for generating and reviewing Standard Operating Procedures (SOPs) in finance using local LLMs, Retrieval-Augmented Generation (RAG), and a modern web UI.

## Project Overview

**Finance SOP Agentic AI** is a multi-agent system that leverages local LLMs (Mistral-7B), vector search (Chroma + FAISS), and a Streamlit web interface to automate SOP creation, compliance checking, and review for finance documents.  
The project is built by a team of three interns, each specializing in a key area (agents/LLM, RAG/vector DB, UI/PDF export).



## Tech Stack & Tools

- **Python 3.9+**
- **Local LLM:** Mistral-7B via [LM Studio](https://lmstudio.ai/)
- **Agent Orchestration:** [LangGraph](https://github.com/langchain-ai/langgraph)
- **Vector Database:** [Chroma](https://www.trychroma.com/)
- **Vector Search:** [FAISS](https://github.com/facebookresearch/faiss)
- **PDF Parsing:** [PyMuPDF](https://pymupdf.readthedocs.io/)
- **PDF Generation:** [fpdf2](https://github.com/PyFPDF/fpdf2)
- **Web UI:** [Streamlit](https://streamlit.io/)
- **Version Control:** Git + GitHub
- **IDE:** Visual Studio Code

---

## 📁 Project Structure

```
finance-sop-agentic-ai/
├── agents/         # Agent logic (OutlineAgent, PolicyAgent, ProcedureAgent, ReviewAgent)
├── graph/          # LangGraph orchestration and RAG logic
├── ui/             # Streamlit UI code
├── utils/          # Helper functions and utilities
├── data/
│   └── sample_data/  # Sample finance documents for testing
├── requirements.txt
├── Dockerfile
├── README.md
├── .gitignore
└── env/            # Python virtual environment (excluded from Git)


## Quickstart

### 1. Prerequisites

- Python 3.9+ installed
- [Git](https://git-scm.com/downloads) installed
- (Optional) [LM Studio](https://lmstudio.ai/) for local LLM inference

### 2. Setup
# Clone the repository
git clone https://github.com/ifnaansari22/finance-sop-agentic-ai.git
cd finance-sop-agentic-ai

# Create and activate a virtual environment
python -m venv env
env\Scripts\activate  # On Windows
source env/bin/activate  # On Mac/Linux

# Install dependencies
pip install -r requirements.txt
pip freeze > requirements.txt


### 3. Run the App

streamlit run ui/app.py


## Features

- Multi-agent orchestration (Outline, Policy, Procedure, Review agents)
- Local LLM inference for privacy and speed
- RAG search with Chroma and FAISS for compliance and policy retrieval
- Finance PDF parsing and SOP generation
- Interactive Streamlit UI for user-friendly operation
- Export generated SOPs as PDF
- Modular, open-source, and privacy-friendly


## License

This project is licensed under the MIT License.


## Credits

- Built by [ifnaansari](https://github.com/ifnaansari22) and team.
- Based on the [7-day-plan1.pdf](./7-day-plan1.pdf) internship roadmap.
- Uses open-source tools and models.


## References

- [LangGraph Documentation](https://github.com/langchain-ai/langgraph)
- [Chroma Vector DB](https://www.trychroma.com/)
- [FAISS](https://github.com/facebookresearch/faiss)
- [PyMuPDF](https://pymupdf.readthedocs.io/)
- [Streamlit](https://streamlit.io/)
- [fpdf2](https://github.com/PyFPDF/fpdf2)

