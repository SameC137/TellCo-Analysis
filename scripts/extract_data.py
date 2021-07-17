
import pandas as pd
def drop_duplicate(self, df:pd.DataFrame,subset:list)->pd.DataFrame:
    """
    drop duplicate rows
    """
    return df.drop_duplicates(subset=subset, keep=False,inplace=false)

    