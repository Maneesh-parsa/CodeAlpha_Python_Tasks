def stock_portfolio():
    stock_prices = {"AAPL": 180, "TSLA": 250, "GOOG": 2700, "AMZN": 3400}
    portfolio = {}
    total_investment = 0

    print("\nEnter your stock portfolio:")
    while True:
        stock = input("Enter stock symbol (or 'done' to finish): ").upper()
        if stock == 'DONE':
            break
        if stock in stock_prices:
            qty = int(input(f"Enter quantity of {stock}: "))
            portfolio[stock] = qty
            total_investment += stock_prices[stock] * qty
        else:
            print("Invalid stock symbol.")

    print("\nPortfolio Summary:")
    for stock, qty in portfolio.items():
        print(f"{stock}: {qty} shares @ ${stock_prices[stock]} each")
    print("Total Investment: $", total_investment)

    with open("portfolio.txt", "w") as f:
        for stock, qty in portfolio.items():
            f.write(f"{stock}: {qty} shares @ ${stock_prices[stock]} each\n")
        f.write(f"Total Investment: ${total_investment}\n")