def print_directory_contents(sPath):
    import os
    sChild = os.listdir(sPath)
    for my_child in sChild:
        my_child_path = os.path.join(sPath, my_child)
        if os.path.isdir(my_child_path):
            print_directory_contents(my_child_path)
        else:
            print(my_child_path)

print_directory_contents("D:\Automation_problems")
