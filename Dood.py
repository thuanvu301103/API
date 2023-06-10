import requests     # for send requests to the webserver

class Doods:

    def __init__(self, api_key):
        """init api
        Args:
            base_url (str): base url from webserver
            api_url (str): api url to webserver
            api_key (str): api key of the user
            """
        self.base_url = 'https://doodstream.com/'
        self.api_url = self.base_url + "api/"
        self.api_key = api_key 


    def req(self, url):     #request to get API
        """requests to api
        Args:
            url (str): api url
        Return:
            (dict): output dic from requests url"""
        try:
            r = requests.get(url)   # get url for uploading
            response = r.json()
            if response["msg"] == "Wrong Auth":
                sys.exit("Invalid API key, please check your API key")
            else:
                return response
        except ConnectionError as e:
            sys.exit(f"ERROR : {e}")


    def local_upload(self, path):
        """Upload from local storage
        Args:
            path (str): path to file
        Retunr:
            file_id/file code of uploaded video
        """
        url = f"{self.api_url}upload/server?key={self.api_key}"
        url_for_upload = self.req(url)["result"]
        
        post_data = {"api_key": self.api_key}
        filename = path.split('/')[-1]
        post_files = {"file": (filename, open(path, "rb"))}
        
        res = requests.post(url_for_upload,data=post_data, files=post_files).json()
        if res["msg"] == "OK":
            self.file_id = res["result"][0]["filecode"]
            return self.file_id
        else:
            raise TypeError(
                f"unsupported video format {filename}, please upload video with mkv, mp4, wmv, avi, mpeg4, mpegps, flv, 3gp, webm, mov, mpg & m4v format"
            )


    def get_link(self):
        # get uploaded video
        return (self.base_url + 'd/' + self.file_id)
