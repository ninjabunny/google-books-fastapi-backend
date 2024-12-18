from fastapi import FastAPI, HTTPException, Query
import requests
import os
from dotenv import load_dotenv
from fastapi.middleware.cors import CORSMiddleware


# Load environment variables from a .env file
load_dotenv()

app = FastAPI()

# Replace this with your actual Google Books API key
GOOGLE_BOOKS_API_KEY = os.getenv("GOOGLE_BOOKS_API_KEY")
GOOGLE_BOOKS_API_URL = "https://www.googleapis.com/books/v1/volumes"



@app.get("/books/")
async def search_books(
    query: str = Query(..., description="Search query for books"),
    max_results: int = Query(10, ge=1, le=40, description="Number of results to fetch (1-40)")
):
    """
    Search for books using the Google Books API.
    """
    params = {
        "q": query,
        "maxResults": max_results,
        "key": GOOGLE_BOOKS_API_KEY
    }

    try:
        response = requests.get(GOOGLE_BOOKS_API_URL, params=params)
        response.raise_for_status()  # Raise HTTPError for bad responses
        data = response.json()
    except requests.exceptions.RequestException as e:
        raise HTTPException(status_code=500, detail=f"Error fetching data from Google Books API: {str(e)}")

    return {
        "query": query,
        "results": data.get("items", [])
    }

@app.get("/book/{book_id}/")
async def get_book_details(book_id: str):
    """
    Get detailed information about a specific book by ID.
    """
    url = f"{GOOGLE_BOOKS_API_URL}/{book_id}"
    params = {"key": GOOGLE_BOOKS_API_KEY}

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()
    except requests.exceptions.RequestException as e:
        raise HTTPException(status_code=500, detail=f"Error fetching book details: {str(e)}")

    return data
