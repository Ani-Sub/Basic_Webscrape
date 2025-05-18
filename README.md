# Basic_Webscrape
Python script that scrapes tables from Google Docs using BeautifulSoup. Extracts X,Y coordinates and characters from a table, then displays them in a text grid at their positions. Includes error handling for network issues and data validation. Creates a 2D visual map by placing each character at its specified coordinate.

Detailed Functionality:

Input Handling:

Prompts the user for a Google Docs URL containing a table
Connects to the specified URL using the requests library


Web Scraping Component:

Uses BeautifulSoup to parse the HTML content from the Google Docs page
Locates the first table in the document regardless of class attributes
Extracts data from the table with the expected structure:

Column 1: X-coordinate (integer)
Column 2: Character (text string)
Column 3: Y-coordinate (integer)




Data Processing:

Skips header row if multiple rows exist
Creates a list of dictionaries, each containing x, y, and character values
Calculates the boundaries of the coordinate system (min/max x and y)
Handles value conversion and validation


Visualization:

Creates a properly sized 2D grid based on coordinate boundaries
Normalizes coordinates to fit within the grid
Places each character at its corresponding position
Renders the result as a text-based grid in the console
Inverts the Y-axis so larger Y values appear higher in the grid


Error Handling:

Manages network connection issues
Validates table structure and presence
Checks for valid coordinate data
Ensures proper grid dimensions



This script is designed to transform tabular coordinate data into a meaningful visual representation, potentially revealing hidden messages, ASCII art, or character maps that are defined by their positions in a coordinate system.
