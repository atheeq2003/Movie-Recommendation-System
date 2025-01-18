# 🎬 Movie Recommendation System

A Movie recommendation system built using Streamlit. The application suggests movies based on user input by leveraging similarity measures between movies. Used content-based filtering and cosine similarity in Python with Streamlit for an interactive UI.

---

## 🌐Deployed App

[➡️ ](https://atheeq2003-movie-recommender.streamlit.app/)**Explore the Deployed App Here**

---

## ✨ Features

* 🎥 Recommends movies similar to the one selected by the user.
* 🖼️ Displays posters of recommended movies.
* 💻 Interactive and user-friendly UI built with Streamlit.

---

## ⚙️ Installation

To run the project locally, follow these steps:

1. **📂 Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/movie-recommender.git
   cd movie-recommender
   ```
2. **💻 Set up a virtual environment (optional but recommended): Can use Pycharm instead**
   ```bash
   python -m venv venv
   # Activate the virtual environment
   # For Windows:
   .\venv\Scripts\activate
   # For macOS/Linux:
   source venv/bin/activate
   ```
3. **📦 Install the required dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
4. **📝 Generate the `movie_dict.pkl` file:**
   Open the provided Jupyter Notebook (`generate_movie_data.ipynb`) in your preferred editor and run all cells to generate the `movie_dict.pkl` and `similarity.pkl` files. Place these files in the root directory of the project.
5. **🚀 Run the application:**
   ```bash
   streamlit run app.py
   ```
6. **🌍 Access the app:**
   Open your browser and navigate to `http://localhost:8501`.

---

## 📋 Requirements

* 🐍 Python 3.8 or later
* Streamlit
* Pandas
* Requests
* Scikit-learn

(Dependencies are listed in `requirements.txt`.)

---

## 🛠️ Usage

1. 🎞️ Select a movie from the dropdown menu.
2. 🎯 Click on the "Recommend" button.
3. 🖼️ View the top 5 similar movies along with their posters.

---

## 📁 Folder Structure

```
movie-recommender/
├── app.py                  # Main application file
├── generate_movie_data.ipynb # Jupyter Notebook to generate .pkl files
├── movie_dict.pkl          # Preprocessed movie data (generated)
├── similarity.pkl          # Precomputed similarity matrix (generated)
├── requirements.txt        # Python dependencies
└── README.md               # Project documentation
```

---

## 🤝 Contributing

Contributions are welcome! If you'd like to improve this project, feel free to fork the repository and submit a pull request.

---

## 📜 License

This project is licensed under the MIT License.
