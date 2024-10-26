import unittest
from unittest.mock import patch

import requests
# from zr_google_scraper import GoogleScraper
from zr_google_scraper.scraper import GoogleScraper
# from zr_web_scraper.zr_google_scraper import GoogleScraper


class TestGoogleScraper(unittest.TestCase):

    def setUp(self):
        self.scraper = GoogleScraper()

    # @patch('scraper.google_scraper.scraper.requests.get')
    @patch('zr_google_scraper.scraper.requests.get')
    def test_scrape_no_results(self, mock_get):
        # Simulate a response with no results
        mock_get.return_value.status_code = 200
        mock_get.return_value.text = '<div class="g"></div>'  # Empty search results
        
        result = self.scraper.scrape("No Results Query")
        self.assertIn("No search results found for query", result)

    # @patch('scraper.google_scraper.scraper.requests.get') 
    @patch('zr_google_scraper.scraper.requests.get')
    def test_scrape_success(self, mock_get):
        # Simulate a successful response with results
        mock_get.return_value.status_code = 200
        mock_get.return_value.text = '''
            <div class="g">
                <h3 class="LC20lb">Test Title</h3>
                <a href="http://example.com">Link</a>
                <div class="VwiC3b">Test Content</div>
            </div>
        '''
        
        result = self.scraper.scrape("Test Query")
        self.assertEqual(len(result), 1)  # One result should be found
        self.assertEqual(result[0]['title'], 'Test Title')

    # @patch('scraper.google_scraper.scraper.requests.get')
    @patch('zr_google_scraper.scraper.requests.get')
    def test_scrape_failure(self, mock_get):
        # Simulate a network error
        mock_get.side_effect = requests.exceptions.RequestException("Network Error")
        
        result = self.scraper.scrape("Error Query")
        self.assertIn("Failed to retrieve search results:", result)

if __name__ == '__main__':
    unittest.main()
