# 🎬 Bollywood Movie Recommendation System

An AI-powered movie recommendation system that suggests similar Bollywood movies based on **genre** and **actor similarity** using NLP techniques and cosine similarity.

---

## 🌐 Live Demo

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

### 1. Data Preprocessing
- Cleaned movie dataset (titles, genres, cast, ratings)
- Converted text to lowercase and handled missing values

### 2. Feature Engineering
- TF-IDF vectorization applied separately on:
  - Genres
  - Cast

### 3. Similarity Calculation
- Cosine similarity used to compute similarity scores
- Supports:
  - Genre similarity
  - Actor similarity

### 4. Recommendation Logic
- Uses fuzzy search to match closest movie title
- Returns Top-N similar movies based on similarity scores

### 5. Poster Fetching
- Fetches movie posters dynamically using TMDB API

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

```text
Bollywood-movie-recommendation-model/
│
├── app.py
├── finalmaster_dataset_movie_cleaned.csv
├── requirements.txt
├── .env
├── README.md
│
├── screenshots/
│   ├── home_page.jpg
│   ├── genere_based_recommendation.jpg
│   └── actor_based_recommendation.jpg
│
└── videos/
    └── demo_video.md
```
---

---

## ⚙️ Installation

### 1. Clone the repository
```bash
git clone https://github.com/iparimalrajb/Bollywood-movie-recommendation-model.git
cd Bollywood-movie-recommendation-model
```
### 2. Install dependencies
```bash
pip install -r requirements.txt
```
### 3. Set TMDB API Key
```bash
export TMDB_API_KEY="your_api_key"
```
### 4. Run the application
```bash
streamlit run app.py
```
---

🎥 Demo Video
👉 View Demo Video(videos/demo_video.md)￼

🎯 Usage
	•	Enter a Bollywood movie name (e.g., 3 Idiots, Dangal, Sholay, Lagaan, PK)
	•	Choose recommendation type:
	•	Genre Based
	•	Actor Based
	•	Get Top similar movie recommendations with posters 🎬

🔥 Future Improvements
	•	Hybrid recommendation system (Genre + Actor + Ratings)
	•	Add movie overview and descriptions
	•	RAG-based conversational recommender system
	•	User-based collaborative filtering
	•	Personalized recommendations based on user behavior

🤝 Contributing

Contributions are welcome!
Feel free to fork this repository and submit a pull request.
