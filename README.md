# Website Availability Checker
This Python script checks the availability of a list of websites and writes to a log file if a site is down. It uses the requests library to send HTTP requests to the specified websites and checks the status code of the response to determine if the site is up or down.

## Prerequisites

- Python 3
- requests library

## Installation

- Clone the repository or download the script file.
- Install requests library using pip command: `pip install requests`

## Usage

- Update the `sites` list in the `checkSite()` function with the websites you want to monitor.
- Run the script using command line or any Python IDE.
- The script will check the websites at the interval specified in the `schedule.every()` function. By default, the script checks every 5 seconds.
- If a website is down, the script will print a message to the console and write an entry to the `logfile.txt` file with the date, time, and error code.

## License

This project is licensed under the MIT License. See the LICENSE file for details.
