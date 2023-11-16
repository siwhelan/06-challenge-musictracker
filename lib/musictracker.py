class MusicTracker:
    def __init__(self):
        self.tracklist = []

    # simple data validation
    def add_track(self, artist, title):
        if not isinstance(artist, str) or not isinstance(title, str):
            raise Exception("Incorrect data! Please check Artist/Title.")

        if artist.strip() == "" or title.strip() == "":
            raise Exception("Missing data! Please check Artist/Title.")

        # add the given track to the tracklist if it is formatted correctly
        self.tracklist.append((artist, title))

    def list_tracks(self):
        # check the tracklist has contents, alert the user if not
        if not self.tracklist:
            return "List is empty!"

        # return the full list of tracks, formatted in an easy to read style.
        return "\n".join([f"{artist}: {title}" for artist, title in self.tracklist])
