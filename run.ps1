# Air Quality Index Search Engine - Quick Start Script
# This script automates setup and launching of the AQI Search Engine
# 
# BEFORE RUNNING:
# 1. Get your free API token from: https://aqicn.org/data-platform/token/
# 2. Replace YOUR_TOKEN_HERE below with your actual token

# ==================== CONFIGURATION ====================

$API_TOKEN = "YOUR_TOKEN_HERE"  # <-- INSERT YOUR WAQI API TOKEN HERE
$PROJECT_DIR = Split-Path -Parent $MyInvocation.MyCommand.Path

# ==================== SETUP ====================

Write-Host "================================" -ForegroundColor Cyan
Write-Host "AQI Search Engine - Setup" -ForegroundColor Green
Write-Host "================================" -ForegroundColor Cyan
Write-Host ""

# Check if API token is set
if ($API_TOKEN -eq "YOUR_TOKEN_HERE") {
    Write-Host "⚠️  WARNING: API token not configured!" -ForegroundColor Yellow
    Write-Host "Please set your WAQI API token before proceeding." -ForegroundColor Yellow
    Write-Host "Get free token: https://aqicn.org/data-platform/token/" -ForegroundColor Cyan
    Write-Host ""
    exit
}

# Step 1: Check Python installation
Write-Host "📦 Checking Python installation..." -ForegroundColor Yellow
try {
    $python_version = python --version 2>&1
    Write-Host "✅ $python_version" -ForegroundColor Green
} catch {
    Write-Host "❌ Python not found. Please install Python 3.8+" -ForegroundColor Red
    Write-Host "Download from: https://www.python.org/downloads/" -ForegroundColor Cyan
    exit
}

# Step 2: Install dependencies
Write-Host ""
Write-Host "📥 Installing dependencies..." -ForegroundColor Yellow
if (Test-Path "$PROJECT_DIR\requirements.txt") {
    pip install -q -r "$PROJECT_DIR\requirements.txt"
    Write-Host "✅ Dependencies installed" -ForegroundColor Green
} else {
    Write-Host "⚠️  requirements.txt not found. Installing manually..." -ForegroundColor Yellow
    pip install -q flask requests python-dotenv
    Write-Host "✅ Dependencies installed" -ForegroundColor Green
}

# Step 3: Set environment variable
Write-Host ""
Write-Host "🔑 Setting API token..." -ForegroundColor Yellow
$env:AQI_TOKEN = $API_TOKEN
Write-Host "✅ API token configured" -ForegroundColor Green

# Step 4: Start the application
Write-Host ""
Write-Host "================================" -ForegroundColor Cyan
Write-Host "🚀 Starting AQI Search Engine" -ForegroundColor Green
Write-Host "================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "Frontend:  http://localhost:5000/" -ForegroundColor Cyan
Write-Host "API Docs:  http://localhost:5000/api/aqi/city/<city_name>" -ForegroundColor Cyan
Write-Host "Health:    http://localhost:5000/api/health" -ForegroundColor Cyan
Write-Host ""
Write-Host "Press Ctrl+C to stop the server" -ForegroundColor Yellow
Write-Host ""

# Launch Flask app
Set-Location $PROJECT_DIR
python app.py
