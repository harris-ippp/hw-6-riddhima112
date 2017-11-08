import pandas as pd
import glob
#Getting the list of filenames from the directory
filename=(glob.glob("*.csv"))
#Creating an empty dataframe to append all the csv files into
frame = pd.DataFrame()
list=[]
for file in filename:
    header = pd.read_csv(file, nrows = 1).dropna(axis = 1)
    d = header.iloc[0].to_dict()
    df= pd.read_csv(file, index_col = 0,
               thousands = ",", skiprows = [1])
    df.rename(inplace = True, columns = d) # rename to democrat/republican
    df.dropna(inplace = True, axis = 1)    # drop empty columns
    df["Year"] = file
    df["Year"] = df["Year"].replace(".csv", "", regex = True) #dropping .csv coming from the filename
    df=df[["Democratic", "Republican", "Total Votes Cast", "Year"]]
    list.append(df)
    frame=frame.append(df) #appending datasets

#Grouping to get the # of Republican vote share and Total votes cast by county/city and year
frame=frame.groupby(['County/City', 'Year'])['Republican','Total Votes Cast'].sum().reset_index()
#Creating a new column for Republican vote share
frame['Republican Vote Share']=frame['Republican']/frame['Total Votes Cast']
#Plotting graphs for relevant counties
#Accomack County
plot1=frame[frame["County/City"]=='Accomack County'].plot(x="Year", y="Republican Vote Share") #creating the mask to get required county
plot1.get_figure().savefig('accomack_county.pdf')

#Albemarle County

plot2=frame[frame["County/City"]=='Albemarle County'].plot(x="Year", y="Republican Vote Share") #creating the mask to get required county
plot2.get_figure().savefig('albemarle_county.pdf')

#Alexandria City

plot3=frame[frame["County/City"]=='Alexandria City'].plot(x="Year", y="Republican Vote Share") #creating the mask to get required county
plot3.get_figure().savefig('alexandria_city.pdf')

#Alleghany County

plot4=frame[frame["County/City"]=='Alleghany County'].plot(x="Year", y="Republican Vote Share") #creating the mask to get required county
plot4.get_figure().savefig('alleghany_county.pdf')
