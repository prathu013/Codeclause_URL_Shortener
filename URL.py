import pyshorteners
import string

class URLShortener:
    def __init__(self):
        self.url_mapping = {}  # To store long URLs with their shortened versions
        self.id_counter = 1  # Unique ID for each URL
        self.base62_chars = string.ascii_letters + string.digits  # Base62 character set (a-zA-Z0-9)

    def encode(self, id):
        """Encodes a numeric ID to a base62 string."""
        if id == 0:
            return self.base62_chars[0]
        base62 = []
        while id > 0:
            remainder = id % 62
            base62.append(self.base62_chars[remainder])
            id = id // 62
        return ''.join(reversed(base62))

    def decode(self, short_url):
        """Decodes a base62 string back to a numeric ID."""
        id = 0
        for char in short_url:
            if 'a' <= char <= 'z':
                id = id * 62 + ord(char) - ord('a')
            elif 'A' <= char <= 'Z':
                id = id * 62 + ord(char) - ord('A') + 26
            elif '0' <= char <= '9':
                id = id * 62 + ord(char) - ord('0') + 52
        return id

    def shorten(self, long_url):
        """Generates a shortened URL for the given long URL using the custom algorithm."""
        short_url = self.encode(self.id_counter)
        self.url_mapping[short_url] = long_url
        self.id_counter += 1
        return short_url

    def retrieve(self, short_url):
        """Retrieves the long URL associated with the shortened URL."""
        return self.url_mapping.get(short_url, "URL not found!")


def shorten_url_with_service(long_url):
    """Shortens the URL using a third-party service like TinyURL."""
    s = pyshorteners.Shortener()
    short_url = s.tinyurl.short(long_url)
    return short_url


def main():
    print("Choose URL shortening method:")
    print("1. Use third-party service (TinyURL)")
    print("2. Use custom algorithm (Base62 Encoding)")
    choice = input("Enter your choice (1/2): ")

    long_url = input("Enter the long URL: ")

    if choice == "1":
        # Use the third-party service to shorten the URL
        short_url = shorten_url_with_service(long_url)
        print(f"Shortened URL using service: {short_url}")
    
    elif choice == "2":
        # Use the custom algorithm to shorten the URL
        shortener = URLShortener()
        short_url = shortener.shorten(long_url)
        print(f"Shortened URL using custom algorithm: {short_url}")
        retrieved_url = shortener.retrieve(short_url)
        print(f"Original URL retrieved from short URL: {retrieved_url}")
    
    else:
        print("Invalid choice! Please select 1 or 2.")

if __name__ == "__main__":
    main()
