import difflib

def recommend(movie_name, data, similarity):
    import difflib
    
    # Step 1: get all titles
    list_of_all_titles = data['title'].tolist()
    
    # Step 2: find closest match
    find_close_match = difflib.get_close_matches(movie_name, list_of_all_titles)
    
    # Step 3: handle case when no match found
    if not find_close_match:
        return [], None
    
    # Step 4: take best match
    close_match = find_close_match[0]
    
    # Step 5: get index of that movie
    index_of_the_movie = data[data.title == close_match].index[0]
    
    # Step 6: compute similarity scores
    similarity_score = list(enumerate(similarity[index_of_the_movie]))
    
    # Step 7: sort movies
    sorted_similar_movies = sorted(similarity_score, key=lambda x: x[1], reverse=True)
    
    # Step 8: collect top recommendations
    recommended = []
    for movie in sorted_similar_movies[1:30]:
        index = movie[0]
        title = data.iloc[index]['title']
        recommended.append(title)
    
    return recommended, close_match