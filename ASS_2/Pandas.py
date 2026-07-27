import pandas as pd
df=pd.read_csv("Car_data.csv")
# display the version of the pandas
# print(pd.__version__)

# # display the first 10 rows
# print(df.head(10))

# # diaplay the last 10 rows
# print(df.tail(10))

# # give the information about the data
# print(df.info())

# # diaplay the first 5 rows--> Default
# print(df.head())

# # give the deatails about the data
# print(df.describe())

# # display the shape of the data
# print(df.shape)

# # give the total Null valued rows
# print(df.isnull())

# # fill the null values
# print(df.fillna(0))

# # display the total column of the data
# print(df.columns)

# # display the index with list
# print(df.index.tolist())

# display the data type of each column
# print(df.dtypes)

#Writes DataFrame to a comma-separated values (CSV) file
# print(df.to_csv("Car_data.csv",index=False))

# diaplay the unique values of the column
# print(df["Name"].unique())

# # print the Random sample rows
# print(df.sample(5))

# # display the first 5 rows of the data
# print(df.loc[0:4])

# display the first 4 rows of the data
# print(df.iloc[0:4])

# Display the rows where the Name is "Maruti 800"
print(df.loc[df["Name"]=="Maruti 800"])