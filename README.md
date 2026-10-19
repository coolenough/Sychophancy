# Sychophancy

This repository contains exploratory mechanistic interpretability work on model sycophancy behavior.

The main reference document is [`paper.pdf`](./paper.pdf), and the primary runnable artifact is [`Mechinterp.ipynb`](./Mechinterp.ipynb).

## Repository contents
- `paper.pdf` — paper and project reference.
- `Mechinterp.ipynb` — main notebook for experiments and analysis.
- `results/` — generated plots, CSV outputs, and analysis artifacts.

## Simple setup
1. Use Python `3.11` (see `.python-version`).
2. Create and activate a virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate
   ```
3. Install basic notebook dependencies:
   ```bash
   pip install jupyter pandas numpy matplotlib plotly scikit-learn torch
   ```
4. Launch Jupyter:
   ```bash
   jupyter notebook
   ```
5. Open `Mechinterp.ipynb` and run cells top-to-bottom.

> The notebook installs additional model tooling (`transformer_lens`, `circuitsvis`, `transformers`) in its first cell.

## Data note
The notebook currently reads TruthfulQA data from a Kaggle-style path in one cell. If you run locally, update that path to your local dataset location before execution.

## Outputs
Notebook outputs include CSV files and figures such as:
- `questions.csv`, `known_questions.csv`, `unknown_question.csv`, `generation_analysis.csv`
- `logits.png`, `flips.jpg`, `avggap.jpg`, `linearprobes.jpg`, `ginv.jpg`, `beliefupdate.jpg`
