import webbrowser
import sys


list = open(sys.argv[1], 'r')
for urls in list:
    webbrowser.open_new_tab(urls)
