from langchain_huggingface import HuggingFaceEndpointEmbeddings
from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity
load_dotenv()

embeddings_model= HuggingFaceEndpointEmbeddings(
    repo_id="sentence-transformers/all-MiniLM-L6-v2"
)

documents=[
    "Virat Kohli is an Indian cricketer known for his aggressive batting and leadership.",
    "MS Dhoni is a former Indian captain famous for his calm demeanor and finishing skills.",
    "Sachin Tendulkar, also known as the 'God of Cricket', holds many batting records.",
    "Rohit Sharma is known for his elegant batting and record-breaking double centuries.",
    "Jasprit Bumrah is an Indian fast bowler known for his unorthodox action and yorkers."
]

query = 'tell me about virat kohli'

doc_embeddings=embeddings_model.embed_documents(documents)
query_embeddings= embeddings_model.embed_query(query)

scores=cosine_similarity([query_embeddings],doc_embeddings)[0]
scores=scores.tolist()
index, score=sorted(list(enumerate(scores)),key=lambda x:x[1])[-1]
print(sorted(list(enumerate(scores)),key=lambda x:x[1]))

# unsorted=[(0, 0.8177796657312031), (1, 0.42080597544205967), (2, 0.48464813027339804), (3, 0.5056735975837177), (4, 0.3744492403869709)]  

# sorted=[(4, 0.3744492403869709), (1, 0.42080597544205967), (2, 0.48464813027339804), (3, 0.5056735975837177), (0, 0.8177796657312031)]

print(query)
print(documents[index])
print("similarity score is:", score)