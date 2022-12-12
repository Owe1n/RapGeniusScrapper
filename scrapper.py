import lyricsgenius
import os


def read_credentials():
    # Open the file
    with open("credentials.txt", "r") as f:
        # Read the file line by line
        creds = {}
        for line in f:
            # Split the line into key-value pairs
            key, value = line.split("=")
            # Strip any leading or trailing whitespace from the key and value
            key = key.strip()
            value = value.strip()
            # Add the key-value pair to the dictionary
            creds[key] = value
    return creds


def fetch_songs(artist_list, num_songs, main_folder):
    creds = read_credentials()
    genius = lyricsgenius.Genius(creds["GENIUS_ACCESS_TOKEN"])
    genius.remove_section_headers = (
        True  # Remove section headers (e.g. [Chorus]) from lyrics when searching
    )

    for artist in artist_list:
        # Create artist's folder in main folder
        artist_folder = os.path.join(main_folder, artist.replace(" ", "_"))
        if not os.path.exists(artist_folder):
            os.makedirs(artist_folder)

        # Search for artist's songs and save lyrics in individual files
        try:
            artist_songs = genius.search_artist(artist, num_songs)
            try:
                for song in artist_songs.songs:
                    song_file = os.path.join(
                        artist_folder, song.title.replace(" ", "_")
                    )
                    with open(song_file, "w", encoding="utf-8") as f:
                        f.write(song.lyrics)
            except:
                print("Error when writting the song")

        except:
            print("Error: Artist '{}' not found".format(artist))


def main():
    # List of artists
    artist_list = ["Ed Sheeran", "Adele"]

    # Number of songs to fetch for each artist
    num_songs = 5

    # Main folder where all artist folders will be stored
    main_folder = "Results"

    fetch_songs(artist_list, num_songs, main_folder)


if __name__ == "__main__":
    main()
