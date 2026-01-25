import pandas as pd
from sklearn.decomposition import PCA

def project_2d(matrix: pd.DataFrame) -> pd.DataFrame:
    """
    Project high-dimensional expression matrix into 2D space using PCA.

    Input:
        matrix: rows = genes, columns = samples
    
    Output:
        coords_df:
            rows = samples
            columns = ["PC1", "PC2"]
    """

    #Transpose: rows = samples, columns = genes
    X = matrix.T

    pca = PCA(n_components=2)
    coords_df = pd.DataFrame(
        coords,
        index=X.index,
        columns=["PC1", "PC2"]
    )

    return coords_df