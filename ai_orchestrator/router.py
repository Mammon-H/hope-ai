import os
import requests

class AIRouter:

    def __init__(self):
        self.openai=os.getenv("OPENAI_API_KEY","")

    def route(self,prompt):

        if not self.openai:
            return "⚠️ OPENAI_API_KEY not set"

        headers={
        "Authorization":f"Bearer {self.openai}",
        "Content-Type":"application/json"
        }

        data={
        "model":"gpt-4o-mini",
        "messages":[{"role":"user","content":prompt}]
        }

        try:

            r=requests.post(
            "https://api.openai.com/v1/chat/completions",
            headers=headers,
            json=data,
            timeout=30
            )

            return r.json()["choices"][0]["message"]["content"]

        except Exception as e:

            return f"AI Error: {e}"


def route(prompt):

    router=AIRouter()
    return router.route(prompt)
