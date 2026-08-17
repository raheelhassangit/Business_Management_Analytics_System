import requests


def fetch_random_quote():
    url = "https://api.freeapi.app/api/v1/public/quotes/quote/random"

    response = requests.get(url)
    data = response.json()

    if data["success"] and "data" in data:
        content = data["data"]["content"]
        author = data["data"]["author"]

        return f'"{content}" - {author}'


def main():
    try:
        quote = fetch_random_quote()
        print(quote)

    except Exception as e:
        print("An error occurred while fetching the quote:", str(e))


if __name__ == "__main__":
    main()