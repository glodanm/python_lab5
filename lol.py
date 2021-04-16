import re

if __name__ == "__main__":
    count = 0
    file = "access.txt"

    regex = r'\[24\/Mar\/2009:[1-2][1-4]:\d{2}:\d{2} [+-]\d{4}] .*\/TH_photo_.* 200 |'\
            r'\[25\/Mar\/2009:[0-1][1-3]:\d{2}:\d{2} [+-]\d{4}] .*\/TH_photo_.* 200 ' 
            




    with open(file, "r", errors="ignore") as file:
        for line in file:
            for searched_number in re.finditer(regex, line):
                count += 1
                print(line)

    file.close()
    print("         Successful number of requests = ", count)   