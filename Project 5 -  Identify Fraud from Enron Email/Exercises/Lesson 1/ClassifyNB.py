def classify(features_train, labels_train):
    """ compute the accuracy of your Naive Bayes classifier """
    ### import the sklearn module for GaussianNB
    from sklearn.naive_bayes import GaussianNB

    ### create classifier
    clf = GaussianNB()

    ### fit the classifier on the training features and labels
    clf.fit(features_train, labels_train)
### use the trained classifier to predict labels for the test features
    return clf.predict(features_test)


print clf.score(features_test, labels_test)
