# Books Web Scraping Project

## Overview
This project scrapes book information from the "Books to Scrape" website and exports the data to an Excel file.

## Features
- Scrapes book details including name, price, availability, and rating
- Converts star ratings to readable format (e.g., "Three" → "3/5")
- Exports data to Excel format for easy analysis

## Requirements
```
requests
pandas
beautifulsoup4
openpyxl
```

## Installation
Install the required packages:
```bash
pip install requests pandas beautifulsoup4 openpyxl
```

## Usage
1. Run the script:
```bash
python Scraping_books.py
```

2. The script will:
   - Fetch data from https://books.toscrape.com/
   - Parse book information from the first page
   - Display results in the console
   - Save data to `Scraping_books.xlsx`

## Output
The script generates an Excel file with the following columns:
- **Book Name**: Title of the book
- **Book Price**: Price in the original currency
- **Book State**: Availability status
- **Book Rating**: Star rating in x/5 format

## Files
- `Scraping_books.py` - Main scraping script
- `site_link.txt` - Contains the target website URL
- `Scraping_books.xlsx` - Generated Excel output file