import pandas as pd

def find_classes(courses: pd.DataFrame) -> pd.DataFrame:
    res = courses.groupby('class')['student'].nunique().reset_index()
    res = res.loc[res['student'] >= 5]
    return pd.DataFrame(res['class'])