import pytest
from main_code.api_interaction import ReservationApi

@pytest.fixture
def api():
    base_url = "https://magic-api-url.com"  # Remplazar la URL
    return ReservationApi(base_url)

def test_retrieve_existing_reservation(api):
    # Test retrieving an existing reservation
    reservation_id = "123"  # Replace with a valid reservation ID
    response = api.retrieve_reservation(reservation_id)
    assert response.status_code == 200

def test_retrieve_nonexistent_reservation(api):
    # Test retrieving a reservation that does not exist
    reservation_id = "999"  # Replace with a non-existing reservation ID
    response = api.retrieve_reservation(reservation_id)
    assert response.status_code == 404
