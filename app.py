import streamlit as st
import os
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')
import seaborn as sns


def main():
    """ML Data Analysis"""
    st.title("ML Data Analysis")
    st.subheader('Machine Learning Analysis with Streamlit')

    def file_selector(folder_path='./Data'):
        filenames = os.listdir(folder_path)
        selected_filename = st.selectbox('Select A File',filenames)
        return os.path.join(folder_path,selected_filename)

    filename= file_selector()
    st.info('You Select {}'.format(filename))

    #Read the data
    df =pd.read_csv(filename)

    #Show the data
    if st.checkbox('Show DataSet'):
        number = st.number_input('Number of Rows to View',5,10)
        st.dataframe(df.head(number))

    #Show the columns
    if st.button('Column Name'):
        st.write(df.columns)

    #Showing the Shape
    if st.checkbox('Shape Of DataSet'):
        st.write(df.shape)
        data_dim = st.radio('Show Dimention By' , ('Rows','Columns'))
        if data_dim == 'Rows' :
         st.text('Number of Rows')
         st.write(df.shape[0])
        elif data_dim == 'Columns' :
         st.text('Number of Columns')
         st.write(df.shape[1])
        else :
         st.write(df.shape)

    #Selected Columns
    if st.checkbox('Select Columns To Show'):
        all_columns = df.columns.tolist()
        selected_columns = st.multiselect('Select',all_columns)
        new_df = df[selected_columns]
        st.dataframe(new_df)
    #Show Values
    if st.button('Value Count'):
        st.text('value Count By Target')
        st.write(df.iloc[  : , 1]).value.counts()

     #Show Data Types
    if st.button('Data Type'):
        st.write(df.dtypes)

    #Show Summary
    if st.checkbox('Summary'):
        st.write(df.describe().T)
    ##Plot and Vesulizaton
    st.subheader('Data Vesualizatoin ')




    #Seaborn Chart
    if st.checkbox('Correlation Plot with Sea born'):
        st.write(sns.heatmap(df.corr(),annot = True))
        st.pyplot()


    #Count Plot
    if st.checkbox('Plot Of Value Count '):
        st.text('Value Count By Target')
        all_columns_names = df.columns.tolist()
        primary_col = st.multiselect('Primary Column To GroupBy', all_columns_names)
        selected_columns_names = st.multiselect('Select Column', all_columns_names)
        if st.button ('Plot'):
            st.text ('Generate Plot')
            if selected_columns_names:
                vc_plot = df.groupby(primary_col)[selected_columns_names].count()
            else:
                vc_plot = df.iloc[:,1].value_counts()
            st.write(vc_plot.plot(kind='bar'))
            st.pyplot()







    #Count Plot
    #Pie Plot
    if st.checkbox('Pie Plot'):
        all_columns_names = df.columns.tolist()
        if st.button('Generate The Plot'):
            st.success('Generating A Pie Plot')
            st.write(df.iloc[:, 1].value_counts().plot.pie(autopct='%1.1f%%'))
            st.pyplot()



    #Customaization Plot

    st.subheader('Costomizable Plot')
    all_columns_names = df.columns.tolist()
    type_of_plot = st.selectbox ('Select Type of Plot',['area' , 'bar', 'line' , 'hist' , 'box','kde'])
    selected_columns_names = st.multiselect('Select Columns To Plot',all_columns_names)

    if st.button('Generate Plot'):
        st.success('Generating Customizable Plot of {} for {}'.format(type_of_plot,selected_columns_names))


        #Plot By Streamlit
        if type_of_plot == 'area':
            cust_data = df[selected_columns_names]
            st.area_chart(cust_data)


        elif type_of_plot == 'bar':
            cust_data = df[selected_columns_names]
            st.bar_chart(cust_data)

        elif type_of_plot == 'line':
            cust_data = df[selected_columns_names]
            st.line_chart(cust_data)

        #Custom Plot

        elif type_of_plot :
            cust_plot = df[selected_columns_names].plot(kind=type_of_plot)
            st.write(cust_plot)
            st.pyplot()

        st.button(' Thank You For Try .. Please if you like it SHARE IT :)')
        st.balloons()





if __name__ == '__main__':
    main()
