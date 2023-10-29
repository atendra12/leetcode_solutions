class Codec:

    def __init__(self):
        self.list = []

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        self.list.append(longUrl)
        index = self.list.index(longUrl)
        return "http://tinyurl.com/" + str(index)
        
    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        index = shortUrl.split("/")[-1]
        return self.list[int(index)]
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))