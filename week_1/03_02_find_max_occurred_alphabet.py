def find_max_occurred_alphabet(string):
    alphabet_occurrence_array = [0] * 26

    for char in string:
        if not char.isalpha():
            continue
        arr_index = ord(char) - ord('a')
        alphabet_occurrence_array[arr_index] += 1


    print(alphabet_occurrence_array)
    max_occurrence = 0
    max_alphabet_index = 0
    for index in range(len(alphabet_occurrence_array)):
        alphabet_occurrence = alphabet_occurrence_array[index]
        if alphabet_occurrence > max_occurrence:
            max_occurrence = alphabet_occurrence
            max_alphabet_index = index

    return chr(max_alphabet_index + ord('a'))


result = find_max_occurred_alphabet
print("정답 = a 현재 풀이 값 =", result("hello my name is sparta"))
print("정답 = a 현재 풀이 값 =", result("sparta coding club"))
print("정답 = s 현재 풀이 값 =", result("best of best sparta"))
