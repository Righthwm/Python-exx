from google.cloud import bigquery
import json
import os


def main():
    client = bigquery.Client()

    query = client.query(
        """
        SELECT location, avg(reputation) as average
        FROM `bigquery-public-data.stackoverflow.users` 
        GROUP BY  location
        ORDER BY average desc
        LIMIT 10
        """
    )

    results = query.result()
    data = {}
    list_name=[]
    f = open("result.json", "w")
    f.write("{ \n")
    for row in results:
        loc = str(row.location)
        data[loc]={}
        average = row.average
        query2 = """
            SELECT display_name
            FROM `bigquery-public-data.stackoverflow.users` 
            WHERE location=?
            """
        job_config = bigquery.QueryJobConfig(
        query_parameters=[
            bigquery.ScalarQueryParameter(None, "STRING", loc),
            ]
        )
        results2 = client.query(query2, job_config=job_config)
        for row2 in results2:
            list_name.append(row2.display_name)
        data[loc]["average_value"]=average
        data[loc]["user_list"]=list_name
        f.write('{}:'.format(json.dumps(loc)))
        f.write("{ \n")
        f.write('        "average value": {}, \n        "user_list": {} \n '.format(data[loc]["average_value"],json.dumps(data[loc]["user_list"])))
        f.write("}, \n")
        list_name=[]
    f.close()

    f = open("result.json", "a")
    f.truncate(os.path.getsize("result.json")-3)
    f.write("\n}")
    f.close()


if __name__ == '__main__':
    main()