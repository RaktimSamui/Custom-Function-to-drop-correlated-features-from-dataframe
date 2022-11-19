def corr_var(df,y):
    '''
    This is a very robust function that takes a Pandas DataFrame as input and
    drops one of the features whose more than 75% of the data is correlated
    with another feature.
    This is done for all the features w.r.t each other
    until there are no correlated features left,
    finally after dropping all of the correlated columns
    it returns the DataFrame with all the correlated features removed.

    Additionally it also prints the features that are correlated
    to each other, to what degree are they correlated and
    the feature that is going to be dropped out of the two.

    input: DataFrame
    y: y variable
    return: DataFrame without correlated features
    '''
    cor=df.corr()
    try:
        cor1=cor.drop([y],axis='index')
        cor2=cor1.drop([y],axis='columns')
    except KeyError as key:
        cor2=cor
    high_cor={}
    for n in cor2.columns:
        for i in cor2.index:
            if n!=i:
                if cor2.loc[n,i]>0.75 or cor2.loc[n,i]<-0.75:
                    high_cor[cor2.loc[n,i]]=[n,i] # mapping only the unique values of correlation using dictionary(that
                                            # is initialized above as high_cor),
                                            # as dictionary keys takes unique values and simultaneously mapping
                                            # the respective columns and rows
    drop_col=[]
    for a,b in high_cor.items():
        print(f'correlation of {round(a,2)} found in columns "{b[0]}" and "{b[1]}"---> dropping column "{b[0]}"')
        drop_col.append(b[0]) # appending the column names that are to be dropped in list initialized as drop_col
    return df.drop(drop_col,axis='columns')