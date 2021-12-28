import csv
from google.cloud import bigquery

def query_stackoverflow():
    client = bigquery.Client()
    query_job = client.query(
    """
    SELECT  user_display_name, score
    FROM `bigquery-public-data.stackoverflow.comments` 
    Order by score desc
    LIMIT 10
    """
    )
    results = query_job.result() 
    header=['user_display_name','highest_score']

    with open('/home/vladvdorin/gcp-training/day08/ex01/result.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(header)

        for row in results:
            score=str(row.score)
            user_name=str(row.user_display_name)
            writer.writerow([user_name,score])
        
        
       

if __name__ == "__main__":
    query_stackoverflow()