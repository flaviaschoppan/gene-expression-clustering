"""
Gene Expression Clustering Pipeline

This script implements a minimal and explicit unsupervised clustering workflow for gene expression data, including:

1. Load raw counts and metadata
2. CPM normalization
3. Log2 transformation
4. KMeans clustering
5. 2D projection for visualization
6. Save results and figures

The goal is to demonstrate the structure of a clustering pipeline, not to perform biological interpretation.

"""

from pipeline.io import load_counts, load_metadata
from pipeline.normalization import cpm
from pipeline.transform import log2_transform
from pipeline.clustering import run_kmeans
from pipeline.plots import plot_clusters
from pipeline.projection import project_2d


def main():
    # ---------------------------------------------------
    # Step 1 - Load data
    # ---------------------------------------------------
    print("Loading raw counts and metadata...")
    counts = load_counts("data/raw/counts.csv")
    metadata = load_metadata("data/raw/metadata.csv")
    print("✓ Step 1 finished: data loaded\n")

    # ---------------------------------------------------
    # Step 2 - Normalize
    # ---------------------------------------------------
    print("Applying CPM normalization...")
    cpm_matrix = cpm(counts)
    print("✓ Step 2 finished: CPM normalization applied\n")

    # ---------------------------------------------------
    # Step 3 - Log transform
    # ---------------------------------------------------
    print("Applying log2 transformation...")
    log_matrix = log2_transform(cpm_matrix)
    print("✓ Step 3 finished: log2 transformation applied\n")

    # ---------------------------------------------------
    # Step 4 - Clustering
    # ---------------------------------------------------
    print("Running KMeans clustering...")
    labels = run_kmeans(log_matrix, n_clusters=2)
    print("✓ Step 4 finished: clustering computed\n")
    
    # ---------------------------------------------------
    # Step 5 - 2D projection
    # ---------------------------------------------------
    print("Projecting samples to 2D...")
    coords = project_2d(log_matrix)
    print("✓ Step 5 finished: projection computed\n")
    
    # ---------------------------------------------------
    # Step 6 - Save results
    # ---------------------------------------------------   
    print("Saving results...")

    labels.to_csv("outputs/matrices/cluster_labels.csv")
    coords.to_csv("outputs/matrices/cluster_projection_2d.csv")

    print("✓ Step 6 finished: result tables saved\n")

    # ---------------------------------------------------
    # Step 7 - Plots clusters
    # --------------------------------------------------- 
    print("Generating cluster plot...")

    plot_clusters(
        coords_df=coords,
        labels=labels,
        outpath="outputs/figures/clustering.png"
    )

    print("✓ Step 7 finished: cluster figure saved\n")

    print("Pipeline finished successfully.")

if __name__ == "__main__":
    main()