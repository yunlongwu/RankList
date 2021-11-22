# 附加题
def compare_verson(v1, v2):
    v1_list = v1.split(".")
    v2_list = v2.split(".")
    v_count = 0
    while v_count < max(len(v1_list), len(v2_list)):
        try:
            v1_num = int(v1_list[v_count])
        except:
            v1_num = 0
        try:
            v2_num = int(v2_list[v_count])
        except:
            v2_num = 0
        if v1_num > v2_num:
            return 1
        if v1_num < v2_num:
            return -1
        v_count += 1
    return 0


version1 = "0.1"
version2 = "1.1"

version1 = "1.0.1"
version2 = "1"

version1 = "7.5.2.4"
version2 = "7.5.3"

version1 = "1.01"
version2 = "1.001"

version1 = "1.0"
version2 = "1.0.0"
print(compare_verson(version1, version2))
