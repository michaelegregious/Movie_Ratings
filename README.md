# Movie Ratings relative to age and genre
### A Jupyter Notebook data analysis of the influence of movie age on popularity

## Installing or manipulating locally:

- Simply clone his repository to your local machine, 
- Open with Jupyter Notebook
- Navigate to http://localhost:8888/notebooks/Movie_Ratings/movie_ratings_by_age.ipynb

## Overview

  After parsing and pre-processing data (binarizing and, in some cases ordinally encoding) categorical data, we first examine basic correlations among the data, and then use Machine Learning to see if any combination of factors might predict a better movie rating.
  
  First explorations were made with basic logistic regression as well as C-Support Vector Classifications for predicting data, but arrived at Linear SVC to achieve best results for our (highly categorical) set.
  
  Drawing obvious outcomes from predictive algorithms was not easy with this dataset. Attempting to draw correlations based on age is made challenging by the unequal distribution of movies from given eras (64% 'new', 17% 'medium', and 20% old). Likewise, genres are disproportionately skewed (the highest distribution with 'Drama' 48%, it's next closest neighbor, 'Comedy' at 30%, followed by 'Thriller' at 16%, and the rest of the stragglers between 1% and 12%).
  
  Prediction reports hovered around 48 percent depending on variable adjustment. The fact that there was a substantial divergence among average ratings by genre (and age) seemed not to have a strong affect on predicted outcomes. (For example, averages in genre ranged from 3.54 for Film Noir to 2.51 for Horror. Similarly, old movies defeated new movies on average: 3.22 to 3.05).
  
  Further exploration would be interesting. It might be useful to factor in unique users and to weight their ratings to balance results.
  
## Developer

- [Michael Bush](https://github.com/michaelegregious)
