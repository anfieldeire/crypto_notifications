import json, ast


with open('portfolio1.txt') as f:
    contents = f.read()
    portfolio_amounts = ast.literal_eval(contents)
    print(portfolio_amounts)
    print(type(portfolio_amounts))
    # portfolio_amounts = ast.literal_eval(contents)
    # print(portfolio_amounts)
