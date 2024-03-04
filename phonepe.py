# ["FRAME WORK LIBRARIES"]
import streamlit as st 
from plotly import express as px  
from streamlit_plotly_events import plotly_events
from streamlit_option_menu import option_menu
from streamlit_lottie import st_lottie 
import PIL
from PIL import Image
import plotly.graph_objects as go

# ["REQUEST LIBRARY FOR CLONE"]
import requests

#["PYTHON LIBRARIES FOR TABULAR DATA AND FILE HANDLING"]
import pandas as pd
import numpy as np
import json

#["SQL LIBRARY FOR DATABASE OPERATIONS"]
import pymysql

# ***** CONNECTING TO SQL *****
conn = pymysql.connect(host="localhost",port=3306,user="root",passwd="admin@123",database="phonepe_db")
cur = conn.cursor()

# *****  GETTING PHONE PE DATA AS DATAFRAME *****
# GETTING AGGREGATED TRANSACTION TABLE DATA.
cur.execute("select * from aggregated_transaction") 
aggregated_trans_df = cur.fetchall()
df_aggregated_trans = pd.DataFrame(aggregated_trans_df, columns = ("States", "Year","Quarter","Transaction_type","Transaction_count","Transaction_amount"))

#GETTING AGGREGATED USER TABLE DATA.
cur.execute("select * from aggregated_user") 
aggregated_user_df = cur.fetchall()
df_aggregated_user = pd.DataFrame(aggregated_user_df, columns = ("States", "Year","Quarter","User_brand","User_count","User_percentage"))

#GETTING MAP TRANSACTION TABLE DATA.
cur.execute("select * from map_transaction") 
map_trans_df = cur.fetchall()
df_map_trans = pd.DataFrame(map_trans_df, columns = ("States", "Year","Quarter","District","Transaction_count","Transaction_amount"))

#GETTING MAP USER TABLE DATA.
cur.execute("select * from map_user") 
map_user_df = cur.fetchall()
df_map_user = pd.DataFrame(map_user_df, columns = ("States", "Year","Quarter","District","Registered_users","Appopens_count"))

#GETTING TOP TRANSACTION DISTRICT TABLE DATA.
cur.execute("select * from top_transaction_districts") 
top_transaction_districts_df = cur.fetchall()
df_top_trans_dis = pd.DataFrame(top_transaction_districts_df, columns = ("States", "Year","Quarter","District","Transaction_count","Transaction_amount"))

#GETTING TOP TRANSACTION PINCODES TABLE DATA.
cur.execute("select * from top_transaction_pincodes") 
top_transaction_pincodes_df = cur.fetchall()
df_top_trans_pin = pd.DataFrame(top_transaction_pincodes_df, columns = ("States", "Year","Quarter","Pincodes","Transaction_count","Transaction_amount"))

#GETTING TOP USER DISTRICTS DATA.
cur.execute("select * from top_user_districts") 
top_user_districts_df = cur.fetchall()
df_top_user_dis = pd.DataFrame(top_user_districts_df, columns = ("States", "Year","Quarter","District","Registered_users"))

#GETTING TOP USER PINCODES TABLE DATA.
cur.execute("select * from top_user_pincodes") 
top_user_pincodes_df = cur.fetchall()
df_top_user_pin = pd.DataFrame(top_user_pincodes_df, columns = ("States","Year","Quarter","Pincodes","Registered_users"))

#**** LOADING JSON LOTTIE FILE *****
path = "C:/Users/mahes/Downloads/HEART BEAT.json"
with open(path,"r") as file: 
	url = json.load(file) 



# ***** STREAMLIT FRAME WORK ***** 

icon = Image.open("phonepe_mainbanner2.jpg")
# SETTING PAGE CONFIGURATION...........
st.set_page_config(page_title='Phone Pe',page_icon=icon,layout="wide")
coll1,coll2,coll3,coll4 = st.columns(4)
with coll1:
    st.image(Image.open("C:\\Users\\mahes\\OneDrive\\Desktop\\MY PRACTICE\\title image.png"))
with coll2:
    st_lottie(url, reverse=True, height=50, width=100, speed=1, loop=True, quality='high', key='heart_beat')
with coll3:    
    st_lottie(url, reverse=True, height=50, width=100, speed=1, loop=True, quality='high', key='heart_beat1')
with coll4:    
    st_lottie(url, reverse=True, height=50, width=100, speed=1, loop=True, quality='high', key='heart_beat2')
        
