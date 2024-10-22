from jikanpy import Jikan

# Fetch anime title
def fetch_ani_title(title):
    jikan = Jikan()
    
    try:
        result = jikan.search('anime', title)
        return result['results'][0]
    except Exception as e:
        print(f"Error from Jikan API: {e}")
        return None