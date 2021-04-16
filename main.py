import re

if __name__ == "__main__":
    count = 0
    file = "access.log"
    time_we_need = False

    regex_start = r'24/Mar/2009:14:39:35'
    regex_end = r'25/Mar/2009:11:43:29'
    regex = r'TH_photo_'
    regex_status = r'200'

    with open(file, "r", errors="ignore") as file:
        for line in file:
            if regex_end in line:
                time_we_need = False
                break

            if regex_start in line:
                time_we_need = True

            if time_we_need:
                if regex_status in line:
                    for searched_number in re.finditer(regex, line):
                        count += 1
                        print(line)

    file.close()
    print("         Successful number of requests = ", count)