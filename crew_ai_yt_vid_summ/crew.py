from crewai import Crew, Process
from agents import blog_researcher, blog_writer
from tasks import research_task,  writin_task

crew = Crew(
    agents = [blog_researcher, blog_writer],
    tasks = [research_task, writin_task],
    Process = Process.sequential,
    memory = True,
    cache = True,
    max_rpm = 100,
    share_crew = True
)


#Start the task execution
result = crew.kickoff(inputs={'topic': "JOY BOY'S HAKI SCARED IMU!🤯| Egghead Ends? | One Piece Chapter 1122 in HIndi"})
print(result)