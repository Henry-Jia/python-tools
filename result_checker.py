#!/usr/bin/env python3

# result_checker.py
# This helper file helps you scrape for result notification on your university website
# As in my university, it was quite difficult to know at what time the semester results
# were going to be declared, so I wrote this helper file to notify me on my Ubuntu desktop.
# This has to be a little bit more modified for other OS to be supported.

# WARNING: Before running the script, change the URL_TO_SCRAPE to the url you want

import os
import re
import time
from urllib import request, error
from platform import platform


class ResultChecker:
	# Constants
	URL_TO_SCRAPE = "URL_TO_SCRAPE"
	PATTERN_TO_MATCH = "PATTERN_TO_MATCH"
	SUCCESS = "SUCCESS"
	NOT_AVAILABLE = "NOT_AVAILABLE"
	SLEEP_TIME = "SLEEP_TIME"
	SUCCESS_HEADER = "SUCCESS_HEADER"
	NOT_AVAILABLE_HEADER = "NOT_AVAILABLE_HEADER"
	NETWORK_ISSUE = "NETWORK_ISSUE"
	UNABLE_TO_CONNECT = "UNABLE_TO_CONNECT"

	_CONSTANTS = {
		"PATTERN_TO_MATCH": "B.E. 5th Semester",
		"SUCCESS": "The results are available",
		"NOT_AVAILABLE": "The result is not available, yet!",
		"SLEEP_TIME": 900,
		"NOT_AVAILABLE_HEADER": "Result is not declared yet",
		"SUCCESS_HEADER": "Result Declared",
		"NETWORK_ISSUE": "Network Error!",
		"UNABLE_TO_CONNECT": "Unable to connect!"
	}

	# Initialize the module with the url to scrape
	def __init__(self, url):
		self._CONSTANTS["URL_TO_SCRAPE"] = url

	# Check for results
	def check_for_result(self):
		# Loop infinitely until quit is called
		while True:
			try:
				# Scrape the html downloaded and convert it to string
				html_dump = str(request.urlopen(self._CONSTANTS[self.URL_TO_SCRAPE]).read())

				# Match the html scraped to the pattern using re
				string_match = re.findall(self._CONSTANTS[self.PATTERN_TO_MATCH].strip(), html_dump)
				if len(string_match) == 0:
					os.system("notify-send {} {}".format(self._CONSTANTS[self.NOT_AVAILABLE], self._CONSTANTS[self.NOT_AVAILABLE_HEADER]))

					# if the result is not available, let the script sleep for given time (in seconds)
					time.sleep(self._CONSTANTS[self.SLEEP_TIME])
				else:
					os.system("notify-send {} {}".format(self._CONSTANTS[self.SUCCESS], self._CONSTANTS[self.SUCCESS_HEADER]))
					quit()
			except error.URLError:
				# If a network issue occurs
				os.system("notify-send {} {}".format(self._CONSTANTS[self.NETWORK_ISSUE], self._CONSTANTS[self.UNABLE_TO_CONNECT]))
				quit()


if __name__ == '__main__':
	try:
		if 'ubuntu' in platform().lower():
			url_to_scrape = "https://www.rgpv.ac.in/"
			result_checker_object = ResultChecker(url_to_scrape)
			result_checker_object.check_for_result()
		else:
			raise RuntimeError("This is not an ubuntu based system. Please run this script on ubuntu based system.")
	except KeyboardInterrupt:
		quit("Exiting system on keyboard interrupt")
	except RuntimeError as error:
		quit(str(error))
