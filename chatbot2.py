from flask import Flask, request, jsonify
import random
import string

app = Flask(__name__)

responses = {

    #greetings
"hello": ["How are you?", "How can I help you?", "Hello!", "Hey!"],
"going": ["Absolute cinema! How about you?"],
 "good": ["Glad to hear!", "Nice to hear! How can I help you?"],
    "bad": ["Oh, sad to hear.", "Hope you get better soon!", "Want to hear a joke? YOU!"],


#singulars

 "ok": ["Alright.", "Got it.", "Okay then!"],
    "yeah": ["Yeah!", "Cool.", "Sounds good."],
    "yes": ["Great!", "Alright!", "Gotcha."],
    "no": ["Oh, okay.", "Alright then.", "Noted."],
    "lol": ["Haha!", "Glad you're amused!", "😂"],
    "haha": ["Glad to make you laugh!", "😆", "Good one!"],
    "hmm": ["Thinking about something?", "Let me know what’s on your mind.", "🤔"],
    "idk": ["That’s okay! We don’t have to know everything.", "No worries!", "Let’s figure it out together!"],
    "huh": ["Not sure I get you.", "Could you explain?", "I’m listening!"],
    "stop": ["Did I say something wrong?", "Alright, I’ll chill.", "No worries!"],
    "bye": ["Goodbye!", "See you later!", "Bye! Have a great day!"],


#in english

"military": ["Otto completed his conscription with the Guard Jaeger Regiment's readiness unit, 1/23."],
"work experience": ["Otto has various experiences from different fields such as; customer service, retail, logistics, golf course management, entrepreneurship, and front-end programming."],
"work ethic": ["Otto values consistency, problem-solving, and a true passion for learning. He believes in challenging himself and never shying away from complex tasks."],
"teamwork": ["Otto likes to have control over his projects and works hard on his own terms, but is never shy about asking for help when needed. He thrives in teams where everyone is on the same wavelength and can collaborate effectively."],
"motivation": ["Otto stays motivated by continuously setting new goals and striving to become a valuable asset through the development of his skills."],
"passion": ["Otto is deeply passionate about animations and keyframes in CSS, creating smooth transitions and interactive elements that captivate users. His goal is to make a lasting impact on user experiences, evoking unforgettable emotions through engaging technology."],


#about otto
"live": ["Otto lives in Oulu, Finland"],
"girlfriend": ["Otto does not have a girlfriend ;)"],

"born": ["Otto was born on 24.01.2003!"],
"profession": ["Otto's mission statement is in the power of continuous learning and creative problem-solving. His goal is to bridge the gap between technical precision and artistic design—crafting digital experiences that are both functional and visually compelling."],
    "my name": ["I'm Otto's personal chatbot!", "You can call me OdeBot!", "I'm OdeBot"],
"old": ["Otto is 22 years old!", "I don’t age, but Otto is 22 years old"],
        "full name": ["Otto Oliver Mulari"],
"challenges": ["One of Otto's most challenging projects was developing an ATM simulator in C. Since C is a low-level programming language, and this ATM was his first real big coding project, he had to deeply understand memory management, pointer manipulation, and system architecture."],
    
    "height": ["Otto is 189 cm height", "He's 6'2.", "Otto stands at 189 cm"],
    "hobbies": ["Otto enjoys golf, programming, submission wrestling (no-gi), and once in a while the gym!", 
                              "He likes working out, coding, and playing golf!", 
                              "Submission wrestling is his thing!"],
    "music": ["Otto listens to rap, chill, and sometimes 2010s pop bangers!", 
                               "He likes a mix of rap, chill, and throwback pop songs!", 
                               "Mostly rap and chill music, but sometimes 2010s hits."],
    "movie": ["Otto’s favorites are The Godfather 1, Django, and Nightcrawler.", 
                                    "He likes The Godfather, Django, and Nightcrawler.", 
                                    "The Godfather, Django, and Nightcrawler are Otto’s top movies."],
    "tv": ["Otto doesn't watch TV shows."],
    "sports": ["Otto is into golf, submission wrestling, and working out.", 
                                "He enjoys grappling, golf, and the gym."], 
    "pet": ["Otto has a Bengal cat, but it lives with his parents right now.", 
                          "Yes! A Bengal cat, but it’s currently living at his parents' place."],
    "food": ["Otto likes Mexican and Southeast Asian food!", 
                         "Mexican and Southeast Asian dishes are his favorite.", 
                         "He enjoys spicy and flavorful food like Mexican and Southeast Asian cuisine."],
    "travel": ["Otto wants to visit Madagascar and Honolulu.", 
                                  "Madagascar and Honolulu are his dream spots."],
    "languages": ["Otto speaks Swedish, Finnish, and English.", 
                                    "He's fluent in English, advanced in Swedish and Finnish is his native language.", 
                                    "He can switch between Swedish, Finnish, and English."],

"phone": ["Otto's phone number is +358 44 300 1249"],
"income": ["Otto charges around 300€ per website."],
"studies": ["Otto studies computer science for his bachelor's degree and is planning on studying AI-engineering as his master's degree."],
"pretty": ["Yeah..."],
"ask": ["You can ask simple questions related to Otto"],

  "wow": ["wow!"],
        "others": ["No problem!"],
                "omg": ["Did I surprise you?"],


#studies related

        "bench": ["I do not have accurate information, but I guess Otto can bench press around 90kg's."],
        "drive": ["Otto can hit his driver 280-290m on a good day."],
        "alcohol": ["Otto doesn't enjoy drinking alcohol and very rarely does so."],


    "balance": ["Right now Otto balances university, self-learning, and projects through passion-driven adaptability, letting his enthusiasm fuel progress rather than rigid structure and scheduling."],

"goal": ["Otto's ultimate goal is to become a well-rounded software engineer, mastering both logical problem-solving and front-end (UI/UX) design to create complete, scalable applications. In the short term, he aims to refine his current skills and work on collaborative projects. In the long run, he envisions expanding his UI/UX expertise beyond web development to include all platforms: games, applications, and operating systems."],

"kops": ["Otto is a strong believer in lifelong learning and make it a habit to explore emerging technologies outside of university coursework. Over the past months, he has been self-learning more than what university has taught him so far. He follows the industry and coding communities, and will experiment with new technologies in personal projects like CerebraStyles."],
 "resume": ["You can ask Otto via email for his resume :)"],
   "strength": ["Otto's strength is front-end related development."],
   "funf": ["Otto takes his studies into his own hands, learning far more independently than what the university requires."],
   "nice": ["Right!"],
    "joke": ["Why don’t skeletons fight each other? They don’t have the guts! ☠️", "Why does Otto prefer dark mode when working? Because light attracts bugs! 🐛"],


 "g": ["Otto has played golf around 10 years. His hcp fluctuates between 1-3."],
        "cs": ["He chose to study computer science since he loves problem-solving and the creative expression it allows."],

   "job": ["Otto is always exploring new job opportunities and can be reached via email for professional inquiries."],
    
            "c": ["Otto has an intermediate understanding of C programming. While it is not a language he aspires to master, learning C has significantly strengthened his grasp of low-level programming concepts, such as memory management, pointers, and system architecture. This foundational knowledge has enhanced his proficiency in other programming languages and problem-solving approaches."],

    "css": ["Otto uses CSS to create visually appealing and responsive web designs. It is one of his favorite languages, as it allows him to express his artistic side through styling and layout design. He has a strong grasp of foundational concepts, keyframes for animations, and scalable/maintainable styles."],
    "html": ["Otto is proficient in HTML, structuring web pages with semantic elements to improve accessibility and SEO. While HTML isn’t a traditional programming language, he still uses logical problem-solving to work around challenges to create efficient and adaptable web layouts."],
    "py": ["Otto is currently enhancing his Python skills, which he started learning recently, with a focus on automation, scripting, and AI-related development. Python has quickly become one of his favorite languages due to its clean syntax and powerful capabilities, allowing him to build complex programs more efficiently. In fact, this chatbot is one of his Python projects!"],
    "java": ["Otto is currently studying Java as part of his university coursework. While it shares similarities with C, Java's extensive libraries and object-oriented approach make it more engaging for him. He considers himself at an intermediate level but views Java as a stepping stone for mastering JavaScript, Python, or other scripting languages. One of his most recent Java projects is a math calculator."],
   "script": ["Otto is expanding his expertise in JavaScript for more dynamic development, focusing on how it interacts with front-end frameworks. While still relatively new to the language, he has a strong determination to dive deeper once he completes his Java course. Currently, his JavaScript skills are primarily focused on front-end web development, enhancing interactivity and UX."],
"ix": ["Otto is passionate about UI/UX design, aiming to create intuitive, user-friendly, and visually engaging interfaces. His future goal is to design seamless experiences not only for web environments but also for applications and games, ensuring both functionality and aesthetic appeal."],
   
   #default
   "da": ["Let's relax."],
   
    # "default": ["Ask something else :)", "I'm not sure...maybe rephrase that", "For more successful answers, keep your questions short or just simply use the keyword for the best accuracy."]
"default": [
    "I’m not sure about that. Maybe try rewording your question?",
    "Hmm, I don’t have that information.",
    "For more successful answers, keep your questions short or just simply use the keyword for the best accuracy.",
    "Ask something else :)",
    "That one's tricky!"
]

}
keywords = {

  
    "ui": "ix",
    "ux": "ix",
    "ui/ux": "ix",


    "dumb": "da",
        "fuck": "da",
    "asshole": "da",
    "idiot": "da",
        "dumbass": "da",


    "bench": "bench",
    "driver": "drive",
    "alcohol": "alcohol",
    "alcohols": "alcohol",
    "drinking": "alcohol",
    "benchpress": "bench",
        "press": "bench",





"javascript": "script",
"Javascript": "script",
"script": "script",
"scripts": "script",
"js": "script",







"java": "java",
"Java": "java",
"java-code": "java",
"java-language": "java",



    "python": "py",
        "phyton": "py",
            "Python": "py",
            "python-code": "py",
                        "python-language": "py",



    "css": "css",
        "CSS": "css",
            "css-code": "css",
            "css-language": "css",

"html": "html",
"html-code": "html",
"html-web": "html",
"HTML": "html",




    "atm": "c",









    "played golf": "g",
        "golf": "g",
"computer science": "cs",
"comp sci": "cs",

"job": "job",
"work": "job",
"hiring": "job",

"hire": "job",
"to work": "job",
"available": "job",





    "salary": "income",
"income": "income",
"budgeting": "income",
"investments": "income",
"stocks": "income",
"crypto": "income",
"savings": "income",
"retirement": "income",
"side hustle": "income",

    "education": "studies",
"learning": "studies",
"motivation": "studies",
"productivity": "studies",

    "dating": "girlfriend",
"boyfriend": "girlfriend",
"relationship": "girlfriend",
"romance": "girlfriend",
"flirting": "girlfriend",
"marriage": "girlfriend",

"vacation": "travel",
"beach": "travel",
"mountains": "travel",
"adventure": "travel",
"backpacking": "travel",
"tourist": "travel",

    "exercise": "sports",
"gym": "sports",
"workout": "sports",
"football": "sports",
"basketball": "sports",
"tennis": "sports",
"running": "sports",
"marathon": "sports",
"soccer": "sports",
"cricket": "sports",
"baseball": "sports",
"athletics": "sports",
"fitness": "sports",
"yoga": "sports",

"military":"military",
"army":"military",
"military-service":"military",
"conscript":"military",
"conscription":"military",




"work-experience":"work experience",
"experience":"work experience",
"worked":"work experience",


"ethic":"work ethic",
"teamwork":"teamwork",
"team":"teamwork",
"teams":"teamwork",
"collaboration":"teamwork",


"motivated":"motivation",
"motivation":"motivation",
"drive":"motivation",


"passion":"passion",
"interested":"passion",
"passionate":"passion",
"interest":"passion",







"cuisine": "food",
"fastfood": "food",
"snacks": "food",
"diet": "food",
"eating": "food",
"vegetarian": "food",
"vegan": "food",
"food": "food",
"cooking": "food",
"restaurant": "food",

    "song": "music",
"band": "music",
"concert": "music",
"playlist": "music",
"music": "music",
"album": "music",
"rap": "music",
"rock": "music",
"pop": "music",
"metal": "music",
"hip-hop": "music",
"classical": "music",
"jazz": "music",
    
    "pastime": "hobbies",
"gaming": "hobbies",
"games": "hobbies",
"chess": "hobbies",
"reading": "hobbies",
"photography": "hobbies",
"painting": "hobbies",


"news": "kops",
"trends": "kops",
"challengesnology": "kops",
"innovation": "kops",
"cutting edge": "kops",
"ai": "kops",
"robotics": "kops",



    "whoa": "wow",
"seriously": "wow",
"unbelievable": "wow",
"holy": "wow",
"blown": "wow",
"shocking": "wow",

    "lmao": "lol",
"rofl": "lol",
"haha funny": "lol",
"heh": "lol",
"hehehe": "lol",
"hilarious": "lol",

    "ofcourse": "yes",
"definitely": "yes",
"absolutely": "yes",
"sure": "yes",
"bet": "yes",
"agree": "yes",
"no way": "no",
"not really": "no",
"nah": "no",
"disagree": "no",
"never": "no",

    "disappointed": "bad",
"not great": "bad",
"sucks": "bad",
"hate this": "bad",
"ugh": "bad",
"awful": "bad",
"annoyed": "bad",
"shame": "bad",
"frustrating": "bad",

    "awesome": "good",
"amazing": "good",
"fantastic": "good",
"brilliant": "good",
"wonderful": "good",
"superb": "good",
"love it": "good",
"excellent": "good",
"cool beans": "good",
"thumbs up": "good",

"feel": "bad",
"sad": "bad",
"tired": "bad",
"happy": "good",
"excited": "good",
"bored": "bad",
"stressed": "bad",

"see ya": "bye",
"catch you later": "bye",
"farewell": "bye",
"peace out": "bye",
"adios": "bye",
"later alligator": "bye",
"bye-bye": "bye",
"gotta go": "bye",

"morning": "hello",
"afternoon": "hello",
"evening": "hello",
"howdy": "hello",
"sup": "hello",
"greetings": "hello",
"long time no see": "hello",


 "strongest": "strength",
    "best at": "strength",

"resume": "resume",
"cv": "resume",
"nice": "nice",
"cool": "nice",
"joke": "joke",
"jokes": "joke",


"fun fact": "funf",
"fact": "funf",
"funfact": "funf",








          "tall": "height",
                "height": "height",



      "hello": "hello",
    "hi": "hello",
    "hey": "hello",
    "whats up": "hello",
    "going": "going",

    "doing": "are you",

            "goal": "goal",
            "goals": "goal",
                        "aim": "goal",
            "aiming": "goal",
            "future": "goal",
            "aim": "goal",

    "food": "food",
    "eat": "food",
        "foods": "food",


    "sport": "sports",
        "sports": "sports",


        "thanks": "others",
        "omg": "omg",



    "profession": "profession",
    "philosophy": "profession",
        "problems": "profession",
                "attack": "profession",
                "attacks": "profession",

            "challenges": "challenges",
                "learn": "profession",
            "challenge": "challenges",
            "intricate": "challenges",
            "hard": "challenges",

            "technology": "kops",
                        "trends": "kops",
         "updated": "kops",

    "wow": "wow",


        "girlfriend": "girlfriend",
        "girlfriend": "girlfriend",



    "balance": "balance",
    "balancing": "balance",
        "plan": "balance",
        "planning": "balance",
        "scheduling": "balance",
        "schedule": "balance",

            "old": "old",
                "age": "old",

                "born": "born",

    "bye": "bye",
    "goodbye": "bye",
    "see you": "bye",
    "later": "bye",
    "leave": "bye",


    "good": "good",
    "great": "good",
    "fine": "good",
    "bad": "bad2",
    "not so good": "bad",
    "terrible": "bad",
    "awful": "bad",
    "sad": "bad",
    "depressed": "bad",

     "lets speak in english": "english",
    "let's speak english": "english",
    "english": "english",
    "in english": "english",

    "name": "Otto's name",
    "name": "Otto's name",
"ok": "ok",
    "yeah": "yeah",
        "yes": "yes",
    "no": "no",
    "lol": "lol",
    "haha": "haha",
    "idk": "idk",
    "stop": "stop",
    "bye": "bye",


"hobby": "hobbies",
    "hobbies": "hobbies",
    "activity": "hobbies",
    "interest": "hobbies",

    "music": "music",
    "song": "music",
    "songs": "music",
    "playlist": "music",


    "movie": "movie",
    "movies": "movie",
    "film": "movie",
    "films": "movie",
    "cinema": "movie",

    "pet": "pet",
    "pets": "pet",
    "animal": "pet",
    "cat": "pet",
    "bengal": "pet",
    "animals": "pet",

    "hmm": "hmm",
        "huh": "huh",



    "language": "languages",
    "languages": "languages",
    "speak": "languages",
    "talk": "languages",
    "fluency": "languages",

    "travel": "travel",
    "trip": "travel",
    "vacation": "travel",
    "destination": "travel",
    "holiday": "travel",
    "journey": "travel",


 "live": "live",
        "lives": "live",
"ask": "ask",
"questions": "ask",
"to ask": "ask",
"phone": "phone",
        "mobile": "phone",
    "number": "phone",


    "earn": "income",
        "earns": "income",

    "studies": "studies",
        "study": "studies",
                "pretty": "pretty"

}





