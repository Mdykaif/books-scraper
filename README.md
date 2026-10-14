# books-scraper
# Books to Scrape — Web Scraping Project

## Overview

This project scrapes book information from [Books to Scrape](https://books.toscrape.com/) using Python, BeautifulSoup, Requests, Pandas, and Threading.

The scraped data is stored in a Pandas DataFrame and exported to a CSV file named `books.csv`.

## Features

- Extracts book titles.
- Extracts book prices.
- Collects stock availability.
- Extracts book ratings.
- Collects book page links.
- Scrapes multiple catalogue pages.
- Exports the collected data to CSV format.
- Uses Python threading to run the scraping function in a separate thread.

## Technologies Used

- **Python** — Core programming language.
- **Requests** — Fetches webpage content.
- **BeautifulSoup** — Parses HTML and extracts book information.
- **Pandas** — Organizes data into a DataFrame and exports CSV files.
- **Threading** — Runs the scraping function in a separate thread.

## Project Structure

```text
books-scraper/
├── main.py
├── books.csv
└── README.md
```

## Installation

### 1. Clone the repository

```bash
git clone <your-repository-url>
cd books-scraper
```

### 2. Install dependencies

```bash
pip install pandas beautifulsoup4 requests
```

No additional installation is required for `threading`, as it is included in Python's standard library.

## How to Run

Execute the Python script:

```bash
python main.py
```

The script will scrape the first 50 catalogue pages, collect the book details, and save the results in `books.csv`.

## Data Fields

| Column | Description |
|---|---|
| `link` | Relative URL of the book page |
| `book` | Complete book title |
| `rate` | Book price |
| `stock` | Stock availability |
| `rating` | Star rating from One to Five |

## Output

The resulting CSV file contains the scraped book information.

Example:

| book | rate | stock | rating |
|---|---|---|---|
| A Light in the Attic | £51.77 | In stock | Three |

The example above is illustrative.

## Important Note About Threading

The current implementation uses `threading.Thread` to execute the scraping function separately from the main thread. However, the requests for individual pages are still sequential.

To fetch multiple pages concurrently and improve performance, consider using `concurrent.futures.ThreadPoolExecutor`.

## Error Handling

The script uses `response.raise_for_status()` to raise an exception when an HTTP request fails. Network errors and request timeouts may interrupt execution.

## Disclaimer

This project is intended for educational purposes and practice with web scraping. Respect the target website's terms, access policies, and request limits.

## Author

Created as a Python web-scraping and data extraction practice project.
