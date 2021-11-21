def reduction(numbers):
    new_numbers = []
    if len(numbers) == 2:
        return numbers
    else:
        for i in range(len(numbers) // 2):
            new_numbers.append(numbers[i] + numbers[-i - 1])
        if len(numbers) % 2 != 0:
            new_numbers.append(numbers[len(numbers) // 2])
        # print(new_numbers)
        return reduction(new_numbers)

 
def compatability(name_1, name_2, d=False):
    name_1 = name_1.lower()
    name_2 = name_2.lower()
    both_names = ''.join([name_1, name_2])
    dupe_letters = list(set(list(both_names)) & set(list(both_names)))
    numbers = []
    if d:
        print(dupe_letters)
        print(both_names)
    for i, letter in enumerate(both_names):
        if letter not in dupe_letters:
            numbers.append(1)
        else:
            if letter in both_names[:i]:
                continue
            numbers.append(both_names.count(letter))
        if d:
            print(letter, numbers)
    pct = reduction(numbers)
    
    return f'{str(pct[0])[0]}{str(pct[-1])[0]}%'


n1 = 'Alexander'
n2 = 'Emily'
print(compatability(n1, n2))
