# IMDB Watchlist Movie Randomizer

A small Streamlit app that picks a random movie from an exported IMDB watchlist (CSV) and shows detailed information fetched from the OMDb API.

Live app: https://movie-randomizer.streamlit.app/

Features

- Loads a local `data.csv` (IMDB watchlist export).
- Picks a random movie from the list.
- Fetches movie details (poster, title, year, runtime, genre, plot, director, cast, awards, ratings) from the OMDb API.
- Displays an IMDB link to the original movie entry.

Prerequisites

- Python 3.8+
- An OMDb API key (get one at http://www.omdbapi.com/apikey.aspx).

Required files / environment

- `data.csv` — exported IMDB watchlist CSV placed in the project root.
- Environment variable `OMDb_API` — set this to your OMDb API key.

Installation

1. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv .venv
   source .venv/bin/activate    # macOS / Linux
   .venv\Scripts\activate       # Windows
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

Usage

1. Export your IMDB watchlist as CSV and save it as `data.csv` in the project root.
2. Set your OMDb API key in the environment:
   - macOS / Linux:

     ```bash
     export OMDb_API=your_api_key
     ```

   - Windows (PowerShell):

     ```powershell
     setx OMDb_API "your_api_key"
     ```

3. Run the app:

   ```bash
   streamlit run streamlit_app.py
   ```

Notes

- The app expects the CSV to include an IMDB identifier column named `Const` and a `URL` column.
- If OMDb returns "N/A" for fields, the app will skip displaying those fields.
- Network access is required to fetch posters and details from OMDb.

License

- MIT (or choose your preferred license)
