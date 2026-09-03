import random 
import pyjokes 

# Greet function
def greet(user_name):
    print(f"----------Hello {user_name}! Welcome to GigglyBot --------") 
    print("This bot will help you to change your current mood either you are feeling happy or sad")
    print("____________________________________________________________")

# Mood Evaluator 
def moodchecker():
    print("-------- Happy or Sad---------")
    print("Type 1 for happy and 2 for sad")
    choice = int(input("\nPlease enter your choice according you mood:"))
    if choice == 1:
        print("Bot:  I'm glad to hear that. Have a good day")
    elif choice == 2:
        print("Bot:  I'm unpleased to hear that.I've a joke to make you happy")
        print(pyjokes.get_joke())
    else:
        print("Bot: I don't understand what do you feeling now.")
    print("____________________________________________________________")

# Function to generate joke or quote
def quotegen(user_req):
    user_req=input("Type funny to get a joke \nType quote to get motivational quote: ")

    def funny_jokes():
        funny_jokes = [
    "Subah jaldi uthne ke do hi faide hain: pehla pata nahi aur doosra mil nahi raha! 😴⏰",
    "Mera dimaag bhi WiFi jaisa hai, jaise hi padhne baitho disconnect ho jata hai! 📡🚫",
    "Log kehte hain waqt ke saath sab theek ho jata hai, par mera phone ka charger nahi hua! 🔌🔋",
    "Duniya ka sab se mushkil kaam subah kambal se bahar nikalna hai! 🛌🥶",
    "Meri kismat itni kharab hai ke agar main lottery khareedun toh inaam mein bhi kaam mil jaye! 🎟️💸",
    "Padhai aur mere darmeyan ek gehra talluq hai, main padhta nahi aur wo mujhe aati nahi! 📚🤷‍♂️",
    "Paisa haath ki meil hai, par lagta hai mere haath bohot zyada saaf hain! 🧼💵",
    "Ghar walon ke mutabiq duniya ki har bimari ki wajah sirf mera mobile phone hai! 📱🤦‍♂️",
    "Soya hua banda uthna aasan hai, lekin sone ki acting karne wale ko uthana namumkin! 😴🎭",
    "Mera dimaag 24 ghante kaam karta hai, bas padhai aur kaam ke waqt rest pe chala jata hai! 🧠💤",
    "Zindagi mein itna stress hai ke ab toh ghusse ko bhi ghussa aane laga hai! 😡💥",
    "Aalasi itna hoon ke agar raste mein paisa gir jaye toh uthane ke liye doosre ka intezar karta hoon! 🦥💵",
    "Mera future itna bright hai ke dekhne ke liye kaala chashma pehanna padta hai! 😎✨",
    "Log pyaar mein pagal hote hain, hum toh garmi mein hi pagal ho jate hain! 🌞🥵",
    "Peechhe baith kar baatein karne walon ko bata doon ke main aage nikal chuka hoon! 🚗💨",
    "Sone se pehle mobile chalana aisi bimari hai jis ka ilaaj sirf low battery hai! 🔋⚠️",
    "Zindagi ek race hai aur main us mein paidal chal raha hoon! 🏃‍♂️🐢",
    "Dost wo hai jo aap ki izzat ki aisi taisi karne ka koi mauka na chhode! 🤪🤝",
    "Khana khane ke baad bartan dhona duniya ka sab se bada dhoka hai! 🍽️🧼",
    "Weekend shuru hote hi khatam ho jana bhi ek qudrati aafat hai! 🗓️⚡"]#
        print("Bot: " + random.choice(funny_jokes))

    # Motivatioanl Quote Set
    def motivational_quotes():
        motivational_quotes = [
    "Khawab wo nahi jo aap sote hue dekhein, khawab wo hain jo aap ko sone na dein! 🌟💪",
    "Manzil unhi ko milti hai jin ke sapno mein jaan hoti hai, pankh se kuch nahi hota hausle se udaan hoti hai! 🦅✨",
    "Jab tak aap haar nahi maante, tab tak aap ko koi haraye nahi sakta! 🛡️🔥",
    "Mehnat itni khamoshi se karo ke aap ki kamyabi shor macha de! 🤫🏆",
    "Apne raaste khud banao, kyun ke bheed aap ko daad toh de sakti hai par pehchan nahi! 🛤️👤",
    "Musibat har insan par aati hai, koi toot jata hai toh koi record tod deta hai! 💥🥇",
    "Waqt aur kismat par kabhi ghamand mat karo, kyun ke subah unki bhi hoti hai jin ke din kharab hote hain! 🌅⏳",
    "Girna koi buri baat nahi hai, gir kar na uthna sab se badi naakaami hai! 🔄👟",
    "Aap ki aaj ki mehnat aap ke kal ka future tay karti hai! 📚🚀",
    "Mushkilein hamesha behtareen logon ke hisse mein aati hain, kyun ke wo use behtareen tareeqe se nibhane ki salahiyat rakhte hain! 👑🎯",
    "Log kya kahenge ye sochna chhod do, kyun ke log tab bhi bolte hain jab aap kuch nahi karte! 🗣️🚫",
    "Zindagi mein kabhi bhi umeed mat chhodo, kyun ke kal ka din aaj se behtar ho sakta hai! 🌄☀️",
    "Kamyabi ka koi shortcut nahi hota, is ke liye mehnat ki seedhiyan hi chadhni padti hain! 🪜🔝",
    "Jo seekhta hai wo aage barhta hai, seekhna band toh jeetna band! 📖💡",
    "Apne aap par bharosa rakho, aap us se kahin zyada taqatwar hain jitna aap sochte hain! 🦁⚡",
    "Chhoti chhoti koshishein hi ek din badi kamyabi ka baais banti hain! 💧🌊",
    "Khudi ko kar buland itna ke har taqdeer se pehle, khuda bande se khud poooche bata teri meza kya hai! 🏔️✨",
    "Rukna nahi hai, thakna nahi hai, bas apne maqsad ki taraf aage barhte rehna hai! 🏃‍♂️🏁",
    "Zindagi milna naseeb ki baat hai, maut aana waqt ki baat hai, par maut ke baad bhi dilon mein zinda rehna achhe aamaal ki baat hai! ❤️🌱",
    "Darr ke aage hi hamesha jeet hoti hai, bas pehla qadam uthane ki der hai! 🧗‍♂️🎖️"
]      
        print("Bot: " + random.choice(motivational_quotes))

    if user_req == "funny":
        funny_jokes()
    elif user_req == "quote":
        motivational_quotes()


    print("__________________________________")

# Goodbye()
def goodbye():
    print("Nice to meet you. \nPlease re run the code to have move conversation with me")
    print("__________________________________")

# main code for bot 
name=input("Please enter your name: ")
print("__________________________________")
greet(name)

for i in range (3):
    print("Bot: What service would you like to have? (moodchecker or quoteGen) ")
    req_ser= input("What service would you like to have")

    if req_ser=="moodchecker":
        moodchecker()
    elif req_ser=="quoteGen":
        quotegen()
    else:
        break

goodbye()
    