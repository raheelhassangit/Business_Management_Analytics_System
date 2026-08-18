import requests


class Quote:

    def fetch_random_quote(self):
        url = "https://api.freeapi.app/api/v1/public/quotes/quote/random"

        try:
            response = requests.get(url, timeout=5)
            response.raise_for_status()

            data = response.json()

            if data.get("success") and "data" in data:
                content = data["data"].get("content")
                author = data["data"].get("author", "Unknown")

                if content:
                    return f'"{content}" - {author}'

            return "Unable to fetch a quote at the moment."

        except requests.RequestException:
            return "Unable to connect to the quote service."

        except (ValueError, KeyError, TypeError):
            return "Invalid response received from the quote service."