import cohere
import tkinter as tk
from tkinter import messagebox

# Set your Cohere API key securely
API_KEY = "vjJSIrB9yBwMAEEtfd3ChNbBZp6j7r1wFhE1cqnX"  # Replace this with your new key

# Initialize Cohere client
co = cohere.Client(API_KEY)

# Pantry to track available ingredients
smart_pantry = set()

# Function to generate recipes with nutritional analysis using Cohere
def get_recipes(ingredients):
    prompt = (
        f"Generate 3 delicious recipes using these ingredients: {', '.join(ingredients)}. "
        f"For each recipe, provide a nutritional breakdown, including calories, protein, carbohydrates, and fat per serving."
    )

    try:
        response = co.generate(
            model='command',  # Choose model (default or 'command')
            prompt=prompt,
            max_tokens=400,
            temperature=0.7,
        )
        
        # Extract the generated text
        return response.generations[0].text.strip()
    
    except Exception as e:
        return f"Error: {str(e)}"

# Function to handle button click and generate recipes
def generate_recipes():
    if not smart_pantry:
        messagebox.showerror("Error", "Your pantry is empty! Add some ingredients first.")
        return

    # Get recipes from Cohere based on pantry items
    recipes = get_recipes(list(smart_pantry))

    # Display recipes with nutritional information
    result_text.delete('1.0', tk.END)
    result_text.insert(tk.END, "🍽️ Recipe Suggestions with Nutritional Info:\n\n" + recipes)

# Function to add an ingredient to the pantry
def add_ingredient():
    ingredient = pantry_entry.get().strip().lower()
    if ingredient:
        smart_pantry.add(ingredient)
        update_pantry_display()
        pantry_entry.delete(0, tk.END)

# Function to remove an ingredient from the pantry
def remove_ingredient():
    ingredient = pantry_entry.get().strip().lower()
    if ingredient in smart_pantry:
        smart_pantry.remove(ingredient)
        update_pantry_display()
        pantry_entry.delete(0, tk.END)
    else:
        messagebox.showerror("Error", f"{ingredient} not found in pantry.")

# Function to update pantry display
def update_pantry_display():
    pantry_list.delete('1.0', tk.END)
    if smart_pantry:
        pantry_list.insert(tk.END, "🧺 Pantry Items:\n" + ", ".join(smart_pantry))
    else:
        pantry_list.insert(tk.END, "🧺 Pantry is empty. Add some ingredients!")

# Create the main application window
root = tk.Tk()
root.title("🍲 Personalized Culinary Companion 🍲")
root.geometry("600x600")

# Heading label
title_label = tk.Label(root, text="🍲 Personalized Culinary Companion 🍲", font=("Arial", 14, "bold"))
title_label.pack(pady=10)

# Section for Smart Pantry
pantry_label = tk.Label(root, text="Smart Pantry: Add/Remove Ingredients")
pantry_label.pack(pady=5)

pantry_entry = tk.Entry(root, width=40)
pantry_entry.pack(pady=5)

add_button = tk.Button(root, text="➕ Add Ingredient", command=add_ingredient)
add_button.pack(pady=2)

remove_button = tk.Button(root, text="❌ Remove Ingredient", command=remove_ingredient)
remove_button.pack(pady=2)

pantry_list = tk.Text(root, height=5, width=60)
pantry_list.pack(pady=5)

# Button to generate recipes
generate_button = tk.Button(root, text="🍽️ Get Recipes", command=generate_recipes)
generate_button.pack(pady=10)

# Text box to display generated recipes with nutrition info
result_text = tk.Text(root, height=15, width=70, wrap=tk.WORD)
result_text.pack(pady=10)

# Run the application
update_pantry_display()
root.mainloop()
