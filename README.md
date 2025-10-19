# 🎬 Netflix EDA Dashboard

An **interactive Exploratory Data Analysis (EDA)** web dashboard built using **Flask** and **Python**, designed to explore and visualize insights from the **Netflix Titles Dataset**.  
It allows users to interact with cleaned data, run predefined queries, and view summaries and charts directly from a web interface.

---

## 🚀 Features

- Interactive **Flask web dashboard** for dataset exploration  
- Preprocessed Netflix data (cleaned and genre-based views)  
- Query-based data retrieval and visualization  
- Clean UI built with HTML, CSS, and JavaScript  
- Modular project structure (easy to extend with new datasets or visuals)  

---

## 🧠 Dataset

**Source:** Netflix Titles Dataset  
Contains metadata about TV Shows and Movies available on Netflix, including:  
- Title, Director, Cast  
- Country, Release Year, Rating  
- Date Added, Type (Movie/TV Show)  
- Genre and Description  

**Files Used**
data/
├── raw/
│ └── netflix_titles.csv # Original dataset
└── processed/
├── netflix_clean.csv # Cleaned dataset after preprocessing
└── netflix_clean_genre.csv # Genre-based split dataset



---

## 🗂️ Project Structure

EDA-DASHBOARD/
│
├── app/
│ └── dashboard.py # Main Flask app (routes + logic)
│
├── data/
│ ├── raw/ # Original Netflix dataset
│ └── processed/ # Cleaned datasets used in dashboard
│
├── notebooks/
│ └── EDA dashboard.ipynb # Jupyter notebook for analysis
│
├── reports/
│ ├── Project Checklist EDA dashboard.docx # Report and checklist
│ └── to run this....png # Setup instructions image
│
├── requirements.txt # Python dependencies
├── README.md # Project documentation
└── .venv/ # Virtual environment 


## 🧩 Technologies Used

Python
Flask
Pandas
Matplotlib / Seaborn
HTML / CSS / JavaScript

## 📊 Example Visuals & Insights

Top genres and countries producing Netflix content
Yearly trend of movie and TV show releases
Ratings distribution across categories
Comparison of average durations by type

## 📘 Future Enhancements

Add search & filter options
Include user-uploaded datasets
Integrate Power BI or Plotly for richer visuals
Deploy on Render/Heroku