# OPTION MENU FOR CHOICES OF VIEWS
selected = option_menu(None,
                       options = ["About","Home","Analysis","Insights"],
                       icons = ["safe2 fill","house-door-fill","bar-chart-line-fill","lightbulb"],
                       default_index=0,
                       orientation="horizontal",
                       styles={"container": {"width": "100%"},
                               "icon": {"color": "white", "font-size": "24px"},
                               "nav-link": {"font-size": "24px", "text-align": "center", "margin": "-2px"},
                               "nav-link-selected": {"background-color": "#6F36AD"}})

# ABOUT TAB......

if selected == "About":
    col1, col2, = st.columns(2)
    
    #col1.image(Image.open("C:\\Users\\mahes\\OneDrive\\Desktop\\MY PRACTICE\\Phonepe_Thumnail_440_851.jpg"),width=200)
    col1.image(Image.open("C:\\Users\\mahes\\OneDrive\\Desktop\\MY PRACTICE\\pulse-2.jpg") ,width=600)
    with col1:
        
        st.subheader("The Indian digital payments story has truly captured the world's imagination. From the largest towns to the remotest villages, there is a payments revolution being driven by the penetration of mobile phones, mobile internet and state-of-the-art payments infrastructure built as Public Goods championed by the central bank and the government. Founded in December 2015, PhonePe has been a strong beneficiary of the API driven digitisation of payments in India. When we started, we were constantly looking for granular and definitive data sources on digital payments in India. PhonePe Pulse is our way of giving back to the digital payments ecosystem.")
        url1 = 'https://www.phonepe.com/app-download/'
        st.markdown(f'''<a href={url1}><button style="background-color:#8a2be2;"><border style="display:inline-block;padding:0.5em 1em;border-radius:12px;border-color:none"><text style="color:#f2f3f4;">DOWNLOAD THE APP</button></a>''',unsafe_allow_html=True)

    with col2:
        st.video("C:\\Users\\mahes\\OneDrive\\Desktop\\MY PRACTICE\\pulse-video.mp4")
        st.image(Image.open("C:\\Users\\mahes\\OneDrive\\Desktop\\MY PRACTICE\\homepg_image.jpg"), width=650)

# HOME TAB
if selected == "Home":
    col1,col2 = st.columns(2)
    with col1:
        st.video("C:\\Users\\mahes\\OneDrive\\Desktop\\MY PRACTICE\\video1.mp4")
        st.image(Image.open("C:\\Users\\mahes\\OneDrive\\Desktop\\MY PRACTICE\\PhonePe-Pulse.jpg"), width=500)
    with col2:
        st.title(':violet[PHONEPE HOME]')
        st.write('PhonePe is an Indian multinational digital payments and financial services company headquartered in Bengaluru, Karnataka, India.PhonePe was founded in December 2015,by Sameer Nigam, Rahul Chari and Burzin Engineer.The PhonePe app, based on the Unified Payments Interface (UPI), went live in August 2016.'
                'The PhonePe app is available in 11 Indian languages.Using PhonePe, users can send and receive money, recharge mobile, DTH, data cards, make utility payments, pay at shops, invest in tax saving funds, buy insurance, mutual funds, and digital gold.')
        st.subheader(':violet[Digital Payments in India: A US$10 Tn Opportunity!]')
        st.write('Check out the new PhonePe Pulse - BCG report on what the future holds for digital payments in India.')
        url2 = 'https://www.phonepe.com/pulsestatic/780/pulse/static/83bc2c9e9038369af2eb9eb7d62cb49f/PhonePe_Pulse_BCG_report.pdf'
        text = "DOWNLOAD BCG REPORT"
        st.markdown(f'''<a href={url2}><button style="background-color:#8a2be2;"><border style="display:inline-block;padding:0.5em 1em;border-radius:12px;"><text style="color:#f2f3f4;">{text}</button></a>''',unsafe_allow_html=True)
        
        st.title(':violet[PHONEPE PULSE DATA VISUALISATION]')
        st.subheader(':violet[Phonepe Pulse]:')
        st.write('PhonePe Pulse is a feature offered by the Indian digital payments platform called PhonePe.PhonePe Pulse provides users with insights and trends related to their digital transactions and usage patterns on the PhonePe app.')
        st.subheader(':violet[Phonepe Pulse Data Visualisation]:')
        st.write('Data visualization refers to the graphical representation of data using charts, graphs, and other visual elements to facilitate understanding and analysis in a visually appealing manner.'
                 'The goal is to extract this data and process it to obtain insights and information that can be visualized in a user-friendly manner.')
        
        st.markdown("## :violet[Done by] : UMAMAHESWARI S")
        st.markdown("[Inspired from](https://www.phonepe.com/pulse/)")
        st.markdown("[Githublink](https://github.com/mahes101)")
        
    st.write("---")


