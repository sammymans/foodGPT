# foodGPT :poultry_leg:

foodGPT is a product that aims to incorporate machine learning to optimize one's cooking experience and reducing the amount of food waste. A minority of XX% of university cook regularly - the other portion seldom cook or never cook. Additionally, those who cook approximately waste XX% of ingredients for several reasons: 

- low cooking confidence
- purchased too many groceries for the week
- unsure of what to do with excess ingredients

foodGPT has three main components: computer vision, ingredient substitution, and recipe recommendation. Computer Vision is yet to be implemented, however the other two components can be found in code.

This project was built using [a Kaggle dataset of recipes from food.com](https://www.kaggle.com/datasets/shuyangli94/food-com-recipes-and-user-interactions).

## Smart Substitution Model

The Smart Substitution Model first tokenizes ingredients to a unique 4-digit ID allowing a recipe to be described as a list of ingredient IDs. This list of ingredient IDs is converted to vectors using the Word2Vec model and is then compared to other recipes to find recipes with similar ingredients. For each recipe it provides a similarity score, which identifies how similar a recipe is to the list of user ingredients from a scale of 0 to 1. The model undestands making substitutions based on the user's shelf such as replacing yellow onions for red onions or coffee for espresso. 

## Matrix Factorization Recommendation Model

The recommendation system is a collaborative filtering model which recommends based on user interactions. The dataset was converted to a rating matrix with users as rows, recipe ID's as columns, and the ratings as the values within the matrix. The matrix factorization model splits the matrix into two matrices (user ID vs latent features and recipe IDs vs latent features) which is used to recommend recipes to the user.

## Combined Model

The output of the smart substitution model is a dataframe with the columns Recipe ID, Ingredient List, and Similarity Score Rating. The output of the recommendation model for each user is a dataframe with a column for Recipe ID and a column for a normalized rating. These are merged based on the Recipe ID and a combined rating is calculated by averaging the similarity score and normalized rating. The dataframe is sorted in descending order for the combined rating to output the best recipes for the user. 

## Discussion

Throughout this project, there were multiple challenges the team faced, which are outlined below. 
- Handling NaN values for matrix factorization models
- Dealing with very sparse matrices for accurate matrix factorization
- Reducing time complexity of comparison algorithm
- Validating unsupervised model results

## Future Considerations

One objective to pursuit is to completely implement the computer vision aspect to the product. Ideally, the application will work by taking a photo of the user's groceries receipt to easily load in their 'shelf' or 'fridge' data to be processed for the recommendation system. We will add an algorithm to tokenize these groceries for a cohesive data pipeline.

Additionally, a generative machine learning recipe recommendation approach should be explored. This method may be more effective rather than being limited to recipes that are found on food.com. This will allow for more effective recommendations based on user preferences, as well as ultimately reducing food waste.

## How it Works

1. the user first uses the camera feature of the app to identify the new groceries they want to add to the foodGPT app

![image](https://user-images.githubusercontent.com/79066805/236366823-786ed2eb-292b-4034-a18d-faf7564a001f.png)


2. The user then takes a picture of their fridge to update the list of ingredients they have using computer vision. It is then updated as a list.

![image](https://user-images.githubusercontent.com/79066805/236366912-0af988db-8b86-4cb9-83a5-b57738dff90d.png)


3.  Next, the user provides a prompt to get a recommendation from the model
[img4]

4. The user can also see the list of their favourite recipes to refer to at a later time
[img5]
