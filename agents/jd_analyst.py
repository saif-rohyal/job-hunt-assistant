from crewai import Agent, Task
from utils.llm import gemini_llm

def get_jd_analyst_agent():
    return Agent(
        role="JD Analyst",
        goal="Understand and summarize government job postings",
        backstory="You're an expert in US federal job listings.",
        llm=gemini_llm,
        verbose=True,
    )


def create_jd_analysis_task(agent, job_description):
    return Task(
        description=f"""
        Analyze this USAJobs job posting.

        Extract:
        - Role summary
        - Required skills
        - Qualifications and eligibility

        Job Description:
        {job_description}
        """,
        expected_output="A structured markdown report.",
        agent=agent,
        output_file="data/report.md",
    )