# Survey Data Analysis Reports

This repository contains Quarto statistical reports analyzing employee survey data. The reports were written for a university statistics course and cover descriptive analysis, interval estimation, hypothesis testing, contingency tables, and log-linear models.

## Files

| Polish source | English translation |
|---------------|---------------------|
| `sprawo1.qmd` | `report1.qmd` |
| `sprawozdanie2.qmd` | `report2.qmd` |
| `sprawozdanie3.qmd` | `report3.qmd` |

The Polish `.qmd` files are the originals. The English `report*.qmd` files are generated copies with translated narrative text, section headings, table captions, and comments. R code, variable names, and factor levels such as `Tak` / `Nie` are kept unchanged because they match the underlying data.

## Report overview

- **Report 1** — Descriptive survey analysis, cross-tabulations, Clopper–Pearson confidence intervals, proportion tests, and Monte Carlo power simulation.
- **Report 2** — Multinomial confidence intervals, chi-square tests, Fisher / Freeman–Halton tests, association measures, correspondence analysis, and distance correlation.
- **Report 3** — Symmetry tests (McNemar, Bowker), Simpson's paradox, and log-linear models.

## Requirements

- [Quarto](https://quarto.org/)
- R (≥ 4.x) with packages used in the reports, including: `tidyverse`, `knitr`, `kableExtra`, `scales`, `gridExtra`, `binom`, and others as referenced in each document
- LaTeX with LuaLaTeX (PDF output)
- Survey data file `ankieta.csv` (UTF-8, `;` separator) in the project directory when rendering Report 1–3

## Rendering

Render a single report:

```bash
quarto render report1.qmd
quarto render report2.qmd
quarto render report3.qmd
```

Render all English reports:

```bash
quarto render report1.qmd report2.qmd report3.qmd
```

Polish originals can be rendered the same way, for example `quarto render sprawo1.qmd`.

## Regenerating English translations

English reports are produced from the Polish sources by a small Python script:

```bash
python3 scripts/translate_reports.py
```

The script reads `sprawo1.qmd`, `sprawozdanie2.qmd`, and `sprawozdanie3.qmd`, applies paragraph-level and phrase-level replacements, sets `lang: en`, and writes `report1.qmd`, `report2.qmd`, and `report3.qmd`.

Translation dictionaries live in:

- `scripts/translate_reports.py` — main mappings and report-specific strings
- `scripts/translations_pass2.py` — long prose paragraphs (reports 1–2)
- `scripts/translations_pass2_r3.py` — long prose paragraphs (report 3)
- `scripts/translations_fixup.py` — additional phrase-level fixes

After editing Polish sources or translation dictionaries, rerun the script and review the generated English files before committing.

## Notes

- Author names in the YAML header are unchanged.
- Reports 2 and 3 assume variables and conventions introduced in Report 1 (for example `CZY_ZADOW`, `WIEK_KAT`).
- Random seed `set.seed(2025)` is used for simulation-based tests.
