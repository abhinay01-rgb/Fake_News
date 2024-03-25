from django.shortcuts import render
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import json

def load_json_data():
    with open('static/news_data.json', 'r') as file:
        return json.load(file)

json_data = load_json_data()
model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

def generate_embeddings(text):
    embeddings = model.encode(text)
    return embeddings

def news(request):
    input_text = request.GET.get('keywords', None)
    context = {'results': None}

    if input_text:
        query_embedding = generate_embeddings(input_text)

        max_similarity = 0
        most_similar_article = None

        for article in json_data.values():
            news_content = article['content']
            news_embedding = generate_embeddings(news_content)
            similarity = cosine_similarity([query_embedding], [news_embedding])[0][0]

            if similarity > max_similarity:
                max_similarity = similarity
                most_similar_article = article

        if most_similar_article:
            max_similarity_formatted = round(max_similarity * 100, 2)
            most_similar_article['similarity'] = max_similarity_formatted
            context['results'] = [most_similar_article]
        print(context)


    return render(request, 'qa_search_results.html', context)
