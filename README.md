# SURF Extractor: Multi-Agent Chemical Reaction Data Extraction

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![RDKit](https://img.shields.io/badge/RDKit-2023.03.3-green.svg)](https://www.rdkit.org/)

## Abstract
The extraction of standardized chemical reaction data from unstructured scientific literature remains a critical bottleneck in data-driven chemistry. We introduce **SURF Extractor**, an autonomous multi-agent pipeline powered by Large Language Models (LLMs) that extracts, validates, and normalizes reaction data from main publications and Supplementary Information (SI) into the rigorous SURF format. Relying on an orchestrated team of specialized agents—including an Extraction Agent, a Hallucination Critic, and a Chemical Resolution Agent—this framework bridges NLP vision models and established cheminformatics tools to generate high-fidelity, machine-readable datasets for retrosynthesis prediction and automated synthesis planning.

## Architecture

![Architecture Diagram Placeholder](https://via.placeholder.com/800x400.png?text=Architecture%3A+Coordinating+5+Agents+%28Parser%2C+Extractor%2C+Critic%2C+Resolver%2C+Formatter%29)
*Figure 1: SURF Extractor pipeline. The Coordinator Agent orchestrates document parsing (VisualHeist), information extraction (Gemini 2.5 Pro), hallucination criticism, chemical resolution (RDKit/CASClient), and SURF-compliant TSV formatting.*

## Context & State-of-the-Art
SURF Extractor directly builds upon recent advances in **Artificial Chemical Intelligence** and autonomous agents. While foundational work has demonstrated the reasoning capacities of LLMs for forward-synthesis and instrument execution, achieving high-throughput, structured data ingestion from legacy formats (PDFs) remains challenging. SURF Extractor directly addresses this by constraining generative capabilities with a "Critic Agent" paradigm and strict RDKit validation, establishing a data-flywheel for training the next generation of chemical foundation models.

## Installation 

We recommend using `conda` to ensure a clean cheminformatics environment:

```bash
git clone https://github.com/YourOrg/surf_extractor.git
cd surf_extractor

conda env create -f environment.yml
conda activate surf_extractor

pip install -e .
```

## Quick Start
Run the primary backend server:
```bash
./run.sh
```

Or programmatically access via agents:
```python
from surf_extractor.agents.coordinator import CoordinatorAgent
from surf_extractor.integrations.mermaid_wrapper import PDFParser

# Initialize coordination
coordinator = CoordinatorAgent()
# ... 
```
