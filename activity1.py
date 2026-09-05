#Part 1: Create a panda series of top player scores

import pandas as pd
print("Part 1 : Panda Series")
scores=[98000,32000,65432,12321,67540]
players=pd.Series(scores,index=["Night Wolf" , "starblaze" , "Pixelxing" , "cyberfox" , "ironstorm"])
print(players)

#Part 2: Create adataframe of gaming stats
print("Part 2: Data frame")
data={"player": ["nightwolf","startblaze", "pixeling", "cyberfox" ,"Ironstorm"] , "level":[42,38,35,30,27],
      "Scores": [90500,82200,70567,65100,65465]}

df=pd.DataFrame(data)
print(df)

#Part 3: Accessing rows using loc
print()
print("Part 3: Accessing rows")
print("Row 0 (top player)")
print(df.loc[0])
print()
print("Rows 2 and 3")
print(df.loc[2:3])

#Part 4: Load leaderfound.row and view the table
print()
print("Part 4: Reading a csv file")
print("First five lows")
print(df.head())
print()
print("Last 3 lows(tail)")
print(df.tail(3))
print()
print("Dataset info:")
print(df.info())

#Part 5: Clean the data
print()
print("Part 5: Cleaning the data")
print("Rows with missing values removed (dropna)")
clean_df=df.dropna()
print(clean_df.to_string)
print()
print("Missing values filled with 0 (filna)")
filled_df=df.fillna(0)
print(filled_df.to_string())
