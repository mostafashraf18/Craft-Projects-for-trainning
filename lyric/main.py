import warnings
from bs4 import GuessedAtParserWarning

import os
import sqlite3

# Checks the existance of PyLyrics
def import_PyLyrics():
	try:
		import PyLyrics
	except ImportError:
		print_songs("Error importing PyLyrics")
		print("Make sure you install the librarie using: \"pip install PyLyrics\"")
		quit()

import_PyLyrics()
from PyLyrics import *

conn = sqlite3.connect("lyrics.db")
c = conn.cursor()
songs = ""

#c.execute("""CREATE TABLE lyrics (
 #             artist text,
  #            title text,
   #           lyrics text
#)""")


# clear screen
def cls():
    os.system("cls" if os.name=="nt" else "clear")

# Menu commands
def get_input(text):
	user_input = input(text)
	if user_input in ["home", "menu", "back"]:
		menu()
	if user_input == "quit":
		quit()
	return user_input

# Adds song to the database
def add_song():
	print("--- Add song ---\n")

	artist = get_input("Artist: ")
	title = get_input("Title: ")

	print("Downloading lyrics")
	lyrics = does_song_exist(artist, title)

	if lyrics != False:
		c.execute("INSERT INTO lyrics VALUES (:artist, :title, :lyrics)", {"artist": artist.title(), "title": title.title(), "lyrics": lyrics})
		conn.commit()
		print("Song Downloaded")
	else:
		print("sorry, unable to find that song")

# Removes song from the database
def remove_song():
	print("--- Remove song ---\n")

	print_songs()

	user_input = get_input("Song number: ")
	if user_input.isdigit():
		if int(user_input) > 0 and int(user_input) <= len(songs):
			c.execute("DELETE FROM lyrics WHERE artist=:artist AND title=:title", {"artist": songs[int(user_input) - 1][0], "title": songs[int(user_input) - 1][1]})
			conn.commit()
			print("Song removed")

			return

	print("sorry, not sure what you mean")

# Checks if song exists
def does_song_exist(artist, title):
	try:
		lyrics = PyLyrics.getLyrics(artist, title)

		if "not licensed to display the full lyrics" in lyrics:
			return False

		return lyrics
	except ValueError:
		return False

# Prints the songs in a table
def print_songs():

	first_row = ["NUMBER", "ARTIST", "TITLE", "AMOUNT OF WORDS"]

	numbers = list(str(number + 1) for number in range(0, len(songs)))
	artists = list(artist[0] for artist in songs)
	titles = list(title[1] for title in songs)
	words = list(str(len(lyric[2].split(" "))) for lyric in songs)

	biggest = [
		len(str(max(numbers + [first_row[0]], key=len))), # number
		len(str(max(artists + [first_row[1]], key=len))), # artist
		len(str(max(titles + [first_row[2]], key=len))), # title
		len(str(max(words + [first_row[3]], key=len)))] # amount of words

	song_info = list(([numbers[i], artists[i], titles[i], words[i]] for i in range(0, len(songs))))

	rows = []
	for song in [first_row] + song_info:
		row = []
		for i in range(0, len(song)):
			space = int((biggest[i] - len(str(song[i]))) / 2) + 1
			
			text = (" "*space + str(song[i]) + " "*space)
			
			if len(text) != biggest[i] + 2:
				text = text + " "

			row.append(text)
		rows.append("|" + "|".join(row) + "|")


	line = "\n|" + "-"*(len(rows[0]) - 2) + "|\n"
	print(line.replace("|", "+") + line.join(rows) + line.replace("|", "+"))

# Get user to choose song, then prints it
def choose_song():
	print("--- Songs ---")
	print_songs()
	user_input = get_input("Song number: ")

	if user_input.isdigit():
		if int(user_input) > 0 and int(user_input) <= len(songs):
			cls()
			print(songs[int(user_input) - 1][2])
			return

	print("sorry, not sure what you mean")

# Main menu
def menu():
	global songs
	options = {"Songs": choose_song, "Add song": add_song, "Remove song": remove_song}
	option_list = list((str(list(options).index(option) + 1) + ". " + option for option in list(options)))
	
	cls()
	while True:

		c.execute("SELECT * FROM lyrics")
		songs = c.fetchall()
		conn.commit()


		print("""
 _            _            _                     _                 _           
| |_   _ _ __(_) ___    __| | _____      ___ __ | | ___   __ _  __| | ___ _ __ 
| | | | | '__| |/ __|  / _` |/ _ \\ \\ /\\ / / '_ \\| |/ _ \\ / _` |/ _` |/ _ \\ '__|
| | |_| | |  | | (__  | (_| | (_) \\ V  V /| | | | | (_) | (_| | (_| |  __/ |   
|_|\\__, |_|  |_|\\___|  \\__,_|\\___/ \\_/\\_/ |_| |_|_|\\___/ \\__,_|\\__,_|\\___|_|   
   |___/                                                                       		
By Mostafa AShraf\n""")

		print("\n".join(option_list))
		option = get_input("")
		if option.isdigit():
			option = int(option)
			if option >= 0 and option <= len(options):
				cls()
				options[list(options)[int(option) - 1]]()

				input("\nPress enter to continue")
		cls()

if __name__ == "__main__":
	menu()