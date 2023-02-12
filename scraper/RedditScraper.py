from abc import ABC

import requests

import util


class RedditScraperInterface(ABC):

    @staticmethod
    def scrape(console_log: bool, limit=None) -> list[dict]:
        """
        :param console_log: enable console logging
        :param limit: how many reddits to fetch, can be None to fetch all
        :return: list of reddits
        """
        pass


class RedditScraper(RedditScraperInterface):

    @staticmethod
    def scrape(console_log, limit=None):

        def _log(msg: str):
            print(f'[RedditScraper] {msg}')

        def _process_reddit(_reddit: dict) -> dict:
            # TODO: add processing, like key parsing, so user can only lookup specific information
            return _reddit

        reddits = list()

        finished = False
        after = None
        max_limit = 100

        if limit and limit < 100:
            max_limit = limit

        base_url = f'https://www.reddit.com/reddits.json?limit={max_limit}'

        if console_log:
            _log('')
            _log(f'Scraping reddits with limit = {limit}')

        while not finished:
            req_url = base_url if not after else f'{base_url}&after={after}'

            if console_log:
                _log(f'\tRequesting {req_url}')

            req = requests.get(req_url, headers=util.gen_headers())
            rdata = req.json()['data']

            after = rdata['after']
            if not after:
                finished = True

            for reddit in rdata['children']:
                reddits.append(_process_reddit(reddit))

                if limit and len(reddits) >= limit:
                    finished = True

            if console_log:
                _log(f'\tReddits fetched so far = {len(reddits)}')

        return reddits
