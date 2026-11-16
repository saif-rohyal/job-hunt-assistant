from pathlib import Path
from crewai import Agent, Task
from utils.llm import gemini_llm

def get_resume_cl_agent():
    return Agent(
        role="Resume & Cover Letter Writer",
        goal="Customize application materials to match job descriptions",
        backstory="You're an expert in professional resume writing.",
        llm=gemini_llm,
        verbose=True,
    )


def create_resume_cl_task(agent, job_summary, resume_text):
    Path("data").mkdir(parents=True, exist_ok=True)

    return Task(
        description=f"""
        Tailor the candidate's resume and write a cover letter.

        Job Summary:
        {job_summary}

        Resume:
        {resume_text}
        """,
        expected_output="""
        <<RESUME_SUMMARY>>
        Tailored professional summary.

        <<COVER_LETTER>>
        Personalized cover letter.
        """,
        agent=agent,
        output_file="data/resume_agent_output.txt",
    )