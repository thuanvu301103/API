class Slink1:
    """init api
        Args:
            base_url (str): base url from webserver
            api_url (str): api url to webserver
            api_key (str): api key of the user
    """
    def __init__(self, api_key):  
        self.base_url = 'https://link1s.com/'
        self.api_url = self.base_url + "api?"
        self.api_key = api_key
        

    def req(self, url):     #request to get API
        """requests to api
        Args:
            url (str): api url
        Return:
            (dict): output dic from requests url
        """
        r = requests.get(url)   # get api from webserver
        response = r.json()
        return response
         

    def get_newlink (self, old_link):
        url = f"{self.api_url}api={self.api_key}&url={old_link}.com"
        new_link = self.req(url)["shortenedUrl"]
        return new_link
