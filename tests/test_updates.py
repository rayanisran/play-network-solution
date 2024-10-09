#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Description: A list of unit tests to simulate every API response.
Author: Rayan
Date Created: 2024-10-08
"""

import unittest
from unittest.mock import patch
import requests
import os
import random
import csv
import logging
from main import update_player

TEST_MAC_ADDRESS = 'a1:bb:cc:dd:ee:ff'
# Configure logging for tests
logging.basicConfig(level=logging.INFO, format='%(message)s')  # Remove timestamp for test messages


def generate_test_csv(file_path, num_rows=1000):
    """Generate a CSV file with random MAC addresses and IDs."""
    with open(file_path, mode='w', newline='') as csv_file:
        fieldnames = ['mac_addresses', 'id1', 'id2', 'id3']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        writer.writeheader()
        for _ in range(num_rows):
            # Generate a random MAC address
            mac_address = ':'.join(['{:02x}'.format(random.randint(0, 255)) for _ in range(6)])
            # Generate random IDs
            id1 = random.randint(1, 100)
            id2 = random.randint(1, 100)
            id3 = random.randint(1, 100)

            writer.writerow({'mac_addresses': mac_address, 'id1': id1, 'id2': id2, 'id3': id3})


class TestUpdateMusicPlayers(unittest.TestCase):
    """Unit tests for the update_player function."""

    @classmethod
    def setUpClass(cls):
        """Set up the test CSV file before running tests."""
        cls.csv_file = 'test_players.csv'
        logging.info(f"Generating test CSV file at: {cls.csv_file}")
        generate_test_csv(cls.csv_file, num_rows=1000)

    # @classmethod
    # def tearDownClass(cls):
    #     """Clean up by removing the generated CSV file after running tests."""
    #     if os.path.exists(cls.csv_file):
    #         os.remove(cls.csv_file)
    #         logging.info(f"Cleaned up: Removed {cls.csv_file}")

    @patch('requests.put')
    def test_update_player_success(self, mock_put):
        """Test the update_player function for a successful response."""
        mock_put.return_value.status_code = 200
        response = update_player(TEST_MAC_ADDRESS)
        self.assertEqual(response, 200)
        logging.info("Test passed: update_player_success - Response was 200")

    @patch('requests.put')
    def test_unauthorized(self, mock_put):
        """Test the update_player function for an unauthorized response."""
        mock_put.return_value.status_code = 401
        response = update_player(TEST_MAC_ADDRESS)
        self.assertEqual(response, 401)
        logging.info("Test passed: update_player_unauthorized - Response was 401")

    @patch('requests.put')
    def test_not_found(self, mock_put):
        """Test the update_player function for a not found response."""
        mock_put.return_value.status_code = 404
        response = update_player('a1:bb:cc:dd:ee:ff')
        self.assertEqual(response, 404)
        logging.info("Test passed: update_player_not_found - Response was 404")

    @patch('requests.put')
    def test_server_error(self, mock_put):
        """Test the update_player function for a server error response."""
        mock_put.return_value.status_code = 500
        response = update_player(TEST_MAC_ADDRESS)
        self.assertEqual(response, 500)
        logging.info("Test passed: update_player_server_error - Response was 500")

    @patch('requests.put')
    def test_conflict(self, mock_put):
        """Test the update_player function for a conflict response."""
        mock_put.return_value.status_code = 409
        response = update_player(TEST_MAC_ADDRESS)
        self.assertEqual(response, 409)
        logging.info("Test passed: update_player_conflict - Response was 409")
        
        
if __name__ == '__main__':
    unittest.main()
