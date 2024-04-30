# Stack Overflow Developers Survey Analysis

## Project Overview
This project explores the dynamic relationship between various IT jobs and the technologies associated with them. Aimed at helping anyone struggling to understand the evolving IT landscape, it provides data-driven insights into which skills are necessary for specific job roles. This is particularly useful for students who are uncertain about the technologies they should learn for different IT careers.

## Problem Statement
With the IT sector rapidly evolving, students frequently face confusion about necessary skills for various IT jobs. Common questions include:
- "Do I need to learn C++ to be a Data Scientist?"
- "Do DevOps and System admins use the same technologies?"
- "I really like JavaScript; can I use it in Data Analytics?"

My solution aims to demystify these questions through a detailed analysis of the Stack Overflow Developer Survey, identifying key relationships between job roles and required technologies.

## Data Source
The dataset used in this project is derived from the Stack Overflow Developer Survey. It includes responses from thousands of IT professionals and developers, detailing their job roles, technologies used, and other professional metrics.

## Methodology
The methodology encompassed a comprehensive approach to data handling and analysis. Initially, I performed data preprocessing which involved cleaning the data and addressing missing values to ensure consistency and accuracy. Then conducted an exploratory data analysis (EDA) to visualize how various technologies are distributed among different IT job titles, which provided foundational insights for further analysis. Building on this, I applied clustering techniques to identify and group job roles based on similar technology stacks, allowing to pinpoint distinct skill sets associated with specific career paths. Finally, I developed a Logistic Regression model that achieved a high accuracy of 93%, enabling users to input their skills and receive tailored job role recommendations. This model was subsequently deployed via Streamlit, offering an interactive tool for users to explore potential career directions based on their technological expertise.



## Tools Used
- Python for data analysis and model development.
- Libraries: Pandas, NumPy, Scikit-Learn,PyTorch, Matplotlib, Seaborn.
- Streamlit for deploying the interactive web application.

Feel free to try the model from here: https://khaledatef00-stackoverflow-survery-analysis-app-ngoqc8.streamlit.app/

## Example of Running the Model:
![Screenshot from 2024-03-22 05-42-59](https://github.com/KhaledAtef00/Stackoverflow-Survery-Analysis/assets/105244576/48d5b00c-fe31-4f55-adb0-42d3740834db)
**________________________________________________________________________________________________**

![Screenshot from 2024-03-22 05-42-40](https://github.com/KhaledAtef00/Stackoverflow-Survery-Analysis/assets/105244576/3b185d17-3b36-4ad7-80dc-1a4f0d2b720e)
**________________________________________________________________________________________________**


![Screenshot from 2024-03-22 05-43-39](https://github.com/KhaledAtef00/Stackoverflow-Survery-Analysis/assets/105244576/d2cb16c5-3e47-4002-9a30-8d192d251c8b)
