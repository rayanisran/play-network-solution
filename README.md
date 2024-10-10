# 🎶 Music Player Update Service

## 🚀 Quick User Guide

### Requirements

- **Python 3.x**
- Basic terminal usage.

### Installation

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/rayanisran/play-network-solution.git
   cd play-network-solution
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
WARNING: add this file to .gitignore.

### Prepare Player Profiles

- Create `test_players.csv` with MAC addresses, each on a new line (note that a default file already exists).

## 🛠️ Running the Service

1. **Start the Mock API**:

   ```bash
   python mock_api.py
   ```

You should observe the following if using the VS Code Terminal:

![Terminal output after running server](https://github.com/rayanisran/play-network-solution/blob/master/readme-pics/p-server.png?raw=true)


2. **Start the Update Script on another terminal window**:

   ```bash
   python main.py
   ```
Alternatively, if using Windows, run the `main.bat` script, which executes both command.

After handling a request, an output log containing the response of each request is generated in an `update_player.log.` file in the main directory.

## 🙋 Need Help?

For assistance, create an issue in the GitHub repository!
