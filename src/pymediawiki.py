# src/pymediawiki_demo.py 

from mediawiki import MediaWiki
from bs4 import BeautifulSoup

nethack = MediaWiki("https://nethackwiki.com/w/api.php")
# print(nethack.__dir__())
knight_search = nethack.search("Knight")
print(knight_search)
knight = nethack.page(knight_search[2])
print(knight.__dict__)

print("\n")

# print(type(knight.html))
# print(knight.html)

print("\n")

knight_soup = BeautifulSoup(knight.html, "html.parser")
knight_lists = knight_soup.find_all("li")

print(knight_lists)

print("\n")
