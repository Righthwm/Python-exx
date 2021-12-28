from concurrent import futures
from typing import Callable
from google.cloud import pubsub_v1


project_id = "infra-327610"
topic_id = "starting-with-UI"

publisher = pubsub_v1.PublisherClient()
topic_path = publisher.topic_path(project_id, topic_id)
publish_futures = []

def get_callback(
    publish_future: pubsub_v1.publisher.futures.Future, data: str
) -> Callable[[pubsub_v1.publisher.futures.Future], None]:
    def callback(publish_future: pubsub_v1.publisher.futures.Future) -> None:
        try:
            print(publish_future.result(timeout=5))
        except futures.TimeoutError:
            print(f"Publishing {data} timed out.")
    return callback

def main():
    for i in range(5):
        data = "This is sent from code message id: " +str(i)
        publish_future = publisher.publish(topic_path, data.encode("utf-8"))
        publish_future.add_done_callback(get_callback(publish_future, data))
        publish_futures.append(publish_future)

    futures.wait(publish_futures, return_when=futures.ALL_COMPLETED)

if __name__ == "__main__":
    main()