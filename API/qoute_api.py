import requests


class Quote:
    def fetch_random_quote(self):
        url = "https://api.freeapi.app/api/v1/public/quotes/quote/random"

        response = requests.get(url)
        data = response.json()

        if data["success"] and "data" in data:
            content = data["data"]["content"]
            author = data["data"]["author"]

            return f'"{content}" - {author}'

