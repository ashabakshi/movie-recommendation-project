# 🎬 HopeMatch — Movie Recommender

[![Live Demo](https://img.shields.io/badge/Live_Demo-Streamlit_App-ff4b4b?style=for-the-badge&logo=streamlit)](https://movie-recommendation-project-by-asha.streamlit.app)
[![Python](https://img.shields.io/badge/Python-3.11-blue?style=for-the-badge&logo=python)](#)
[![FastAPI](https://img.shields.io/badge/FastAPI-Backend-009688?style=for-the-badge&logo=fastapi)](#)

HopeMatch is a fully responsive, modern Full-Stack Movie Recommendation System. It combines the power of Machine Learning (TF-IDF content-based filtering) with real-time data from the TMDB API to provide incredibly accurate and visually stunning movie recommendations.

---

## ✨ Features

- **Personalized Recommendations:** Get tailored movie recommendations based on content similarity (TF-IDF + Cosine Similarity).
- **Genre-Based Discovery:** Explore similar movies based on TMDB genre data.
- **Real-Time TMDB Integration:** Fetches up-to-date movie posters, ratings, cast, and overview.
- **Trending & Popular Sections:** Discover what's hot today, top-rated movies, and upcoming releases.
- **High-Performance API:** Lightning-fast backend powered by FastAPI.
- **Premium UI/UX:** A stunning, responsive glassmorphism interface built with Streamlit.

## 🛠️ Tech Stack

- **Frontend:** Streamlit
- **Backend API:** FastAPI & Uvicorn
- **Machine Learning:** Scikit-Learn, Pandas, NumPy
- **Data Source:** [The Movie Database (TMDB) API](https://developer.themoviedb.org/docs)
- **Deployment:** 
  - Frontend hosted on **Streamlit Community Cloud**
  - Backend hosted on **Render**

---

## 🚀 Live Demo

Check out the live web application here:  
👉 **[HopeMatch Movie Recommender](https://movie-recommendation-project-by-asha.streamlit.app)**

---

## 💻 Local Setup & Installation

If you'd like to run this project locally on your machine, follow these steps:

### 1. Clone the Repository
```bash
git clone https://github.com/ashabakshi/movie-recommendation-project.git
cd movie-recommendation-project
```

### 2. Create a Virtual Environment & Install Dependencies
We highly recommend using `uv` or `pip` to install the requirements.
```bash
python -m venv .venv
# Activate on Windows:
.\.venv\Scripts\Activate.ps1
# Activate on Mac/Linux:
source .venv/bin/activate

pip install -r requirements.txt
```

### 3. Setup Environment Variables
Create a `.env` file in the root directory and add your TMDB API Key:
```env
TMDB_API_KEY=your_api_key_here
```

### 4. Run the Backend (FastAPI)
Start the Uvicorn server to serve the API locally.
```bash
uvicorn main:app --reload
```
*The API will be available at `http://127.0.0.1:8000` (Visit `/docs` for Swagger UI).*

### 5. Run the Frontend (Streamlit)
Open a **new terminal window**, activate your virtual environment, and run the Streamlit app.
```bash
streamlit run app.py
```
*The app automatically detects if the local backend is running and connects to it. Otherwise, it falls back to the live Render backend!*

---

## 📂 Project Structure

```text
📁 movie-recommendation-project
 ┣ 📄 app.py               # Streamlit Frontend application
 ┣ 📄 main.py              # FastAPI Backend API server
 ┣ 📄 requirements.txt     # Python dependencies
 ┣ 📄 .env                 # Environment variables (Ignored in Git)
 ┣ 📄 df.pkl               # Pickled Pandas DataFrame of movies
 ┣ 📄 indices.pkl          # Pickled dictionary of movie indices
 ┣ 📄 tfidf.pkl            # Pickled Scikit-Learn TF-IDF Vectorizer
 ┗ 📄 tfidf_matrix.pkl     # Pickled sparse TF-IDF matrix
```

## 🤝 Contributing
Contributions, issues, and feature requests are welcome! Feel free to check the [issues page](https://github.com/ashabakshi/movie-recommendation-project/issues).

---
*Created with ❤️ by Asha Bakshi.*
