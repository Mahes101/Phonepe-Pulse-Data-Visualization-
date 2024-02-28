# Phonepe-Pulse-Data-Visualization-
![title image](https://github.com/Mahes101/Phonepe-Pulse-Data-Visualization-/assets/153369828/ed6980c1-d85c-4625-b267-68131f7e8957)
Data Visualization and Exploration : A User-Friendly Tool Using Streamlit and Plotly
What is PhonePe Pulse?
The PhonePe Pulse website showcases more than 2000+ Crore transactions by consumers on an interactive map of India. With over 45% market share, PhonePe's data is representative of the country's digital payments. The insights on the website and in the report have been drawn from two key sources - the entirety of PhonePe's transaction data combined with merchant and customer interviews. The report is available as a free download on the PhonePe Pulse website and GitHub.

Libraries/Modules needed for the project!
Plotly - (To plot and visualize the data)
Pandas - (To Create a DataFrame with the scraped data)
pymysql - (To store and retrieve the data)
Streamlit - (To Create Graphical user Interface)
json - (To load the json files)
git.repo.base - (To clone the GitHub repository)
Workflow
Step 1:
Importing the Libraries:

Importing the libraries. As I have already mentioned above the list of libraries/modules needed for the project. First we have to import all those libraries. If the libraries are not installed already use the below piece of code to install.

    !pip install ["Name of the library"]
If the libraries are already installed then we have to import those into our script by mentioning the below codes.

    import pandas as pd
    import pymysql
    import streamlit as st
    import plotly.express as px
    import os
    import json
    from streamlit_option_menu import option_menu
    from PIL import Image
    from git.repo.base import Repo
Step 2:
Data extraction:

Clone the Github using scripting to fetch the data from the Phonepe pulse Github repository and store it in a suitable format such as JSON. Use the below syntax to clone the phonepe github repository into your local drive.

    from git.repo.base import Repo
    Repo.clone_from("GitHub Clone URL","Path to get the cloded files")
Step 3:
Data transformation:

In this step the JSON files that are available in the folders are converted into the readeable and understandable DataFrame format by using the for loop and iterating file by file and then finally the DataFrame is created. In order to perform this step I've used os, json and pandas packages. And finally converted the dataframe into CSV file and storing in the local drive.

path1 = "Path of the JSON files"
agg_trans_list = os.listdir(path1)

# Give any column names that you want
columns1 = {'State': [], 'Year': [], 'Quarter': [], 'Transaction_type': [], 'Transaction_count': [],'Transaction_amount': []}
Looping through each and every folder and opening the json files appending only the required key and values and creating the dataframe.
  path1 = "C:/Users/mahes/OneDrive/Desktop/phonepe/pulse/data/aggregated/transaction/country/india/state/"
aggre_trans_state_list = os.listdir(path1)

columns1 = {"States":[], "Year":[], "Quarter":[], "Transaction_type":[], "Transaction_count":[], "Transaction_amount":[]}
for state_name in aggre_trans_state_list:
    curr_st_name = path1+state_name+"/"
    aggre_year_list = os.listdir(curr_st_name)
    
    for year_name in aggre_year_list:
        curr_yr = curr_st_name+year_name+"/"
        aggre_file_list = os.listdir(curr_yr)
        
        for file_name in aggre_file_list:
            curr_file = curr_yr+file_name
            data = open(curr_file,"r")
            
            Agg_trans = json.load(data)
            
            for i in Agg_trans["data"]["transactionData"]:
                name = i["name"]
                count = i["paymentInstruments"][0]["count"]
                amount = i["paymentInstruments"][0]["amount"]
                columns1["States"].append(state_name)
                columns1["Year"].append(int(year_name))
                columns1["Quarter"].append(int(file_name.strip(".json")))
                columns1["Transaction_type"].append(name)
                columns1["Transaction_count"].append(count)
                columns1["Transaction_amount"].append(amount)

                
aggregated_transaction = pd.DataFrame(columns1)                
aggregated_transaction["States"] = aggregated_transaction["States"].str.replace("andaman-&-nicobar-islands","Andaman & Nicobar")
aggregated_transaction["States"] = aggregated_transaction["States"].str.replace("-"," ")
aggregated_transaction["States"] = aggregated_transaction["States"].str.title()
aggregated_transaction['States'] = aggregated_transaction['States'].str.replace("Dadra & Nagar Haveli & Daman & Diu", "Dadra and Nagar Haveli and Daman and Diu")

    

Step 4:
Database insertion:

To insert the datadrame into SQL first I've created a new database and tables using "pymysql" library in Python to connect to a MySQL database and insert the transformed data using SQL commands.

Creating the connection between python and mysql

    conn = sql.connect(host="localhost",
               user="username",
               password="password",
               database= "phonepe_db"
              )
    cur = conn.cursor(buffered=True)
Creating tables

   cur.execute("create table 'Table name' (col1 varchar(100), col2 int, col3 int, col4 varchar(100), col5 int, col6 double)")

    for i,row in df.iterrows():
    
        #here %S means string values 
        sql = "INSERT INTO agg_trans VALUES (%s,%s,%s,%s,%s,%s)"
        cur.execute(sql, tuple(row))
        
        # the connection is not auto committed by default, so we must commit to save our changes
        conn.commit()
Step 5:
Dashboard creation:

To create colourful and insightful dashboard I've used Plotly libraries in Python to create an interactive and visually appealing dashboard. Plotly's built-in Pie, Bar, Geo map functions are used to display the data on a charts and map and Streamlit is used to create a user-friendly interface with multiple dropdown options for users to select different facts and figures to display.

Step 6:
Data retrieval:

Finally if needed Using the "pymysql" library to connect to the MySQL database and fetch the data into a Pandas dataframe.

