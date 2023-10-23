import pytest
import requests
from src.api_module import get_trivia_questions, API_URL


def test_get_trivia_questions_mocked(mocker):
    mock_response = {
        "response_code": 0,
        "results": [
            {
                "category": "Entertainment: Film",
                "type": "multiple",
                "difficulty": "easy",
                "question": "This movie contains the quote, &quot;Nobody puts Baby in a corner.&quot;",
                "correct_answer": "Dirty Dancing",
                "incorrect_answers": [
                    "Three Men and a Baby",
                    "Ferris Bueller&#039;s Day Off",
                    "Pretty in Pink",
                ],
            }
        ],
    }
    mocker.patch(
        "src.api_module.requests.get"
    ).return_value.json.return_value = mock_response
    response = get_trivia_questions()
    requests.get.assert_called_once_with(API_URL)
    assert response == mock_response
