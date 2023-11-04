# # Description: This file is used to scrape job postings from Indeed.com using the Claude 2 LLM API.
# from langchain.chat_models import ChatAnthropic
# from langchain.chains import create_extraction_chain
# import pprint
# from langchain.text_splitter import RecursiveCharacterTextSplitter


# llm = ChatAnthropic(anthropic_api_key= "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")

# schema = {
#     "properties": {
#         "job_title": {"type": "string"},
#         "company": {"type": "string"},
#         "location": {"type": "string"},
#         "description": {"type": "string"},
#         "salary": {"type": "string"},
#         "application_deadline": {"type": "string"},
#         "required_skills": {"type": "string"},
#         "preferred_skills": {"type": "string"},
#         "required_experience": {"type": "string"},
#         "required_education": {"type": "string"},
#         "date_posted": {"type": "string"},
#     },
# }

# def extract(content: str, schema: dict):
#     return create_extraction_chain(schema=schema, llm=llm).run(content)


from bs4 import BeautifulSoup
import requests


url = 'https://www.indeed.com/jobs?q=data+engineer&l=United+States'

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
response = requests.get(url, headers=headers)
data = response.text
soup = BeautifulSoup(data, 'html.parser')
jobs = soup.find_all('div',{'class':'jobsearch-SerpJobCard'})

print(data)

for job in jobs:
    print(job)