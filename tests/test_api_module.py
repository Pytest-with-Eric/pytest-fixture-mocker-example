import pytest
import requests
from src.api_module import get_trivia_questions


def test_get_trivia_questions():
    response = get_trivia_questions()
    print(response)


def test_get_trivia_questions_mocked(mocker):
    mock_response = [
        {
            "category": "Entertainment: Film",
            "type": "multiple",
            "difficulty": "easy",
            "question": "What was the first James Bond film?",
            "correct_answer": "Dr. No",
            "incorrect_answers": ["Goldfinger", "From Russia With Love", "Thunderball"],
        }
    ]
    mocker.patch(
        "src.api_module.requests.get"
    ).return_value.json.return_value = mock_response

    response = get_trivia_questions()
    # requests.get.assert_called_once_with("https://opentdb.com/api.php")  #
    assert response == mock_response
