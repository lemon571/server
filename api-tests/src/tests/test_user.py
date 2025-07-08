import pytest
from utils.test_helpers import assert_user_response_structure
from src.client.endpoints.user import UserEndpoint
from utils.testdata import user_name_cases
from utils.test_value_factory import get_test_value

@pytest.fixture
def user_endpoint(client):
    """Фикстура для инициализации UserEndpoint с клиентом."""
    return UserEndpoint(client)

@pytest.mark.parametrize("new_name,expected_status_code", user_name_cases)
def test_api_name(user_endpoint, api_username, api_password, new_name, expected_status_code):
    """Тест API на изменение имени пользователя."""
    # Получение тестового значения нового имени
    new_name = get_test_value(new_name, api_username=api_username)
    
    # Вызов метода для изменения имени
    response = user_endpoint.change_name(new_name, api_username, api_password)
   
    # Проверка кода статуса ответа
    assert response["status_code"] == expected_status_code, (
        f"Expected status code {expected_status_code} but got {response['status_code']} for new name '{new_name}'"
    )
    
    # Проверка ответа при успешном изменении имени
    if expected_status_code == 200:
        assert response["body"]["user"]["name"] == new_name, (
            f"Expected user name '{new_name}' but got '{response['body']['user']['name']}'"
        )
        
def test_api_user(user_endpoint, api_username, api_password):
    """Тест API на получение текущего пользователя."""
    # Вызов метода для получения текущего пользователя
    response = user_endpoint.get_current_user(api_username, api_password)
    
    # Проверка структуры ответа пользователя
    assert_user_response_structure(response, api_username)