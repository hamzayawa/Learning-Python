# Define a dictionary to store the user profiles
user_profiles = {}

# Function to add a viewed product to a user's profile
def add_viewed_product(user_id, product_id):
    # Check if the user already exists in the dictionary
    if user_id not in user_profiles:
        # If not, create a new set for the user's viewed products
        user_profiles[user_id] = {'viewed': set(), 'purchased': set()}
    # Add the product ID to the user's viewed products set
    user_profiles[user_id]['viewed'].add(product_id)

# Function to add a purchased product to a user's profile
def add_purchased_product(user_id, product_id):
    # Check if the user already exists in the dictionary
    if user_id not in user_profiles:
        # If not, create a new set for the user's purchased products
        user_profiles[user_id] = {'viewed': set(), 'purchased': set()}
    # Add the product ID to the user's purchased products set
    user_profiles[user_id]['purchased'].add(product_id)

# Function to get a set of similar products based on a user's profile
def get_similar_products(user_id):
    # Create an empty set to store the similar products
    similar_products = set()
    # Get the user's viewed and purchased products sets
    viewed_products = user_profiles[user_id]['viewed']
    purchased_products = user_profiles[user_id]['purchased']
    # Loop through the viewed products set
    for viewed_product in viewed_products:
        # Check if the viewed product is also in the purchased products set
        if viewed_product in purchased_products:
            # If so, add all of the products that are associated with the viewed product to the similar products set
            similar_products |= viewed_to_products[viewed_product]
    # Return the similar products set
    return similar_products

# Example usage
add_viewed_product(1, 100)
add_viewed_product(1, 200)
add_viewed_product(2, 100)
add_purchased_product(2, 300)
add_purchased_product(3, 100)

# Define a dictionary to map viewed products to associated products
viewed_to_products = {
    100: {101, 102, 103},
    200: {201, 202, 203},
    300: {301, 302, 303}
}

# Get similar products for user 2
similar_products = get_similar_products(1)

# Print
print(similar_products)
