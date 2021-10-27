import uuid
from locust import HttpUser, task, between

class User1(HttpUser):
    wait_time = between(1, 3)
    host = "https://lhvtge5np9.execute-api.us-east-1.amazonaws.com/Prod"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.identifier = uuid.uuid4()

    @task (3)
    def get_task(self):
        self.client.get(f"/hash?id={self.identifier}")

    def on_start(self):
        self.client.post("/hash", json={"ID":f"{self.identifier}", "document":"the same old message"})
