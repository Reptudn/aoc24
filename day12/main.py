#!/usr/bin/python3

from sys import argv
from typing import List

# cost = area * perimter
#	area => amount of letters next to each other
#	perimeter => sides of the edges of the field

file_content: list[str] = []

def get_garden_price(x: int, y: int, letter: str) -> int:
	perimeter = 0
	area = 0

	if file_content[x][y] != letter:
		return -1

	def flood_search(x: int, y: int, letter: str) -> None:
		nonlocal perimeter, area
		if x < 0 or y < 0 or x >= len(file_content) or y >= len(file_content[0]):
			print(f"Incrementing perimeter at {x}, {y}")
			print(file_content)
			perimeter += 1
			return
		if file_content[x][y] == ' ':
			print(f"Incrementing perimeter at {x}, {y}")
			print(file_content)
			perimeter += 1
			return
		if file_content[x][y] != letter:
			return

		area += 1
		file_content[x] = file_content[x][:y] + ' ' + file_content[x][y+1:]

		flood_search(x + 1, y, letter)
		flood_search(x - 1, y, letter)
		flood_search(x, y + 1, letter)
		flood_search(x, y - 1, letter)

	flood_search(x, y, letter)

	print(f"Letter: {letter} Area: {area}, Perimeter: {perimeter}")

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

	left = 0
	for line in file_content:
		for letter in line:
			if (letter != ' '):
				print(letter)
				left += 1
	print(f"There are {left} letters left")
	print(f"Second run cost: {str(get_total_cost())}")

if __name__ == "__main__":
	main()