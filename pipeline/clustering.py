import pandas as pd
from sklearn.cluster import KMeans

def run_kmeans(matrix: pd.DataFrame, n_clusters: int = 2, random_state: int = 42) -> pd.Series:
    """
    Run KMeans clustering on an expression matrix.

    Input:
        matrix: pd.DataFrame
            rows = genes
            columns = samples
    
    Output:
        labels: pd.Series
            index = sample names
            values = cluster assignment (0, 1, 2, ...)
    """

    # ---------------------------------------------------------------
    # Transpose: now rows = samples, columns = genes
    # ---------------------------------------------------------------
    X = matrix.T


    # ---------------------------------------------------------------
    # Fit KMeans
    # ---------------------------------------------------------------
    kmeans = KMeans(n_clusters=n_clusters, random_state=random_state)
    clusters = kmeans.fit_predict(X)

    # ---------------------------------------------------------------
    # Build result as a labeled series
    # ---------------------------------------------------------------
    labels = pd.Series(
        clusters,
        index=X.index,
        name="cluster"
    )

    return labels