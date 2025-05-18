from bs4 import BeautifulSoup
import requests

try:
    # get the URL of the Google Docs page from the user
    url = input("Enter the URL of the Google Docs page: ")
    page_scrape = requests.get(url)
    # check if the request was successful
    page_scrape.raise_for_status()
    
    # parse the HTML content of the page
    soup = BeautifulSoup(page_scrape.text, "html.parser")
    
    # find ALL tables, regardless of class
    tables = soup.find("table")
    if not tables:
        print("No tables found on the page.")
        exit()
    
    # finds all rows in the table
    rows = tables.find_all("tr")
    if not rows:
        print("No rows found in the tables.")
        exit()
    
    # create a list to store the positions of the characters
    # each position is a dictionary with x, y coordinates and the character
    pos = []

    #skip the first row (header) if there are multiple rows
    row_start = 1 if len(rows) > 1 else 0

    # iterate through the rows and find the cells
    for row in rows[row_start:]:
        cells = row.find_all("td")
        if not cells:
            print("No cells found in the rows.")
            exit()

        if len(cells) >= 3:
            try:
                # extract the text from the first three cells
                x_coord = int(cells[0].get_text(strip=True))
                char = cells[1].get_text(strip=True)
                y_cord = int(cells[2].get_text(strip=True))

                # append the extracted text to the list
                pos.append({'x': x_coord, 'y': y_cord, 'char': char})
            except (IndexError, ValueError):
                print("Invalid data in the table.")
                exit()
            except ValueError:
                continue
            
    if not pos:
        print("No valid data found in the table.")
        exit()

    # find the minimum and maximum x and y coordinates
    # this is to find the bounding box of the characters
    min_x = min(p['x'] for p in pos)
    max_x = max(p['x'] for p in pos)
    min_y = min(p['y'] for p in pos)
    max_y = max(p['y'] for p in pos)

    # create a grid of the appropriate size
    width = max_x - min_x + 1
    height = max_y - min_y + 1
    if width <= 0 or height <= 0:
        print("Invalid grid size.")
        exit()

    # fill the grid with spaces
    # and place the characters in their respective positions
    grid = [[' ' for _ in range(width)] for _ in range(height)]
    for p in pos:
        x = p['x'] - min_x
        y = max_y - p['y']
        grid[y][x] = p['char']

    # print the grid
    for row in grid:
        print(''.join(row))


except requests.exceptions.RequestException as e:
    print(f"Error fetching the page: {e}")
except Exception as e:
    print(f"An error occurred: {e}")