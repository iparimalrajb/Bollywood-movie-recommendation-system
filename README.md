# 🎬 Bollywood Movie Recommendation System

An AI-powered movie recommendation system that suggests similar Bollywood movies based on **genre** and **actor similarity** using NLP techniques and cosine similarity.

**Live Demo:**  
👉 https://movierecommendation-project-mwazzqgh9xzclw5pdlagoe.streamlit.app/


---

## 🚀 Features

- 🎯 **Genre-Based Recommendations**
- 🎭 **Actor-Based Recommendations**
- 🔍 **Fuzzy Search** for better movie matching
- 🖼️ **Movie Posters** via TMDB API
- ⚡ **Fast & Optimized** using caching
- 🎨 Interactive UI built with Streamlit

---

## 🧠 How It Works

1. **Data Preprocessing**
   - Cleaned movie dataset (titles, genres, cast, ratings)
   - Converted text to lowercase and handled missing values

2. **Feature Engineering**
   - Separate TF-IDF vectorization for:
     - Genres
     - Cast

3. **Similarity Calculation**
   - Cosine similarity used to find similar movies
   - Two modes:
     - Genre similarity
     - Actor similarity

4. **Recommendation Logic**
   - Finds closest movie match using fuzzy search
   - Ranks movies based on similarity scores

5. **Poster Fetching**
   - Uses TMDB API to fetch movie posters dynamically

---

## 🛠️ Tech Stack

- **Python**
- **Pandas**
- **Scikit-learn**
- **Streamlit**
- **TMDB API**
- **Requests**

---

## 📂 Project Structure

├── app.py
├── finalmaster_dataset_movie_cleaned.csv
├── screenshots/
│   ├── home_page.jpg
│   ├── genere_based_recommendation.jpg
│   └── actor_based_recommendation.jpg
├── videos/
├── requirements.txt
├── .env
└── README.md
---

## ⚙️ Installation

1. Clone the repository

```bash
git clone https://github.com/iparimalrajb/Bollywood-movie-recommendation-model.git
cd Bollywood-movie-recommendation-model

2.	Install dependencies:

```bash
pip install -r requirements.txt

3.	Set TMDB API Key:

```bash
export TMDB_API_KEY="your_api_key"

4. Run the Streamlit app:

```bash
streamlit run app.py

## 🎯 Demo

## 🎥 Demo Video

Check the demo here: [View Demo Video](videos/demo_video.md

## Demo
	•	Enter a Bollywood movie name ( we have 3000+ movies in our dataset! like "3 Idiots", "Dangal", "Sholay", "Kabhi Khushi Kabhie Gham", "Lagaan", "Bajrangi Bhaijaan", "PK", "Sultan", "Dhoom 2", "Barfi!", "Queen", "Gully Boy")
	•	Choose recommendation type:
	•	Genre Based
	•	Actor Based
	•	Get top similar movies with posters 🎬


🔥 Future Improvements
	•	Hybrid recommendation system (Genre + Actor + Ratings)
	•	Add movie overview & description
	•	Deploy on Streamlit Cloud
	•	RAG-based conversational movie recommender
	•	User-based collaborative filtering
    •	Personalized recommendations based on user preferences

🤝 Contributing

Feel free to fork this repo and improve the system!
