from crewai import Agent, Task
from utils.llm import gemini_llm

def get_messaging_agent():
    return Agent(
        role="Outreach Message Writer",
        goal="Draft personalized job outreach messages",
        backstory="You're a professional career coach.",
        llm=gemini_llm,
        verbose=True,
    )


def create_messaging_task(
    agent,
    job_summary,
    agency_name,
    user_bio="I'm a data professional passionate about public service.",
):
    return Task(
        description=f"""
        Write a professional outreach message under 150 words.

        Agency: {agency_name}

        Job Summary:
        {job_summary}

        Candidate Bio:
        {user_bio}
        """,
        expected_output="A professional outreach message under 150 words.",
        agent=agent,
    )