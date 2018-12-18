import webbrowser

q_list = ["블랙핑크","migos"]
url = "https://www.google.com/search?&q="

for q in q_list:

    webbrowser.open(url+q)

