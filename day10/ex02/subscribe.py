from concurrent.futures import TimeoutError
from google.cloud import pubsub_v1

project_id = "infra-327610"
subscription_id = "Fully-automated-sub"
timeout = 5.0

subscriber = pubsub_v1.SubscriberClient()
subscription_path = subscriber.subscription_path(project_id, subscription_id)

def callback(message: pubsub_v1.subscriber.message.Message) -> None:
    print(message.data)

streaming_pull_future = subscriber.subscribe(subscription_path, callback=callback)
with subscriber:
    try:
        streaming_pull_future.result(timeout=timeout)
    except TimeoutError:
        streaming_pull_future.cancel()  
        streaming_pull_future.result()  