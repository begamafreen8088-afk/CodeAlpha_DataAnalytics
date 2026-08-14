# Web Scraping - Books Dataset

## Project Overview

This project was developed as part of the CodeAlpha Data Analytics Internship.

The objective of this project is to collect book information from a publicly available website using Python web scraping techniques and convert the collected information into a structured dataset.

## Objective

The main objectives of this project are:

- Extract book information from a public webpage.
- Understand the structure of HTML webpages.
- Use BeautifulSoup to locate and extract required information.
- Store the extracted information in a Pandas DataFrame.
- Create a clean CSV dataset for further analysis.

## Technologies Used

- Python
- Requests
- BeautifulSoup
- Pandas

## Data Collected

The following information was collected for each book:

- Book Title
- Price
- Availability
- Rating

## Dataset

The scraped data is stored in:

`books_dataset.csv`

The current dataset contains 20 book records.

## How the Project Works

1. The Python program sends a request to the public website.
2. The webpage response is received using the Requests library.
3. BeautifulSoup parses the HTML content.
4. Book titles, prices, availability, and ratings are extracted.
5. The extracted information is stored in a Pandas DataFrame.
6. The DataFrame is saved as a CSV file.

## Installation

Install the required Python libraries using:

```bash
pip3 install -r requirements.txt