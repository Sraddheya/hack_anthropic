from anthropic import Anthropic, HUMAN_PROMPT, AI_PROMPT
anthropic = Anthropic(api_key="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")
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

output_format = """{
    "job_title": xxxx,
    "company": xxxx,
    "location": xxxx,
    "description": xxxx,
    "salary": xxxx,
    "application_deadline": xxxx,
    "required_skills": xxxx,
    "experience_level": xxxx,
    "education_level": xxxx,
    "date_posted": xxxx}"""

from bs4 import BeautifulSoup
from selenium import webdriver

import requests
base_url = 'https://www.reed.co.uk'
url = 'https://www.reed.co.uk/jobs/software-design-engineer-jobs-in-london'

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.content, 'html.parser')
jobs = soup.find_all('a',{'class':'job-card_jobCard__blockLink__PeeZx'})[:3]

for job_link in jobs:
    print('----------------')
    print()
    url = base_url + job_link.get('href')
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    job = soup.find('div',{'class':'col-lg-12'})
    job_summary = anthropic.completions.create(
        model="claude-2",
        max_tokens_to_sample=3000,
        prompt=f"{HUMAN_PROMPT} You will be given some html that contains a descriptions for a job. Extract the following information and present it as a where each element is in the JSON format: {output_format}. Do not provide any preamble or closing, just the raw JSON. Make sure to remove all html tags and newline characters from the text <html>{job}</html> {AI_PROMPT}",
    )
    jjson = job_summary.completion
    print(jjson)


# # Name



# # for job in jobs:
# #    print(job)

# options = webdriver.ChromeOptions()
# options.add_argument('headless')
# browser = webdriver.Chrome(options=options)
# browser.get(url)
# html = browser.page_source
# print(html)