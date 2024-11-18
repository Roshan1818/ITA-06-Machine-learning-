def find_s_algorithm(training_data):
    num_attributes = len(training_data[0]) - 1
    specific_hypothesis = ['0'] * num_attributes
    
    for example in training_data:
        if example[-1] == 'Yes':
            for i in range(num_attributes):
                if specific_hypothesis[i] == '0':
                    specific_hypothesis[i] = example[i]
                elif specific_hypothesis[i] != example[i]:
                    specific_hypothesis[i] = '?'
    
    return specific_hypothesis

training_data = [
    ['Sunny', 'Warm', 'Normal', 'Strong', 'Warm', 'Same', 'Yes'],
    ['Sunny', 'Warm', 'High', 'Strong', 'Warm', 'Same', 'Yes'],
    ['Rainy', 'Cold', 'High', 'Strong', 'Warm', 'Change', 'No'],
    ['Sunny', 'Warm', 'High', 'Strong', 'Cool', 'Change', 'Yes']
]

hypothesis = find_s_algorithm(training_data)
print("The most specific hypothesis found by FIND-S:")
print(hypothesis)
