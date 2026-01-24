import pandas as pd

def load_counts(path: str) -> pd.DataFrame:
    """
    Load raw gene expression count matrix.

    Expected format:
    • Rows = genes
    • Columns = samples
    • First Column  = genes indentifiers
    """
    counts = pd.read_csv(path, index_col=0)
    return counts
    