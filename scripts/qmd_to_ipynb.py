#!/usr/bin/env python3
"""Convert Polish Quarto (.qmd) reports to Jupyter notebooks with R cells."""

from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

FILES = [
    ("sprawo1.qmd", "sprawozdanie1.ipynb"),
    ("sprawozdanie2.qmd", "sprawozdanie2.ipynb"),
    ("sprawozdanie3.qmd", "sprawozdanie3.ipynb"),
]

CHUNK_RE = re.compile(
    r"^```\{([^\}]*)\}\s*\n(.*?)^```\s*$",
    re.MULTILINE | re.DOTALL,
)

YAML_RE = re.compile(r"^---\s*\n.*?\n---\s*\n", re.DOTALL)


def parse_title_author(text: str) -> tuple[str, str]:
    title_m = re.search(r'^title:\s*"(.*?)"', text, re.MULTILINE)
    author_m = re.search(r'^author:\s*"(.*?)"', text, re.MULTILINE)
    title = title_m.group(1) if title_m else "Sprawozdanie"
    author = author_m.group(1) if author_m else ""
    return title, author


def md_cell(source: str) -> dict | None:
    source = source.strip("\n")
    if not source.strip():
        return None
    lines = [line + "\n" for line in source.splitlines()]
    if lines:
        lines[-1] = lines[-1].rstrip("\n")
    return {"cell_type": "markdown", "metadata": {}, "source": lines}


def code_cell(source: str, chunk_opts: str = "") -> dict:
    source = source.strip("\n")
    lines = [line + "\n" for line in source.splitlines()]
    if lines:
        lines[-1] = lines[-1].rstrip("\n")
    meta: dict = {"vscode": {"languageId": "r"}}
    if chunk_opts:
        meta["chunk_opts"] = chunk_opts.strip()
    return {
        "cell_type": "code",
        "metadata": meta,
        "source": lines,
        "outputs": [],
        "execution_count": None,
    }


def setup_cell() -> dict:
    code = """# Ustaw katalog roboczy na korzeń repozytorium (dla ankieta.csv)
for (p in c(".", "..", normalizePath(".."))) {
  if (file.exists(file.path(p, "ankieta.csv"))) {
    setwd(p)
    break
  }
}"""
    return code_cell(code, "setup")


def convert_qmd(path: Path) -> list[dict]:
    raw = path.read_text(encoding="utf-8")
    yaml_m = YAML_RE.match(raw)
    title, author = parse_title_author(yaml_m.group(0) if yaml_m else "")
    body = YAML_RE.sub("", raw, count=1)

    cells: list[dict] = []
    header = f"# {title}\n"
    if author:
        header += f"\n**Autorzy:** {author}\n"
    cells.append(md_cell(header))
    cells.append(setup_cell())

    pos = 0
    for m in CHUNK_RE.finditer(body):
        md = body[pos : m.start()]
        c = md_cell(md)
        if c:
            cells.append(c)
        opts = m.group(1)
        code = m.group(2)
        code = code.replace("dev='ragg_png'", "dev='png'").replace('dev="ragg_png"', 'dev="png"')
        cells.append(code_cell(code, opts))
        pos = m.end()

    tail = body[pos:]
    c = md_cell(tail)
    if c:
        cells.append(c)

    return cells


def build_notebook(cells: list[dict]) -> dict:
    return {
        "cells": cells,
        "metadata": {
            "kernelspec": {
                "display_name": "R",
                "language": "R",
                "name": "ir",
            },
            "language_info": {
                "name": "R",
                "pygments_lexer": "r",
                "version": "4.5.0",
            },
        },
        "nbformat": 4,
        "nbformat_minor": 5,
    }


def main() -> None:
    out_dir = ROOT / "notebooks"
    out_dir.mkdir(exist_ok=True)
    for src_name, dst_name in FILES:
        src = ROOT / src_name
        cells = convert_qmd(src)
        nb = build_notebook(cells)
        out = out_dir / dst_name
        out.write_text(json.dumps(nb, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
        print(f"{src_name} -> {dst_name} ({len(cells)} cells)")


if __name__ == "__main__":
    main()
