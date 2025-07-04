import pytest
from utils.test_helpers import assert_auth_response_structure
from client.endpoints.auth import AuthEndpoint
from utils.testdata import registration_cases, auth_login_cases
from utils.test_value_factory import get_test_value

@pytest.fixture
def auth_endpoint(client):
    """Фикстура для инициализации AuthEndpoint с клиентом."""
    return AuthEndpoint(client)

@pytest.mark.parametrize("email,password,age,expected_status_code", registration_cases)
def test_api_registration(auth_endpoint, email, password, age, expected_status_code, api_username):
    """Тест API регистрации пользователя."""
    email = get_test_value(email, api_username=api_username, api_password=None)
    password = get_test_value(password, api_username=api_username, api_password=None)
    age = get_test_value(age)
    
    # Вызов метода регистрации
    response = auth_endpoint.register(email, password, age)
    
    # Проверка кода состояния ответа
    assert response["status_code"] == expected_status_code, f"Expected status {expected_status_code} but got {response['status_code']}"
    
    # Проверка структуры ответа, если статус 200
    if expected_status_code == 200:
        assert_auth_response_structure(response, email, age)

@pytest.mark.parametrize("email,password,expected_status_code", auth_login_cases)
def test_api_login(auth_endpoint, api_username, api_password, email, password, expected_status_code):
    """Тест API входа пользователя."""
    # Замена значений на тестовые значения
    email = get_test_value(email, api_username=api_username, api_password=api_password)
    password = get_test_value(password, api_username=api_username, api_password=api_password)
    
    # Вызов метода входа
    response = auth_endpoint.login(email, password)
    
    # Проверка кода состояния ответа
    assert response["status_code"] == expected_status_code, f"Expected status {expected_status_code} but got {response['status_code']}"
    
    # Проверка структуры ответа, если статус 200
    if expected_status_code == 200:
        assert_auth_response_structure(response, email)