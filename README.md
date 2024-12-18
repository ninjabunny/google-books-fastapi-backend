# google-books-fastapi-backend
## Instructions
**REQUIREMENT**
You must create a `.env` file and insert the env var for google books API key like this:
`GOOGLE_BOOKS_API_KEY = "yourGoogleBooksAPIKeyHere"`

To start the server:
`python -m uvicorn main:app --reload`

It will start server here:
`http://127.0.0.1:8000`

Check if its working by using this URL:
`http://127.0.0.1:8000/books/?query=harry+potter&max_results=2`
It should return some JSON with 2 results about harry potter