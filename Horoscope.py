# # dictionary  for the horoscope 
# Horoscope_dictionary={
#                     'Aries':'your energy seems high today .good day to start a new project',
#                     'Taurus':'Stay grounded.patience will bring you the result you want',
#                     'Gemini':'A busy day ahead! Communication is your strongest tool today ',
#                     'Cancer':'Trust your intuition.Its a good time to focus on home and family',
#                     'Virgo':'Attention to detail will help you solve a tricky problem today.',
#                     'Libra':'Balance is key.Take some time to find peace in your surrounding ',
#                     "Scorpio":"Focus on your goals with intensity. Great things are coming.",
#                     "Sagitarius":"Adventure is calling! Be open to learning something totally new.",
#                     "Capricorn":"Hard work pays off. Keep pushing toward your long-term dreams",
#                     "Aquarius":"Your original ideas will inspire others. Think outside the box.",
#                     "Pisces":"Your creativity is at its peak. Let your imagination run wild",

# }
# user_sign=input(' hey i hope you are having a great day in your life , can you please tell me you sign ').capitalize().strip()
# # if user_sign in  Horoscope_dictionary:
# #     print(Horoscope_dictionary[user_sign])
# # else:
# #     print("sorry, i don't recognise this sign ")

# # the same logic you we can is with .get() it works as the safety net if the program crashes it gives the default message as well 
# fortune=Horoscope_dictionary.get(user_sign,"That sign wasn't found. Check your spelling!")
# print(fortune)

##-----------now instead of this we are going to read it straight from the files
# --- STEP 1: INITIALIZATION ---
# We start with an empty dictionary. We will fill this from the file.
horoscope_data = {}

# --- STEP 2: FILE LOADING (The "Database" Phase) ---
# We use try/except in case the file is missing or named incorrectly.
try:
    with open("horoscopes.txt", "r") as file:
        for line in file:
            # We check if the colon exists to avoid errors on empty lines
            if ":" in line:
                # split(":", 1) ensures we only split at the FIRST colon
                sign, message = line.strip().split(":", 1)
                horoscope_data[sign.strip()] = message.strip()
    print("✨ Database loaded successfully! ✨")

except FileNotFoundError:
    print("❌ Error: 'horoscopes.txt' not found. Please create the file first!")
    # We create some dummy data so the program doesn't crash if the file is missing
    horoscope_data = {"Aries": "You forgot to create the text file!"}

# --- STEP 3: THE MAIN LOOP (The "App" Phase) ---
while True:
    print("\n" + "="*30)
    user_input = input("Enter a Zodiac Sign (or type 'exit' to quit): ").strip().capitalize()

    # Exit condition
    if user_input == "Exit":
        print("May the stars be with you. Goodbye!")
        break

    
    # This provides a 'default' message if the sign isn't in our dictionary
    prediction = horoscope_data.get(user_input, "Sign not found. Please check your spelling.")

    print(f"\n[{user_input.upper()}]")
    print(prediction)