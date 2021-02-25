# imports
import pandas as pd
import numpy as np
import os


# 1. Attendance Data

#### Load the attendance.csv file and calculate an attendnace percentage for each student. One half day is worth 50% of a full day, and 10 tardies is equal to one absence.

# Loading the data
attendance = pd.read_csv('attendance.csv')
attendance

# Using melt to narrow a wide data set
attendance = pd.melt(attendance, id_vars = 'Unnamed: 0',
        var_name = 'date',
        value_name= 'count')

# Using rename to clear up a column name
attendance = attendance.rename(columns={'Unnamed: 0': 'student'})

# 2. Coffee Levels

#### Read the coffee_levels.csv file. 

coffee = pd.read_csv('coffee_levels.csv')
coffee.head()

#### Transform the data so that each carafe is in its' own column. 

# Using pivot_table to give each carafe is in its' own column
coffee_tidy = coffee.pivot_table(index = ['hour'],
                                columns = 'coffee_carafe', values = 'coffee_amount')

# Renaming to make the columns clearer
coffee_tidy = coffee_tidy.rename(columns={'x': 'carafe_x', 'y': 'carafe_y', 'z': 'carafe_z'})
coffee_tidy

#### Is this the best shape for the data?

"Best" is a matter of opinion. However, the data is more organized and readable in this form.

# 3. Cake Recipes

#### Read the cake_recipes.csv data. 

cake = pd.read_csv('cake_recipes.csv')

#### Tidy the data as necessary.

# First, melt the data to get temp and rating into unique columns
cake_df = pd.melt(cake, id_vars = 'recipe:position',
                 var_name = 'temp', 
                 value_name = 'rating')

# Using the .rename function to clean up a messy column heading
cake_df = cake_df.rename(columns={'recipe:position': 'recipe'})

# Splitting the recipe column into two seperate columns
cake_df[['recipe', 'oven_position']]= cake_df.recipe.str.split(':', expand = True)

#### Which recipe, on average, is the best? 

# Using groupby function to determine the avg rating by recipe
recipe_rating = cake_df.groupby('recipe').rating.mean()

#### Which oven temperature, on average, produces the best results? 

# Using groupby function to determine the avg rating by temp
temp_rating = cake_df.groupby('temp').rating.mean()

#### Which combination of recipe, rack position, and temperature gives the best result? 

highest_rating = cake_df.sort_values(['rating'], ascending=[False])
highest_rating.head(1)

