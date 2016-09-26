__author__ = 'rameshho'

def check_datatype ( reverse_string ):
    def my_reverse_string(string):
        if type(string) == str:
            return reverse_string(string)
        else:
            print("It is of not type string")
            return False
    return my_reverse_string

@check_datatype
def reverse_string(string):

    if string == "":
        return string
    else:
        return reverse_string(string[1:]) + string[0]

print(reverse_string("ramesh"))
