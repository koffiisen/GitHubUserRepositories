from time import sleep
from urllib.parse import urlparse

import requests
from bs4 import BeautifulSoup
from scripts import SmartJson


class RepoInterface:
    def __init__(self, url="", name="", type=""):
        self.url = url
        self.name = name
        self.type = type


class GitHubUserRepositories:
    def __init__(self, repo_url, next_page_time_interval=2):
        """
        :param repo_url:
        :param next_page_time_interval:
        """
        self.repo_url = repo_url
        self.repo_list = []
        # next_page_time_interval is time interval for scrapping next page
        self.next_page_time_interval = next_page_time_interval

    def __getFinalUrl__(self):
        try:
            tab = "/repositories"
            final_url = self.repo_url
            if tab in self.repo_url:
                pass
            else:
                uri_infos = urlparse(self.repo_url)
                final_url = "{scheme}://{netloc}/{path}{query}".format(scheme=uri_infos.scheme, netloc=uri_infos.netloc,
                                                                       path=str(self.repo_url).split("/")[3], query=tab)
            return final_url
        except Exception as e:
            print(e)
            return

    def __getFinalUrl2__(self):
        try:
            tab = "?tab=repositories"
            final_url = self.repo_url
            if tab in self.repo_url:
                pass
            else:
                uri_infos = urlparse(self.repo_url)
                final_url = "{scheme}://{netloc}/{path}{query}".format(scheme=uri_infos.scheme, netloc=uri_infos.netloc,
                                                                       path=str(self.repo_url).split("/")[3], query=tab)
            return final_url
        except Exception as e:
            print(e)
            return

    def __getNumberOfPage__(self, final_url):
        try:
            page = requests.get(final_url)
            soup = BeautifulSoup(page.content, "html.parser")
            ALL_PAGE = []

            for pagination in soup.findAll("div", class_="pagination"):
                infos = BeautifulSoup(str(pagination), "html.parser")
                a = infos.findAll("a")

                for page in a:
                    if str(page.text).isdigit():
                        ALL_PAGE.append(int(page.text))

            if 1 not in ALL_PAGE:
                ALL_PAGE.append(1)

            return max(ALL_PAGE)
        except Exception as e:
            print(e)
            return 0

    def __parse__(self, final_url=""):
        try:
            pages = self.__getNumberOfPage__(final_url)
            print(pages)

            if pages <= 1:
                self.next_page_time_interval = 0  # disable interval for only 1 page

            for pg in range(1, (pages + 1)):
                if "?" in final_url:
                    final_url = "%s&page=%s" % (final_url, pg)
                else:
                    final_url = "%s?page=%s" % (final_url, pg)
                print("Process for page :", pg)

                page = requests.get(final_url)
                soup = BeautifulSoup(page.content, "html.parser")

                uri_infos = urlparse(self.repo_url)

                for h3 in soup.findAll("h3", class_="wb-break-all"):
                    infos = BeautifulSoup(str(h3), "html.parser")
                    a = infos.find("a")

                    uri = "{0}://{1}{2}".format(uri_infos.scheme, uri_infos.netloc, a.get("href", ""))
                    name = str(uri).split("/")[-1].replace("%20", " ")
                    type = "Public"

                    self.repo_list.append(
                        RepoInterface(uri, name, type)
                    )
                print("--- End for process page", pg, "---")
                sleep(self.next_page_time_interval)
        except Exception as e:
            print(e)
            return

    def getList(self):

        final_url = self.__getFinalUrl__()
        self.__parse__(final_url)
        if len(self.repo_list) == 0:
            final_url = self.__getFinalUrl2__()
            self.__parse__(final_url)

        print("Final Url", final_url)
        print("Number of page", self.__getNumberOfPage__(final_url))
        return self.repo_list

        # print(soup)


"""repo = GitHubUserRepositories("https://github.com/koffiisen")
all_repo = repo.getList()
# SmartJson({"repos": all_repo}).serializeToJsonFile()
print(SmartJson({"repos": all_repo}).serialize())"""
