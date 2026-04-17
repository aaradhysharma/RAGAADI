# Cloud Architecture RAG Assistant (portfolio)

## Summary
RAG assistant that answers cloud architecture questions grounded in your own documents (notes, standards, certification material), returning **citations to the exact source chunk**.

## Why it’s credible
- Retrieval-first debugging (chunking + top-k tuning)
- Source-aware answers (citations)
- Small benchmark/eval loop (not “vibes only”)
- Production mapping (what changes from notebook → service)

## How to run (Colab)
1. Put your documents in `data/docs/` (txt/markdown recommended).
2. Open `projects/cloud_arch_assistant_rag.ipynb` in Colab.
3. Run top-to-bottom.

## Architecture (notebook version)
- Ingest local docs
- Chunk (char-based baseline)
- Embed (local sentence-transformers)
- Index (FAISS)
- Retrieve top-k
- Generate grounded response + citations

## Production mapping (high level)
- Offline ingestion pipeline with versioned parsing + chunking
- Store embeddings in managed vector DB/search service
- Add ACL-aware metadata filtering
- Add observability: trace retrieval sets, latency, failure cases
- Add continuous evaluation and regression tests

## Future upgrades (good interview talking points)
- Hybrid retrieval (dense + BM25)
- Reranking (retrieve 20 → rerank top 5)
- Better chunking (semantic / section-aware)
- LLM-based answer generation + structured citations
- Tooling: LangSmith/DeepEval/RAGAS for richer eval

