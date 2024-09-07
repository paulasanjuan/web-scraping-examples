# Web Scraping Examples

This repository contains three different web scraping examples that demonstrate various techniques and approaches to extracting data from the web. Each example is structured to showcase specific methods used in scraping, along with the tools and libraries that enable efficient data extraction. These projects reflect how to handle dynamic pages, extract meaningful data, and store the results for further use.

## Table of Contents

1. [Ent_1](#ent_1)
2. [Ent_2](#ent_2)
3. [Biosearch Scraper](#biosearch_scraper)

## Requirements

To run the web scraping scripts in this repository, ensure that you have the following prerequisites installed:

- Python 3.x
- Libraries: `BeautifulSoup`, `requests`, `pandas`, `Selenium`, `Biopython`

You can install the necessary dependencies using the following command:

```bash
pip install -r requirements.txt
```

## Project Descriptions
### biosearch_scraper

#### Description
This project demonstrates the use of the `Bio.Entrez` API from the Biopython package to extract scientific literature from PubMed. It shows how to interact with an API to retrieve articles based on search queries. The code handles user authentication, retrieves metadata about scientific articles, and processes the data for further analysis.
#### Techonologies used

- `Bio.Entrez` from Biopython for interacting with PubMed API
- `requests` for making authenticated requests to the API
#### Key features

- Scraping scientific literature from PubMed using the Biopython API
- Handling API requests and data extraction
- Processing data for bioinformatics or academic use
#### Running the project

The project is in the biosearch_scraper Jupyter Notebook.

### Ent_1

#### Description

This project demonstrates web scraping from static HTML pages, particularly focusing on scraping help results from Stack Overflow. A generic function `SOS_help` is created, which retrieves relevant help results based on the input provided. The project also includes a function `print_output` for executing and printing Python commands dynamically.

#### Techonologies used
- `BeautifulSoup` for HTML parsing
- `requests` for HTTP requests
#### Key features

- Static page scraping from Stack Overflow
- Dynamic command execution using a helper function `print_output`
#### Running the project

The project is in the Ent_1 Jupyter Notebook.

### Ent_2

#### Description

This example demonstrates scraping data from two separate sources—one from the Spanish National Institute of Statistics (INE) and the other from the European Union (EU). The script extracts data from these two sources, specifically focused on combining the datasets using a common field such as `date`. The extracted data can later be visualized using Power BI or similar tools.

#### Techonologies used
- `requests` for retrieving data from APIs
- `pandas` for data processing
#### Key features
- Scraping structured data from the INE and EU APIs
- Visualization in Power BI
#### Running the project
The project is in the Ent_2 Jupyter Notebook.


