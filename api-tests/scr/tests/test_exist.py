import pytest
from utils.testdata import exist_cases
from utils.test_value_factory import get_test_value

@pytest.fixture
def shock_endpoint(client):
    """Фикстура для предоставления клиентского эндпоинта."""
    return client

@pytest.mark.parametrize("email,expected_exist,expected_status_code", exist_cases)
def test_api_exist(shock_endpoint, api_username, email, expected_exist, expected_status_code):
    test_email = get_test_value(email, api_username=api_username)
    
    # Вызов метода для проверки существования
    response = shock_endpoint.check_exist(test_email)
    
    # Проверка кода состояния ответа
    assert response["status_code"] == expected_status_code, (
        f"Expected status {expected_status_code} for email '{test_email}' but got {response['status_code']}"
    )
    
    # Проверка наличия пользователя в ответе, если статус 200
    if expected_status_code == 200:
        assert response["body"]["exist"] == expected_exist, (
            f"Expected exist value {expected_exist} for email '{test_email}' but got {response['body']['exist']}"
        )