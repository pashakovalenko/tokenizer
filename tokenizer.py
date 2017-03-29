import re
def tokenize(text):
    # List of abbreviations that cannot occure at the end of sentence
    # Replace periods in them by '#'
    abbr = ['Mr', 'Ms', 'Mrs', 'Dr', 'Prof', 'Gen', 'Jn', 'Sn', 'Hon', 'St', 
            'Mt', 'i.e', 'e.g', 'a.k.a']
    text = re.sub(r'(' + '|'.join(abbr) +')\.', r'\1#', text)
    # Replace periods by '#' in initials
    text = re.sub(r'(?<!\w)([A-Z]\. ?)*[A-Z]\. [A-Z]', 
                  lambda x: x.group(0).replace('.', '#'), text)
    # Split into sentences. Sentence should start with capital or number 
    # and end with '.', '?', '!' or '...'
    # May also have brackets or quotes at the beginning and at the end
    text = re.sub(r'(([.?!]|\.\.\.)["\')]?) (?=["\'(]?[A-Z0-9])', 
                  r' \1\n', text)
    # Special case for the last sentence before the end of line
    text = re.sub(r'(([.?!]|\.\.\.)["\')]?)\Z', r' \1', text)
    # Add spaces before and after punctuation marks
    text = re.sub(r'([?!",]|\.\.\.)', r' \1 ', text)
    # Special case for ':', ';': should be followed by a space
    text = re.sub(r'([:;])(?![^ ])', r' \1 ', text)
    # Special case for '(', ')': sholud be surrounded by letters, numbers, 
    # spaces, '".,?!
    allowed = 'a-zA-Z0-9 \'".,?!#\n'
    text = re.sub(r'(?<![^' + allowed + r'])([()])(?![^' + allowed + r'])', 
                  r' \1 ', text)
    # Special case for ': it shouldn't have letters at least at one side
    text = re.sub(r'((?<!\w)\'|\'(?!\w))', r" ' ", text)
    # Delete extra spaces
    text = re.sub(r' +', r' ', text)
    # Replace '#' back with spaces
    text = re.sub('#', '.', text)
    # Strip the strings to remove spaces at the beginning and at the end
    return list(map(lambda s: s.strip(), text.split('\n')))

if __name__ == '__main__':
    text = ''.join(open('input.txt', 'r').readlines()).replace('\n', ' ')
    result = tokenize(text)
    open('output.txt', 'w').write('\n'.join(result))