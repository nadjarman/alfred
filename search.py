'''
By: Arman Nadjarian

this file is meant to contain the code associated 
with alfred's google searching capabilities.
'''
import webbrowser


def open_google():
    print("Opening Google...")
    webbrowser.open("https://google.com", new=2)

def search_for(term: str):
    google_search = "https://www.google.com/search?q=" + term

    print(f"Opening Google and searching for \"{term}\"...")
    webbrowser.open(google_search, new=2)