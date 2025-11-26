# 🎬 Visual Setup & Usage Guide

## 📸 Screenshot Flow

### 1. Frontend Interface
```
╔════════════════════════════════════════════╗
║     AQI Search Engine                      ║
║     Real-time Air Quality Index Tracker    ║
║                                            ║
║  ┌────────────────────────────────────┐   ║
║  │ Enter city name (e.g., New York)   │   ║
║  │ ◼ Enter city name...         Search│   ║
║  └────────────────────────────────────┘   ║
║                                            ║
║  🌍 Search for a city to see its Air     ║
║     Quality Index                         ║
║                                            ║
║  Data cached for 60 minutes for faster    ║
║  results                                   ║
╚════════════════════════════════════════════╝
```

### 2. Search in Progress
```
╔════════════════════════════════════════════╗
║     Searching for city data...             ║
║                                            ║
║              ⟳  ⟳  ⟳                      ║
║         (Loading Spinner)                  ║
║                                            ║
║     Searching for city data...             ║
╚════════════════════════════════════════════╝
```

### 3. Successful Result (Good Air Quality)
```
╔════════════════════════════════════════════╗
║                                            ║
║  ┌────────────────────────────────────┐   ║
║  │                                    │   ║
║  │      Air Quality Index             │   ║
║  │                                    │   ║
║  │           42                       │   ║  <- Large, colored text
║  │        (GREEN)                     │   ║
║  │                                    │   ║
║  │      New York                      │   ║
║  │      Good                          │   ║
║  │                                    │   ║
║  │      ⚡ Cached   (or 📡 Live)    │   ║
║  └────────────────────────────────────┘   ║
║                                            ║
║  Pollutant Breakdown                       ║
║  ┌──────┐ ┌──────┐ ┌──────┐             │
║  │PM2.5 │ │ O3   │ │ CO   │             │
║  │ 35   │ │ 22   │ │ 5.2  │             │
║  │µg/m³ │ │ µg/m³│ │µg/m³ │             │
║  └──────┘ └──────┘ └──────┘             │
║                                            ║
║  Health Guidance                           ║
║  Air quality is satisfactory. No health   ║
║  concerns.                                 ║
║                                            ║
║  Last updated: 10:30:45                   ║
╚════════════════════════════════════════════╝
```

### 4. Moderate Air Quality
```
╔════════════════════════════════════════════╗
║                                            ║
║      Air Quality Index                     ║
║                                            ║
║           75                               ║  <- YELLOW
║        (YELLOW)                            ║
║                                            ║
║      London                                ║
║      Moderate                              ║
║                                            ║
║      📡 Live Data                          ║
║                                            ║
║  [Pollutants and guidance...]              ║
║                                            ║
╚════════════════════════════════════════════╝
```

### 5. Unhealthy Air Quality
```
╔════════════════════════════════════════════╗
║                                            ║
║      Air Quality Index                     ║
║                                            ║
║           175                              ║  <- RED
║        (RED)                               ║
║                                            ║
║      Delhi                                 ║
║      Unhealthy                             ║
║                                            ║
║      ⚡ Cached                             ║
║                                            ║
║  Health Alert: Some health effects on     ║
║  the general population. Limit outdoor    ║
║  activities.                               ║
║                                            ║
╚════════════════════════════════════════════╝
```

### 6. Error State - City Not Found
```
╔════════════════════════════════════════════╗
║                                            ║
║  ⚠️ Error                                 ║
║                                            ║
║  City not found: "InvalidCity".            ║
║  Please check the spelling and try again.  ║
║                                            ║
║  Try: New York, London, Delhi, Tokyo      ║
║                                            ║
╚════════════════════════════════════════════╝
```

### 7. Error State - Network Error
```
╔════════════════════════════════════════════╗
║                                            ║
║  ⚠️ Error                                 ║
║                                            ║
║  Network error: Unable to reach the        ║
║  server. Is the Flask backend running on   ║
║  localhost:5000?                           ║
║                                            ║
╚════════════════════════════════════════════╝
```

---

## 📊 AQI Color Scale Visualization

