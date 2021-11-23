class Song:
    """create a new song

    Attributes:
        title (str): name of the song
        artist (Artist): maker of the song
        duration (minutes): length of the song
    """

    def __init__(self, title, artist, duration) -> None:
        """initializes a song
        
        Args:
            title (str): name of the song
            artist (Artist): maker/creator of song
            duration (minutes): length of a song
        """

        self.title = title
        self.artist = artist
        self.duration = duration


class Album:
    """Reperesented by songs tracklist
    
    Attributes:
        album_name (str): name of the album
        year (int): year in which album was released
        artist (Artist): creator of a album. If not specified then default will be 'Various artists'
        tracks (List[Song]): numbers of songs on album

    Methods:
        add_song(Song): will add a new song to album track list
    """

    def __init__(self, name, year, aritst=None) -> None:
        self.name = name
        self.year = year
        if aritst is None:
            self.aritst = Artist("Various atists")
        else:
            self.aritst = aritst
        self.tracks = []

    def add_song(self, song, position=None):
        """Adds a song to the tracklist
        
        Args:
            song (Song): new song object
            position [optional]: If specified, will be added in that position. 
                                Otherwise added to theend of the list
        """
        if position is None:
            self.tracks.append(song)
        else:
            self.tracks.insert(position, song) 

class Artist:
    """Maker/creator of the album(s)/song(s)
    
    Argruments:
        name (str): name of the artist
        album (List[Album]): artist list of albums
        
    Methods:
        add_album: adds a new album to the album list
    """

    def __init__(self, name) -> None:
        self.name = name
        self.album = []

    def add_album(self, album):
        """adds new album to the album list
        
        Args:
            album (Album): add Album object to the list
        """
        self.album.append(album)
    
def load_data():
    new_artist = None
    new_album = None
    album_list = []

    with open("./song-project/albums.txt", 'r') as albums:
        for line in albums:
            # reading line by line  artist_field, album_field, year_field, song_field
            artist_field, album_field, year_field, song_field = tuple(line.strip('\n').split('\t'))
            print(artist_field, album_field, year_field, song_field)


load_data()







        