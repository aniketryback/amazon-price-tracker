# 🛒 Amazon Price Tracker

Scrapes Amazon product price and name, logs it to a CSV file, and plots a price trend chart using Matplotlib.

---

## 🚀 How It Works

1. Fetches product price & title using `requests` and `BeautifulSoup`
2. Appends it to `price_tracker.csv` with timestamp
3. Plots latest 10 prices to `output/price_trend.png`

---

## 📁 Project Structure

amazon-price-tracker/
├── price_tracker.py ← Main script
├── price_tracker.csv ← Auto-created log file
├── output/
│ └── price_trend.png ← Auto-generated chart