# ANALYSIS TAB
option1 = ""
option2 = 1
quarter_option = 1
if selected == "Analysis":
    st.title(':violet[ANALYSIS]')
    col1, col2, col3 = st.columns(3)
    with col1:
        st.header(":violet[COUNTRY]")
        option = st.selectbox(':violet[CHOOSE COUNTRY]',["INDIA"])
        
    with col2:
        st.header(":violet[CHOOSE]")
        option1 = st.selectbox(':violet[CHOOSE DATA ANALYSIS OPTION]',["TRANSACTIONS","USER"])
        #map_view = st.button(":violet[MAP REPRESENTATION]")
    with col3:
        year = [2018,2019,2020,2021,2022,2023]
        quarter = ['Q1-(JAN-MAR)','Q2-(APR-JUN)','Q3-(JUL-SEP)','Q4-(OCT-DEC)']
        st.header(":violet[CHOOSE YEAR]")
        option2 = st.selectbox(':violet[CHOOSE THE YEAR]',year)
        st.header(":violet[CHOOSE QUARTER]")
        option3 = st.selectbox(':violet[CHOOSE QUARTER OF THE YEAR]',quarter)
        quarter_option =int(option3[1])
        
    st.header(":violet[MAP REPRESENTATION]")        

    #***** INDIA MAP IN GRAPHICAL REPRESENTATION WITH DATA OF TRANSACTIONS AND USER******
    #if map_view:
    col4,col5 = st.columns(2)
    if option1 == "TRANSACTIONS":
        cur.execute(f"select States , sum(Transaction_count) as Total_Transactions, sum(Transaction_amount) as Total_amount from map_transaction where Year = {option2} and Quarter = {quarter_option} group by States order by States")
        df1 = pd.DataFrame(cur.fetchall(),columns= ['State', 'Total_Transactions', 'Total_amount'])
        df2 = pd.read_csv('C:/Users/mahes/OneDrive/Desktop/MY PRACTICE/state_names.csv')
        df1.State = df2
        with col4:
            # FOR TOTAL TRANSACTION AMOUNT MAP REPRESENTATION.
            fig = px.choropleth(df1,geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
                        featureidkey='properties.ST_NM',
                        locations='State',
                        color='Total_amount',
                        color_continuous_scale=px.colors.sequential.Viridis,
                        title="STATES AND TOTAL_TRANSACTION_AMOUNT MAP")

            fig.update_geos(fitbounds="locations", visible=False)

            st.plotly_chart(fig, use_container_width=True) 
            
            # FOR TOTAL TRANSACTION COUNT MAP REPRESENTATION.
            fig = px.choropleth(df1,geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
                        featureidkey='properties.ST_NM',
                        locations='State',
                        color='Total_Transactions',
                        color_continuous_scale=px.colors.sequential.Viridis,
                        title="STATES AND TOTAL_TRANSACTION_COUNT MAP")

            fig.update_geos(fitbounds="locations", visible=False)

            st.plotly_chart(fig, use_container_width=True)  
        with col5: 
            
            st.header(":violet[STATES]")
            state_name_list = df1.State.unique()
            option_state = st.selectbox(':violet[CHOOSE STATES]',state_name_list)
            total_transactions = df1.loc[df1['State'] == option_state, 'Total_Transactions'].item()
            total_amount = df1.loc[df1['State'] == option_state, 'Total_amount'].item()
            st.subheader(f'TRANSACTION DETAILS OF {option_state}')
            st.subheader("All PhonePe transactions (UPI + Cards + Wallets)")
            st.subheader(f'{total_transactions}')
            st.subheader("Total payment value")
            st.subheader(f'{total_amount}')
            exam =  df_aggregated_trans[(df_aggregated_trans['States'] == option_state)]
            df_agg = exam.groupby(['Transaction_type']).agg({'Transaction_amount':sum})
            df_agg.sort_values(by=['Transaction_type'],ascending=False)
            st.subheader(":violet[CATEGORIES]")
            st.dataframe(df_agg,use_container_width=True)
            
            
    if option1 == "USER":
        cur.execute(f"select States , sum(Registered_users) as Total_Users, sum(Appopens_count) as Total_App_Opens from map_user where Year = {option2} and Quarter = {quarter_option} group by States order by States")
        df3 = pd.DataFrame(cur.fetchall(),columns= ['State', 'Total_Users', 'Total_App_Opens'])
        df4 = pd.read_csv('C:/Users/mahes/OneDrive/Desktop/MY PRACTICE/state_names.csv')
        df3.State = df4
        with col4:
            # FOR TOTAL TRANSACTION AMOUNT MAP REPRESENTATION.
            fig = px.choropleth(df3,geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
                        featureidkey='properties.ST_NM',
                        locations='State',
                        color='Total_Users',
                        color_continuous_scale=px.colors.sequential.Viridis,
                        title="STATES AND TOTAL_USERS_COUNT MAP")

            fig.update_geos(fitbounds="locations", visible=False)

            st.plotly_chart(fig, use_container_width=True)  
            # FOR TOTAL TRANSACTION COUNT MAP REPRESENTATION.
            fig = px.choropleth(df3,geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
                        featureidkey='properties.ST_NM',
                        locations='State',
                        color='Total_App_Opens',
                        color_continuous_scale=px.colors.sequential.Viridis,
                        title="STATES AND TOTAL_APP_OPENS_COUNT MAP")

            fig.update_geos(fitbounds="locations", visible=False)

            st.plotly_chart(fig, use_container_width=True)  
    
        with col5:
            st.header(":violet[STATES]")
            state_name_list = df3.State.unique()
            option_state = st.selectbox(':violet[CHOOSE STATES]',state_name_list)
            total_users = df3.loc[df3['State'] == option_state, 'Total_Users'].item()
            total_appopens = df3.loc[df3['State'] == option_state, 'Total_App_Opens'].item()
            st.subheader(f'USER DETAILS OF {option_state}')
            st.subheader("Registered PhonePe users")
            st.subheader(f'{total_users}')
            st.subheader("PhonePe app opens")
            st.subheader(f'{total_appopens}')
 
