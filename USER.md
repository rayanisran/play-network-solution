# 🎶 Music Player Update Service

## 🚀 Quick User Guide

### Requirements

- **Python 3.x**
- Basic terminal usage.

### Installation

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/yourrepo/music-player-update-service.git
   cd music-player-update-service
   ```

2. **Install Dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

3. **Configure Your API Keys**:

   Edit the `keys.conf` file with:

   ```ini
   CLIENT_ID = "your_client_id"
   AUTH_TOKEN = "your_auth_token"
   ```

### Prepare Player Profiles

- Create `test_players.csv` with MAC addresses, each on a new line (note that a default already exists).

## 🛠️ Running the Service

1. **Start the Mock API**:

   ```bash
   python mock_api.py
   ```

2. **Start the Update Script**:

   ```bash
   python main.py
   ```
Alternatively, run the `main.bat` script, which executes both command.

An output log containing the response of each request is listed in `update_player.log.`

## 🙋 Need Help?

For assistance, create an issue in the GitHub repository.
