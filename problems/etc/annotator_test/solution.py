import sys
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
print(BASE_DIR)
sys.path.append(BASE_DIR)

from utils.profiling import profile_time_memory

@profile_time_memory
def decode_secret(url: str) -> None:
    import requests
    from bs4 import BeautifulSoup
    resonse = requests.get(url)
    soup = BeautifulSoup(resonse.text, 'html.parser')
    targets = []
    
    rows = soup.find_all('tr')

    for row in rows:
        cells = row.find_all(["td", "th"])
        values = [cell.get_text() for cell in cells]

        try:
            x = int(values[0])
            y = int(values[2])
            char = values[1]
            targets.append((x, y, char))
        except:
            continue
    
    max_x = max(targets, key=lambda x: x[0])[0]
    max_y = max(targets, key=lambda x: x[1])[1]
    print(max_x, max_y)

    grid = [[' ' for _ in range(max_x + 1)] for _ in range(max_y + 1)]

    for x, y, char in targets:
        grid[y][x] = char

    for y in range(max_y, -1, -1):
        print(''.join(grid[y]))





@profile_time_memory
def othersolution(s1: str, s2: str) -> int:
    pass
        

if __name__ == "__main__":
    # url = 'https://docs.google.com/document/d/e/2PACX-1vTMOmshQe8YvaRXi6gEPKKlsC6UpFJSMAk4mQjLm_u1gmHdVVTaeh7nBNFBRlui0sTZ-snGwZM4DBCT/pub'
    url = 'https://docs.google.com/document/d/e/2PACX-1vSvM5gDlNvt7npYHhp_XfsJvuntUhq184By5xO_pA4b_gCWeXb6dM6ZxwN8rE6S4ghUsCj2VKR21oEP/pub'
    mysolution(url)
    # print(othersolution(s1, s2))
    