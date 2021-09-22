from github import GitHubUserRepositories
from scripts import SmartJson



repo = GitHubUserRepositories("https://github.com/koffiisen")
all_repo = repo.getList()
# SmartJson({"repos": all_repo}).serializeToJsonFile()
print(SmartJson({"repos": all_repo}).serialize())



