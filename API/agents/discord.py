import requests

from API.common import APIBase
from API.structs import Discord
from crawlers.common import News
from renderers import render_text_default


class DiscordAPI(APIBase):
    LOGGING_NAME = __name__
    JSON_KEY=discord

    def broadcast_prod(self, news: News, school_name: str) -> None:
        discord_tokens: Discord = self.get_agent_tokens(school_name)
        if not discord_tokens:
            return
        rendered_text = render_text_default(news, school_name)
        api_url = "https://discordapp.com/api/webhooks/"

        payload = {
            "messages": [
                {
                    "type": "text",
                    "text": rendered_text
                }
            ]
        }

        headers = {
            "Authorization": discord_tokens.webhook_token,
            "Content-Type": "application/json"
        }

        requests.post(api_url, json=payload)