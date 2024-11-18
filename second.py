import pandas as pd

def is_more_general(h1, h2):
    more_general_parts = []
    for x, y in zip(h1, h2):
        mg = x == '?' or (x != '0' and (x == y or y == '0'))
        more_general_parts.append(mg)
    return all(more_general_parts)

def generalize_S(example, S):
    for i in range(len(S)):
        if S[i] == '0':
            S[i] = example[i]
        elif S[i] != example[i]:
            S[i] = '?'
    return S

def specialize_G(example, G, domain):
    new_G = []
    for hypothesis in G:
        for i in range(len(hypothesis)):
            if hypothesis[i] == '?':
                for value in domain[i]:
                    if value != example[i]:
                        new_hypothesis = hypothesis[:i] + (value,) + hypothesis[i+1:]
                        new_G.append(new_hypothesis)
    return new_G

def remove_inconsistent_hypotheses(S, G, X, y):
    S = [s for s in S if all(is_more_general(g, s) for g in G)]
    G = [g for g in G if all(is_more_general(g, s) for s in S)]
    return S, G

def candidate_elimination_algorithm(X, y):
    num_attributes = len(X[0])
    S = ['0'] * num_attributes
    G = [('?',) * num_attributes]
    
    domain = [set([X[i][j] for i in range(len(X))]) for j in range(num_attributes)]

    for i, example in enumerate(X):
        if y[i] == 'Yes':
            S = generalize_S(example, S)
            G = [g for g in G if is_more_general(g, S)]
        else:
            G = specialize_G(example, G, domain)
            S = [s for s in S if all(is_more_general(g, s) for g in G)]
    
    S, G = remove_inconsistent_hypotheses([S], G, X, y)
    
    return S, G

def get_user_input():
    num_examples = int(input("Enter the number of training examples: "))
    attributes = int(input("Enter the number of attributes per example: "))
    
    X = []
    y = []

    for i in range(num_examples):
        example = []
        print(f"Enter the attributes for example {i+1}:")
        for j in range(attributes):
            attribute = input(f"Attribute {j+1}: ")
            example.append(attribute)
        X.append(example)
        label = input(f"Enter the class label (Yes/No) for example {i+1}: ")
        y.append(label)

    return X, y

X, y = get_user_input()
S_final, G_final = candidate_elimination_algorithm(X, y)
print("Final Specific Hypothesis (S):", S_final)
print("Final General Hypotheses (G):", G_final)
