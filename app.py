"""
Air Quality Index (AQI) Search Engine - Flask Backend
A performant, RESTful web service with in-memory caching for AQI data.

External API: WAQI (api.waqi.info)
Caching: In-memory dictionary with TTL (60 min) and LRU eviction (max 50 entries)

SETUP INSTRUCTIONS:
1. Install dependencies: pip install flask requests python-dotenv
2. Set your API token in environment variable or update AQI_TOKEN below
   - Get free token at: https://aqicn.org/data-platform/token/
   - Set: $env:AQI_TOKEN = "YOUR_TOKEN_HERE" (PowerShell)
   - Or: export AQI_TOKEN="YOUR_TOKEN_HERE" (Linux/Mac)
3. Run: python app.py
4. Frontend available at: http://localhost:5000/
"""

from flask import Flask, jsonify, send_from_directory
from dotenv import load_dotenv
import requests
import time
import os
from datetime import datetime
import logging

# ==================== CONFIGURATION ====================
AQI_TOKEN = os.getenv('AQI_TOKEN', 'PLACEHOLDER_TOKEN_INSERT_YOUR_TOKEN_HERE')
WAQI_FEED_URL = 'https://api.waqi.info/feed/'
CACHE_TTL = 3600  # 60 minutes in seconds
MAX_CACHE_ENTRIES = 50
REQUEST_TIMEOUT = 10  # seconds

# ==================== LOGGING ====================
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# ==================== FLASK APP ====================
app = Flask(__name__, static_folder='.', static_url_path='')

# Load local .env for development if present (keeps tokens out of source control)
load_dotenv()

# ==================== CACHE MANAGEMENT ====================
cache = {}


def is_cache_expired(timestamp):
    """Check if a cache entry has expired based on TTL."""
    return time.time() - timestamp > CACHE_TTL


def evict_oldest_entry():
    """Remove the oldest cache entry (lowest timestamp) when cache is full."""
    if cache:
        oldest_key = min(cache.keys(), key=lambda k: cache[k]['timestamp'])
        del cache[oldest_key]
        logger.info(f"Evicted oldest cache entry: {oldest_key}")


def get_cached_data(city_name):
    """
    Retrieve data from cache if available and not expired.
    Returns: (data, is_cached) or (None, False) if not in cache or expired.
    """
    if city_name in cache:
        entry = cache[city_name]
        if not is_cache_expired(entry['timestamp']):
            logger.info(f"Cache HIT for city: {city_name}")
            return entry['data'], True
        else:
            logger.info(f"Cache EXPIRED for city: {city_name}")
            del cache[city_name]
    
    return None, False


def update_cache(city_name, data):
    """Update cache with new data, evicting oldest if necessary."""
    if len(cache) >= MAX_CACHE_ENTRIES:
        evict_oldest_entry()
    
    cache[city_name] = {
        'data': data,
        'timestamp': time.time()
    }
    logger.info(f"Cache updated for city: {city_name} (Cache size: {len(cache)}/{MAX_CACHE_ENTRIES})")


def fetch_from_waqi_api(city_name):
    """
    Fetch AQI data from WAQI API using /feed/ endpoint.
    Returns: (response_data, error_message) or (None, error_message) on failure.
    """
    try:
        params = {
            'token': AQI_TOKEN
        }
        
        # Use /feed/ endpoint with city name
        url = f"{WAQI_FEED_URL}{city_name}/?token={AQI_TOKEN}"
        
        logger.info(f"Fetching data from WAQI API for: {city_name}")
        response = requests.get(url, timeout=REQUEST_TIMEOUT)
        response.raise_for_status()
        
        data = response.json()
        
        if data.get('status') != 'ok':
            return None, f"API Error: {data.get('data', 'Unknown error')}"
        
        result = data.get('data')
        if not result:
            return None, f"No results found for city: {city_name}"
        
        return result, None
    
    except requests.exceptions.Timeout:
        error_msg = "Request timeout: API took too long to respond"
        logger.error(error_msg)
        return None, error_msg
    except requests.exceptions.ConnectionError:
        error_msg = "Connection error: Unable to reach WAQI API"
        logger.error(error_msg)
        return None, error_msg
    except requests.exceptions.RequestException as e:
        error_msg = f"Request error: {str(e)}"
        logger.error(error_msg)
        return None, error_msg
    except ValueError as e:
        error_msg = f"JSON parsing error: {str(e)}"
        logger.error(error_msg)
        return None, error_msg


