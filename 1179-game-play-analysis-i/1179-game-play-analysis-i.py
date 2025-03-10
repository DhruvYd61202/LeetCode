import pandas as pd

def game_analysis(activity: pd.DataFrame) -> pd.DataFrame:
    activity.sort_values(by='event_date', inplace=True)
    final  = activity.drop_duplicates(subset=['player_id'], keep='first')
    final.rename({'event_date' : 'first_login'}, axis=1, inplace=True)
    return final[['player_id', 'first_login']]