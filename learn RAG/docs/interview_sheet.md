# RAG interview sheet (AI Engineer)

## What is RAG?
RAG (Retrieval-Augmented Generation) is a pattern where you **retrieve relevant documents** from a knowledge base and provide them as context to a model so answers are grounded in **your data** instead of only the model’s training data.

## When should you use RAG?
- When answers must be based on **private/internal** documents
- When information changes frequently (policies, product docs)
- When you need **citations** or auditability
- When fine-tuning is too slow/expensive or not appropriate for up-to-date knowledge

## When should you *not* use RAG?
- Purely creative generation (no grounding needed)
- Data is small enough to fit reliably in the prompt
- You don’t control the source quality (garbage in → garbage out)

## What are the main failure modes?
- **Bad ingestion**: parsing issues, tables/PDFs, duplicated boilerplate
- **Bad chunking**: splits semantic units, loses context
- **Bad retrieval**: misses the relevant chunk (dense-only can miss exact keywords)
- **Overstuffed context**: irrelevant chunks cause the model to drift
- **Hallucination**: model answers beyond retrieved evidence

## Why does chunking matter so much?
Chunking defines the units retrieval can return. If the right fact is split across chunks, retrieval may fail even with a perfect embedding model. Chunk size and overlap are usually the first high-leverage knobs.

## Why can vector search alone fail?
Dense embeddings are great for semantic similarity but can miss:
- exact names/IDs
- rare terms
- short keyword queries

That’s why many production systems use **hybrid retrieval** (dense + lexical/BM25) and then rerank.

## What is reranking?
Two-stage retrieval:
1) retrieve top 20–100 cheaply (vector/BM25)\n
2) rerank top results with a stronger model (cross-encoder) to select best 5–10

Reranking often improves precision@k without changing your index.

## How do you reduce hallucinations in RAG?
- Always show **citations** (source_id + chunk ids)
- Force “answer only from context” prompting (API mode)
- Add an “I don’t know” rule when retrieval confidence is low
- Evaluate faithfulness and track failure cases
- Log retrieved context so you can debug issues

## How do you evaluate a RAG system?
Minimum viable evaluation:
- Create 20–30 Q/A pairs from your own docs
- Track whether retrieved context contains the expected facts (retrieval recall proxy)
- Track answer correctness with human labels

More advanced:
- Metrics like faithfulness/answer relevance/context precision\n
- Regression tests across changes to chunking, k, embedding model, prompts

## How would you productionize a Colab RAG prototype?
- **Offline indexing pipeline** (async): parse → clean → chunk → embed → index, versioned
- **Online query service**: retrieve → rerank (optional) → generate → cite
- **Vector DB**: FAISS → managed vector DB / search service (Azure AI Search, OpenSearch, Pinecone, etc.)
- **Security**: metadata filtering, ACLs per user/document
- **Observability**: log retrieval sets, scores, latency; trace requests end-to-end
- **Cost/latency**: caching, smaller embeddings, fewer tokens, reranking trade-offs

## Strong “project pitch” (use this)
I built a cloud-architecture RAG assistant over my own documents. I focused on retrieval quality first (chunking and top-k tuning), returned citations for every answer, and added a small evaluation loop to measure improvements instead of relying on demos. I can explain how to take the notebook into production with an ingestion pipeline, managed vector search, ACL-aware filtering, observability, and continuous evaluation.

