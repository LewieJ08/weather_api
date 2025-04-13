# 🌦️ Weather API (with Redis Caching)

A Python Flask-based weather API that fetches weather data from the [Visual Crossing Weather API](https://www.visualcrossing.com/) and caches it using Redis. This project demonstrates 3rd-party API integration, Redis caching, rate limiting, and environment variable configuration.

## 📁 Project Structure
<pre>
WEATHER_API/ │ 
    ├── weather_api/│ 
        ├── init.py │ 
        ├── app.py # Flask app and route definitions │ 
        ├── cache.py # Redis caching logic │ 
        ├── weather.py # Weather API fetching logic │ 
        ├── .env # Environment variables (excluded by .gitignore) 
    ├── .gitignore 
    ├── README.md 
    ├── requirements.txt 
    ├── setup.py
</pre>

## 🚀 Features

- ✅ Fetches current weather data from Visual Crossing
- 🧠 Caches results using Redis to reduce API calls
- ⏱️ Built-in rate limiting with `Flask-Limiter`
- 🔐 Secure API credentials using environment variables
- 🧰 Simple setup and usage via `setup.py`

## 📦 Installation

### 1. Install Redis (if you don't already have it)
This app requires a Redis server running locally.

#### 🔹 🐧 Linux (Ubuntu/Debian)

```bash
sudo apt update
sudo apt install redis
sudo systemctl enable redis
sudo systemctl start redis
```

Verify it's working:
```bash
redis-cli ping
# → PONG
```

#### 🔹 🍎 macOS (with Homebrew)

```bash
brew install redis
brew services start redis
```
Verify it's working:
```bash
redis-cli ping
# → PONG
```

#### 🔹 🪟 Windows (via WSL)
Redis is not natively supported on Windows. It’s recommended to install Redis inside WSL (Windows Subsystem for Linux)

Inside WSL:

```bash
sudo apt update
sudo apt install redis
redis-server 
```
Verify it's working:
```bash
redis-cli ping
# → PONG
```
#### 💡 If you're using another method to run Redis on Windows (e.g., Docker or Redis Stack), make sure it's available on `localhost:6379`.

### 2. Install the Weather API App
After Redis is installed and running:

Clone and install locally:
```bash
git clone https://github.com/LewieJ08/weather_api.git
cd weather_api
pip install .
```

Start the API:
```bash
cd weather_api # ONLY if not in package location already
weather-api
```

## ⚙️ Environment Setup (Required)

To run this project, you'll need to create a `.env` file that includes your own [Visual Crossing Weather API](https://www.visualcrossing.com/weather-api) key and Redis connection settings.

### 🔑 Get Your Free API Key

1. Go to [Visual Crossing Weather API](https://www.visualcrossing.com/weather-api).
2. Sign up for a free account.
3. Once signed in, navigate to **Account** in the top right.
4. Copy your API key — you'll use it in the steps below.


#### 🐧 Linux / 🍎 macOS / 🪟 Windows (WSL):
```bash
cd weather_api #ONLY if not in package location already
cat > .env <<EOL
API_KEY = your_visual_crossing_api_key
REDIS_URL = redis://localhost:6379/0
EOL
```

Then open the .env file to replace your_visual_crossing_api_key with your real key:
```bash
nano .env
```

#### 🪟 Windows (PowerShell or CMD, NOT using WSL):
```bash
cd weather_app #ONLY if not in package location already
@"
API_KEY=your_visual_crossing_api_key
REDIS_URL=redis://localhost:6379/0
"@ | Out-File -FilePath .env -Encoding utf8
```
Then open the .env file to replace your_visual_crossing_api_key with your real key:
```bash
notepad .env
```

## 🔗 API Usage

Open this URL replacing LOCATION with a random location:
### http://127.0.0.1:5000/?location=LOCATION

## 🔒 Rate Limiting
To prevent abuse, this app uses Flask-Limiter for rate limiting. You can configure rate limits in the app code as needed. By defult this is set to **10 requests an hour**

## Roadmap.sh Project:
https://roadmap.sh/projects/weather-api-wrapper-service