def parse_aqi_data(result):
    """
    Parse WAQI API response from /feed/ endpoint and extract relevant AQI information.
    Returns structured JSON response.
    """
    try:
        aqi = result.get('aqi', 'N/A')
        city = result.get('city', {}).get('name', 'Unknown')
        
        # Extract pollutant details if available
        details = {}
        iaqi = result.get('iaqi', {})
        
        pollutant_map = {
            'pm25': 'PM2.5',
            'pm10': 'PM10',
            'o3': 'O3',
            'no2': 'NO2',
            'so2': 'SO2',
            'co': 'CO'
        }
        
        for key, label in pollutant_map.items():
            if key in iaqi:
                details[label] = iaqi[key].get('v', 'N/A')
        
        # Determine health implications based on US EPA AQI scale
        if isinstance(aqi, str):
            aqi_value = int(aqi) if aqi != 'N/A' else None
        else:
            aqi_value = aqi
        
        if aqi_value is None:
            health_implications = "Unknown"
        elif aqi_value <= 50:
            health_implications = "Good"
        elif aqi_value <= 100:
            health_implications = "Moderate"
        elif aqi_value <= 150:
            health_implications = "Unhealthy for Sensitive Groups"
        elif aqi_value <= 200:
            health_implications = "Unhealthy"
        elif aqi_value <= 300:
            health_implications = "Very Unhealthy"
        else:
            health_implications = "Hazardous"
        
        response = {
            'status': 'success',
            'city': city,
            'aqi': aqi_value,
            'health_implications': health_implications,
            'details': details,
            'timestamp': datetime.now().isoformat(),
            'url': result.get('city', {}).get('url', 'N/A')
        }
        
        return response
    
    except Exception as e:
        logger.error(f"Error parsing AQI data: {str(e)}")
        return None


# ==================== API ENDPOINTS ====================

@app.route('/')
def serve_frontend():
    """Serve the main HTML frontend."""
    return send_from_directory('.', 'index.html')


@app.route('/api/aqi/city/<city_name>', methods=['GET'])
def get_aqi_by_city(city_name):
    """
    RESTful endpoint to fetch AQI data for a city.
    
    Query Parameters:
    - city_name (path): Name of the city to search for
    
    Returns:
    - 200 OK: Successful AQI data retrieval
    - 400 Bad Request: Invalid city name
    - 404 Not Found: City not found
    - 500 Internal Server Error: Server/API error
    """
    try:
        # Validate input
        if not city_name or not isinstance(city_name, str):
            return jsonify({
                'status': 'error',
                'message': 'Invalid city name provided'
            }), 400
        
        city_name_clean = city_name.strip()
        if not city_name_clean:
            return jsonify({
                'status': 'error',
                'message': 'City name cannot be empty'
            }), 400
        
        # Check cache first
        cached_data, is_cached = get_cached_data(city_name_clean)
        if cached_data:
            response_data = cached_data.copy()
            response_data['cached'] = True
            return jsonify(response_data), 200
        
        # Fetch from external API if not in cache
        result, error = fetch_from_waqi_api(city_name_clean)
        
        if error:
            if 'No results found' in error:
                return jsonify({
                    'status': 'error',
                    'message': error
                }), 404
            else:
                return jsonify({
                    'status': 'error',
                    'message': error
                }), 500
        
        # Parse the result
        if result:
            parsed_data = parse_aqi_data(result)
            
            if parsed_data:
                parsed_data['cached'] = False
                
                # Update cache with new data
                update_cache(city_name_clean, parsed_data)
                
                return jsonify(parsed_data), 200
            else:
                return jsonify({
                    'status': 'error',
                    'message': 'Failed to parse API response'
                }), 500
        else:
            return jsonify({
                'status': 'error',
                'message': f'No data found for city: {city_name_clean}'
            }), 404
    
    except Exception as e:
        logger.error(f"Unexpected error in get_aqi_by_city: {str(e)}")
        return jsonify({
            'status': 'error',
            'message': 'Internal server error'
        }), 500


@app.route('/api/health', methods=['GET'])
def health_check():
    """Health check endpoint."""
    return jsonify({
        'status': 'healthy',
        'cache_size': len(cache),
        'max_cache_entries': MAX_CACHE_ENTRIES,
        'timestamp': datetime.now().isoformat()
    }), 200


# ==================== ERROR HANDLERS ====================

@app.errorhandler(404)
def not_found(error):
    """Handle 404 errors."""
    return jsonify({
        'status': 'error',
        'message': 'Endpoint not found'
    }), 404


@app.errorhandler(500)
def internal_error(error):
    """Handle 500 errors."""
    logger.error(f"Internal server error: {str(error)}")
    return jsonify({
        'status': 'error',
        'message': 'Internal server error'
    }), 500


# ==================== STARTUP ====================

if __name__ == '__main__':
    if AQI_TOKEN == 'PLACEHOLDER_TOKEN_INSERT_YOUR_TOKEN_HERE':
        logger.warning("="*60)
        logger.warning("⚠️  API_TOKEN NOT CONFIGURED!")
        logger.warning("Please set your WAQI API token:")
        logger.warning("  PowerShell: $env:AQI_TOKEN = 'YOUR_TOKEN_HERE'")
        logger.warning("  Bash:       export AQI_TOKEN='YOUR_TOKEN_HERE'")
        logger.warning("Get free token: https://aqicn.org/data-platform/token/")
        logger.warning("="*60)
    
    logger.info("Starting AQI Search Engine Backend...")
    logger.info(f"Cache TTL: {CACHE_TTL}s, Max Entries: {MAX_CACHE_ENTRIES}")
    logger.info("Frontend available at: http://localhost:5000/")
    logger.info("API endpoint: http://localhost:5000/api/aqi/city/<city_name>")
    
    app.run(debug=True, host='localhost', port=5000)
