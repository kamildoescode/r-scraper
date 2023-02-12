from RScraper import RScraper

if __name__ == '__main__':
    rs = RScraper(console_log=True)

    reddits: list[dict]
    reddits = rs.scrape_reddits(limit=2, save_to_file=True)

    rs.scrape_submissions(None, 2)
