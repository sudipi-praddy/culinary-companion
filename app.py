import streamlit as st
import openai

# Set OpenAI API Key
openai.api_key = "YOUR_OPENAI_API_KEY"

# Page Title
st.title("🍲 The Personalized Culinary Companion")

# User Input for Ingredients
ingredients = st.text_input("Enter Ingredients (comma-separated):", "eggs, onion, tomato")

# Cooking Preference Options
preference = st.selectbox("Choose Cooking Preference:", ["Quick", "Gourmet", "Budget-Friendly"])

# Button to Generate Recipes
if st.button("🍽️ Generate Recipes"):
    # Create prompt for GPT
    prompt = f"Generate 5 {preference.lower()} recipes using these ingredients: {ingredients}. Provide a nutritional breakdown for each recipe."

    # Call GPT API
    try:
        response = openai.Completion.create(
            model="gpt-3.5-turbo",
            prompt=prompt,
            max_tokens=500,
            temperature=0.7,
        )

        # Display the recipes
        recipes = response.choices[0].text.strip()
        st.text_area("🍲 Suggested Recipes:", value=recipes, height=300)
    except Exception as e:
        st.error(f"Error: {e}")
