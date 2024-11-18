import pandas as pd
import math

def entropy(data):
    labels = data.iloc[:, -1]
    label_counts = labels.value_counts()
    total_instances = len(labels)
    entropy_value = 0
    for count in label_counts:
        prob = count / total_instances
        entropy_value -= prob * math.log2(prob)
    return entropy_value

def information_gain(data, attribute):
    total_entropy = entropy(data)
    values = data[attribute].unique()
    weighted_entropy = 0
    for value in values:
        subset = data[data[attribute] == value]
        prob = len(subset) / len(data)
        weighted_entropy += prob * entropy(subset)
    return total_entropy - weighted_entropy

def best_attribute(data):
    attributes = data.columns[:-1]
    info_gains = {attr: information_gain(data, attr) for attr in attributes}
    return max(info_gains, key=info_gains.get)

def id3(data, tree=None):
    target = data.iloc[:, -1].unique()
    if len(target) == 1:
        return target[0]
    if data.shape[1] == 1:
        return data.iloc[:, -1].mode()[0]
    best_attr = best_attribute(data)
    if tree is None:
        tree = {}
        tree[best_attr] = {}
    for value in data[best_attr].unique():
        subset = data[data[best_attr] == value].drop(columns=[best_attr])
        subtree = id3(subset)
        tree[best_attr][value] = subtree
    return tree

def classify(instance, tree):
    if not isinstance(tree, dict):
        return tree
    attribute = next(iter(tree))
    value = instance[attribute]
    subtree = tree[attribute].get(value, None)
    if subtree is None:
        return None
    return classify(instance, subtree)

data = {
    'Outlook': ['Sunny', 'Sunny', 'Overcast', 'Rainy', 'Rainy', 'Rainy', 'Overcast', 'Sunny', 'Sunny', 'Rainy', 'Sunny', 'Overcast', 'Overcast', 'Rainy'],
    'Temperature': ['Hot', 'Hot', 'Hot', 'Mild', 'Cool', 'Cool', 'Cool', 'Mild', 'Cool', 'Mild', 'Mild', 'Mild', 'Hot', 'Mild'],
    'Humidity': ['High', 'High', 'High', 'High', 'Normal', 'Normal', 'Normal', 'High', 'Normal', 'Normal', 'Normal', 'High', 'Normal', 'High'],
    'Wind': ['Weak', 'Strong', 'Weak', 'Weak', 'Weak', 'Strong', 'Strong', 'Weak', 'Weak', 'Weak', 'Strong', 'Strong', 'Weak', 'Strong'],
    'Play Tennis': ['No', 'No', 'Yes', 'Yes', 'Yes', 'No', 'Yes', 'No', 'Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'No']
}
df = pd.DataFrame(data)

decision_tree = id3(df)

print("Decision Tree:", decision_tree)

new_instance = {'Outlook': 'Sunny', 'Temperature': 'Cool', 'Humidity': 'High', 'Wind': 'Strong'}
classification = classify(new_instance, decision_tree)
print(f"The classification for the new instance is: {classification}")
