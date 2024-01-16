# foodGPT :poultry_leg:
Created by: [@sammymans](https://www.github.com/sammymans) 🦧, [@rspcunningham](https://www.github.com/rspcunningham) 😈, [@rohansaxena1224](https://www.github.com/rohansaxena1224) 🦦, and [@meoson129](https://www.github.com/meoson129) :dog:

Built for [Borealis AI](https://www.borealisai.com) (Lets Solve It program).

Read our white paper [here](https://www.rspcunningham.com/foodGPT-white-paper.pdf). 
******

foodGPT is a product that leverages machine learning to optimize one's cooking experience and to reduce the amount of food waste. Only 15% of university students cook regularly - the other portion cooks occasionally or not at all. Those who do cook throw out more than 50% of their ingredients for several reasons: 

- low cooking confidence
- purchased too many groceries for the week
- unsure of what to do with excess leftovers

foodGPT has three main components: an ingredient substitution model, a recommendation engine, and a computer vision pipeline (which has yet to be implemented, see Future Considerations below). 

This project was built using [a Kaggle dataset of aggregated recipes from food.com](https://www.kaggle.com/datasets/shuyangli94/food-com-recipes-and-user-interactions).

## Smart Substitution Model

The Smart Substitution Model first tokenizes ingredients to a unique 4-digit ID, allowing each recipe to be described as a unique list of these IDs. Ingredient embeddings are generated using a Word2Vec implementation that takes each ID as a 'word' and each recipe as the provided context. Using a ball tree algorithm, the IDs from the user's inventory are compared with the ingredients in each recipe, generating a similarity score which identifies how similar a recipe is to the best match from what the user has available. Smart substitutions are provided, such as replacing white onions with yellow onions, or coffee for espresso based on the model's knowledge of ingredient usage context. The similarity score for each recipe is generated between 0 and 1. 

## Recommendation Model

The Recommendation System is a collaborative filtering model that provides recommendations based on user interactions. The dataset provided review data that was converted to a matrix comparing users and recipes, with individual values representing the rating that user gave to that recipe. Two latent feature matrices are generated, which are iteratively solved for by the model and multiplied together to fill in the missing review data of the initially sparse review matrix. The rating for each recipe is normalized to between 0 and 1. 

## Combined Model

The output of the smart substitution model is a dataframe with the columns Recipe ID, Ingredient List, and Similarity Score. The output of the recommendation model for each user is a dataframe with the columns Recipe ID, and Rating. The two scorings are combined by simply averaging their values to create a hybrid score that reflects both how minor the substitutions needed are and how likely the user is to enjoy it.

## Challenges

Through this project, the team faced multiple issues:
- Handling NaN values for matrix factorization models
- Dealing with very sparse matrices for accurate matrix factorization
- Reducing time complexity of comparison algorithm
- Validating unsupervised model results

## Future Considerations

The next step is to completely implement the computer vision aspect of the product. Ideally, the application will allow a user to take a photo of their fridge, pantry, or grocery receipt to easily load ingredients into their inventory ('shelf'). We will add an algorithm to tokenize these groceries for a cohesive data pipeline.

Additionally, a generative machine learning recipe recommendation approach should be explored. This method may be more effective because it will not be limited by the recipes found on food.com. It will also be more 'consistent' in the recipes it provides, rather than having certain recipes clearly in the 'style' of the source that added them to food.com. This will allow for more effective recommendations based on user preferences, ultimately reducing food waste.

## How it Works

1. The user first uses the camera feature of the app to identify the new groceries they want to add to the foodGPT app
2. The user then takes a picture of their fridge to update the list of ingredients they have using computer vision. It is then updated as a list.
3.  Next, the user provides a prompt to get a recommendation from the model
4. The user can also see the list of their favourite recipes to refer to at a later time

https://user-images.githubusercontent.com/79066805/236372270-62de19d6-d56e-4ce2-afde-92fc03527e9e.mp4
