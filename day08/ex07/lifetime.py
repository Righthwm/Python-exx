from google.cloud import bigquery, datastore

def main():
    client = bigquery.Client()

    query = client.query(
        """
        SELECT title, body, TIMESTAMP_DIFF(last_activity_date, creation_date, DAY) as lifetime
        FROM `bigquery-public-data.stackoverflow.stackoverflow_posts` 
        ORDER BY lifetime desc
        LIMIT 15
        """
    )

    results = query.result()
    for row in results:
        title = row.title
        body = str(row.body)[0:1500]
        lifetime = row.lifetime
        client = datastore.Client()
        with client.transaction():
            incomplete_key = client.key("lifetime")
            new_entity = datastore.Entity(key=incomplete_key)
            new_entity.update(
            {
                "title": title,
                "body": body,
                "lifetime": lifetime
            }
            )
            client.put(new_entity)


if __name__ == '__main__':
    main()