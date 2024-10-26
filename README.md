# Web Scraper Package

This package allows you to scrape Web search results using Python.

### Necessary Commands
# To test be on directory zr_web_scraper
pytest test/

# Web Scraper

This package allows you to scrape Web search results using Python. It’s useful for retrieving information from search results for automated data collection or analysis tasks. The `GoogleScraper` class in this package is designed to fetch and parse search results, returning structured data for further processing.

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Testing](#testing)
- [Dependencies](#dependencies)
- [Notes](#notes)
- [License](#license)

## Installation

### Clone the Repository
Clone this repository to your local machine:
```bash
git clone https://github.com/yourusername/zr_web_scraper.git
cd zr_web_scraper
```

### Install Required Packages
Use `pip` to install the necessary packages:
```bash
pip install -r requirements.txt
```

## Usage

### Example Code
To scrape Web search results, use the `GoogleScraper` class. Here’s a simple example:
```python
from zr_google_scraper.scraper import GoogleScraper

# Initialize the scraper
scraper = GoogleScraper()

# Perform a search and print the results
results = scraper.scrape("OpenAI ChatGPT")
for result in results:
    print(f"Title: {result['title']}")
    print(f"Link: {result['link']}")
    print(f"Content: {result['content']}
")
```

This code performs a search for "OpenAI ChatGPT" and prints out the title, link, and content snippet for each result.

## Project Structure

```
zr_web_scraper/
├── zr_google_scraper/
│   ├── __init__.py
│   ├── scraper.py            # Contains the main GoogleScraper class
├── tests/
│   ├── test_zr_google_scraper.py    # Unit tests for GoogleScraper
├── setup.py
├── requirements.txt
├── README.md
```

- `zr_google_scraper/`: Contains the Google scraping logic.
- `tests/`: Unit tests for validating scraper functionality.
- `setup.py`: Script for packaging the module.
- `requirements.txt`: Lists dependencies required for this project.
- `README.md`: Documentation for the project.

## Testing

To run the tests, navigate to the root directory (`zr_web_scraper`) and use `pytest`:
```bash
cd zr_web_scraper
pytest tests/
```

This command will execute all tests in `tests/test_zr_google_scraper.py` and provide output on the test status.

### Test Coverage
- **No Results Test**: Ensures that the scraper correctly identifies when there are no search results.
- **Success Test**: Validates that the scraper accurately parses titles, links, and content from search results.
- **Failure Test**: Simulates a network error to confirm the scraper handles exceptions gracefully.

## Dependencies

Install the following dependencies as listed in `requirements.txt`:
- `requests`: For handling HTTP requests.
- `beautifulsoup4`: For parsing HTML content.

## Notes

- **Legal Considerations**: Scraping Google results might violate Google’s terms of service. Use this tool responsibly and check Google’s policies regarding automated data collection.
- **Rate Limiting**: Google might block IPs that perform automated searches frequently. Consider adding delays between requests if running multiple searches in succession.

## License

This project is licensed under the MIT License.
