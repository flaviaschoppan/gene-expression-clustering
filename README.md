# Gene Expression Clustering Pipeline

## Overview

This repository implements a minimal, explicit, and reproducible unsupervised clustering pipeline for gene expression data.

The goal of this project is to demonstrate the structure and organization of a typical clustering workflow applied to expression matrices, including normalization, transformation, clustering, and 2D visualization of sample structure.

The focus is not on biological interpretation, but on building a clear, inspectable, and reproducible computational pipeline.

---

## What this pipeline does

1. Loads a raw gene expression count matrix and sample metadata  
2. Normalizes counts to CPM (Counts Per Million)  
3. Applies log2(x + 1) transformation  
4. Runs KMeans clustering on samples  
5. Projects samples to 2D for visualization  
6. Saves clustering results and figures as versionable artifacts   

---

## Why clustering

In transcriptomics and other high-dimensional biological datasets, clustering is commonly used to:

- Inspect global structure of samples  
- Detect groups, subpopulations, or unexpected patterns  
- Identify potential batch effects or outliers  
- Explore similarity relationships without supervision  

This project formalizes this step as an explicit and reproducible pipeline.

---

## Project structure

```text
gene-expression-clustering/
├── data/
│   └── raw/
│       ├── counts.csv
│       └── metadata.csv
├── pipeline/
│   ├── __init__.py
│   ├── io.py
│   ├── normalization.py
│   ├── transform.py
│   ├── clustering.py
│   ├── projection.py
│   └── plots.py
├── outputs/
│   ├── matrices/
│   └── figures/
├── run_pipeline.py
├── requirements.txt
├── README.md
└── LICENSE
```

---

## Outputs

The pipeline produces the following versionable artifacts:

```text
outputs/matrices/cluster_labels.csv
outputs/matrices/cluster_projection_2d.csv

outputs/figures/clustering.png
```

---

## How to run

1. Install dependencies: ```pip install -r requirements.txt```

2. Run the pipeline: ```python run_pipeline.py```

All outputs will be written to the ```outputs/``` folder.

---

## Reproducibility

All steps in this pipeline are:
- Explicit
- Deterministic
- Scripted
- And produce versionable artifacts

This repository is designed as a didactic and structural example of a real clustering stage in gene expression analysis pipelines.

---

## Data note

The data used in this repository are synthetic and intended solely to demonstrate the numerical behavior of the pipeline and the structure of the workflow.

---

## License

This project is released under the MIT License.