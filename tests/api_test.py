from API.qoute_api import Quote

def main():
    Quote_obj = Quote()
    quote = Quote_obj.fetch_random_quote()
    print(quote)

    
if __name__ == "__main__":
    main()    