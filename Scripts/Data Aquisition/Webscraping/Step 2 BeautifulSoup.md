Start your firstscrape.py file with:

```
web_server = 'domain.com'
import requests
from bs4 import BeautifulSoup


page = requests.get(f'http://{web_server}/archive/')
soup = BeautifulSoup(page.content, "lxml")
#We're not printing the entire thing
str(list(soup)[1])[:800]
print(soup.prettify()[:800])
```
This allows you to see how things are nested together, you can usually see that they are separated by div elements.
If you see, for example this:
```
<div class="phish" id="1186816">
   <div class="subject">
    <h3>
     <a href="/archive/1186816.html">
      Mailbox Upgrade
     </a>
    </h3>
   </div>
   <div class="body_sample">
    <pre>
To ensure quic...</pre>
   </div>
</div>
```
Then we would know that there s a div class called subject.

Now you can run a new pythong script that is more specific to this

```
#now examine the contents of the page based on those elements
web_server = 'domain.com'
import requests
from bs4 import BeautifulSoup


page = requests.get(f'http://{web_server}/archive/')
soup = BeautifulSoup(page.content, "lxml")

subject_divs = soup.find_all("div", {"class":"subject"})
# Let's use a list comprehension 
results = [i for i in subject_divs][:20]
print(results)
```
