#demo62

import wikipedia

print(wikipedia.summary("Pythonidae"))
print(wikipedia.search("C++"))

taipei = wikipedia.page("Taipei")
print(taipei.title, taipei.url)
print(taipei.content)