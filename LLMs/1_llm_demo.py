from langchain_openai import OpenAI
from dotenv import load_dotenv


load_dotenv()

llm = OpenAI(model = 'gpt-3.5-turbo-instruct')

result = llm.invoke('What is the capital of india');

print(result) #due to i have not credit in open AI api platform that reason answer not show after printing

