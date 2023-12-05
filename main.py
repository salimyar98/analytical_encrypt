import data, enc_dec

while True:
    word = input('Введите слово кириллицей из 6 букв, которое нужно зашифровать: ').upper()
    if len(word) == 6:
        try:
            matrix_option = int(input('Введите номер варианта от 1 до 50 для определения матрицы ключей: '))
            if 0 < matrix_option < 51:
                break
        except ValueError:
            print("Неверный ввод числа. Попробуйте снова.")

num_eq = []
matrix = data.matrix_option_list[matrix_option]

for i in word:  # вычисление числового эквивалента слова
    num_eq.append(data.coding_alphabet[i])

vector0 = num_eq[:3]
vector1 = num_eq[3:]

result_encrypt = enc_dec.multiply_matrix_vector(matrix, vector0) + enc_dec.multiply_matrix_vector(matrix, vector1)
print('Зашифорованное слово -', result_encrypt)

vector2 = result_encrypt[:3]
vector3 = result_encrypt[3:]
inv_mat = enc_dec.inverse_matrix(matrix)
decode = enc_dec.multiply_matrix_vector(inv_mat, vector2) + enc_dec.multiply_matrix_vector(inv_mat, vector3)
result_decode = []

rounded_numbers = enc_dec.round_numbers(decode)
for num in rounded_numbers:
    result_decode.append(int(num))

print('Расшифрованное слово -', result_decode)

result_word = ''

for i in result_decode:
    result_word += data.coding_alphabet_reverse[i]

print('Слово переведенное из числового эквивалента -', result_word)