ignored_words = {
    "what", "how", "why", "who", "when", "where", "which", "whose",
    "is", "are", "was", "were", "can", "could", "would", "should", "will", "shall", "do", "does", 
    "did", "have", "has", "had", "am", "being",
    "to", "of", "in", "on", "at", "for", "with", "about", "from", "by", "as", "if", "than", "then", 
    "and", "but", "or", "nor", "yet", "so",
    "like", "so", "well", "uh", "um", "okay", "basically", "literally", "actually", "really",
    "otto", "chatbot", "bot", "odebot"
}



def clean_input(user_input):
    ignored_words = {
        "what", "how", "why", "who", "when", "where", "which", "whose",
        "is", "are", "was", "were", "can", "could", "would", "should", "will", "shall", "do", "does",
        "did", "have", "has", "had", "am", "being",
        "to", "of", "in", "on", "at", "for", "with", "about", "from", "by", "as", "if", "than", "then",
        "and", "but", "or", "nor", "yet", "so",
        "like", "so", "well", "uh", "um", "okay", "basically", "literally", "actually", "really",
        "otto", "chatbot", "bot", "odebot"
    }

    user_input = user_input.lower().translate(str.maketrans('', '', string.punctuation))
    
    words = user_input.split()
    
    filtered_words = [word for word in words if word not in ignored_words]
    
    return " ".join(filtered_words)

