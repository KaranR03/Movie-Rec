# Movie Recommender

A content-based movie recommender. Pick a film you like and it suggests five similar ones, each with its poster and a short description.

**[Try the live app](https://movie-rec-wklvwq59ehekkeoqzcdsct.streamlit.app/)**

## How it works

1. Each movie in the [TMDB](https://www.themoviedb.org/) dataset is turned into a vector from its metadata.
2. Cosine similarity between those vectors gives a score for every pair of movies. The scores are stored as a reduced sparse matrix (`similarity_sparse_reduced.npz`) so the app stays small and fast.
3. When you choose a movie, the app takes the five highest-scoring neighbours and fetches their poster and overview from the TMDB API.

The full workings, from data cleaning to the similarity matrix, are in [`movie-recommender-system.ipynb`](movie-recommender-system.ipynb).

## Run it yourself

You need a free [TMDB API key](https://www.themoviedb.org/settings/api).

```bash
git clone https://github.com/KaranR03/Movie-Rec.git
cd Movie-Rec
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
export TMDB_API_KEY="your-key-here"
streamlit run app.py
```

On Streamlit Cloud, add `TMDB_API_KEY` under **Settings → Secrets** instead.

## Built with

Python · Streamlit · pandas · SciPy · TMDB API

## Licence

[MIT](LICENSE)
