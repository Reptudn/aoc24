#!/usr/bin/python3

from sys import argv
from typing import List

# cost = area * perimter
#	area => amount of letters next to each other
#	perimeter => sides of the edges of the field

file_content: List[str] = []

# replace the letter when found with a space
def get_garden_price(x: int, y: int, letter: str) -> int:
	if file_content[x][y] != letter:
		return -1

	perimeter: int = 0
	area: int = 0

	def flood_search(x: int, y: int, letter: str) -> None:
		nonlocal perimeter, area
		if x < 0 or x >= len(file_content):
			return
		if y < 0 or y >= len(file_content[x]):
			return
		if file_content[x][y] != letter:
			return

		row = list(file_content[x])
		row[y] = ' '
		file_content[x] = ''.join(row)
		area += 1

		if x + 1 >= len(file_content) or file_content[x + 1][y] != letter:
			perimeter += 1
		if x - 1 < 0 or file_content[x - 1][y] != letter:
			perimeter += 1
		if y + 1 >= len(file_content[x]) or file_content[x][y + 1] != letter:
			perimeter += 1
		if y - 1 < 0 or file_content[x][y - 1] != letter:
			perimeter += 1

		flood_search(x + 1, y, letter)
		flood_search(x - 1, y, letter)
		flood_search(x, y + 1, letter)
		flood_search(x, y - 1, letter)

	flood_search(x, y, letter)

	return perimeter * area

def get_total_cost() -> int:
	cost: int = 0
	for x in range(len(file_content)):
		for y in range(len(file_content[x])):
			if file_content[x][y] != ' ':
				cost += get_garden_price(x, y, file_content[x][y])
	return cost


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
	print(f"Total cost: {str(get_total_cost())}")

if __name__ == "__main__":
	main()