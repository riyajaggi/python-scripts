def add_line(content):
    return content.replace('##', '\n##')

def main():
    path = " " # insert path to markdown file here
    f = open(path, 'r')
    contents = f.read()
    new_contents = add_line(contents)
    f.close()

    f = open(path, 'w')
    print()
    f.write(new_contents)
    f.close()

if __name__ == "__main__":
    print("RUNNING add-line-before-heading SCRIPT\n")
    main()
    print("\n\nEND OF add-line-before-heading SCRIPT")
