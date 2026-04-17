# Learn RAG (15-day locked-in)

This folder contains **Colab-first notebooks** to learn Retrieval-Augmented Generation (RAG) in a job-oriented way.

## What you will build
- `notebooks/notebook_01_basic_rag.ipynb`: end-to-end RAG over local documents with citations
- `notebooks/notebook_02_retrieval_experiments.ipynb`: chunking/metadata experiments + retrieval debugging
- `notebooks/notebook_03_rag_evaluation.ipynb`: a small eval set + measurable comparisons
- `projects/cloud_arch_assistant_rag.ipynb`: portfolio-style capstone tied to cloud architecture/cert material
- `docs/interview_sheet.md`: interview-ready explanations + production mapping

## Corporate restricted environment notes
These notebooks are designed to work with **minimal external dependencies** and **local documents**.

You can choose one of two runtime modes inside the notebooks:
- **API mode (recommended)**: use an LLM provider + embedding API (Gemini or OpenAI). Works best if your environment allows those endpoints.
- **Local fallback mode**: uses local embeddings (sentence-transformers) and a lightweight local generator fallback (extractive QA / summarization style). This keeps learning moving even if LLM APIs are blocked.

## Quick start (Google Colab)
1. Upload this folder to Google Drive (or `git clone` if allowed).
2. Open any notebook from `notebooks/` in Colab.
3. Run the first cell to install dependencies.
4. Put your documents in `data/docs/` (txt/markdown recommended).

## Recommended dataset
Start with **5–20 small docs** you already have access to (your own notes, cloud architecture snippets, policy docs, or certification material you’re allowed to use).

## Folder layout
- `data/docs/`: your source documents
- `data/eval/`: small evaluation set (we’ll build this)
- `notebooks/`: learning notebooks (01–03)
- `projects/`: capstone notebook
- `src/`: reusable utility code shared by notebooks

