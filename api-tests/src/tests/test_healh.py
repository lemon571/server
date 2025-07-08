def test_api_available(client):
    """Тест на проверку доступности API."""
    
    # Выполнение запроса для проверки состояния API
    response = client.check_health()
    
    # Проверка кода состояния ответа
    assert response["status_code"] == 200, (
        f"Expected status code 200 but got {response['status_code']}"
    )
    
    # Проверка тела ответа
    body = response["body"]
    
    # Проверка статуса API
    assert body["status"] == "ok"
    
    # Проверка подключения к базе данных
    assert body["database"] == "connected"