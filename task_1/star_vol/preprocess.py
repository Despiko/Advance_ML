from sklearn.feature_extraction.text import CountVectorizer
label_prefix = "__label__"
data = []
with open("text.txt") as f:
    data = f.read().splitlines()
count_vectorizer = CountVectorizer(min_df=0, max_df=0.99, max_features=10000)
X_train = count_vectorizer.fit_transform(data)
X_train = count_vectorizer.inverse_transform(X_train)
with open("train_starspace.txt", 'w+') as file:
    for number, row in enumerate(X_train):
        file.write(' '.join(X_train[number]) + ' ' + label_prefix + str(number))
        file.write('\n')
file.close()