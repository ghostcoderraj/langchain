from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv

load_dotenv()

model = ChatAnthropic(model = "claude-3-5-sonnet-20141022")

result = model.invoke('what is the capital of bihar?')

print(result.content)