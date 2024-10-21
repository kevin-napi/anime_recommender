import pandas as pd

def main():
    df = pd.read_csv('anime.csv')

    all_genres = df['genre'].str.split(',').explode().str.strip().str.lower()
    ani_genres = all_genres.unique().tolist()

    all_types = df['type'].str.split(',').explode().str.strip().str.lower()
    ani_types = all_types.unique().tolist()

    ep_amount = df['episodes']

    amount_no_unknown = df[df.episodes != "Unknown"]['episodes']
    max_amount_episodes = amount_no_unknown.max()


    ani_dict = df.to_dict(orient='records')

    user_genre = input("Welcome to Anime Recommendations\nPlease enter a genre: ").lower()



    user_type = input("Please enter the type (Movie, TV, OVA, Special): ").lower()
    user_type.split(',') # list

    for anime in ani_dict:
        if isinstance(anime['genre'], str):
            genres = [genre.strip().lower() for genre in anime['genre'].split(',')] # list of genres
    
            if user_genre in genres:
                if isinstance(anime['type'], str) and anime['type'].lower() == user_type:
                    print(anime['name'])
                
                
if __name__ == "__main__":
    main()