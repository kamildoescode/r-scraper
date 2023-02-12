import json
from datetime import datetime, timezone

import util
from scraper.RedditScraper import RedditScraper
from scraper.SubmissionScraper import SubmissionScraper


class RScraper:
    """
    Scrap publicly available reddit data
    """

    def __init__(self, console_log: bool):
        """
        :param console_log: enable console logging
        """
        if not console_log:
            raise Exception('Parameter "console_log_enabled" not provided [True/False]')

        self.console_log = console_log

    def scrape_reddits(self, limit: int = None, save_to_file: bool = False) -> list[dict]:
        """
        Scrape reddits, just like https://www.reddit.com/reddits
        :param limit: how many reddits to fetch, can be None to fetch all
        :param save_to_file: should data be saved to a file
        :return: list of reddits
        """

        reddits = RedditScraper.scrape(self.console_log, limit)
        if save_to_file:
            filepath = 'data/reddits.json'
            util.dir_create('data')
            util.remove_file(filepath)

            with open('data/reddits.json', 'w') as out_file:
                json.dump({
                    'count': len(reddits),
                    'fetched_utc': str(datetime.now(timezone.utc)),
                    'reddits': reddits
                }, out_file, indent=4)

            if self.console_log:
                print(f'\nReddits data saved to {filepath}\n')

        return reddits

    def scrape_submissions(self, reddit_url_list: list[str] | None, limit: int = None) -> None:
        """
        Scrape reddits, just like https://www.reddit.com/r/CasualUK
        :param reddit_url_list: list of reddit urls to scrape submissions from,
         example: ['https://www.reddit.com/r/CasualUK'],
          can be None to use the 'data/reddits.json' file as base and scrape all
        :param limit: how many submissions per reddit to fetch, can be None to fetch all
        :return:
        """

        return SubmissionScraper.scrape(self.console_log, reddit_url_list, limit)
