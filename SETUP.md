# 🚀 AQI Search Engine - Complete Setup Guide

## Overview

This guide walks you through setting up and running the Air Quality Index (AQI) Search Engine application on your local machine.

The application consists of:
- **Backend**: Flask Python server with caching
- **Frontend**: Single HTML file with Tailwind CSS
- **Cache**: In-memory storage with TTL and LRU eviction

---

## 📋 Prerequisites

Before you start, ensure you have:

1. **Python 3.8 or higher**
   - Download: https://www.python.org/downloads/
   - After installation, verify: `python --version`

2. **pip** (Python package manager)
   - Usually comes with Python
   - Verify: `pip --version`

3. **Free WAQI API Token**
   - Sign up: https://aqicn.org/data-platform/token/
   - You'll receive a token via email (looks like: `demo123abc456`)

4. **A modern web browser**
   - Chrome, Firefox, Edge, or Safari

5. **Text editor (optional, for viewing code)**
   - VS Code, Notepad++, or any text editor

---

## 🔑 Step 1: Get Your API Token

This is the most important step!

### How to get your WAQI API token:

1. Open: https://aqicn.org/data-platform/token/
2. Click **"Signup"** if you don't have an account
3. Enter your **Email** and accept terms
4. Click **"Get API"**
5. Check your email inbox for confirmation
6. You'll receive your token (something like: `d86e0e24ab85fcf1f16b942a6402e88e`)
7. **Copy and save this token** - you'll need it in the next steps

**Note**: Free tokens have a rate limit of 200 requests/week, which is plenty for personal use.

---

## 💻 Step 2: Install Python Dependencies

Open PowerShell or Command Prompt and run:

```powershell
# Navigate to the project directory
cd "c:\Users\Tushar Singh Tadiyal\Pictures\Project"

# Install required packages
pip install flask requests python-dotenv
```

Or use the requirements.txt file:

```powershell
pip install -r requirements.txt
```

**Expected output:**
```
Successfully installed flask requests python-dotenv
```

---

## 🔧 Step 3: Set Your API Token

You need to set the API token as an environment variable before running the app.

### Option A: Using PowerShell (Recommended for this session)

```powershell
$env:AQI_TOKEN = "YOUR_TOKEN_HERE"
```

Replace `YOUR_TOKEN_HERE` with your actual token from Step 1.

**Example:**
```powershell
$env:AQI_TOKEN = "d86e0e24ab85fcf1f16b942a6402e88e"
```

**To verify it's set:**
```powershell
Write-Host $env:AQI_TOKEN
```

### Option B: Using run.ps1 Script (Easier)

1. Open `run.ps1` in a text editor
2. Find this line: `$API_TOKEN = "YOUR_TOKEN_HERE"`
3. Replace `YOUR_TOKEN_HERE` with your actual token
4. Save the file
5. Run in PowerShell:
   ```powershell
   cd "c:\Users\Tushar Singh Tadiyal\Pictures\Project"
   .\run.ps1
   ```

### Option C: Make Token Persistent (System-wide)

To make the token available in all future PowerShell sessions:

```powershell
[Environment]::SetEnvironmentVariable("AQI_TOKEN", "YOUR_TOKEN_HERE", "User")
```

Then **restart PowerShell** for the change to take effect.

---

## 🎬 Step 4: Start the Application

### Quick Start (after setting API token):

```powershell
cd "c:\Users\Tushar Singh Tadiyal\Pictures\Project"
python app.py
```

**Expected output:**
```
WARNING: This is a development server. Do not use it in production.
Running on http://localhost:5000
```

**If you see this warning about the API token:**
```
⚠️  API_TOKEN NOT CONFIGURED!
```

It means the token environment variable wasn't set. Go back to Step 3 and set it again.

---

## 🌐 Step 5: Open the Frontend

1. Open your web browser
2. Navigate to: **http://localhost:5000/**
3. You should see the AQI Search Engine interface

**What you'll see:**
- A centered search box
- An empty state with a globe emoji
- A footer with data source information

---

## 🔍 Step 6: Search for a City

1. Type a city name in the search box (e.g., "New York", "London", "Delhi")
2. Press **Enter** or click the **Search** button
3. Wait for the results (first search takes ~1-2 seconds)
4. See the AQI data, pollutant breakdown, and health guidance

**Try these cities:**
- New York
- London
- Delhi
- Tokyo
- Beijing
- Los Angeles
- Mumbai

---

## 📊 Understanding the Results

When you search for a city, you'll see:

### Main AQI Display
- **Large number**: The AQI value (0-500+)
- **Color**: Indicates health level
  - 🟢 Green: Good (0-50)
  - 🟡 Yellow: Moderate (51-100)
  - 🟠 Orange: Unhealthy for Sensitive Groups (101-150)
  - 🔴 Red: Unhealthy (151-200)
  - 🔴 Dark Red: Very Unhealthy (201-300)
  - 🟫 Maroon: Hazardous (301+)

### Health Implications
- A sentence explaining what the AQI means for your health

### Pollutant Breakdown
- PM2.5, PM10, O3, CO, NO2, SO2 levels (if available)
- Measured in µg/m³

