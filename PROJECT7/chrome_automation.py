import webbrowser as wb



chrome_path = "C:\Program Files\Google\Chrome\Application\chrome.exe"
wb.register('chrome', None,wb.BackgroundBrowser(chrome_path))


def webauto():
    chrome_path = "C:\Program Files\Google\Chrome\Application\chrome.exe"
    URLS = {
        "stackoverflow.com",
        "gmail.com",
        "google.com",
        "youtube.com"
    }

    for url in URLS:
        print('opening :'+ url)
        wb.get("chrome").open(url)


webauto()