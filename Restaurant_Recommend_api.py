from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

# A sample dictionary to store the restaurant data

restaurants = {
    1: {"name": "Le Big Mac", "rating": 4.5},
    2: {"name": "Lafayette", "rating": 4.2},
    3: {"name": "KFC", "rating": 4.7},
    4: {"name": "Sushi", "rating": 3.9},
    5: {"name": "Steak", "rating": 4.8},
}

#To  be extracted from database



# Route to get a list of recommended restaurants
@app.route('/recommend', methods=['GET'])
def recommend_restaurant():
    # Retrieve the rating parameter from the request
    rating = request.args.get('rating')
    
    # Convert the rating parameter to a float
    rating = float(rating)
    
    # Find all restaurants with a rating greater than the provided rating
    recommended_restaurants = [restaurant for restaurant in restaurants.values() if restaurant['rating'] >= rating]
    
    # Return the recommended restaurants as JSON
    return jsonify(recommended_restaurants)


    
@app.route('/recommend/choose-restaurant', methods=['GET'])
def choose_retaurant():
    


if __name__ == '__main__':
    app.run(debug=True)
