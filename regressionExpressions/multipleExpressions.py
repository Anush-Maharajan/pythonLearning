import re

def main():
    print("="*8 + " Multiple Regressions " + "="*8 + "\n")
    
    values = []
    syntaxes = [r'(\w+) letter is (\w)', r'word (?:has|contains) (\d+) letters']
    statement = input().strip().lower()
    for syntax in syntaxes:
        value = re.findall(syntax, statement)
        values.extend(value)
    print(values)

if __name__ == "__main__":
    main()