from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_distances
import numpy as np

load_dotenv()

embedding = OpenAIEmbeddings(model='text-embedding-3-large',dimensions=300)



