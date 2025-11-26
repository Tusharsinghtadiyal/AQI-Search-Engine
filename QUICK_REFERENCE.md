# 🎯 Quick Reference Card

## File Locations
```
c:\Users\Tushar Singh Tadiyal\Pictures\Project\
  ├── app.py                 (Flask backend - 400+ lines)
  ├── index.html             (Frontend - 500+ lines)  
  ├── README.md              (Full documentation)
  ├── SETUP.md               (Setup guide)
  ├── DELIVERABLES.md        (Checklist)
  ├── requirements.txt       (Dependencies)
  └── run.ps1                (Quick-start script)
```

## 🚀 One-Minute Startup

```powershell
# 1. Set API token
$env:AQI_TOKEN = "YOUR_TOKEN_HERE"

# 2. Go to project directory
cd "c:\Users\Tushar Singh Tadiyal\Pictures\Project"

# 3. Install packages (if not done)
pip install -r requirements.txt

# 4. Run Flask app
python app.py

# 5. Open browser
# http://localhost:5000/
```

## 🔑 Getting Your API Token

1. Visit: https://aqicn.org/data-platform/token/
2. Sign up with email
3. Check email for token
4. Copy token
5. Set: `$env:AQI_TOKEN = "YOUR_TOKEN"`

## 📍 Key Endpoints

| Endpoint | Method | Purpose |
|----------|--------|---------|
| `/` | GET | Frontend UI |
| `/api/aqi/city/<city>` | GET | Get AQI data |
| `/api/health` | GET | Health check |

## 🎨 AQI Color Reference

| AQI | Color | Level |
|-----|-------|-------|
| 0-50 | 🟢 Green | Good |
| 51-100 | 🟡 Yellow | Moderate |
| 101-150 | 🟠 Orange | Unhealthy for Sensitive |
| 151-200 | 🔴 Red | Unhealthy |
| 201-300 | 🔴 Dark Red | Very Unhealthy |
| 301+ | 🟫 Maroon | Hazardous |

## 💾 Cache Settings

```python
CACHE_TTL = 3600            # 60 minutes
MAX_CACHE_ENTRIES = 50      # Maximum cities
```

Edit in `app.py` to customize.

## 🧪 Test URLs

```
Frontend:      http://localhost:5000/
New York:      http://localhost:5000/api/aqi/city/New York
Health Check:  http://localhost:5000/api/health
```

## ⚡ Performance

- **First search**: ~1-2 seconds
- **Cached search**: <100ms
- **Cache duration**: 60 minutes
- **Max cached**: 50 cities

## 📁 Project Structure

```
Backend (app.py):
  - Flask initialization
  - Cache management (dict with TTL)
  - WAQI API integration
  - LRU eviction logic
  - RESTful endpoints
  - Error handling

Frontend (index.html):
  - Search interface
  - Results display
  - Color-coded AQI
  - Pollutant breakdown
  - Error states
  - Responsive design
```

## 🔧 Common Commands

```powershell
# Start app
python app.py

# Check Python
python --version

# Install packages
pip install -r requirements.txt

# Set token (PowerShell)
$env:AQI_TOKEN = "YOUR_TOKEN"

# Stop app
Ctrl + C
```

## 🐛 Quick Troubleshooting

| Issue | Solution |
|-------|----------|
| Module not found | `pip install -r requirements.txt` |
| No data found | Try different city name |
| Can't reach API | Check internet, wait 5 min |
| Token error | Set: `$env:AQI_TOKEN = "YOUR_TOKEN"` |
| Page won't load | Refresh (Ctrl+F5), check localhost:5000 |

## 📊 Response Example

```json
{
  "status": "success",
  "city": "New York",
  "aqi": 75,
  "health_implications": "Moderate",
  "cached": false,
  "details": {
    "PM2.5": 55,
    "O3": 25,
    "CO": 5.2
  }
}
```

## 📚 Documentation Files

- **README.md**: Full project overview
- **SETUP.md**: Step-by-step setup guide
- **DELIVERABLES.md**: Complete checklist
- **app.py**: Backend code with comments
- **index.html**: Frontend code with comments

## 🌟 Key Features

✅ Real-time AQI data  
✅ Smart caching (60 min TTL)  
✅ Responsive design  
✅ Color-coded display  
✅ Pollutant breakdown  
✅ Error handling  
✅ Performance optimized  

## 💡 Tips

1. First search is slower (API call)
2. Repeated searches are fast (cached)
3. Try major cities first
4. Data updates every ~60 min
5. Mobile-friendly design
6. Share your findings!

## 🎓 Learning

- **Backend**: Flask, caching, REST API
- **Frontend**: HTML5, Tailwind CSS, Vanilla JS
- **API**: WAQI integration, error handling
- **Performance**: Caching strategies

## ✅ Before You Start

- [ ] Python 3.8+ installed
- [ ] API token obtained
- [ ] Dependencies installed
- [ ] Token environment variable set
- [ ] Flask running on localhost:5000
- [ ] Browser showing http://localhost:5000/

## 🚨 Common Mistakes

❌ Forget to set API token  
❌ Use wrong city name (spelling)  
❌ Don't install dependencies  
❌ Access wrong URL  
❌ Flask not running  

**Always check:**
1. Token is set
2. Flask is running
3. URL is correct
4. City name spelled right

## 📞 Getting Help

1. Read SETUP.md
2. Check browser console (F12)
3. Look at Flask logs
4. Verify prerequisites
5. Try different city

---

**Last Updated**: November 2025
**Status**: Production Ready ✅
