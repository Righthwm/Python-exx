from google.cloud import bigquery
import csv

def main():
    client = bigquery.Client()

    query = client.query(
        """
        SELECT title, body, tags 
        FROM `bigquery-public-data.stackoverflow.stackoverflow_posts`
        WHERE tags LIKE "%python%" 
        LIMIT 10
        """
    )

    results = query.result()
    header = ['post_title', 'body', 'all_tags']
    with open('result.csv', 'w') as f:
        writer = csv.writer(f)
        writer.writerow(header)
        for row in results:
            title = str(row.title)
            body = str(row.body)
            tag = str(row.tags)
            writer.writerow([title, body, tag])
            writer.writerow('\n')


if __name__ == '__main__':
    main()