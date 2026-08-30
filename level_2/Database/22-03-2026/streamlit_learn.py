import streamlit as st

st.set_page_config(page_title="Data Science  Dashboard",
                    page_icon=":guardsman:",
                      layout="centered",)


st.title("Data Science Dashboard")
st.subheader("This is a simple dashboard created using Streamlit for data science applications.")
st.write("You can use this dashboard to visualize data, create interactive plots, and perform data analysis tasks.")

tab1,tab2,tab3=st.tabs(["Data Visualization","Data Analysis","Machine Learning"])

with tab1:
    st.header("Data Visualization")
    st.write("In this section, you can create various types of plots and visualizations using your data.")
    st.write("You can upload your dataset and choose the type of plot you want to create.")
    col1,col2,col3=st.columns(3) # This will create the three columns for the data visualization section
    #  with col1:
    #     st.subheader("Upload Dataset")
    #     uploaded_file = st.file_uploader("Choose a CSV file", type="csv")
    #     if uploaded_file is not None:
    #         import pandas as pd
    #         df = pd.read_csv(uploaded_file)
    #         st.write("Dataset Preview:")
    #         st.dataframe(df.head())


    # with col2:

    #     st.subheader("Select Plot Type")
    #     plot_type = st.selectbox("Choose a plot type", ["Line Plot", "Bar Plot", "Scatter Plot", "Histogram"])
    #     if uploaded_file is not None:
    #         if plot_type == "Line Plot":
    #             st.line_chart(df)
    #         elif plot_type == "Bar Plot":
    #             st.bar_chart(df)
    #         elif plot_type == "Scatter Plot":
    #             st.write("Scatter plot requires two numerical columns. Please select them below.")
    #             numeric_columns = df.select_dtypes(include=['float64', 'int64']).columns.tolist()
    #             x_axis = st.selectbox("Select X-axis", numeric_columns)
    #             y_axis = st.selectbox("Select Y-axis", numeric_columns)
    #             st.write(f"Scatter plot of {x_axis} vs {y_axis}")
    #             st.scatter_chart(df[[x_axis, y_axis]])
    #         elif plot_type == "Histogram":
    #             st.write("Histogram requires one numerical column. Please select it below.")
    #             numeric_columns = df.select_dtypes(include=['float64', 'int64']).columns.tolist()
    #             hist_column = st.selectbox("Select Column for Histogram", numeric_columns)
    #             st.write(f"Histogram of {hist_column}")
    #             st.bar_chart(df[hist_column].value_counts())  


    with col1:
                    st.write("Left section (HOME)!")
                    st.button("Click Left Section Button", type="primary")
            
    with col2:
                    st.write("Centre section (HOME)!")
                    st.button("Click Centre Section Button", type="secondary")
            
    with col3:
                    st.write("Right section (HOME)!")
                    st.button("Click Right Section Button", type="tertiary")
           

with tab2:
    st.header("Data Analysis")
    st.write("In this section, you can perform various data analysis tasks such as data cleaning, feature engineering, and statistical analysis.")
    st.write("You can also use this section to explore your data and gain insights.")

with tab3:
    st.header("Machine Learning")
    st.write("In this section, you can build and evaluate machine learning models using your data.")
    st.write("You can choose from various algorithms and tune hyperparameters to improve model performance.")


st.divider() # This will create a horizontal line to separate the sections of the dashboard.

st.subheader("Level 3 - Widgets")

#Container --> It is like the div tag in HTML. It is used to group elements together and apply styles to them. It can also be used to create a layout for the dashboard.
with st.container(height=200, border=True):
    for i in range(100):
        st.write(f"Hello {i}")

#Input Widgets --> These are the interactive elements that allow users to input data or make selections. They can be used to create forms, filters, and other interactive features in the dashboard.

if st.button("Say Hello"):# button by efault vaue is False. When the button is clicked, it becomes True and the code inside the if statement is executed.
    st.write("Hello there!")

st.link_button("Streamlit Widget Page Redirect", url="https://docs.streamlit.io/develop/api-reference/widgets")

