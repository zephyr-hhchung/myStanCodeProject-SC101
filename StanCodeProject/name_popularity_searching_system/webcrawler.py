"""
File: webcrawler.py
Name: Hui-Hsuan Chung
--------------------------
This file collects more data from
https://www.ssa.gov/oact/babynames/decades/names2010s.html
https://www.ssa.gov/oact/babynames/decades/names2000s.html
https://www.ssa.gov/oact/babynames/decades/names1990s.html
Please print the number of top200 male and female on Console
You should see:
---------------------------
2010s
Male Number: 10890537
Female Number: 7939153
---------------------------
2000s
Male Number: 12975692
Female Number: 9207577
---------------------------
1990s
Male Number: 14145431
Female Number: 10644002
"""

import requests
from bs4 import BeautifulSoup


def main():
    for year in ['2010s', '2000s', '1990s']:
        print('---------------------------')
        print(year)
        url = 'https://www.ssa.gov/oact/babynames/decades/names'+year+'.html'    # Inspected website for baby names
        response = requests.get(url)               # Send a request to the website
        html = response.text                       # The html source code of the requested website
        soup = BeautifulSoup(html, 'html.parser')  # Pass the html code into the BeautifulSoup constructor
        # ----- Write your code below this line ----- #
        items = soup.find_all(['tbody', 'tr'])   # Select the tags with 'tbody' and 'tr'
        num_male = 0                             # Variable to store the male baby number
        num_female = 0                           # Variable to store the female baby number
        for item in items:                                 # Inspect every lines
            target = item.text.split('\n')[1].split(' ')   # Parse the text into male name/number, female name/number
            if len(target) == 4:                           # The required info should be parsed into a 4-item list
                if ',' in target[1] and ',' in target[3]:  # Deal with the ',' in the male and female number (string)
                    # By splitting and recalculating the number: '182,993' -> 182 * 1000 + 993
                    num_male += int(target[1].split(',')[0])*1000+int(target[1].split(',')[1])
                    num_female += int(target[3].split(',')[0])*1000+int(target[3].split(',')[1])
                else:
                    print('Either the male or female baby number is below 1,000. Need to adjust the code!')
        print(f"Male Number: {num_male}")
        print(f"Female Number: {num_female}")


if __name__ == '__main__':
    main()
