import pandas as pd 
import glob

files = glob.glob("/home/atul/Documents/PandasProjects/Coworking/*.csv")
review_list = []
main_list = []
for file in files:
    pos  = file.find('_reviews')
    if(pos == -1):
        main_list.append(file)
    else:
        review_list.append(file)

# print(main_list)

main_df = []
review_df = []

for file in review_list:
    review_df.append(pd.read_csv(file, low_memory=False))

for file in main_list:
    main_df.append(pd.read_csv(file, low_memory=False))


df_main = pd.concat(main_df, axis=0, ignore_index=True)
print(df_main.count())
df_main.to_csv('coworker.csv', index=False)

df_review = pd.concat(review_df, axis=0, ignore_index=True)
print(df_review.count())
df_review.to_csv('coworker_reviews.csv', index=False)