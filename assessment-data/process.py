log_file = open("um-server-01.txt")


def sales_reports(log_file):                # 'def' is defining the function 'sales_report' which takes in the parameter 'log_file' which is the file it will sort thru
    for line in log_file:                   # for loop that will iterate thru the file log_file 
        line = line.rstrip()                # line is taking on method '.rstrip' which removes the trailing space at the end of string 
        day = line[0:3]                     # string splicing first number is the start index (inclusive) and second number the end index (exclusive)
        if day == "Mon":                    # conditional statement if variable 'day' equals 'Mon' then return with print statement
            print(line)


sales_reports(log_file)

