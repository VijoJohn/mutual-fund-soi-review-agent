from tools.pdf_parser import extract_text_from_pdf
from rag.retriever import load_knowledge, retrieve_context
from groq import Groq
import os

PDF_PATH = "data/afs-retail-total-return-fund-en.pdf"

client = Groq(api_key=os.getenv("GROQ_API_KEY"))


def analyze_soi():

    print("\nLoading knowledge base...")
    load_knowledge()

    print("Reading mutual fund report...")
    report_text = extract_text_from_pdf(PDF_PATH)

    query = "Schedule of Investments review rules and common reporting errors"

    context = retrieve_context(query)

    prompt = f"""
You are a financial reporting reviewer for a US mutual fund.

Use the following regulatory guidance and historical errors
to review the Schedule of Investments section of the report.

Knowledge Base:
{context}

Report Content:
{report_text[:8000]}

Tasks:

1. Identify possible SOI reporting issues
2. Check classification accuracy
3. Detect missing footnotes
4. Highlight presentation inconsistencies
5. Suggest preventive controls

Provide a structured review summary.
"""

    response = client.chat.completions.create(
        model="llama3-8b-8192",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3,
        max_tokens=2000,
    )

    print("\nSOI REVIEW SUMMARY\n")
    print(response.choices[0].message.content)


if __name__ == "__main__":
    analyze_soi()
