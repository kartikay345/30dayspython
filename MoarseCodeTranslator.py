# so today we are going to build moarse code translator 
# we will start by making a dictionary of it 
Moarse_dictionary= {
    'a':".-",
    'b':"-...",
    'c':"-.-.",
    'd':"-..",
    'e':".",
    'f':"..-.",
    'g':"--.",
    'h':"....",
    'i':"..",
    'j':".---",
    'k':"-.-",
    'l':".-..",
    'm':"--",
    'n':"-.",
    'o':"---",
    'p':".--.",
    'q':"--.-",
    'r':".-.",
    's':"...",
    't':"-",
    'u':"..-",
    'v':"...-",
    'w':".--",
    'x':"-..-",
    'y':"-.--",
    'z':"--..",
    '1':".----",
    '2':"..---",
    '3':"...--",
    '4':"....-",
    '5':".....",
    '6':"-....",
    '7':"--...",
    '8':"---..",
    '9':"----.",
    '0':"-----",
    }
# now we are builting reverse dictory as well Since we already have the dictionary we can do this 
reversed_morse={value :key for key , value in Moarse_dictionary.items()}
words =input("which words you would like to traslate").lower().strip()
morse_code =[]# to store the translation in it 
for ch in words:
    if ch==' ':
        morse_code.append('/')
    elif ch in Moarse_dictionary:
        morse_code.append(Moarse_dictionary[ch])
    else:
        # for the unknow character
        morse_code.append('?')        

print('here is your translation '," ".join(morse_code))
morse_input = input("Enter Morse code (use spaces between letters and / between words): ").strip()

word_blocks = morse_input.split("/")
decoded_words = []

for word_block in word_blocks:
    letters = word_block.strip().split()  # split by any whitespace
    decoded_letters = []

    for code in letters:
        decoded_letters.append(reversed_morse.get(code, "?"))

    decoded_words.append("".join(decoded_letters))

print("Decoded text:", " ".join(decoded_words))