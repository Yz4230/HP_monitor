<<<<<<< HEAD
from typing import Dict

import requests
from faker import Faker

from API.common import APIBase
=======
import requests

from API.common import APIBase
from API.structs import Discord
>>>>>>> eb8c9af955db6bfcc12ab45487aa19bda432744e
from crawlers.common import News
from renderers import render_text_default


class DiscordAPI(APIBase):
    LOGGING_NAME = __name__
<<<<<<< HEAD
    JSON_KEY = "discord"

    def broadcast_prod(self, news: News, school_name: str) -> None:
        discord_tokens = self.get_agent_tokens(school_name)
        if not discord_tokens:
            return
        print(discord_tokens)
        print("\n\n\n")
        rendered_text = render_text_default(news, school_name)
        api_base_url = "https://discordapp.com/api/webhooks/"


        payload = {
            "content": rendered_text
        }

        api_uri = api_base_url + discord_tokens["webhook_token"]

        requests.post(api_uri, 
        json=payload
        )

    @classmethod
    def generate_fake_tokens(cls, fake: Faker) -> Dict[str, str]:
        return {
            "webhook_token": fake.password(18)+"/"+fake.password(68)
        }
=======
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
>>>>>>> eb8c9af955db6bfcc12ab45487aa19bda432744e
