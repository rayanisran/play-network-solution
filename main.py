"""
Description: Main script that runs a scheduled task every 15 minutes to update MAC addresses.
Author: Rayan
Date Created: 2024-10-08
"""

import csv
import logging
import configparser
import requests
import schedule
import time

#######################################################################
# Configure logging
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    handlers=[logging.FileHandler("update_player.log")]
                    )

API_URL = "http://127.0.0.1:5000/profiles/clientId:{macaddress}"

# Load configuration from keys.conf
config = configparser.ConfigParser()
config.read('keys.conf')

CLIENT_ID = config['credentials']['CLIENT_ID']
AUTH_TOKEN = config['credentials']['AUTH_TOKEN']

SCHEDULED_DURATION = 15     # in minutes
DELAY = 0.01                # seconds
#######################################################################


def read_csv(file_path):
    """Read MAC addresses from a CSV file and return a list."""
    try:
        with open(file_path, mode='r') as csv_file:
            reader = csv.DictReader(csv_file)
            mac_addresses = [row['mac_addresses'] for row in reader]
            return mac_addresses
    except Exception as e:
        logging.error(f"Error reading CSV file: {e}")
        return []


def update_player(mac_address):
    """Send a PUT request to update a player with the given MAC address."""
    url = API_URL.format(macaddress=mac_address)
    headers = {
        "Content-Type": "application/json",
        "x-client-id": CLIENT_ID,
        "x-authentication-token": AUTH_TOKEN
    }
    data = {
        "profile": {
            "applications": [
                {"applicationId": "music_app", "version": "v1.4.11"},
                {"applicationId": "diagnostic_app", "version": "v1.2.7"},
                {"applicationId": "settings_app", "version": "v1.1.6"}
            ]
        }
    }

    try:
        response = requests.put(url, headers=headers, json=data)
        handle_response(response, mac_address)
        return response.status_code
    except requests.exceptions.RequestException as e:
        logging.error(f"Request failed for MAC: {mac_address} - {e}")
        return None


def handle_response(response, mac_address):
    """Handle the server response for the player update request."""
    if response.status_code == 200:
        logging.info(f"Successfully updated player with MAC: {mac_address}")
    elif response.status_code == 401:
        logging.error(f"Unauthorized (401) for MAC: {mac_address} - Invalid client ID or token")
    elif response.status_code == 404:
        logging.error(f"Not Found (404) for MAC: {mac_address} - Profile not found")
    elif response.status_code == 409:
        logging.error(f"Conflict (409) for MAC: {mac_address} - Profile update failed due to conflicting data")
    elif response.status_code == 500:
        logging.error(f"Internal Server Error (500) for MAC: {mac_address} - An error occurred on the server")
    else:
        logging.error(f"Failed to update MAC: {mac_address} - Status Code: {response.status_code}")


def main(csv_file_path):
    """Main function to process all MAC addresses in the CSV file."""
    mac_addresses = read_csv(csv_file_path)
    if not mac_addresses:
        logging.error("No MAC addresses found in the CSV file.")
        return

    for mac_address in mac_addresses:
        update_player(mac_address)
        time.sleep(DELAY) # rate limit


def job():
    """Scheduled job to run every 15 minutes."""
    csv_file_path = 'test_players.csv'
    logging.info("Running scheduled update job...")
    main(csv_file_path)


if __name__ == "__main__":
    logging.info("Starting scheduler...")
    job()
    while True:
        schedule.every(SCHEDULED_DURATION).minutes.do(job)
        schedule.run_pending()
        time.sleep(1)  # Wait for one second before checking again
