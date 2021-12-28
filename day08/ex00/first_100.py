from google.cloud import bigquery

def query_stackoverflow():
    client = bigquery.Client()
    query_job = client.query(
    """
    SELECT score, text, creation_date 
    FROM `bigquery-public-data.stackoverflow.comments` 
    Order by creation_date
    LIMIT 100
    """
    )
    results = query_job.result() 

    f=open("result.txt","w")

    for row in results:
        score=str(row.score)[0:5]
        text=str(row.text)[0:120]
        creation_date=str(row.creation_date)[0:10]
        f.write("Score: "+score+"Comment:"+text+"Creation date:"+creation_date)
        f.write("\n")
    f.close()

if __name__ == "__main__":
    query_stackoverflow()