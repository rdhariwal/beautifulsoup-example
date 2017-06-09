from bs4 import BeautifulSoup
import requests
import os


base_url = "http://www.cl.cam.ac.uk/~rja14/"
soup_response = BeautifulSoup(requests.get("{}{}".format(base_url, "book.html")).text, "html5lib").ul
links = [(item.text, "{}{}".format(base_url, item.a['href'])) for item in soup_response.findAll('li')]

dir_name = "books"
directory = "{}/{}/".format(os.getcwd(), dir_name)
os.makedirs(directory)
print(directory)
for l in links:
    title = l[0].strip().replace(":", "").replace(",", "").replace("?", "").replace(" ", "_")
    file_name = "{}{}{}".format(directory, title, ".pdf")
    url = l[1]
    print("Getting {}...".format(l[0]))
    pdf_res = requests.get(url)
    with open(file_name, "w") as f:
        f.write(pdf_res.content)
        print("Wrote to {}. Finished with it.".format(file_name))

print("All done.")
