import requests


class NewsFeed:

    """
    This class will fetch the data using api call from newsapi
    """

    base_url="https://newsapi.org/v2/everything?"
    api_key="04f8b0a684134d00be9580eb6fe0bcd8"
    def __init__(self,interest,language,to_date,from_date):
        self.from_date=from_date
        self.to_date=to_date
        self.interest=interest
        self.language=language

    def get(self):
        
        """
        This method will fetch the data that is interested to the person and returns the needed content
        """

        url=self.base_url+"qInTitle="+self.interest+"&from="+self.from_date+"&to="+self.to_date+"&language="+self.language+"&sortBy=publishedAt&apiKey="+self.api_key
        response=requests.get(url)
        content=response.json()
        articles=content["articles"]
        email_body=""
        for article in articles:
            email_body+=article["title"]+"\n"+article["url"]+"\n\n"
        return email_body



# https://newsapi.org/v2/everything?q=tesla&from=2022-11-19&sortBy=publishedAt&apiKey=04f8b0a684134d00be9580eb6fe0bcd8
