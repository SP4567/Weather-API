## 🌦️ Weather Information System

**FastAPI + Streamlit + RapidAPI**

A full-stack weather application that provides **current weather details**, **latitude**, and **longitude** for a given city.
The backend is built using **FastAPI**, and the frontend is built using **Streamlit**.
Weather data is fetched from **WeatherAPI via RapidAPI**.

---

## 📌 Features

* 🌍 Search weather by **city name**
* 🌡️ Displays **current temperature**
* 🧭 Shows **latitude & longitude**
* 🔁 Supports **JSON and XML output formats**
* 🔐 Secure API key handling (backend only)
* 🖥️ Clean Streamlit UI
* 🚀 FastAPI backend with proper error handling

---

## 🏗️ Architecture

```
Streamlit UI  →  FastAPI Backend  →  RapidAPI WeatherAPI
```

* **Streamlit** handles user input and display
* **FastAPI** processes requests and formats responses
* **RapidAPI WeatherAPI** provides real-time weather data

---

## 📁 Project Structure

```
weather-app/
│
├── main.py          # FastAPI backend
├── app.py           # Streamlit frontend
├── README.md        # Project documentation
└── requirements.txt # Dependencies
```

---

## ⚙️ Prerequisites

* Python **3.9+**
* RapidAPI account
* WeatherAPI subscription on RapidAPI

---

## 🔑 Get RapidAPI Key

1. Sign up at **[https://rapidapi.com](https://rapidapi.com)**
2. Subscribe to **WeatherAPI**
3. Copy your **RapidAPI Key**

---

## 📦 Installation

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/weather-app.git
cd weather-app
```

### 2️⃣ Create Virtual Environment (Recommended)

```bash
python -m venv venv
venv\Scripts\activate     # Windows
source venv/bin/activate  # Mac/Linux
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 📄 requirements.txt

```txt
fastapi
uvicorn
requests
dicttoxml
streamlit
pydantic
```

---

## 🚀 Running the Application

### ▶️ Start FastAPI Backend

```bash
uvicorn main:app
```

Backend runs at:

```
http://127.0.0.1:8000
```

---

### ▶️ Start Streamlit Frontend

Open a **new terminal**:

```bash
streamlit run app.py
```

Streamlit runs at:

```
http://localhost:8501
```

---

## 🔌 API Usage

### Endpoint

```
POST /weather
```

### Request Body

```json
{
  "city": "London",
  "output_format": "json"
}
```

### Supported Output Formats

* `json`
* `xml`

---

## 📤 Sample JSON Response

```json
{
  "city": "London",
  "temperature_celsius": 18.2,
  "condition": "Partly cloudy",
  "latitude": 51.52,
  "longitude": -0.11
}
```

---

## 📤 Sample XML Response

```xml
<weather>
  <city>London</city>
  <temperature_celsius>18.2</temperature_celsius>
  <condition>Partly cloudy</condition>
  <latitude>51.52</latitude>
  <longitude>-0.11</longitude>
</weather>
```

---

## 🖥️ Streamlit UI Features

* Text input for city name
* Dropdown for JSON / XML selection
* Weather details display
* Error handling for invalid input or server issues

---

## ❗ Common Issues & Fixes

### 405 Method Not Allowed

* `/weather` is **POST only**
* Use Streamlit or Postman, not browser GET

### Windows Reload Crash

* Do **not** use:

```bash
uvicorn main:app --reload
```

* Use:

```bash
uvicorn main:app
```

---

## 🔐 Security Notes

* API key is stored **only in backend**
* Frontend never exposes RapidAPI credentials
* Ready for `.env` integration

---

## 🚧 Future Enhancements

* 🌍 Weather map using latitude & longitude
* ⏱️ Hourly & 7-day forecast
* 🎨 Improved UI with icons
* 🐳 Docker deployment
* ☁️ Cloud deployment (Render + Streamlit Cloud)

---

## 🧪 Tested On

* Windows 10 / 11
* Python 3.9 – 3.12
* FastAPI 0.110+
* Streamlit 1.30+

---

## 📜 License

This project is licensed under the **MIT License**.

---

## 🙌 Author

**Suyash Pandey**
AI & Software Engineer
