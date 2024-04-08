# README
## CompuTrabajo Scraper

This project is a web scraper designed to extract job offers from the CompuTrabajo website. It is built using Python and the Scrapy framework.
This project is solely intended for learning purposes and to demonstrate the usage of the Scrapy framework. It provides a convenient way to extract job offers from the CompuTrabajo website and view them in a clear and accessible manner. The scraped data can be saved either in a CSV file or in a database table.

Please note that this scraper should be used responsibly and in compliance with the terms of service of the CompuTrabajo website.

### Prerequisites

- Python 3
- pip
- scrapy
- sqlalchemy

### Setting Up the Environment

To set up the environment, you need to create a virtual environment and install the necessary packages. You can do this by running the `preparar-venv.sh` script with the package name as an argument. If the virtual environment does not exist, it will be created, and the package will be installed.

```shellscript
./preparar-venv.sh <package-name>

This step is optional, the `preparar-venv.sh` script is a tool that helps you create the virtual environment more easily and install the necessary packages.

```

If you want the scraped data to be saved in a CSV file, you can add the `-o` option followed by the file name to the command:

```shellscript
scrapy crawl listWorks -o filename.csv
```

### Output

The scraped data will be stored in the SQLite database specified in the `settings.py` file. Each row in the database corresponds to a job offer, with fields for the job title, company, location, and more.

### Note

Please ensure to use this scraper responsibly and in accordance with the terms of service of the CompuTrabajo website.
```