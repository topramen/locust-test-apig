import uuid
# import gevent
from locust import HttpUser, task, between
# from locust.env import Environment
# from locust.stats import stats_printer, stats_history
# from locust.log import setup_logging

# setup_logging("INFO", None)

# def uuid():
#   return uuid.uuid4()

class User1(HttpUser):
    wait_time = between(1, 3)
    host = "https://lhvtge5np9.execute-api.us-east-1.amazonaws.com/Prod"
    identifier = uuid.uuid4()
    @task (3)
    def get_task(self):
        self.client.get(f"/hash?id={self.identifier}")
    def on_start(self):
        self.client.post("/hash", json={"ID":f"{self.identifier}", "document":"the same old message"})

class User2(HttpUser):
    wait_time = between(1, 3)
    host = "https://lhvtge5np9.execute-api.us-east-1.amazonaws.com/Prod"
    identifier = uuid.uuid4()
    @task (3)
    def get_task(self):
        self.client.get(f"/hash?id={self.identifier}")
    def on_start(self):
        self.client.post("/hash", json={"ID":f"{self.identifier}", "document":"the same old message"})

class User3(HttpUser):
    wait_time = between(1, 3)
    host = "https://lhvtge5np9.execute-api.us-east-1.amazonaws.com/Prod"
    identifier = uuid.uuid4()
    @task (3)
    def get_task(self):
        self.client.get(f"/hash?id={self.identifier}")
    def on_start(self):
        self.client.post("/hash", json={"ID":f"{self.identifier}", "document":"the same old message"})
# setup Environment and Runner
# env = Environment(user_classes=[User])
# env.create_local_runner()

# # start a WebUI instance
# env.create_web_ui("127.0.0.1", 8089)

# # start a greenlet that periodically outputs the current stats
# gevent.spawn(stats_printer(env.stats))

# # start a greenlet that save current stats to history
# gevent.spawn(stats_history, env.runner)

# # start the test
# env.runner.start(1, spawn_rate=10)

# # in 60 seconds stop the runner
# gevent.spawn_later(60, lambda: env.runner.quit())

# # wait for the greenlets
# env.runner.greenlet.join()

# # stop the web server for good measures
# env.web_ui.stop()
