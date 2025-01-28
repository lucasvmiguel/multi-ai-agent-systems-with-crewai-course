import warnings
warnings.filterwarnings("ignore")

from langchain_community.llms import Ollama
from crewai import Agent, Task, Crew

model = Ollama(model="llama3.2")



print(model.invoke("when Brazil was discovered?"))