from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embedding = OpenAIEmbeddings(model='text-embedding-3-large',dimensions=300)

documents = [
    "Virat Kohli is an indian cricketer known for his aggressive batting and leadership."
]

query = 'tell me about virat kohli'

doc_embeddings = embedding.embed_documents(documents)

query_embedding = embedding.embed_query(query)

scores = cosine_similarity([query_embedding],doc_embeddings)[0]

index,score = sorted(list(enumerate(scores)),key=lambda x:x[1])[-1]

print(query)
print(documents[index])
print('similarity score is:',score)
