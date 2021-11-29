import pyshorteners

url = input("Enter url: ")

print("URL after shortening :- ", pyshorteners.Shortener().tinyurl.short(url))

