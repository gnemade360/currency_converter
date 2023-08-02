First, you need to install the forex-python library using pip. If you don't have it installed, run the following command:

Copy code
pip install forex-python

from forex_python.converter import CurrencyRates

def currency_converter(amount, from_currency, to_currency):
    c = CurrencyRates()
    converted_amount = c.convert(from_currency, to_currency, amount)
    return converted_amount

def main():
    print("Currency Converter")

    amount = float(input("Enter the amount: "))
    from_currency = input("Enter the currency code of the source currency (e.g., USD, EUR, INR): ").upper()
    to_currency = input("Enter the currency code of the target currency (e.g., USD, EUR, INR): ").upper()

    converted_amount = currency_converter(amount, from_currency, to_currency)

    print(f"{amount:.2f} {from_currency} is equal to {converted_amount:.2f} {to_currency}")

if __name__ == "__main__":
    main()
