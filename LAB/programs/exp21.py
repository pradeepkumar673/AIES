# Implement Pattern Recognition.

import numpy as np
from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, classification_report

digits = load_digits()
X, y = digits.data, digits.target

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

clf = SVC(kernel='rbf', C=10, gamma=0.01, random_state=42)
clf.fit(X_train, y_train)

y_pred = clf.predict(X_test)
print("Pattern Recognition - Handwritten Digit Classification")
print("Accuracy:", accuracy_score(y_test, y_pred))
print("\nClassification Report:")
print(classification_report(y_test, y_pred))

sample = X_test[:5]
predictions = clf.predict(sample)
print("Sample Predictions:", predictions)
print("Actual Labels:     ", y_test[:5])
