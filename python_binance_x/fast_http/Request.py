# TODO error checking
class Request:
    def __init__(self, url: str, protocol: str = 'https', method: str = 'GET', headers: dict = None, body=None):
        self.protocol = protocol
        self.method = method
        self.url = url
        self.headers = headers
        self.body = body
        self._parse_url(url)
        self._verify_method()

    def _verify_method(self):
        if self.method != 'GET' and self.method != 'POST':
            raise SyntaxError(self.method+' is not a defined method.')

    def _parse_url(self, url: str):
        url = url.split('://')
        if len(url) > 1:
            self.protocol = url[0]
        url = url[1].partition('/')
        self.host = url[0]
        self.path = '/'+url[2]
