from main_code.api_interaction import ReservationApi

def main():
    base_url = "https://magic-api-url.com"  # Cambiar la URL a la api real

    # Initialize the ReservationApi with the base URL
    api = ReservationApi(base_url)

    # Example payload for creating a reservation
    create_payload = {
        "carId": "123",
        "startDate": "2023-08-15",
        "endDate": "2023-08-20",
        "customerName": "John Doe"
    }

    # Create a reservation using the API
    create_response = api.create_reservation(create_payload)
    print("Create Reservation Response:", create_response.status_code)

    # Example reservation ID for retrieval and deletion
    reservation_id = "123"  # Replace with a valid reservation ID

    # Retrieve the reservation using the API
    retrieve_response = api.retrieve_reservation(reservation_id)
    print("Retrieve Reservation Response:", retrieve_response.status_code)

    # Delete the reservation using the API
    delete_response = api.delete_reservation(reservation_id)
    print("Delete Reservation Response:", delete_response.status_code)

if __name__ == "__main__":
    main()
