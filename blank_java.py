from read_conf import read_config
import packs
from IPython import embed

blank_dict, info_dict = read_config()

blank_file = open("Fake/{}.java".format(info_dict["CLASS"]), "w")
blank_file.write(packs.l1 % (info_dict["CLASS"]))
blank_file.write(packs.l2 % (info_dict["RETURN"], info_dict["FUNC_NAME"], info_dict["INPUT"]))
blank_file.write("        " + blank_dict[info_dict["RETURN"]] + '\n')
blank_file.write(packs.end)
blank_file.close()