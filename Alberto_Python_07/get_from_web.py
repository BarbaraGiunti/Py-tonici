import urllib.request

url = "https://www.w3.org/TR/PNG/iso_8859-1.txt"
destination_filename = "sample.txt"

urllib.request.urlretrieve(url, destination_filename)