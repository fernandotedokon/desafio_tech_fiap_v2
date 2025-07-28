# app/main.py

from fastapi import FastAPI, HTTPException, Query
from app.scraper import extract_books
from app.models import Book
from app.utils import load_books, get_book_by_id, search_books, get_categories
import os

app = FastAPI(title="Biblioteca API", version="1.0")

@app.get("/api/v1/extrair/{pages}")
def extrair_e_salvar(pages: int):
    try:
        if (pages >= 0 and pages <= 5) or pages == 50:
            extract_books(pages=pages)
            df = load_books()
            return {"status": "ok", "books_count": len(df)}
        else:
            raise HTTPException(status_code=400, detail="Número de páginas deve ser entre 1 e 5 ou 50 para extrair todas as paginas")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/api/v1/health")
def health_check():
    try:
        df = load_books()
        return {"status": "ok", "books_count": len(df)}
    except Exception as e:
        raise HTTPException(status_code=500, detail="Erro ao carregar dados")

@app.get("/api/v1/books", response_model=list[Book])
def list_books():
    df = load_books()
    return df.to_dict(orient="records")

@app.get("/api/v1/books/{book_id}", response_model=Book)
def get_book(book_id: int):
    book = get_book_by_id(book_id)
    if not book:
        raise HTTPException(status_code=404, detail="Livro não encontrado")
    return book

@app.get("/api/v1/books/search", response_model=list[Book])
def search(title: str = Query(default=None), category: str = Query(default=None)):
    results = search_books(title=title, category=category)
    return results

@app.get("/api/v1/categories")
def categories():
    return get_categories()
