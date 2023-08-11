import pytest
from main_code.api_interaction import ReservationApi

@pytest.fixture
def api():
    base_url = "https://magic-api-url.com"  # Cambiar la URL
    return ReservationApi(base_url)

def test_create_reservation(api):
    # Test creating a reservation with valid payload
    payload = {
        "carId": "123",
        "startDate": "2023-08-15",
        "endDate": "2023-08-20",
        "customerName": "John Doe"
    }
    response = api.create_reservation(payload)
    assert response.status_code == 201

def test_create_reservation_same_dates(api):
    # Test creating a reservation with same start and end dates
    payload = {
        "carId": "123",
        "startDate": "2023-08-15",
        "endDate": "2023-08-15",
        "customerName": "Jane Smith"
    }
    response = api.create_reservation(payload)
    assert response.status_code == 201

def test_create_reservation_long_customer_name(api):
    # Test creating a reservation with a customer name exceeding 30 characters
    payload = {
        "carId": "123",
        "startDate": "2023-08-15",
        "endDate": "2023-08-20",
        "customerName": "ThisIsALongCustomerNameThatExceedsThirtyCharacters"
    }
    response = api.create_reservation(payload)
    assert response.status_code == 201

def test_create_reservation_missing_car_id(api):
    # Test creating a reservation without the carId field
    payload = {
        "startDate": "2023-08-15",
        "endDate": "2023-08-20",
        "customerName": "John Doe"
    }
    response = api.create_reservation(payload)
    assert response.status_code == 400

def test_create_reservation_end_date_before_start_date(api):
    # Test creating a reservation with end date before start date
    payload = {
        "carId": "123",
        "startDate": "2023-08-20",
        "endDate": "2023-08-15",
        "customerName": "John Doe"
    }
    response = api.create_reservation(payload)
    assert response.status_code == 400
