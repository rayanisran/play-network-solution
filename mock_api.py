#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Description: Local server with Flask
Author: Rayan
Date Created: 2024-10-08
"""

from flask import Flask, request, jsonify
import random
import json

app = Flask(__name__)

# Load JSON responses from file
with open('responses.json') as f:
    responses = json.load(f)

# Mock API route to simulate player update
@app.route('/profiles/clientId:<mac_address>', methods=['PUT'])
def update_profile(mac_address):
    """Update the profile for a given MAC address."""

    client_id = request.headers.get('x-client-id')
    auth_token = request.headers.get('x-authentication-token')

    # Check if client_id is missing
    if not client_id:
        return jsonify(responses["unauthorized_missing_client_id"]), 401

    # Check if auth_token is missing
    if not auth_token:
        return jsonify(responses["unauthorized_missing_auth_token"]), 401

    # Check if MAC address matches "notfound" for simulation
    if mac_address.startswith("notfound"):
        return jsonify(responses["not_found"]), 404

    # Check if MAC address matches "conflict" for simulation
    if mac_address.startswith("conflict"):
        return jsonify(responses["conflict"]), 409

    # Randomly simulate a 500 Internal Server Error (e.g., 5% chance)
    if random.random() < 0.05:
        return jsonify(responses["internal_server_error"]), 500

    # Simulate successful update
    return jsonify(responses["successful_update"]), 200


if __name__ == '__main__':
    app.run(port=5000)
