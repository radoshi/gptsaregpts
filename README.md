# An analysis of LLM impacts on Jobs

## Introduction

This is the code that backs the blog post at:
https://rushabhdoshi.com/posts/2023-09-18-llm-leverage/

This is based on the GPTs are GPTs paper. I was interested in building an intuition around the broad impacts of LLMs and used that as a starting point.
The paper is available [here](https://arxiv.org/pdf/2103.10385.pdf).

## Installation

This repo is essentially three parts:

1. Building up a sqlite db from SQL files from O\*Net. The actual files aren't included because they're large. You can download them here: https://www.onetcenter.org/database.html#all-files
2. Classifying the DWAs from the O\*Net using OpenAI. This is done in `notebooks/classification.ipynb`. The results are stored in `data/readonly`
3. Analyzing the results. This is done in `notebooks/analysis.ipynb`. The results are stored in `data/output`

To get up and running, after downloading the repo, do:

```sh
poetry install
```

I prefer to run jupyter notebooks in VSCode but YMMV.

## Contributions

Contributions are welcome, especially if you see bugs and issues. Please open a PR.

## Future directions

[ ] Replicate with GPT-4 (costs quite a bit more)
[ ] Look at `gpt-3.5-turbo-instruct` with log-probs, to see if it improves classification
[ ] Classify tasks instead of DWAs
[ ] Classify occupations instead of DWAs
