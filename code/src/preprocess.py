'''
    Contains some functions to preprocess the data used in the visualisation.
'''
import pandas as pd
from modes import MODE_TO_COLUMN


def summarize_lines(my_df):
    '''
        Sums each player's total of number of lines and  its
        corresponding percentage per act.

        The sum of lines per player per act is in a new
        column named 'PlayerLine'.

        The percentage of lines per player per act is
        in a new column named 'PlayerPercent'

        Args:
            my_df: The pandas dataframe containing the data from the .csv file
        Returns:
            The modified pandas dataframe containing the
            information described above.
    '''
    # TODO : Modify the dataframe, removing the line content and replacing
    # it by line count and percent per player per act
    # Show the columns from dataframe before preprocessing
    print("Columns in the DataFrame:", my_df.columns)
    # Remove Playerline column and raise error if not found
    if 'PlayerLine' in my_df.columns:
        my_df.drop('PlayerLine', axis=1, inplace=True)
    else:
        raise KeyError("Column 'PlayerLine' not found in the DataFrame before dropping")
    
    # Group by 'Act' and 'Player', and count the number of lines for each group
    my_df = my_df.groupby(['Act', 'Player']).size().reset_index(name='PlayerLine')
    print("Columns after grouping and counting lines:", my_df.columns)
    print(my_df.head())
    
    # Total lines per act
    total_lines_per_act = my_df.groupby('Act')['PlayerLine'].transform('sum')
    # Debug
    print("Calculated total_lines_per_act:", total_lines_per_act)
    
    # Calculate 'PlayerPercent' based on the new 'LineCount' column
    my_df['PlayerPercent'] = (my_df['PlayerLine'] / total_lines_per_act) * 100
    print("Calculated 'PlayerPercent'")
    
    return my_df  


def replace_others(my_df):
    '''
        For each act, keeps the 5 players with the most lines
        throughout the play and groups the other plyaers
        together in a new line where :

        - The 'Act' column contains the act
        - The 'Player' column contains the value 'OTHER'
        - The 'LineCount' column contains the sum
            of the counts of lines in that act of
            all players who are not in the top
            5 players who have the most lines in
            the play
        - The 'PercentCount' column contains the sum
            of the percentages of lines in that
            act of all the players who are not in the
            top 5 players who have the most lines in
            the play

        Returns:
            The df with all players not in the top
            5 for the play grouped as 'OTHER'
    '''
    # TODO : Replace players in each act not in the top 5 by a
    # new player 'OTHER' which sums their line count and percentage
    # Identify top players
    top_players = my_df.groupby(['Act', 'Player'])['PlayerLine'].sum().groupby(level=0).nlargest(5).reset_index(level=0, drop=True)
    
    # Keep only the top players
    top_players_df = my_df[my_df['Player'].isin(top_players.index.get_level_values('Player'))]
    
    # Replace other players with 'OTHER'
    my_df.loc[~my_df['Player'].isin(top_players.index.get_level_values('Player')), 'Player'] = 'OTHER'
    
    return my_df


def clean_names(my_df):
    '''
        In the dataframe, formats the players'
        names so each word start with a capital letter.

        Returns:
            The df with formatted names
    '''
    # TODO : Clean the player names
    # Debug: show dataframe sample before and after 
    print("Before cleaning names:", my_df.head())  
    print("DataFrame info before cleaning names:")
    my_df.info()  
    
    # Modify names format
    if 'Player' in my_df.columns:
        my_df['Player'] = my_df['Player'].str.title()
        print("After cleaning names:", my_df.head())  
        print("DataFrame info after cleaning names:")
        my_df.info()  
    else:
        print("Error: 'Player' column not found in the DataFrame")
    return my_df
