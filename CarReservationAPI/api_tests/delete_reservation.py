import pytest
from main_code.api_interaction import ReservationApi

@pytest.fixture
def api():
    base_url = "https://magic-api-url.com"  # Remplazr ccon la URL
    return ReservationApi(base_url)

def test_delete_existing_reservation(api):
    # Test deleting an existing reservation
    reservation_id = "123"  # Replace with a valid reservation ID
    response = api.delete_reservation(reservation_id)
    assert response.status_code == 204

    # Check if the reservation is actually deleted (expecting a 404)
    response_after_delete = api.retrieve_reservation(reservation_id)
    assert response_after_delete.status_code == 404

def test_delete_nonexistent_reservation(api):
    # Test deleting a reservation that does not exist
    reservation_id = "999"  # Replace with a non-existing reservation ID
    response = api.delete_reservation(reservation_id)
    assert response.status_code == 400