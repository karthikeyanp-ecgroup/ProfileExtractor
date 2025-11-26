from openai import OpenAI
#client = OpenAI(api_key="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") ecgroup mail
client = OpenAI(api_key="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")
PROMPT = """
Extract candidate information from this resume text.
Return ONLY valid JSON with fields:

full_name
email
phone
skills
total_experience_years
last_company
past_companies
education
certifications
notice_period

Resume Text:
-------------------
{resume}
"""

def parse_resume(text):
    response = client.chat.completions.create(
        model="gpt-4.1",
        messages=[{"role": "user", "content": PROMPT.format(resume=text)}]
    )

    return response.choices[0].message.content
