"""Code to get trivia questions from an API."""
"""https://opentdb.com/api_config.php"""

import requests

API_URL = (
    "https://opentdb.com/api.php?amount=1&category=11&difficulty=easy&type=multiple"
)


def get_trivia_questions() -> list:
    """Get trivia questions from an API."""
    response = requests.get(API_URL)
    if response.status_code in (200, 201):
        return response.json()["results"]
    else:
        return []
