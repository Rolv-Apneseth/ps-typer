import requests


class FactsApi:
    URL: str = "https://uselessfacts.jsph.pl/random.json?language=en"

    @classmethod
    def get_random_fact(cls) -> dict | None:
        result = None

        try:
            response = requests.get(cls.URL)
            if response.status_code == requests.codes.ok:
                result = response.json()
        except requests.exceptions.RequestException:
            pass

        return result.get("text").replace("`", "'") if result else None
