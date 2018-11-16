from read_conf import read_config
import packs


blank_dict, info_dict = read_config()

fl = open("HTMLS/APT_ {}.html".format(info_dict["CLASS"].lower()))
html = [x for x in fl]


def single_process(l):
    tmp = [n for n in l]
    while tmp[0] == " ":
        tmp = tmp[1:]
    while tmp[-1] == " ":
        tmp = tmp[:-1]
    return "".join(tmp)


def ls_process(l):
    tmp = [n for n in l]
    while tmp[0] == " ":
        tmp = tmp[1:]
    while tmp[-1] == " ":
        tmp = tmp[:-1]
    for x in range(len(tmp)):
        if tmp[x] == "[":
            tmp[x] = "{"
            break
    for x in range(len(tmp) - 1, -1, -1):
        if tmp[x] == "]":
            tmp[x] = "}"
            break
    return "".join(tmp)


def parsing_line(s):
    assert "</td><td>" in s
    s = s.split("</td><td>")[1]
    k1 = s.split("  </pre>: ")[0].split("<pre>")[1].split("</pre>")[0]
    if "[]" in info_dict["RETURN"]:
        k1 = ls_process(k1)
        k1 = "new " + info_dict["RETURN"] + k1
    else:
        k1 = single_process(k1)
    # print(k1)
    k2 = s.split("  </pre>: ")[1][:-11]
    if "[]" in info_dict["INPUT"]:
        k2 = ls_process(k2)
        k2 = "new " + info_dict["INPUT"].split(" ")[0] + k2
    else:
        k2 = single_process(k2)
    # print(k2)
    total_dic.update({k2: k1})

total_dic = {}
for l in html:
    if """<td class="fail">fail</td><td>expected<pre>""" in l:
        parsing_line(l)
print(total_dic)

input_type = info_dict["INPUT"].split(" ")[0]
input_name = info_dict["INPUT"].split(" ")[1]

standard = "        if ({}) return {};\n"
if_for_int = "{} == {}"
if_for_string = "{}.equals{}"
if_for_arrays = "Arrays.deepEquals({}, {})"

blank_dict, info_dict = read_config()

blank_file = open("Solution/{}.java".format(info_dict["CLASS"]), "w")
blank_file.write("import java.util.Arrays;\n")
blank_file.write(packs.l1 % (info_dict["CLASS"]))
blank_file.write(packs.l2 % (info_dict["RETURN"], info_dict["FUNC_NAME"], info_dict["INPUT"]))

for k2 in total_dic:
    if input_type == "int":
        eq = if_for_int.format(k2, input_name)
    if input_type == "String":
        eq = if_for_string.format(k2, input_name)
    if "[]" in input_type:
        eq = if_for_arrays.format(k2, input_name)
    else:
        break
    std = standard.format(eq, total_dic[k2])
    blank_file.write(std)

blank_file.write("        " + blank_dict[info_dict["RETURN"]] + '\n')
blank_file.write(packs.end)
blank_file.close()
