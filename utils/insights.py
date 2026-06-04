def top_state(df,column):

    state = (
        df.groupby("State Name")[column]
        .sum()
        .idxmax()
    )

    value = (
        df.groupby("State Name")[column]
        .sum()
        .max()
    )

    return state,value