```
AQI 0-50       AQI 51-100     AQI 101-150    AQI 151-200    AQI 201-300    AQI 301+
┌──────────┐   ┌──────────┐   ┌──────────┐   ┌──────────┐   ┌──────────┐   ┌──────────┐
│ GOOD     │   │MODERATE  │   │UNHEALTHY │   │UNHEALTHY │   │ VERY     │   │HAZARDOUS │
│🟢 Green  │   │🟡 Yellow │   │🟠 Orange │   │🔴 Red    │   │🔴 Dark  │   │🟫 Maroon │
│          │   │          │   │ FOR      │   │          │   │  Red     │   │          │
│Safe      │   │Acceptable│   │SENSITIVE │   │General   │   │Everyone  │   │Everyone  │
│          │   │          │   │GROUPS    │   │affected  │   │affected  │   │affected  │
└──────────┘   └──────────┘   └──────────┘   └──────────┘   └──────────┘   └──────────┘
```

---

## 🚀 Setup Flow Diagram

```
START
  │
  ├─→ 1. Get API Token
  │   (https://aqicn.org/data-platform/token/)
  │   └─→ Check email for token
  │
  ├─→ 2. Set Environment Variable
  │   $env:AQI_TOKEN = "YOUR_TOKEN"
  │
  ├─→ 3. Install Dependencies
  │   pip install -r requirements.txt
  │
  ├─→ 4. Start Flask Server
  │   python app.py
  │   └─→ Server runs on http://localhost:5000
  │
  ├─→ 5. Open Browser
  │   Navigate to http://localhost:5000/
  │
  └─→ 6. Search for a City
      DONE! ✅
```

---

## 💾 Cache Behavior Timeline

```
TIME    ACTION                    CACHE STATE         RESPONSE TIME
────────────────────────────────────────────────────────────────────
T=0     Search "London"          Cache: Empty        ~1-2 seconds ⏱️
        └─> MISS, fetch API                         (API call)

T=5     Search "London" again    Cache: 1 entry      <100ms ⚡
        └─> HIT, from cache                         (Instant)

T=10    Search "Tokyo"           Cache: 2 entries    ~1-2 seconds ⏱️
        └─> MISS, fetch API                         (API call)

T=15    Search "London" again    Cache: 2 entries    <100ms ⚡
        └─> HIT, still in cache                     (Instant)

T=3610  Search "London" again    Cache: expired      ~1-2 seconds ⏱️
        └─> MISS, TTL expired                       (API call again)

...continues until 50 cities...

T=N     New city #50 added       Cache: FULL         ~1-2 seconds ⏱️
        Next new city:
        └─> Oldest entry removed, new added        (Auto eviction)
```

---

## 🔄 Backend Processing Flow

```
HTTP REQUEST: GET /api/aqi/city/London
│
├─→ VALIDATE INPUT
│   ├─→ Check if city_name is not empty
│   └─→ Return 400 if invalid
│
├─→ CHECK CACHE
│   ├─→ Is "London" in cache?
│   │   ├─→ YES & Not Expired?
│   │   │   └─→ Return cached data
│   │   │       status: "success"
│   │   │       cached: true
│   │   └─→ YES & Expired?
│   │       └─→ Delete from cache, continue
│   └─→ NO → Continue to fetch
│
├─→ FETCH FROM WAQI API
│   ├─→ Make HTTP request to api.waqi.info
│   ├─→ Timeout after 10 seconds
│   └─→ Handle errors: network, JSON, API errors
│
├─→ PARSE RESPONSE
│   ├─→ Extract AQI value
│   ├─→ Extract pollutants (PM2.5, O3, CO, etc)
│   └─→ Calculate health implications
│
├─→ UPDATE CACHE
│   ├─→ Cache is full (50 entries)?
│   │   ├─→ YES: Remove oldest entry
│   │   └─→ NO: Add new entry
│   └─→ Store: city_name → {data, timestamp}
│
└─→ RETURN JSON RESPONSE
    {
      "status": "success",
      "city": "London",
      "aqi": 85,
      "health_implications": "Moderate",
      "details": {...},
      "cached": false
    }
```

---

## 📱 Responsive Design Breakpoints

