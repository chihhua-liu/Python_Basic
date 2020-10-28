# pip install ipython jupyter jupyterlab
#jupyter-notebook
cd C:\Users\Admin\PycharmProjects\BDPY1026
##
import wikipedia

print(wikipedia.summary("Pythonidae"))
print(wikipedia.search("C++"))

taipei = wikipedia.page("Taipei")

##
taipei.title, taipei.url
##
taipei.content
##
taipei.links
##
wikipedia.set_lang('zh')
wikipedia.summary("Taipei", sentences=3)