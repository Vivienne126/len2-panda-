import pandas as pd
print("Part 1 : Panda Series")
scores=[98000,32000,65432,12321,67540]
players=pd.Series(scores,index=["Night Wolf" , "starblaze" , "Pixelxing" , "cyberfox" , "ironstorm"])
print(players)

