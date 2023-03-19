from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample data
restaurants = [
    {"id": 1, "name": "Joe's Pizza", "address": "123 Main St", "cuisine": "Italian", "rating": 4.5, "reviews": 100},
    {"id": 2, "name": "Mama Mia's", "address": "456 Elm St", "cuisine": "Italian", "rating": 4.2, "reviews": 50},
    {"id": 3, "name": "Pizzeria Uno", "address": "789 Oak St", "cuisine": "Italian", "rating": 0, "reviews": 0},
]

# Endpoint to retrieve all restaurants
@app.route('/restaurants', methods=['GET'])
def get_restaurants():
    # Get search query from request parameter
    query = request.args.get('q')
    
    # Filter restaurants based on search query
    filtered_restaurants = [r for r in restaurants if (query.lower() in r['name'].lower() or query.lower() in r['cuisine'].lower())]
    
    # Sort restaurants based on request parameters
    sort_by = request.args.get('sort_by', 'rating')
    sort_order = request.args.get('sort_order', 'desc')
    reverse = True if sort_order == 'desc' else False
    sorted_restaurants = sorted(filtered_restaurants, key=lambda r: r[sort_by], reverse=reverse)
    
    # Return response as JSON
    return jsonify(sorted_restaurants)

# Endpoint to retrieve a single restaurant by ID
@app.route('/restaurants/<int:id>', methods=['GET'])
def get_restaurant(id):
    restaurant = next((r for r in restaurants if r['id'] == id), None)
    if restaurant:
        return jsonify(restaurant)
    else:
        return jsonify({"message": "Restaurant not found"}), 404

# Endpoint to create a new restaurant
@app.route('/restaurants', methods=['POST'])
def create_restaurant():
    # Get data from request body
    data = request.get_json()
    name = data.get('name')
    address = data.get('address')
    cuisine = data.get('cuisine')
    rating = data.get('rating', 0)
    reviews = data.get('reviews', 0)
    
    # Generate new ID
    new_id = max(r['id'] for r in restaurants) + 1
    
    # Create new restaurant object
    new_restaurant = {
        "id": new_id,
        "name": name,
        "address": address,
        "cuisine": cuisine,
        "rating": rating,
        "reviews": reviews
    }
    
    # Add new restaurant to list
    restaurants.append(new_restaurant)
    
    # Return response as JSON
    return jsonify(new_restaurant), 201

if __name__ == '__main__':
    app.run(debug=True)
