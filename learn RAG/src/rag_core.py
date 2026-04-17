from __future__ import annotations

import os
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional, Sequence, Tuple


@dataclass(frozen=True)
class DocChunk:
    text: str
    metadata: Dict[str, Any]


def load_text_docs(docs_dir: str | Path) -> List[Tuple[str, str]]:
    """
    Load .txt/.md files from docs_dir.
    Returns list of (source_id, text).
    """
    docs_path = Path(docs_dir)
    if not docs_path.exists():
        return []

    out: List[Tuple[str, str]] = []
    for p in sorted(docs_path.rglob("*")):
        if not p.is_file():
            continue
        if p.suffix.lower() not in {".txt", ".md"}:
            continue
        text = p.read_text(encoding="utf-8", errors="ignore")
        source_id = str(p.relative_to(docs_path)).replace("\\", "/")
        out.append((source_id, text))
    return out


def simple_chunk_text(
    text: str,
    chunk_chars: int = 1200,
    overlap_chars: int = 150,
) -> List[str]:
    """
    Simple, dependency-free chunker by character count.
    Good enough for early notebooks; later notebooks experiment with alternatives.
    """
    text = re.sub(r"\r\n?", "\n", text).strip()
    if not text:
        return []

    chunks: List[str] = []
    i = 0
    n = len(text)
    while i < n:
        j = min(n, i + chunk_chars)
        chunk = text[i:j].strip()
        if chunk:
            chunks.append(chunk)
        if j >= n:
            break
        i = max(0, j - overlap_chars)
    return chunks


def build_chunks(
    docs: Sequence[Tuple[str, str]],
    chunk_chars: int = 1200,
    overlap_chars: int = 150,
) -> List[DocChunk]:
    chunks: List[DocChunk] = []
    for source_id, text in docs:
        parts = simple_chunk_text(text, chunk_chars=chunk_chars, overlap_chars=overlap_chars)
        for idx, part in enumerate(parts):
            chunks.append(
                DocChunk(
                    text=part,
                    metadata={
                        "source_id": source_id,
                        "chunk_index": idx,
                        "chunk_chars": chunk_chars,
                        "overlap_chars": overlap_chars,
                    },
                )
            )
    return chunks


def get_env(name: str, default: Optional[str] = None) -> Optional[str]:
    v = os.getenv(name)
    if v is None or not v.strip():
        return default
    return v.strip()