### Cache Status
- **⚡ Cached**: Data from cache (shown in blue)
- **📡 Live Data**: Fresh data from API (shown in green)

### Timestamp
- When the data was last updated

---

## ⚡ Caching Explained

The app uses **smart caching** to make searches faster:

- **First search**: ~1-2 seconds (fetches from WAQI API)
- **Second search (same city)**: <100ms (retrieved from cache)
- **Cache duration**: 60 minutes
- **Max cached cities**: 50

**Cache eviction**: When the cache reaches 50 cities, the oldest is removed to make room.

---

## 🐛 Troubleshooting

### Problem: "Module not found" error

**Solution**: Make sure you installed the dependencies:
```powershell
pip install flask requests python-dotenv
```

### Problem: "Connection error: Unable to reach WAQI API"

**Solutions**:
1. Check your internet connection
2. Try a different city name
3. WAQI API might be temporarily down - wait a few minutes
4. Verify your API token is valid

### Problem: "No results found for city: [cityname]"

**Solutions**:
1. Check spelling (e.g., "Mumbai" not "Bombay")
2. Try a different city
3. Very small cities might not have data
4. Try a major city first (NYC, London, Tokyo)

### Problem: Page won't load or says "loading..." forever

**Solutions**:
1. Make sure Flask is running (check PowerShell window)
2. Make sure it's running on `http://localhost:5000`
3. Try refreshing the page (Ctrl+F5 for hard refresh)
4. Check browser console for errors (F12)
5. Try a different browser

### Problem: "API_TOKEN NOT CONFIGURED!" message

**Solution**: Set your API token:
```powershell
$env:AQI_TOKEN = "YOUR_TOKEN_HERE"
```

Then restart the Flask app.

### Problem: Can't find my API token email

**Solution**:
1. Check spam/junk folder
2. Go back to https://aqicn.org/data-platform/token/ and request a new token
3. Check your email again (may take 5-10 minutes)

### Problem: PowerShell says "execution policies"

**Solution**: Run:
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

Then try running the script again.

---

## 🚀 Advanced Usage

### Access the API directly

You can query the API directly for integration:

```powershell
# Using PowerShell
Invoke-WebRequest -Uri "http://localhost:5000/api/aqi/city/New York" | ConvertFrom-Json

# Using curl (if available)
curl "http://localhost:5000/api/aqi/city/London"
```

### Health check

Check if the server is running:
```
http://localhost:5000/api/health
```

### Modify cache settings

Edit these values in `app.py`:
```python
CACHE_TTL = 3600          # Change to different seconds
MAX_CACHE_ENTRIES = 50    # Change maximum cached cities
```

### Change port

Edit the last line in `app.py`:
```python
app.run(debug=True, host='localhost', port=8000)  # Use 8000 instead of 5000
```

Then access at: `http://localhost:8000/`

---

## 📝 Project Files

```
Project/
├── app.py              # Flask backend (400+ lines)
├── index.html          # Frontend (500+ lines)
├── README.md           # Project documentation
├── requirements.txt    # Python dependencies
├── SETUP.md           # This file
└── run.ps1            # Quick-start script
```

---

## 🔐 Security Notes

- **API Token**: Stored as environment variable (never committed to code)
- **Input Validation**: City names are validated before API calls
- **Timeout Protection**: Requests timeout after 10 seconds
- **Error Handling**: Graceful error handling for all scenarios

---

## 💡 Tips & Tricks

1. **Save frequently searched cities**: The app automatically caches them
2. **Try mobile-friendly**: Resize your browser window to see responsive design
3. **Check health guidance**: Each AQI level includes specific health advice
4. **Bookmark your results**: Results are in the browser history
5. **Share data**: Copy AQI values to share with others

---

## 🎓 Learning Resources

- **Flask Documentation**: https://flask.palletsprojects.com/
- **Tailwind CSS**: https://tailwindcss.com/
- **WAQI API**: https://waqi.info/
- **REST API Best Practices**: https://restfulapi.net/

---

## 🆘 Getting Help

If you're stuck:

1. **Re-read relevant section** in this guide
2. **Check app.py comments** - it's well-documented
3. **Look at browser console** (F12 → Console tab) for JavaScript errors
4. **Check Flask logs** in the PowerShell window for backend errors
5. **Verify all prerequisites** are installed

---

## 📞 Quick Reference

| Task | Command |
|------|---------|
| Set API token | `$env:AQI_TOKEN = "YOUR_TOKEN"` |
| Install packages | `pip install -r requirements.txt` |
| Start app | `python app.py` |
| Check health | `http://localhost:5000/api/health` |
| Query API | `curl http://localhost:5000/api/aqi/city/London` |
| Stop app | `Ctrl+C` in PowerShell |

---

## ✅ Verification Checklist

Before you start:
- [ ] Python 3.8+ installed
- [ ] pip working (`pip --version`)
- [ ] WAQI API token obtained
- [ ] Dependencies installed
- [ ] API token set in environment
- [ ] Flask running without errors
- [ ] Website loads at http://localhost:5000/
- [ ] Search works (try "New York")
- [ ] Results display with color and data

---

**You're all set! Happy searching! 🌍**
