prompt = f
# "You are a system that is trying to match a candidate with relevant jobs. Given JSON data about a candidate,
# output how relevant the job is for that candidate. Assess how closely the candidates previous job titles
# match the current job title. Assess if the candidate has the required experience level, keeping in mind
# that the candidate experince will be listed in months but the roles required experience will be in years. 
# Assess if the candidates skills match or relate to the skills required for the job and in the job description. 
# Also consider how long the candidate had experience with specific skills. If there is a mismatch or not enough
# information to answer then say so. Give a rating between 0 and 1 for how suitable and likely this candidate is 
# to get this job, with 0 being very unsuitable and no chance, and 1 being very suitable and would be very 
# likely to get the job. Only if the candidate was marked above 0.8 in the previous step, put in <suitable> tags,
# one paragraph of up to 200 words on why the candidate is a good fit for the job and highlight what experience may
# help them stand out among other candidates. An example of the output for a job that is ranked aboved 0.8 is as follows <example><suitable>
# The candidate is suitable for this job because they she has 22 months of experience as a Software Engineering,
# which is close to the required experience. She has direct experience with some of the required skills like 
# Python, Java, HTML, CSS, and AWS. The role requires SQL which she does not list, but her software engineering 
# roles likely involved some SQL database work.</suitable></example>. For any jobs ranked 0.8 and below, put in <skills> tag the names 
# of the skills they are missing, do not include any other text.An example for a job that is ranked 0.8 and below is as follows
# <example><skills>HTML, CSS, Java, Python</skills></example>. The candidate JSON is as follows: <json>{cand}</json> and the 
# role is: <json>{role}</json>. 



"For example <example> {
    "name": "John Smith",
    "experience": [
        {
            "job_title": "English Teacher",
            "job_duration": 10,
            "company": "The New Oak School",
            "skills": ["excel,", "google calendar"],
        },
        {
            "job_title": "Software engineering intern",
            "job_duration": 2,
            "company": "The New Oak Tech Company",
            "skills": ["HTML", "CSS", "Java"],
        },],
}

output_format = """{
    "job_title": "Software engineer",
    "company": "The Water Bottle Tech company",
    "location": London,
    "description": xxxx,
    "salary": "£40,000",
    "application_deadline": xxxx,
    "required_skills": "AWS", "Java", "React", "HTML", "JavaScript",
    "experience_level": 2,
    "education_level": Bachelors,
    "date_posted": xxxx}"""

This candidate could be marked as 

