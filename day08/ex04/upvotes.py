from google.cloud import bigquery
import json
import os

def main():
    client = bigquery.Client()

    query = client.query(
        """
        SELECT display_name, website_url, up_votes
        FROM `bigquery-public-data.stackoverflow.users` 
        WHERE website_url LIKE "%.com%"
        ORDER BY up_votes desc
        LIMIT 15
        """
    )

    results = query.result()
    data = {}
    f = open("result.json", "w")
    f.write('[ \n { \n')
    for row in results:
        name = str(row.display_name)
        nr_upvotes = row.up_votes
        data[name]={}
        data[name]['upvotes']=nr_upvotes
        data[name]['domain']=".com"
        f.write('{}:'.format(json.dumps(name)))
        f.write("{ \n")
        f.write('        "upvotes": {}, \n        "domain": "{}" \n '.format(data[name]['upvotes'],data[name]['domain']))
        f.write("}, \n")
    f.close()

    f = open("result.json", "a")
    f.truncate(os.path.getsize("result.json")-3)
    f.write("\n}\n]")
    f.close()


if __name__ == '__main__':
    main()