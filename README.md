# 🇺🇸 Presidential Speeches NLP Analysis

## 📌 Project Overview

This project analyzes United States presidential inaugural speeches using Natural Language Processing (NLP) techniques.

The objective is to identify:
- recurring themes,
- sentiment evolution,
- important keywords,
- speech patterns over time.

The project was completed as part of a Data Visualization and NLP practical assignment.

---

# 📂 Project Structure

```bash
presidential-speeches-nlp-analysis/
│
├── data/
│   └── inaug_speeches.csv
│
├── notebooks/
│   └── analysis.ipynb
│
├── src/
│   ├── preprocessing.py
│   ├── sentiment_analysis.py
│   └── tfidf_analysis.py
│
├── visuals/
│   ├── sentiment_over_time.png
│   ├── wordcloud.png
│   ├── tfidf_barplot.png
│   └── ...
│
├── report/
│   └── rapport_analyse_discours.pdf
│
├── requirements.txt
└── README.md
```

---

# 📊 Dataset

Dataset used:
- Presidential inaugural speeches dataset from Kaggle

Source:
https://www.kaggle.com/datasets/adhok93/presidentialaddress

---

# 🛠 Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- NLTK
- spaCy
- Scikit-learn
- WordCloud
- VaderSentiment

---

# ⚙️ NLP Techniques Applied

## Data preprocessing
- Cleaning text
- Removing stopwords
- Tokenization
- Lemmatization

## Linguistic analysis
- POS tagging
- Named Entity Recognition (NER)

## Sentiment Analysis
- VaderSentiment polarity analysis

## TF-IDF Analysis
- Keyword extraction
- Important word identification

---

# 📈 Visualizations

The project includes several visualizations:
- Sentiment evolution over time
- Word frequency charts
- TF-IDF barplots
- Heatmaps
- Wordclouds
- Scatter plots
- Distribution plots

---

# 🔍 Key Insights

- Most speeches contain a positive or neutral tone.
- Themes related to freedom, nation, democracy, and people are highly recurrent.
- Speech length and tone evolve depending on historical periods.
- TF-IDF analysis highlights specific priorities for different presidents.

---

# 🚀 How to Run

## Install dependencies

```bash
pip install -r requirements.txt
```

## Launch Jupyter Notebook

```bash
jupyter notebook
```

Open:

```bash
notebooks/analysis.ipynb
```

---

# 👩‍💻 Author

Yasmine Ben Haj Salah

Master 2 Artificial Intelligence & Robotics
ENSEA Engineering School

---

# 📄 License

This project is for educational purposes only.