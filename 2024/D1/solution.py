def preplist_sorted(input):
    with open(input, 'r') as file:
        text = file.read()
    array = text.split()
    list1 = []
    list2 = [] 
    for i, item in enumerate(array):
        if i % 2 == 0:
            list1.append(item)
        else:
            list2.append(item)
    list1.sort()        
    list2.sort()
    return list1, list2

def measure_distance(list1, list2):
    distance =[]
    for i in range(len(list1)):
        distance.append(abs(int(list1[i]) - int(list2[i])))
    return sum(distance)

def measure_similarity(list1, list2):
    similarity =[]
    for item in list1:
        count = list2.count(item)
        if count == 0:
            similarity.append(0)
        else:
            score = int(item) * count
            similarity.append(int(score))
    return sum(similarity)

def main():
    input = 'input.txt'
    list1, list2 = preplist_sorted(input)
    distance = measure_distance(list1, list2)
    similarity = measure_similarity(list1, list2)
    print("Total distance: ", distance)
    print("Similarity score: ", similarity)

if __name__ == '__main__':
    main()
