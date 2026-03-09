# dictionary  for the horoscope 
Horoscope_dictionary={
                    'Aries':'your energy seems high today .good day to start a new project',
                    'Taurus':'Stay grounded.patience will bring you the result you want',
                    'Gemini':'A busy day ahead! Communication is your strongest tool today ',
                    'Cancer':'Trust your intuition.Its a good time to focus on home and family',
                    'Virgo':'Attention to detail will help you solve a tricky problem today.',
                    'Libra':'Balance is key.Take some time to find peace in your surrounding ',
                    "Scorpio":"Focus on your goals with intensity. Great things are coming.",
                    "Sagitarius":"Adventure is calling! Be open to learning something totally new.",
                    "Capricorn":"Hard work pays off. Keep pushing toward your long-term dreams",
                    "Aquarius":"Your original ideas will inspire others. Think outside the box.",
                    "Pisces":"Your creativity is at its peak. Let your imagination run wild",

}
user_sign=input(' hey i hope you are having a great day in your life , can you please tell me you sign ').capitalize().strip()
# if user_sign in  Horoscope_dictionary:
#     print(Horoscope_dictionary[user_sign])
# else:
#     print("sorry, i don't recognise this sign ")

# the same logic you we can is with .get() it works as the safety net if the program crashes it gives the default message as well 
fortune=Horoscope_dictionary.get(user_sign,"That sign wasn't found. Check your spelling!")
print(fortune)