name = st.text_input("Enter your name") # text_input is used to take input from the user. It returns a string value.
print(name) # print is used to display the output in the console. It can take multiple arguments and display them in a formatted way.
st.write(f"Hello {name}!") # st.write is used to display the output on the dashboard. It can take multiple arguments and display them in a formatted way.

count = 0
if st.button("Click here to add 1 to the count"):
    count+=1
    st.write(f"Hello there!, the current count value is {count}")


u_name = st.text_input("User Name")
p_u_name = st.text_input("Password", type="password")
bio = st.text_area("Tell us about yourself", height=100)


st.subheader("Level 4 - Widgets")

import datetime
today = datetime.date.today()

picked_date = st.date_input("Pick a date", today)
st.write(picked_date)

st.divider()

#uploaded_file = st.file_uploader("Upload a csv", type=["csv", "txt"])

# from io import StringIO

# if uploaded_file is not None:
#     stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
#     # df = pd.read_csv(uploaded_file)
#     string_data = stringio.read()
    
#     st.write(f"{type(uploaded_file)}")
#     st.write(f"{type(string_data)}")

#     st.write(f"File Contents :")
#     st.code(string_data, language="text")
#     # st.write("File Uploaded!!")
#     st.success("File Uploaded!!")

# st.warning("File loading warning!")
# st.error("Error!")
# st.info("Here is a helpful tip!")




uploadedFile=st.file_uploader("Upload a File", type=["csv", "txt"])
from io import StringIO

if uploadedFile is not None:
    # To print what is present in the file
    st.write(f"{uploadedFile}")
    # Tocheck the type of the file
    st.write(f"{type(uploadedFile)}")
    stringio= StringIO(uploadedFile.getvalue().decode("utf-8")) ## This will convert the uploaded file into a string format
    stringData=stringio.read() ## This will read the string data from the uploaded file
    st.write(f"{type(stringData)}") # now the type of the string data is str
    st.write(f"File Contents :")
    st.code(stringData, language="text") ## This will display the string data in a code format
    st.success("File Uploaded!!  ")
    #st.write("File Uploaded!!  ")
    st.warning("File loading warning!")
    st.error("Error!")








#Understand Session State --> It is used to store the state of the application. It can be used to store variables, dataframes, and other objects that need to be accessed across different pages of the dashboard. It can also be used to store user inputs and selections.
# Instead of using global variables(pythonic vatiables), we can use session state to store the state of the application. This will help us to avoid the issues related to global variables and will also help us to maintain the state of the application across different pages of the dashboard.  
#session state is a dictionary-like object that can be used to store variables and their values. It can be accessed using the st.session_state object. The keys of the dictionary are the names of the variables and the values are the values of the variables. The session state is persistent across different pages of the dashboard and can be used to store user inputs and selections.


st.divider()

if 'count' not in st.session_state:
    st.session_state.count = 0

if st.button("Increment"):
    st.session_state.count += 1

st.write(st.session_state.count)

st.divider()

st.title("Main Title") # Large
st.header("Section Header") # Medium
st.subheader("Sub-section") # Small

st.markdown("We have **bold** in this statement.")

st.markdown("<h1 style='color: blue;'>Custom html</h1>", unsafe_allow_html=True)

st.divider()

st.subheader("Level 5 - Extra")

import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(10, 2), columns=['A', 'B'])
st.write("Streamlit Dataframe visualization")
st.dataframe(df)

st.write("Streamlit Dataframe barchart")
st.bar_chart(df)

# image
st.image(r"C:\Users\scl\Downloads\Downloads-Cleaned(13226)\wallpaper\wallhaven.png", caption="My Image", width=300)

st.divider()

import time
bar = st.progress(0)
for percent in range(100):
    time.sleep(0.1)
    bar.progress(percent + 1)

st.divider()

text_to_save = "1,2,3,4,5"
st.download_button(
    label="Download text file",
    data=text_to_save,
    file_name="dummy_csv.txt",
    mime="text/plain"
)