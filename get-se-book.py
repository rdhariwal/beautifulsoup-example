from bs4 import BeautifulSoup
import requests
import os


base_url = "http://www.cl.cam.ac.uk/~rja14/"
soup_response = BeautifulSoup(requests.get("{}{}".format(base_url, "book.html")).text, "html5lib").ul
links = [(item.text, "{}{}".format(base_url, item.a['href'])) for item in soup_response.findAll('li')]

dir_name = "book"
directory = "{}/{}/".format(os.getcwd(), dir_name)
os.makedirs(directory)
for l in links:
    file_name = l[0].strip().replace(":", "").replace(",", "").replace("?", "").replace(" ", "_")
    path = "{}{}{}".format(directory, file_name, ".pdf")
    url = l[1]
    print("Getting {}...".format(l[0]))
    response = requests.get(url)
    with open(path, "w") as f:
        f.write(response.content)
        print("Wrote to {}. Finished with it.\n".format(path))

print("All done.")