def get_all_matches(cleaned_input, keywords):
    """Finds all exact keyword matches in the user's input."""
    words = set(cleaned_input.split())  
    matched_categories = [keywords[key] for key in keywords if key in words]  
    return matched_categories

def chatbot2():
    """Main chatbot function handling user input, keyword detection, and response generation."""
    print("Hello! I'm Otto's personal Chatbot, programmed in Python. I can manage a simple Q&A about him!")
    print("To achieve more successful answers, keep your questions short or just simply use the keyword for the best accuracy.")
    
    while True:
        user_input = input("You: ").strip()
        if not user_input:
            continue  
        
        if user_input.lower() == "pause":
            print("OdeBot:", random.choice(["Goodbye!", "See you later!", "Bye! Have a great day!"]))
            break

        cleaned_input = clean_input(user_input)
        matched_categories = get_all_matches(cleaned_input, keywords)

        if not matched_categories:
            response = responses["default"]
            print("OdeBot:", random.choice(response))

        else:
            combined_response = " ".join([random.choice(responses.get(category, responses["default"])) for category in matched_categories])
            print("OdeBot:", combined_response)

@app.route('/')
def home():
    return app.send_static_file('index.html')


@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get('user_input', '').strip()
    if not user_input:
        return jsonify({'response': 'Please provide a valid input.'})

    cleaned_input = clean_input(user_input)
    matched_categories = get_all_matches(cleaned_input, keywords)

    if not matched_categories:
        response = "I'm not sure about that, could you ask something else?"
    else:
        combined_response = " ".join([random.choice(responses.get(category, "No response")) for category in matched_categories])
        response = combined_response

    return jsonify({'response': response})


# Run 
if __name__ == '__main__':
    app.run(debug=True)






