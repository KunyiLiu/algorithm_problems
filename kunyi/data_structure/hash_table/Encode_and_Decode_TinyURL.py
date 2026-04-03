class Codec:
    def __init__(self):
        self.BASE62 = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.counter = 1
        
        self.code_to_url = {}
        self.url_to_code = {}  # handle duplicate URLs

    def _encode_base62(self, num: int) -> str:
        """Convert integer to Base62 string"""
        if num == 0:
            return self.BASE62[0]
        
        chars = []
        while num > 0:
            num, rem = divmod(num, 62)
            chars.append(self.BASE62[rem])
        
        return ''.join(reversed(chars))

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL."""
        
        # ✅ Return existing mapping if already encoded
        if longUrl in self.url_to_code:
            return self.url_to_code[longUrl]
        
        short_code = self._encode_base62(self.counter)
        self.counter += 1
        
        self.code_to_url[short_code] = longUrl
        self.url_to_code[longUrl] = short_code
        
        # Optional: simulate real TinyURL
        return short_code  # or "http://tinyurl.com/" + short_code

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL."""
        return self.code_to_url.get(shortUrl, "")