# INSIGHTS TAB.            
if selected == "Insights":
    st.title(':violet[INSIGHTS]')
    questions = ["1.YEAR BASED EVALUATION OF PHONEPE TRANSACTIONS OF A STATE",
                 "2.YEAR BASED EVALUATION OF PHONEPE TRANSACTION AMOUNT OF A STATE",
                 "3.YEAR BASED EVALUATION OF PHONEPE USERS OF A STATE",
                 "4.BRANDS OF USERS APP ANALYSIS ",
                 "5.TOP 10 STATES OF TRANSACTIONS",
                 "6.TOP 10 STATES OF USERS",
                 "7.TOP 10 DISTRICTS OF TRANSACTIONS",
                 "8.TOP 10 PINCODES OF TRANSACTIONS",
                 "9.TOP 10 DISTRICTS OF USERS",
                 "10.TOP 10 PINCODES OF USERS"]
    option_ques = st.selectbox(':violet[CHOOSE THE FOLLOWING TO GET GRAPHICAL VIEW]',questions)
    
    ### CONDITIONAL STATEMENTS FOR CHOICE OF USER...###
    if option_ques == questions[0]:
        state_name_list = df_aggregated_trans.States.unique()
        option_state0 = st.selectbox(':violet[CHOOSE STATES]',state_name_list)
        ex1 = df_aggregated_trans[(df_aggregated_trans['States'] == option_state0)]
        fig1 = px.bar(ex1, x = 'Year', y = 'Transaction_count', color= 'Transaction_amount',title='PHONEPE TRANSACTIONS OF A STATE')
        st.plotly_chart(fig1,use_container_width=True)
    elif option_ques == questions[1]:
        state_name_list = df_aggregated_trans.States.unique()
        option_state1 = st.selectbox(':violet[CHOOSE STATES]',state_name_list)
        ex2 = df_aggregated_trans[(df_aggregated_trans['States'] == option_state1)]
        fig2 = px.bar(ex2, x = 'Year', y = 'Transaction_amount', color= 'Transaction_count',title='PHONEPE TRANSACTION AMOUNT OF A STATE')
        st.plotly_chart(fig2,use_container_width=True)    
    elif option_ques == questions[2]:
        state_name_list = df_aggregated_user.States.unique()
        option_state2 = st.selectbox(':violet[CHOOSE STATES]',state_name_list)
        ex3 = df_aggregated_user[(df_aggregated_user['States'] == option_state2)]
        fig3 = px.bar(ex3, x = 'Year', y = 'User_count', color= 'User_percentage',title='PHONEPE USERS OF A STATE')
        st.plotly_chart(fig3,use_container_width=True)
    elif option_ques == questions[3]:
        state_name_list = df_aggregated_user.States.unique()
        option_state3 = st.selectbox(':violet[CHOOSE STATES]',state_name_list)
        ex4 = df_aggregated_user[(df_aggregated_user['States'] == option_state3)]
        fig4 = px.pie(ex4,values='User_count',names='User_brand',title="BRANDS OF USERS APP ANALYSIS")
        st.plotly_chart(fig4)   
    elif option_ques == questions[4]:
        df_agg = df_aggregated_trans.groupby(['States']).agg({'Transaction_amount':sum})
        dff = df_agg.sort_values(by=['Transaction_amount'],ascending=False)
        ex5 = dff.head(10)
        st.subheader(':violet[TOP 10 TRANSACTIONS OF STATES OF PHONEPE]')
        st.dataframe(ex5, width=600, height=400)
        st.subheader(':violet[TOP 10 TRANSACTIONS OF STATES OF PHONEPE IN CHART REPRESENTATION]')
        fig5 = px.line(ex5, x=ex5.index, y=ex5.columns, title='TOP 10 STATES TRANSACTIONS OF PHONEPE')
        st.plotly_chart(fig5)
    elif option_ques == questions[5]:
        df_agg1 = df_aggregated_user.groupby(['States']).agg({'User_count':sum})
        dff1 = df_agg1.sort_values(by=['User_count'],ascending=False)
        ex6 = dff1.head(10)
        st.subheader(':violet[TOP 10 STATES OF USERS OF PHONEPE]')
        st.dataframe(ex6, width=600, height=400)  
        st.subheader(':violet[TOP 10 STATES OF USERS OF PHONEPE]')
        fig6 = px.line(ex6, x=ex6.index, y=ex6.columns, title='TOP 10 STATES OF USERS OF PHONEPE')
        st.plotly_chart(fig6)  
    elif option_ques == questions[6]:
        df_agg2 = df_top_trans_dis.groupby(['District']).agg({'Transaction_amount':sum}) 
        dff2 = df_agg2.sort_values(by=['Transaction_amount'],ascending=False)  
        ex7 = dff2.head(10)
        st.subheader(':violet[TOP 10 DISTRICTS OF TRANSACTIONS]') 
        st.dataframe(ex7, width=600, height=400)
        st.subheader(':violet[TOP 10 DISTRICTS OF TRANSACTIONS IN CHART REPRESENTATION]')
        fig7 = px.funnel(ex7, x=ex7.columns, y=ex7.index)
        st.plotly_chart(fig7)
    elif option_ques == questions[7]:
        df_agg3 = df_top_trans_pin.groupby(['Pincodes']).agg({'Transaction_amount':sum}) 
        dff3 = df_agg3.sort_values(by=['Transaction_amount'],ascending=False)  
        ex8 = dff3.head(10)
        st.subheader(':violet[TOP 10 PINCODES OF TRANSACTIONS]') 
        st.dataframe(ex8, width=600, height=400)
        st.subheader(':violet[TOP 10 PINCODES OF TRANSACTIONS IN CHART REPRESENTATION]')
        fig8 = px.funnel(ex8, x=ex8.columns, y=ex8.index)
        st.plotly_chart(fig8)
    elif option_ques == questions[8]:
        df_agg4 = df_top_user_dis.groupby(['District']).agg({'Registered_users':sum}) 
        dff4 = df_agg4.sort_values(by=['Registered_users'],ascending=False)  
        ex9 = dff4.head(10)
        st.subheader(':violet[TOP 10 DISTRICTS OF USERS]') 
        st.dataframe(ex9, width=600, height=400)    
        st.subheader(':violet[TOP 10 DISTRICTS OF USERS IN CHART REPRESENTATION]')
        fig9 = px.area(ex9, x=ex9.index, y=ex9.columns, color=ex9.index, line_group=ex9.index)
        st.plotly_chart(fig9)
    elif option_ques == questions[9]:
        df_agg5 = df_top_user_pin.groupby(['Pincodes']).agg({'Registered_users':sum}) 
        dff5 = df_agg5.sort_values(by=['Registered_users'],ascending=False)  
        ex10 = dff5.head(10)
        st.subheader(':violet[TOP 10 PINCODES OF USERS]') 
        st.dataframe(ex10, width=600, height=400)   
        st.subheader(':violet[TOP 10 PINCODES OF USERS IN CHART REPRESENTATION]')
        fig10 = px.area(ex10, x=ex10.index, y=ex10.columns, color=ex10.index, line_group=ex10.index)
        st.plotly_chart(fig10)
    else:
        st.write("CHOOSE AN CORRECT OPTION")         
        