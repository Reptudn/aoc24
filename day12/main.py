#!/usr/bin/python3

import os
import fileinput
from sys import argv

# cost = area * perimter
#	area => amount of letters next to each other
#	perimeter => sides of the edges of the field

file_content: list[str] = []

# replace the letter when found with a space
def get_garden_price(x: int, y: int, letter: str) -> int:
	if file_content[x][y] != letter:
		print(f"{letter} not at x={x} Y={y}")
		return -1
	
	perimeter: int = 0
	area: int = 0

	def flood_search(x: int, y: int, letter: str) -> None:
		if x < 0 or x > len(file_content):
			return
		if y < 0 or y > len(file_content[x]):
			return
		# implement logic... gotta exit the train now lol

	return perimeter * area

def get_total_cost() -> int:
	# get cost until the file_content is all space
	return -1


def get_file_content(path: str) -> None:
	with open(path, 'r') as file:
		for line in file:
			file_content.append(line.strip())


def main():
	if len(argv) != 2:
		print("Only argument allowed is the filepath")
		return
	get_file_content(argv[1])
	if not len(file_content):
		print("Failed to read or get file contents")
		return
	print(file_content)
	

if __name__ == "__main__":
	main()