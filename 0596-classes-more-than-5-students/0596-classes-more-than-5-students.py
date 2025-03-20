import pandas as pd

def find_classes(courses: pd.DataFrame) -> pd.DataFrame:
    res = courses.groupby('class')['student'].count().reset_index()
    return res[res['student'] >= 5][['class']]