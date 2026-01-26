import pandas as pd
from sklearn.decomposition import PCA

def project_2d(matrix: pd.DataFrame) -> pd.DataFrame:
    """
    Project high-dimensional expression matrix into 2D space using PCA.

    Input:
        matrix: rows = genes, columns = samples
    
    Output:
        coords_df: DataFrame with 2D coordinates (x, y)
                    index = samples names
    """

    # ---------------------------------------------------
    # Transpose: rows = samples, columns = genes
    # ---------------------------------------------------
    X = matrix.T


    # ---------------------------------------------------
    # Fit PCA with 2 components
    # ---------------------------------------------------
    pca = PCA(n_components=2)
    coords = pca.fit_transform(X)

    # ---------------------------------------------------
    # Build DataFrame with sample names
    # ---------------------------------------------------
    coords_df = pd.DataFrame(
        coords,
        index=X.index,
        columns=["x", "y"]
    )

    return coords_df