import numpy as np
from collections import Counter

def euclidean_distance(x1, x2):
    return np.sqrt(np.sum((x1 - x2) ** 2))

def knn(train_data, train_labels, test_data, k):
    predictions = []
    for test_instance in test_data:
        distances = []
        for i, train_instance in enumerate(train_data):
            distance = euclidean_distance(test_instance, train_instance)
            distances.append((distance, train_labels[i]))
        distances.sort(key=lambda x: x[0])
        neighbors = distances[:k]
        output_labels = [label for _, label in neighbors]
        most_common = Counter(output_labels).most_common(1)
        predictions.append(most_common[0][0])
    return predictions

train_data = np.array([[1, 2], [2, 3], [3, 4], [5, 7], [6, 8], [7, 9]])
train_labels = np.array([0, 0, 0, 1, 1, 1])
test_data = np.array([[1, 2], [6, 7]])

k = 3
predictions = knn(train_data, train_labels, test_data, k)
print(predictions)
