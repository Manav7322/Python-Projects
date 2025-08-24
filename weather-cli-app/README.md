# 🌦️ Weather CLI App

A simple **Command-Line Interface (CLI)** tool built in Python to fetch and display weather forecasts using the [OpenWeatherMap API](https://openweathermap.org/).  
The app also saves forecast data into a CSV file for further analysis.

---

## 📖 Features
- Fetch **current weather forecast** for any city.
- Display the **next 5 time intervals** (3-hourly data).
- Save full forecast into a **CSV file**.
- CLI-friendly using **argparse**.
- Beginner-friendly and extendable project.

---

## ⚙️ Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/Manav7322/Python-Projects/weather-cli-app.git
   cd weather-cli-app
   ```

2. Install dependencies:
   ```bash
   pip install requests pandas
   ```

3. Get a free API key from [OpenWeatherMap](https://openweathermap.org/api).

4. Add your API key inside the script:
   ```python
   API_KEY = "your_api_key_here"
   ```

---

## 🚀 Usage

Run the script from the terminal:

```bash
python weather.py --city London
```

### Example Output:
```
2025-08-23 12:00:00  25°C  clear sky
2025-08-23 15:00:00  26°C  scattered clouds
2025-08-23 18:00:00  24°C  light rain
2025-08-23 21:00:00  22°C  broken clouds
2025-08-24 00:00:00  21°C  clear sky
```

➡️ Full forecast saved into:
```
forecast.csv
```

---

## 📂 Example forecast.csv
| datetime            | temp | description       |
|---------------------|------|------------------|
| 2025-08-23 12:00:00 | 25   | clear sky        |
| 2025-08-23 15:00:00 | 26   | scattered clouds |
| 2025-08-23 18:00:00 | 24   | light rain       |

---

## 🔧 Arguments

| Argument  | Description                     | Example Usage                  |
|-----------|---------------------------------|--------------------------------|
| `--city`  | City name to fetch weather for | `python weather.py --city Delhi` |

---

## 📌 Next Steps (Ideas to Extend)
- Add `--days` argument (limit forecast days).
- Add `--units` argument (metric / imperial).
- Add support for multiple cities at once.
- Export data to **Excel (XLSX)** instead of CSV.

---

## 🧑‍💻 Tech Stack
- **Python 3**
- **Requests** (API calls)
- **Pandas** (data handling)
- **Argparse** (CLI support)

---
