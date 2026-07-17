from dotenv import load_dotenv
import os
from crewai_tools import SerperDevTool


load_dotenv()
api_key = os.getenv('SERPER_API_KEY')
if api_key is not None:
    os.environ['SERPER_API_KEY'] = api_key

tool= SerperDevTool()