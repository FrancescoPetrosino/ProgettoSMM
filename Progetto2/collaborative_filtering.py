# function to get the top k similar users
def get_similar_users(user_id, user_index_map, cosine_sim, k=5):
    user_index = user_index_map[user_id]
    similar_users = list(enumerate(cosine_sim[user_index]))
    similar_users = sorted(similar_users, key=lambda x: x[1], reverse=True)
    similar_users = similar_users[1:k+1]
    return similar_users

# function to make recommendations to a user
def recommend_items(user_id, user_item_matrix, cosine_sim, k=5):
    similar_users = get_similar_users(user_id, user_item_matrix, cosine_sim, k)
    similar_users_index = [index for index, similarity in similar_users]
    similar_users_ratings = user_item_matrix.iloc[similar_users_index]
    recommended_items = similar_users_ratings.mean().sort_values(ascending=False)
    return recommended_items