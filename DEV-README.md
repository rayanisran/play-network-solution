
# ♪ Music Player Update Service

Imagine you want to update the software of thousands of music players that are already in the field. A music player is composed of multiple components, each having its own version. This project is a Python-based solution designed to update these music players through an API running on a local Flask server. The project consists of three main components:

1. **`main.py`** – Handles the main logic of sending requests to a server to update music player profiles. Requests are scheduled every 15 minutes.
2. **`tests.py`** – Unit tests for the `update_player` function using the `unittest` framework.
3. **`mock_api.py`** – A mock API running on a local server that simulates the responses for the player profile updates, including success and error cases.

## Table of Contents

- [Quick Setup](#quick-setup)
- [Main Functionality](#main-functionality)
- [Running Tests](#running-tests)
- [Mock API Details](#mock-api-details)
- [Usage](#usage)
- [Contributing](#contributing)

## Quick Setup

### Requirements

- Python 3.x
- Libraries: flask, request, and unittest.

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com//rayanisran/play-network-solution.git
   cd play-network-solution
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Replace the placeholders in `keys.conf` with the client ID and authentication token:
```ini
CLIENT_ID = "your_client_id"
AUTH_TOKEN = "your_auth_token"
```

WARNING: add this file to .gitignore.

## Main Functionality

The `main.py` script is intended to run indefinitely. It runs a scheduled task every 15 minutes which:
 1. Reads a .csv containing player profiles, each of which is identified by its MAC address. These MAC Addresses are consolidated into a list.
 2. Pass each profile to an `update_player` function, which sends an HTTP PUT request to a local server with a predefined client ID and token. The function handles multiple response scenarios, returning various status codes (success, unauthorized, not found, conflict, server errors).


## Running Tests

The `tests.py` file contains unit tests to validate the behavior of `update_player` under all possible conditions. The conditions are listed in the `responses.json` file.

To run the tests:
   ```bash
   python -m unittest test_main.py
   ```

The output will comprise a series of test results,  each validating a unique condition of the `update_player` functionality.

## API Details

The `mock_api.py` contains a simple REST API using Flask, which handles PUT requests. It contains dummy conditions to check and return each response.

### Endpoints

- `PUT /profiles/clientId:<mac_address>` – Updates a profile with the given MAC address.

#### Example Request

```http
PUT /profiles/clientId:*a1:bb:cc:dd:ee:ff*
Headers:
  x-client-id: <client-id>
  x-authentication-token: <auth-token>
```

#### Possible Responses

- **200 OK**: Profile update success
- **401 Unauthorized**: Missing or invalid `clientId` or `auth-token`
- **404 Not Found**: Player profile not found
- **409 Conflict**: Profile conflict error
- **500 Internal Server Error**: Internal server error

###  Adding New Responses

All responses must be listed in the `responses.json` file. To add a new response, create a new entry in the JSON object with `statusCode`, `error`, and `message` attributes. Then, change the `update_profile` function in `mock_api.py` to include a condition that checks for your response and return a message and code accordingly.

```python
    "random_error": {
        "statusCode": 512,
        "error": "Random Error",
        "message": "Information about the error goes here."
    }
```

Remember to include a test case in `tests.py` to validate the status code of the response:

```python
    @patch('requests.put')
    def test_random_error(self, mock_put):
        """Test the update_player function for a random error."""
        mock_put.return_value.status_code = 512
        response = update_player(TEST_MAC_ADDRESS)
        self.assertEqual(response, 512)
        logging.info("Test passed: test_random_error - Response was 512")
```

## Contributing

Feel free to fork this project, create an issue, or submit pull requests to improve the functionality or add new features.
