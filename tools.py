from crewai_tools import YoutubeChannelSearchTool
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

yt_tool = YoutubeChannelSearchTool(youtube_channel_handle='@BBFisLive', llm=llm )

