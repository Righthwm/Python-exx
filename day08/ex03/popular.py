from google.cloud import bigquery

def main():
    client = bigquery.Client()

    query = client.query(
        """
        SELECT user_display_name, COUNT(user_display_name) as nr_comments
        FROM `bigquery-public-data.stackoverflow.comments` 
        GROUP BY user_display_name
        ORDER BY nr_comments desc
        LIMIT 10
        """
    )

    results = query.result()
    f = open("result.txt", "w")
    for row in results:
        name = str(row.user_display_name)
        nr_comments = str(row.nr_comments)
        f.write("{} -> {} comments".format(name, nr_comments))
        f.write("\n")

    f.close()


if __name__ == '__main__':
    main()