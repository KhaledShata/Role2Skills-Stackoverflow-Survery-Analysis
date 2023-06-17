import streamlit as st
import pickle
import plotly.express as px
import pandas as pd

@st.cache_data
def load_skills():
    file_path1 = 'skills.pkl'  # Path to the pickle file
    file_path2 = 'normalized_skills.pkl'  # Path to the pickle file

    with open(file_path1, 'rb') as file:
        skills = pickle.load(file)

    with open(file_path2 ,'rb') as file:
        normalized_skills = pickle.load(file)

    return skills , normalized_skills

@st.cache_data
def load_data():
    file_path = 'df.pkl'  # Path to the pickle file
    with open(file_path, 'rb') as file:
        df = pickle.load(file)
    return df



skills , normalized_skills = load_skills()
df = load_data()

def get_skills(role):
    single_role_skills = pd.concat([skills.loc[role], normalized_skills.loc[role]], axis=1)
    single_role_skills.columns = ['percentage', 'specificity']
    single_role_skills = single_role_skills.sort_values('percentage')
    threshold = 25
    single_role_skills = single_role_skills[single_role_skills['percentage'] > threshold]
    return single_role_skills

def run():
    st.markdown('<h1 class="title">Role2Skills</h1>', unsafe_allow_html=True)
    st.markdown('<h2 Based on Stackoverflow Developers  Survey</h2>', unsafe_allow_html=True)

    role = st.selectbox("Select Role :",
                       ['Data scientist or machine learning specialist', 'Academic researcher',
                             'Data or business analyst',
                             'Database administrator',
                             'Designer',
                             'DevOps specialist',
                             'Developer, QA or test',
                             'Developer, back-end',
                             'Developer, desktop or enterprise applications',
                             'Developer, embedded applications or devices',
                             'Developer, front-end',
                             'Developer, full-stack',
                             'Developer, game or graphics',
                             'Developer, mobile',
                             'Educator',
                             'Engineer, data',
                             'Engineer, site reliability',
                             'Engineering manager',
                             'Marketing or sales professional',
                             'Product manager',
                             'Scientist',
                             'Senior executive/VP',
                             'System administrator'])

    search_button = st.button("Go")
    if search_button:
        single_role_skills = get_skills(role)

        fig = px.bar(
            df,
            y=single_role_skills.index,
            x=single_role_skills["percentage"],
            color=single_role_skills["specificity"],
            color_continuous_scale="orrd",
            range_color=[normalized_skills.values.min(), normalized_skills.values.max()],
            orientation="h"
        )

        fig.update_layout(width=800, height=700, title=role)

        st.plotly_chart(fig)




run()
