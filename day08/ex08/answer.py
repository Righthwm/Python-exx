from google.cloud import bigquery
from fpdf import FPDF


def get_ticket(pdf, title, body, time_until_answer):
    pdf.set_text_color(0, 0, 0)
    pdf.set_font('Times', '', 24.0)
    pdf.cell(8.0, 0.0, title,0,0,'C')
    pdf.ln(0.5)

    pdf.set_text_color(0, 0, 255)
    pdf.set_font('Times','', 12.0)
    pdf.cell(1.0, 0.0, body,0,0,'L')
    pdf.ln(0.5)

    pdf.set_text_color(0, 255, 0)
    pdf.set_font('Times', '', 12.0)
    pdf.cell(1.0, 0.0, str(time_until_answer),0,0,'L')
    pdf.ln(1)


def main():
    client = bigquery.Client()

    query = client.query(
        """
        SELECT q.title, TIMESTAMP_DIFF(a.creation_date, q.creation_date, MINUTE) as time_until_answer, a.body
        FROM `bigquery-public-data.stackoverflow.posts_questions` as q 
        JOIN `bigquery-public-data.stackoverflow.posts_answers` as a
        ON q.accepted_answer_id=a.id
        ORDER BY q.answer_count desc
        LIMIT 15
        """
    )

    pdf = FPDF(format='letter', unit='in')
    pdf.add_page()
    results = query.result()
    for row in results:
        title = row.title
        body = str(row.body)[0:1500]
        time_until_answer = row.time_until_answer
        get_ticket(pdf, title, body, time_until_answer)
        
    pdf.output('ex08.pdf', 'F')


if __name__ == '__main__':
    main()