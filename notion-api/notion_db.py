import requests


class NotionDB:
    def __init__(self, bearer_token, database_id):
        self.NOTION_VERSION = "2022-02-22"
        self.NOTION_ENDPOINT_DB = "https://api.notion.com/v1/databases"
        self.bearer_token = bearer_token
        self.database_id = database_id

    def retrieve_database(self):
        headers = {"Authorization": f"Bearer {self.bearer_token}",
                   "Notion-Version": self.NOTION_VERSION}
        response = requests.get(f"{self.NOTION_ENDPOINT_DB}/{self.database_id}",
                                headers=headers)

    def create_database(self, body: dict):
        headers = {"Authorization": f"Bearer {self.bearer_token}",
                   "Notion-Version": self.NOTION_VERSION,
                   "Content-Type": "application/json"}
        response = requests.get(f"{self.NOTION_ENDPOINT_DB}",
                                headers=headers, data=body)
