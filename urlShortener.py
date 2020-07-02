# install pyshorteners
# using 'pip install pyshortneres'
import pyshorteners

# replace URL with you url
url = 'URL'

shortURL = pyshorteners.Shortner().tinyurl.short(url)

# printing shortened url
print(f'URL after shortening {shortURL}')
