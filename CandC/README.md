# Towards Robust and Interactive Text-to-Visualization Translation: Enhancing Model Robustness and Mitigating Ambiguity in Natural Language Queries

This folder contains the code for the **Choose and Clarify (C&C)** component
used in the above paper.

C&C is provided here as a lightweight code folder. It keeps the core scripts
needed to run the C&C pipeline after the base GRED generation results have been
produced by the top-level `generate/` folder.

## Folder Structure

```text
CandC/
├── README.md
├── __init__.py
├── config.py
├── prompt.py
├── generate_candidate_set.py
├── generate_content_prob.py
├── multi-turn.py
└── run_CandC.sh
```

### Script Description

- `generate_candidate_set.py` generates candidate DVQs and their confidence
  scores from the GRED output.
- `generate_content_prob.py` aggregates candidate-level confidence into
  content-level probability distributions.
- `multi-turn.py` runs the multi-turn clarification stage and writes the final
  DVQ result.
- `prompt.py` stores prompt templates used by the three C&C scripts.
- `config.py` reads LLM API settings from environment variables. It stores no
  API keys.
- `run_CandC.sh` is a convenience wrapper for running the three-stage pipeline.



## Usage

First run the base GRED pipeline from the top-level `generate/` folder so that
`*_result_debugged_by_db_ann.json` files are available.

Then run C&C from this folder:

```bash
cd CandC
python ./generate_candidate_set.py
python ./generate_content_prob.py
python ./multi-turn.py
```

You can also run the same sequence with:

```bash
bash run_CandC.sh
```
