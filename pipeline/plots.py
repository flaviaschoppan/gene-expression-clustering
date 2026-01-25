import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_theme(style="whitegrid", context="talk")

def plot_clusters(coords_df: pd.DataFrame, labels: pd.Series, outpath: str):
    """
    Plot samples in2D space colored by cluster assignment.

    Parameters
    ----------
    coords_df : pd.DataFrame
        DataFrame with 2D coordinates (e.g., from PCA).
        Index = sample identifications
        Columns = ["x", "y"] or ["PC1", "PC2"]
    
    labels : pd.Series
        Cluster labels per sample.
        Index = sample identifications
    
    outpath : str
        Path to save the figure.
    """

    # Merge coordinates and cluster labels
    df = coords_df.join(labels)

    plt.figure(figsize=(7, 6))

    sns.scatterplot(
        data=df,
        x=df.columns[0],
        y=df.columns[1],
        hue="cluster",
        palette="tab10",
        s=100
    )

    plt.title("Clustering of samples")
    plt.xlabel(df.columns[0])
    plt.ylabel(df.columns[1])

    plt.tight_layout()
    plt.savefig(outpath, dpi=150)
    plt.close()