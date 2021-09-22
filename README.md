# GitHubUserRepositories
Small python scrapping of github users repository

# How to uses ?
* First install packages :

* ```pip install -r requirements.txt```
* OR install manually
* requests, beautifulsoup4, smartjson
*  ```pip install requests```
*  ```pip install beautifulsoup4```
*  ```pip install smartjson``` just for convert class to json

```python 
from github import GitHubUserRepositories
from scripts import SmartJson # not neccessary

repo = GitHubUserRepositories("https://github.com/koffiisen")

# or
# repo = GitHubUserRepositories("https://github.com/koffiisen",next_page_time_interval=2)
# next_page_time_interval is time interval for scrapping next page

all_repo = repo.getList()
# SmartJson({"repos": all_repo}).serializeToJsonFile()
print(SmartJson({"repos": all_repo}).serialize()) #not neccessary

```

* OR run ```python test.py```

# OUTPUT

```json

{
  "repos": [
    {
      "name": "GitHubUserRepositories",
      "type": "Public",
      "url": "https://github.com/koffiisen/GitHubUserRepositories"
    },
    {
      "name": "bot",
      "type": "Public",
      "url": "https://github.com/koffiisen/bot"
    },
    {
      "name": "deliv",
      "type": "Public",
      "url": "https://github.com/koffiisen/deliv"
    },
    {
      "name": "livestream",
      "type": "Public",
      "url": "https://github.com/koffiisen/livestream"
    },
    {
      "name": "SmartSwitchCase",
      "type": "Public",
      "url": "https://github.com/koffiisen/SmartSwitchCase"
    },
    {
      "name": "aaef",
      "type": "Public",
      "url": "https://github.com/koffiisen/aaef"
    },
    {
      "name": "WLocker",
      "type": "Public",
      "url": "https://github.com/koffiisen/WLocker"
    },
    {
      "name": "vaadin.min.js",
      "type": "Public",
      "url": "https://github.com/koffiisen/vaadin.min.js"
    },
    {
      "name": "Requests.js",
      "type": "Public",
      "url": "https://github.com/koffiisen/Requests.js"
    },
    {
      "name": "Animate.js",
      "type": "Public",
      "url": "https://github.com/koffiisen/Animate.js"
    },
    {
      "name": "js-splash",
      "type": "Public",
      "url": "https://github.com/koffiisen/js-splash"
    },
    {
      "name": "hsterling",
      "type": "Public",
      "url": "https://github.com/koffiisen/hsterling"
    },
    {
      "name": "SmartJson",
      "type": "Public",
      "url": "https://github.com/koffiisen/SmartJson"
    },
    {
      "name": "notesstudio",
      "type": "Public",
      "url": "https://github.com/koffiisen/notesstudio"
    },
    {
      "name": "workdir-yi-2018",
      "type": "Public",
      "url": "https://github.com/koffiisen/workdir-yi-2018"
    },
    {
      "name": "MediaStore",
      "type": "Public",
      "url": "https://github.com/koffiisen/MediaStore"
    },
    {
      "name": "gitignore",
      "type": "Public",
      "url": "https://github.com/koffiisen/gitignore"
    }
  ]
}

```
