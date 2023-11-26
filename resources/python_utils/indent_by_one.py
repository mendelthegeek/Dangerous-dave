import re

filename = r"C:\Users\Mendel\AppData\Roaming\JetBrains\PyCharmCE2023.2\scratches\scratch_4.txt"

file = open(filename, 'r')
lines = file.readlines()
file.close()


def recursive_indent(sub_str):
    # print("FUNCTION CALL:" +sub_str)
    if sub_str[-1] != "\n":
        sub_str += "\n"
    pattern = re.compile(r"(.*?)\((\d{2,3})(.*)")
    match = pattern.match(sub_str)
    if not match:
        return sub_str
    # print("MATCH: " + match.group(2))
    extracted_value = match.group(2)
    value = int(extracted_value)
    if value > 750:
        return sub_str
    replace_value = str(value - 1) if value > 35 else str(value)
    newline = match.group(1) + "(" + replace_value + recursive_indent(match.group(3))
    return newline


with open(filename, 'w') as file:
    for line in lines:
        newline = recursive_indent(line)
        # print("FINISHED PRODUCT: " +newline)
        file.write(newline)
