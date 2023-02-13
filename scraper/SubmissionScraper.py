import json
from abc import ABC

import util


class SubmissionScraperInterface(ABC):

    @staticmethod
    def scrape(console_log: bool, reddit_url_list: list[str] | None, limit=None) -> None:
        """
        :param console_log: enable console logging
        :param reddit_url_list: list of reddit urls to scrape submissions from,
         example: ['https://www.reddit.com/r/CasualUK'],
         can be None to use the 'data/reddits.json' file as base and scrape all
        :param limit: how many submissions per reddit to fetch, can be None to fetch all
        :return: None
        """
        pass


class SubmissionScraper(SubmissionScraperInterface):

    @staticmethod
    def scrape(console_log, reddit_url_list, limit=None):
        def _load_reddits():
            path = 'data/reddits.json'

            if not util.file_exists(path):
                raise ValueError("Either provide reddit URL list or ensure 'data/reddits.json' file exists")

            with open(path, 'r') as in_file:
                in_data = json.load(in_file)

                reddits = list()
                for rdata in in_data['reddits']:
                    rel_url = rdata['data']['url']

                    reddits.append(f'https://www.reddit.com/{parse_url(rel_url)}')

                return reddits

        def parse_url(url: str) -> str:
            """
            Parse url to get rid of / at the beginning and end
            :param url: url to be passed
            :return: url
            """

            if url.startswith('/'):
                url = url[1:]

            if url.endswith('/'):
                url = url[:-1]

            return url

        def _log(msg: str):
            print(f'[SubmissionScraper] {msg}')

        if not reddit_url_list:
            reddit_url_list = _load_reddits()

        _log('')
        _log(f'Scraping {limit} submissions each for reddits: {reddit_url_list}')
