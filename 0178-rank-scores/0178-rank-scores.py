import pandas as pd

def order_scores(scores: pd.DataFrame) -> pd.DataFrame:
    #Creating a dataframe of unique scores
    scores_unique = scores.score.drop_duplicates()
    scores_unique = pd.DataFrame(scores_unique.sort_values(ascending=False)).reset_index()

    #creating a rank column with lowest value correspoinding to highest rank
    rank = pd.DataFrame([int(x) for x in range(1,len(scores_unique)+1)],columns=['rank'])
    
    #concatenate both the dataframes 
    concat_score_rank = pd.concat([scores_unique, rank], axis=1)

    #dropping the index column which was created while calling the reset_index() function
    concat_score_rank.drop(['index'], inplace=True,axis=1)

    #merging both the dataframes and returning the sorted values by rank
    merged_df  = scores.merge(concat_score_rank, on='score', how='left')
    return merged_df.sort_values(by=['rank']).loc[:,['score','rank']]
    
