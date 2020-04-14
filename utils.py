import json
import unicodedata
from typing import List, Dict

from crawlers.common import News
from settings import HISTORY_JSON_PATH, CRAWLER_CLASSES, MESSAGE_TEMPLATE, MESSAGE_TEMPLATE_SHORT


def check_update() -> Dict[str, List[News]]:
    crawled_news: Dict[str, List[News]] = {}

    with open(HISTORY_JSON_PATH, "r", encoding="utf-8") as rf:
        history: Dict = json.load(rf)

    for crawler_class in CRAWLER_CLASSES:
        hashes: List[str] = history.get(crawler_class.SCHOOL_NAME, [])
        crawler = crawler_class()
        latest_news = crawler.get_latest_news(hashes)
        history[crawler_class.SCHOOL_NAME] = hashes + list(map(lambda x: x.hash, latest_news))
        crawled_news[crawler_class.SCHOOL_NAME] = latest_news

    with open(HISTORY_JSON_PATH, "w", encoding="utf-8") as wf:
        json.dump(history, wf, indent=4, ensure_ascii=False)

    return crawled_news


def render_message_text(news: News, school_name: str) -> str:
    return MESSAGE_TEMPLATE.format(
        name=school_name,
        title=news.title,
        content=news.content,
        url=news.origin_url
    )


def render_message_text_short(news: News, school_name: str) -> str:
    return MESSAGE_TEMPLATE_SHORT.format(
        name=school_name,
        title=news.title,
        url=news.origin_url
    )


def get_east_asian_width_count(text):
    count = 0
    for c in text:
        if unicodedata.east_asian_width(c) in 'FWA':
            count += 2
        else:
            count += 1
    return count
