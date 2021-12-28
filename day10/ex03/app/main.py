from flask import Flask, render_template, request
from concurrent.futures import TimeoutError
from concurrent import futures
from google.cloud import pubsub_v1
from typing import Callable

app = Flask(__name__,
            static_url_path='', 
            static_folder='app/static',
            template_folder='app/templates')



@app.route('/pull', methods=['GET'])
def pull():
    data=[]
    def callback(message: pubsub_v1.subscriber.message.Message) -> None:
        data.append(message.data)
    
    project_id = "infra-327610"
    subscription_id = "Fully-automated-sub"

    timeout = 5.0

    subscriber = pubsub_v1.SubscriberClient()
    subscription_path = subscriber.subscription_path(project_id, subscription_id)

    streaming_pull_future = subscriber.subscribe(subscription_path, callback=callback)

    with subscriber:
        try:
            streaming_pull_future.result(timeout=timeout)
        except TimeoutError:
            streaming_pull_future.cancel()  
            streaming_pull_future.result() 
    return render_template('public/pull.html', data=data)

@app.route('/push', methods=['GET', 'POST'])
def push():
    if request.method == 'POST':
        project_id = "smart-bonus-327310"
        topic_id = "Fully-automated"

        publisher = pubsub_v1.PublisherClient()
        topic_path = publisher.topic_path(project_id, topic_id)
        publish_futures = []

        def get_callback(
            publish_future: pubsub_v1.publisher.futures.Future, data: str
        ) -> Callable[[pubsub_v1.publisher.futures.Future], None]:
            def callback(publish_future: pubsub_v1.publisher.futures.Future) -> None:
                try:
                    print(publish_future.result(timeout=3600))
                except futures.TimeoutError:
                    print(f"Publishing {data} timed out.")

            return callback

        data = "This is a message from Flask"
        publish_future = publisher.publish(topic_path, data.encode("utf-8"))
        publish_future.add_done_callback(get_callback(publish_future, data))
        publish_futures.append(publish_future)

        futures.wait(publish_futures, return_when=futures.ALL_COMPLETED)
        return render_template('public/push.html')
    else:
        return render_template('public/push.html')


if __name__ == '__main__':
    app.run(debug=True)