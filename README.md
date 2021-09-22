# GitHubUserRepositories
Small python scrapping of github users repository

# How to uses ?
* First install packages :
* requests, beautifulsoup4, smartjson
*  ```pip install requests```
*  ```pip install beautifulsoup4```
*  ```pip install smartjson``` just for convert class to json

```python 

repo = GitHubUserRepositories("https://github.com/koffiisen")
all_repo = repo.getList()
# SmartJson({"repos": all_repo}).serializeToJsonFile()
print(SmartJson({"repos": all_repo}).serialize())

```
