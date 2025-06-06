import pandas as pd
from utils.openspace import Openspace

# load the name of people（each line is a name and no title）
df = pd.read_csv("colleagues.csv", header=None)
names = df[0].dropna().tolist()

# Init Openspace（for example 6 tables，4 seats for each table）
openspace = Openspace(number_of_tables=6, seats_per_table=4)

# assign the seat
openspace.organize(names)

# show the distribution
openspace.display()

# Save all distribution as a excel file
openspace.store("result.xlsx")
