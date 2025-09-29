from crewai import Agent
from tools import yt_tool

import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()
os.environ["GOOGLE_API_KEY"] = os.getenv("GOOGLE_API_KEY")
llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash", # Use gemini-1.5-flash or gemini-1.0-pro, gemini-2.5-flash might not be directly available via ChatGoogleGenerativeAI model parameter
    verbose=True,
    temperature=0.1,
    google_api_key=os.getenv("GOOGLE_API_KEY") # Explicitly pass the key
)


#Senior blog content researcher
blog_researcher = Agent(
    role='Blog Researcher from Youtube Videos',
    goal="get the relevant video content for the topic {Topic} from yt video",
    verbose=True,
    memory=True,
    backstory=(
        "Expert in understanding videos in AI Data Science, Machine Learning and Gen AI and providing suggestions."
    ),
    llm=llm,
    tools= [yt_tool],
    alloe_delegation=True

)

#Create a senior blog writer agent with yt tools
blog_writer = Agent(
    role="Blog Writer",
    goal="Narrate complelling tech stories about the video {topic} from YT channel",
    verbose=True,
    memory=True,
    backstory=(
        "With a flair for simpifying complex topics, you carft"
        "Enaging narratives that captivate and educate, bringing new"
        "discoveries to light in an accessible manner."
    ),
    tools=[yt_tool],
    llm=llm,
    allow_delegation=True
)

