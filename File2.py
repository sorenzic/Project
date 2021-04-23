import pandas as pd
import sqlite3

connection = sqlite3.connect("C:\\ratingrecommendation_app.sqlite")

# Load the data into a DataFrame
get_course_rating = pd.read_sql_query("SELECT course_id,rating from ratings", connection)
# Select only data for 2002
recommendPandas = (get_course_rating.groupby(['course_id'],).mean())

recommendPandasSorted = recommendPandas.sort_values(by=['rating','course_id'],  ascending=[False,False])
print(recommendPandasSorted)

# Write the new DataFrame to a new SQLite table
recommendPandasSorted.to_sql("recommendPandas", connection, if_exists="replace")


connection.close()