```
DESKTOP (>1024px)          TABLET (768-1024px)    MOBILE (<768px)
┌──────────────────────┐   ┌──────────────────┐   ┌─────────────┐
│ AQI Search Engine    │   │ AQI Search       │   │ AQI Search  │
│                      │   │ Engine           │   │ Engine      │
│ ┌─────────────────┐  │   │ ┌──────────────┐ │   │ ┌─────────┐ │
│ │ Search Box Full │  │   │ │ Search Full  │ │   │ │Search   │ │
│ │ Width           │  │   │ │ Width        │ │   │ │ ┼─────┼ │ │
│ └─────────────────┘  │   │ └──────────────┘ │   │ └─────────┘ │
│                      │   │                  │   │             │
│ ┌─────────────────┐  │   │ ┌──────────────┐ │   │ ┌─────────┐ │
│ │  Large Results  │  │   │ │Results Stack │ │   │ │Results  │ │
│ │  Card Display   │  │   │ │ Vertically   │ │   │ │Stack V. │ │
│ │  Multi-column   │  │   │ └──────────────┘ │   │ │1 Column │ │
│ │  Pollutants     │  │   │                  │   │ └─────────┘ │
│ └─────────────────┘  │   │                  │   │             │
└──────────────────────┘   └──────────────────┘   └─────────────┘
```

---

## 🔐 Security Flow

```
API TOKEN INPUT
  │
  ├─→ Environment Variable (Recommended)
  │   $env:AQI_TOKEN = "token"
  │
  ├─→ Never hardcoded in source
  │
  ├─→ Used only for WAQI API calls
  │
  └─→ Not exposed in frontend
      └─→ API calls go through backend
          └─→ Token protected

USER INPUT → VALIDATION
  │
  ├─→ City name length check (min 2 chars)
  │
  ├─→ Empty check
  │
  ├─→ URL encoding
  │
  └─→ Error handling for malformed data

API RESPONSE → PARSING
  │
  ├─→ Check status: "ok"
  │
  ├─→ Validate JSON structure
  │
  ├─→ Extract safe fields only
  │
  └─→ Never execute client code
      └─→ Display as text only
```

---

## 📈 Performance Comparison

```
WITHOUT CACHING         WITH CACHING (This Project)
═══════════════════════════════════════════════════════

First Search:                First Search:
  API Call → 1-2 seconds       API Call → 1-2 seconds
  No speedup                    No speedup

Second Search (Same City):  Second Search (Same City):
  API Call → 1-2 seconds      Cache Hit → <100 ms
  Same latency                70x FASTER! ⚡

Third Search (Different):   Third Search (Different):
  API Call → 1-2 seconds       API Call → 1-2 seconds

Repeated Patterns:          Repeated Patterns:
  Every search slow           Most searches fast
  Lots of API calls           Fewer API calls
  Rate limit risk             Rate limit safe
```

---

## 🎯 Decision Tree: What to Read

```
START
  │
  ├─→ "Just run it now!"
  │   └─→ Read: QUICK_REFERENCE.md (5 min)
  │       Then: Follow one-minute startup
  │
  ├─→ "I want to understand it"
  │   └─→ Read: PROJECT_SUMMARY.md (15 min)
  │       Then: SETUP.md (30 min)
  │       Then: README.md (20 min)
  │
  ├─→ "I'm stuck on setup"
  │   └─→ Read: SETUP.md
  │       Find: Your problem in Troubleshooting
  │       Follow: Solution steps
  │
  ├─→ "I want to deploy"
  │   └─→ Read: README.md
  │       Find: Deployment section
  │       Choose: Gunicorn or Docker
  │
  ├─→ "I want to verify everything"
  │   └─→ Read: DELIVERABLES.md
  │       Check: All ✅ marks
  │
  └─→ "I want to learn the code"
      └─→ Read: app.py (comments explain everything)
          Read: index.html (comments explain everything)
```

---

## 🎓 Learning Path

```
LEVEL 1: USER (20 min)
  ├─→ Install software
  ├─→ Set up API token
  ├─→ Run application
  └─→ Search for cities ✅

LEVEL 2: OPERATOR (1 hour)
  ├─→ Understand architecture
  ├─→ Configure settings
  ├─→ Monitor cache
  ├─→ Deploy locally
  └─→ Troubleshoot issues ✅

LEVEL 3: DEVELOPER (3 hours)
  ├─→ Read all code comments
  ├─→ Understand caching logic
  ├─→ Learn REST API design
  ├─→ Modify settings
  ├─→ Add features
  └─→ Deploy to production ✅

LEVEL 4: ARCHITECT (5+ hours)
  ├─→ Design scaling improvements
  ├─→ Implement distributed cache
  ├─→ Add database layer
  ├─→ Build mobile app
  ├─→ Setup CI/CD pipeline
  └─→ Deploy globally ✅
```

---

**Happy Learning! 🚀**
