import os
import glob

base_path = os.getcwd()
text_dir = 'text_files'

file_name = []
file_len = []
file_text = []
for filename in glob.glob(os.path.join(base_path, text_dir, '*.txt')):
    file_name.append(filename[-5:])
    with open(filename, encoding='utf-8') as file:
        text_lines = file.readlines()
        i = []
        for el in text_lines:
            i.append(el.strip())
        file_text.append(i)
        i = []

        file_len.append(len(text_lines))
zip_text = list(zip(file_name, file_len, file_text))

text1 = []
text2 = []
text3 = []

for elements in zip_text:
    if elements == zip_text[0]:
        if elements[0]:
            text1.append(elements[0])
        if elements[1]:
            text1.append(elements[1])
        if elements[2]:
            text1.append(elements[2])
    elif elements == zip_text[1]:
        if elements[0]:
            text2.append(elements[0])
        if elements[1]:
            text2.append(elements[1])
        if elements[2]:
            text2.append(elements[2])
    else:
        if elements[0]:
            text3.append(elements[0])
        if elements[1]:
            text3.append(elements[1])
        if elements[2]:
            text3.append(elements[2])

final_text = []

if text1[1] > text2[1]:
    if text1[1] > text3[1] and text2[1] > text3[1]:
        final_text.append(text1)
        final_text.append(text2)
        final_text.append(text3)
    elif text3[1] > text2[1] and text3[1] > text1[1]:
        final_text.append(text2)
        final_text.append(text1)
        final_text.append(text3)

for elements in final_text:
    for element in elements:
        if element == elements[2]:
            for line in element:
                print(line)
        else:
            print(element)
