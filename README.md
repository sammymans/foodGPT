# foodGPT :poultry_leg:

foodGPT is a product that aims to incorporate machine learning to optimize one's cooking experience and reducing the amount of food waste. A minority of XX% of university cook regularly - the other portion seldom cook or never cook. Additionally, those who cook approximately waste XX% of ingredients for several reasons: 

- low cooking confidence
- purchased too many groceries for the week
- unsure of what to do with excess ingredients

foodGPT has three main components: computer vision, ingredient substitution, and recipe recommendation. Computer Vision is yet to be implemented, however the other two components can be found in code.

This project was built using [This Dataset](https://www.kaggle.com/datasets/shuyangli94/food-com-recipes-and-user-interactions).

## Smart Substitution Model

The Smart Substitution Model first tokenizes ingredients to a unique 4-digit ID allowing a recipe to be described as a list of ingredient IDs. This list of ingredient IDs is converted to vectors using the Word2Vec model and is then compared to other recipes to find recipes with similar ingredients. The model undestands making substitutions based on the user's shelf such as replacing yellow onions for red onions or coffee for espresso.

## Matrix Factorization Recommendation Model

## Combined Model

## Discussion

## Future Considerations
