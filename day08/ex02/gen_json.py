from google.cloud import bigquery
import json

def main():
    client = bigquery.Client()

    query = client.query(
        """
        SELECT DISTINCT  u.display_name, c.score
        FROM `bigquery-public-data.stackoverflow.users` as u
        INNER JOIN `bigquery-public-data.stackoverflow.comments` as c
        ON u.display_name=c.user_display_name
        ORDER BY c.score desc
        LIMIT 10
        """
    )

    results = query.result()
    data = {}
    with open('result.json', 'w') as f:
        
        for row in results:
            user = str(row.display_name)
            score = str(row.score)
            data[user]=score

        f.write(json.dumps(data))


if __name__ == '__main__':
    main()