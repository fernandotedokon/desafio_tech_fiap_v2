# app/utils.py

import pandas as pd
import os

DATA_DIR = "data"
CSV_PATH = os.path.join(DATA_DIR, "books.csv")


def load_books():
    return pd.read_csv(CSV_PATH)

def get_book_by_id(book_id: int):
    df = load_books()
    book = df[df["id"] == book_id]
    return book.to_dict(orient="records")[0] if not book.empty else None

def search_books(title: str = None, category: str = None):
    df = load_books()
    if title:
        df = df[df["title"].str.contains(title, case=False, na=False)]
    if category:
        df = df[df["category"].str.contains(category, case=False, na=False)]
    return df.to_dict(orient="records")

def get_categories():
    df = load_books()
    return sorted(df["category"].dropna().unique().tolist())
