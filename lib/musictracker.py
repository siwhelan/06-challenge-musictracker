class MusicTracker:
    def __init__(self):
        self.tracklist = []

    # simple data validation
    def add_track(self, artist, title):
        if not isinstance(artist, str) or not isinstance(title, str):
            raise Exception("Incorrect data! Please check Artist/Title.")
        if artist.strip() == "" or title.strip() == "":
            raise Exception("Missing data! Please check Artist/Title.")
        self.tracklist.append((artist, title))

    def list_tracks(self):
        if not self.tracklist:
            return "List is empty!"
        return "\n".join([f"{artist}: {title}" for artist, title in self.tracklist])
