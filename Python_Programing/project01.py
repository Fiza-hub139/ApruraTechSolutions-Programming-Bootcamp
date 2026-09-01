import random 
import pyjokes


def greetUser(user_name):
    print(f"\n================== Hey {user_name}! 👋=========================\n")
    print("             Welcome to mood changer mini Bot!       ")
    print("This bot is designed to lift your spirits and brighten your day with a touch of humor or motivation.\nYou can choose to receive either a funny joke or a motivational quote. Let's get started!\n")
    print("\n====================================================================")       


def moodCheck():
    mood = input("How are you feeling today? (happy/sad/neutral): ").lower()
    if mood == "happy":
        print("That's great to hear! Let's keep the good vibes going!")
    elif mood == "sad":
        print("I'm sorry to hear that. Here's a joke to cheer you up!")
        print(pyjokes.get_joke())
    elif mood == "neutral":
        print("Thanks for sharing! Let's see if we can make your day better.")
    else:
        print("I didn't understand that. Please enter 'happy', 'sad', or 'neutral'.")
#     def quotesGen(req_quote):
#         funny_jokes = [
#     "Subah jaldi uthne ke do hi faide hain: pehla pata nahi aur doosra mil nahi raha! 😴⏰",
#     "Mera dimaag bhi WiFi jaisa hai, jaise hi padhne baitho disconnect ho jata hai! 📡🚫",
#     "Log kehte hain waqt ke saath sab theek ho jata hai, par mera phone ka charger nahi hua! 🔌🔋",
#     "Duniya ka sab se mushkil kaam subah kambal se bahar nikalna hai! 🛌🥶",
#     "Meri kismat itni kharab hai ke agar main lottery khareedun toh inaam mein bhi kaam mil jaye! 🎟️💸",
#     "Padhai aur mere darmeyan ek gehra talluq hai, main padhta nahi aur wo mujhe aati nahi! 📚🤷‍♂️",
#     "Paisa haath ki meil hai, par lagta hai mere haath bohot zyada saaf hain! 🧼💵",
#     "Ghar walon ke mutabiq duniya ki har bimari ki wajah sirf mera mobile phone hai! 📱🤦‍♂️",
#     "Soya hua banda uthna aasan hai, lekin sone ki acting karne wale ko uthana namumkin! 😴🎭",
#     "Mera dimaag 24 ghante kaam karta hai, bas padhai aur kaam ke waqt rest pe chala jata hai! 🧠💤",
#     "Zindagi mein itna stress hai ke ab toh ghusse ko bhi ghussa aane laga hai! 😡💥",
#     "Aalasi itna hoon ke agar raste mein paisa gir jaye toh uthane ke liye doosre ka intezar karta hoon! 🦥💵",
#     "Mera future itna bright hai ke dekhne ke liye kaala chashma pehanna padta hai! 😎✨",
#     "Log pyaar mein pagal hote hain, hum toh garmi mein hi pagal ho jate hain! 🌞🥵",
#     "Peechhe baith kar baatein karne walon ko bata doon ke main aage nikal chuka hoon! 🚗💨",
#     "Sone se pehle mobile chalana aisi bimari hai jis ka ilaaj sirf low battery hai! 🔋⚠️",
#     "Zindagi ek race hai aur main us mein paidal chal raha hoon! 🏃‍♂️🐢",
#     "Dost wo hai jo aap ki izzat ki aisi taisi karne ka koi mauka na chhode! 🤪🤝",
#     "Khana khane ke baad bartan dhona duniya ka sab se bada dhoka hai! 🍽️🧼",
#     "Weekend shuru hote hi khatam ho jana bhi ek qudrati aafat hai! 🗓️⚡"
#     ]
#         motivational_quotes = [
#     "Khawab wo nahi jo aap sote hue dekhein, khawab wo hain jo aap ko sone na dein! 🌟💪",
#     "Manzil unhi ko milti hai jin ke sapno mein jaan hoti hai, pankh se kuch nahi hota hausle se udaan hoti hai! 🦅✨",
#     "Jab tak aap haar nahi maante, tab tak aap ko koi haraye nahi sakta! 🛡️🔥",
#     "Mehnat itni khamoshi se karo ke aap ki kamyabi shor macha de! 🤫🏆",
#     "Apne raaste khud banao, kyun ke bheed aap ko daad toh de sakti hai par pehchan nahi! 🛤️👤",
#     "Musibat har insan par aati hai, koi toot jata hai toh koi record tod deta hai! 💥🥇",
#     "Waqt aur kismat par kabhi ghamand mat karo, kyun ke subah unki bhi hoti hai jin ke din kharab hote hain! 🌅⏳",
#     "Girna koi buri baat nahi hai, gir kar na uthna sab se badi naakaami hai! 🔄👟",
#     "Aap ki aaj ki mehnat aap ke kal ka future tay karti hai! 📚🚀",
#     "Mushkilein hamesha behtareen logon ke hisse mein aati hain, kyun ke wo use behtareen tareeqe se nibhane ki salahiyat rakhte hain! 👑🎯",
#     "Log kya kahenge ye sochna chhod do, kyun ke log tab bhi bolte hain jab aap kuch nahi karte! 🗣️🚫",
#     "Zindagi mein kabhi bhi umeed mat chhodo, kyun ke kal ka din aaj se behtar ho sakta hai! 🌄☀️",
#     "Kamyabi ka koi shortcut nahi hota, is ke liye mehnat ki seedhiyan hi chadhni padti hain! 🪜🔝",
#     "Jo seekhta hai wo aage barhta hai, seekhna band toh jeetna band! 📖💡",
#     "Apne aap par bharosa rakho, aap us se kahin zyada taqatwar hain jitna aap sochte hain! 🦁⚡",
#     "Chhoti chhoti koshishein hi ek din badi kamyabi ka baais banti hain! 💧🌊",
#     "Khudi ko kar buland itna ke har taqdeer se pehle, khuda bande se khud poooche bata teri meza kya hai! 🏔️✨",
#     "Rukna nahi hai, thakna nahi hai, bas apne maqsad ki taraf aage barhte rehna hai! 🏃‍♂️🏁",
#     "Zindagi milna naseeb ki baat hai, maut aana waqt ki baat hai, par maut ke baad bhi dilon mein zinda rehna achhe aamaal ki baat hai! ❤️🌱",
#     "Darr ke aage hi hamesha jeet hoti hai, bas pehla qadam uthane ki der hai! 🧗‍♂️🎖️"
# ]
#         if req_quote == "funny":
#             print("Bot: " + random.choice(funny_jokes))
#         elif req_quote == "motivational":
#             print("Bot: " + random.choice(motivational_quotes))
#         else:
#             print("Invalid input. Please choose 'funny' or 'motivational'.")
#     quotesGen(input_choice)

name = input("Please enter your name: ")
greetUser(name)

for i in range(3):
    print("You can choose to receive either a funny joke or a motivational quote.")
    input_choice = input("Type 'funny' for a joke or 'motivational' for a quote: ").lower()
    # moodCheck()


