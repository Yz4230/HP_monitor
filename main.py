from API import line_api
from API.twitter_api import twitter_api
from utils import check_update, render_message_text, render_message_text_short, get_east_asian_width_count

if __name__ == "__main__":
    for school_name, news_list in check_update().items():
        for news in news_list:
            rendered_text = render_message_text(news, school_name)
            line_api.broadcast(rendered_text)

            if get_east_asian_width_count(rendered_text) - len(news.origin_url) <= 140:
                twitter_api.update_status(rendered_text)
            else:
                rendered_text_short = render_message_text_short(news, school_name)
                if get_east_asian_width_count(rendered_text_short) - len(news.origin_url) <= 140:
                    twitter_api.update_status(rendered_text_short)
                else:
                    print("Message length exceeded tweet length limit")
