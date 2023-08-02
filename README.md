# currency_converter


In this program, we use the CurrencyRates class from the forex-python library to perform currency conversion. The currency_converter function takes three parameters: the amount, the source currency code, and the target currency code. It returns the converted amount based on the real-time exchange rates.

Run the script, and it will prompt you to enter the amount and the source and target currency codes. The program will then calculate and display the converted amount.

Keep in mind that the accuracy of the conversion depends on the real-time exchange rates provided by the API. You may need to have an internet connection to fetch the latest rates.

Currency Converter in Python
Introduction
Welcome to the Currency Converter Python program! This program allows you to convert currency using real-time exchange rates. It utilizes the forex-python library to fetch exchange rate data from various sources like Open Exchange Rates.

Requirements
This program requires Python 3.x and the forex-python library to run.

How to Install Dependencies
If you don't have Python installed, you can download it from the official Python website (https://www.python.org/downloads/).

You can install the forex-python library using pip. Open your terminal or command prompt and run the following command:

Copy code
pip install forex-python
How to Run the Program
Clone or download the repository to your local machine.
Navigate to the project directory containing the Python script (currency_converter.py).
Run the currency_converter.py script using the following command:
Copy code
python currency_converter.py
The program will start, prompting you to enter the amount, source currency code, and target currency code.
The converted amount will be displayed based on real-time exchange rates.
Program Description
The currency_converter function uses the CurrencyRates class from the forex-python library to perform currency conversion. It takes three parameters:

amount: The amount of money you want to convert.
from_currency: The currency code of the source currency (e.g., USD, EUR, INR).
to_currency: The currency code of the target currency (e.g., USD, EUR, INR).
Example Usage
mathematica
Copy code
Currency Converter

Enter the amount: 100
Enter the currency code of the source currency (e.g., USD, EUR, INR): USD
Enter the currency code of the target currency (e.g., USD, EUR, INR): EUR
100.00 USD is equal to 85.94 EUR

Customization

If you want to modify the currency data source, you can explore the options available in the forex-python library and change the source in the currency_converter function.
