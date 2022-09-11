"""
Reverses the sections in a markdown down. A section is a block of text that starts with the Heading 2 mark (i.e. ##).

Example:
    The file contents:
        ## Section 1
        text text text

        ## Section 2
        text text text

        ## Section 3
        text text text
    
    become:
        ## Section 3
        text text text

        ## Section 2
        text text text

        ## Section 1
        text text text

Usage: 
    python reverse-md-sections.py

Author: 
    Riya Jaggi - Sep 10, 2022

"""

def get_sections(s):
    for sec in s.split('\n## '):
        yield sec if sec.startswith('## ') else '## '+sec

def reverse_sections(contents):
    lst = []

    for sec in get_sections(contents):
        lst.insert(0, sec)
    
    return lst

def convert_list_to_string(lst):
    return ''.join(lst)

def main():
    path = " " # INSERT PATH TO MARKDOWN FILE
    f = open(path, 'r')
    contents = f.read()
    # print(contents)
    reversed_contents = convert_list_to_string(reverse_sections(contents))
    f.close()

    f = open(path, 'w')
    f.write(reversed_contents)
    f.close()
    # print(reversed_contents)

if __name__ == "__main__":
    print("RUNNING reverse-md-sections SCRIPT\n\n")
    main()
    print("\n\nEND OF reverse-md-sections SCRIPT")
