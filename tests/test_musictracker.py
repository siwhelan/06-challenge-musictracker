from lib.musictracker import *
import pytest


# test an error is raised if an empty string is passed into the add method
def test_error_on_empty_string_input():
    track = MusicTracker()
    with pytest.raises(Exception) as err:
        track.add_track("", "")
    assert str(err.value) == "Missing data! Please check Artist/Title."


# test to make sure the data type is correct - i.e. a string 'artist' and string 'title
# raise an error if the data type is incorrect
def test_error_on_incorrect_data_input():
    track = MusicTracker()
    with pytest.raises(Exception) as err:
        track.add_track("artist 1", 3.5)
    assert str(err.value) == "Incorrect data! Please check Artist/Title."


# check add track adds the correctly given track and artist to the list
def test_add_track_adds_given_track_to_the_tracklist():
    track = MusicTracker()
    track.add_track("Beatles", "Now and Then")
    assert track.tracklist == [("Beatles", "Now and Then")]


# test that list_tracks returns the contents of the tracklist
# when a song has been added
def test_list_tracks_lists_all_of_the_songs_in_the_tracklist():
    track = MusicTracker()
    track.add_track("Beatles", "Now and Then")
    tracklist = track.list_tracks()
    assert tracklist == "Beatles: Now and Then"


# test that list_tracks returns the contents of the tracklist
# when multiple songs have been added
def test_list_tracks_lists_all_of_the_songs_when_multiple_are_added():
    track = MusicTracker()
    track.add_track("Beatles", "Now and Then")
    track.add_track("Queen", "Bohemian Rhapsody")
    track.add_track("U2", "One")
    tracklist = track.list_tracks()
    assert tracklist == "Beatles: Now and Then\nQueen: Bohemian Rhapsody\nU2: One"


# test to alert the user if list_tracks is called on an empty list
def test_handle_empty_tracklist():
    track = MusicTracker()
    assert track.list_tracks() == "List is empty!"
