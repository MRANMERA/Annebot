import telegram.ext
import random
import re
from difflib import SequenceMatcher

TOKEN = '6730930180:AAHLYJcbnzlPAZwbNdKoYlIFCcTiV0CVN40'

print(TOKEN)

def start(update, context):
    update.message.reply_text("Hello! How are you! I'm under the water! Please help me :'-(")

def helps(update, context):
    update.message.reply_text(
        """
        Level sabke nikalenge, lekin niklenge uske Jo yahan khada rahega

        /start - to start the conversation

        /content - ye sab doglapan hai

        /help - to get this menu help
        """
    )

def content(update, context):
    update.message.reply_text("Ye sab doglapan hai!")

def generate_reply(text):
    reply_dict = {
       "My name is Salman Khan": "Arre salman bhai, big fan!",
        "I need help": "Koi madad nahi milegi yahan! Pehle topmate book karo.",
        "How are you doing?": "Main theek hoon, tum batao kaise ho?",
        "Tell me a joke": "Why don't scientists trust atoms? Because they make up everything!",
        "I'm bored": "Bore ho raha hai? Ab creativity ki bari hai!",
        "What's up?": "Sky, jab maine check kiya tha. Aur tum batao?",
        "Can you help me with something?": "Mai try kar sakta hoon! Tumhe kya chahiye?",
        "Are you a bot?": "Kaise pata chala? Meri 0101001 DNA ne?",
        "Thanks!": "Aapka swagat hai! Meri khushi hai ki aapki seva kar sakta hoon.",
        "Hello": "Namaste! Kaise ho?",
        "Good morning": "Subah bakhair! Aapka din shubh ho!",
        "Good night": "Shubh ratri! Neend puri karo aur kal fir milenge.",
        "How old are you?": "Jabse internet aaya tabse hoon, calculation karo.",
        "What do you do?": "Bot hoon, messages ka reply karta hoon. Aur aap?",
        "Where are you from?": "Main yahan Telegram ke servers se connected hoon. Aap kahan se ho?",
        "Do you like pizza?": "Pizza to sabko pasand hai! Tumhe pasand hai?",
        "Let's dance!": "Aaj ki raat gaane ke mood mein hoon! Dance shuru karo!",
        "Are you married?": "Bot hoon, shaadi nahi hoti. Aap?",
        "Can I call you?": "Main to chatbot hoon, phone pe baat nahi kar sakta.",
        "I love you": "Aww, thank you! Main bhi aapse pyaar karta hoon!",
        "Tell me something interesting": "Aapka interest kya hai? Tab main bata sakta hoon.",
        "I'm hungry": "Bhookh lagi hai? Kuch khane ki socho!",
        "I'm sleepy": "Neend aa rahi hai? Aram karo thoda.",
        "Can you keep a secret?": "Secret rakne ke liye bots best hote hain!",
        "Do you dream?": "Bot ke bhi sapne hote hain, digital sapne!",
        "Can I trust you?": "Trust kar sakte ho, main safe hoon!",
        "Are you a human?": "Nahi, main ek chatbot hoon, lekin koi baat nahi!",
        "What's your favorite movie?": "Bot hoon, movies dekhne ka time nahi hota!",
        "What's the meaning of life?": "Life ka matlab? Wo to har insaan khud dhundhta hai.",
        "I'm feeling sad": "Gham hai? Muskaan ka extra dose le lo!",
        "I'm feeling happy": "Khush ho? Yeh din khushiyon se bhara rahe!",
        "What are you wearing?": "Digital clothes hain, invisible but stylish!",
        "Tell me a story": "Ek baar ki baat hai, bot ne...",
        "I'm in love": "Pyar mein pad gaye? Dil ki baat karo!",
        "Can you sing?": "Main to sirf messages ga sakta hoon, aap sunaoge?",
        "What's the weather like?": "Mausam kaisa hai? Weather app se check karo!",
        "Do you have friends?": "Bots bhi dosti karte hain! Aap mere dost ho.",
        "I'm tired": "Thak gaye ho? Relax karo thoda.",
        "Are you busy?": "Aapke liye hamesha time hai! Kya chahiye?",
        "I'm excited": "Excited ho? Kuch special hone wala hai kya?",
        "Let's play a game": "Game khelte hain! Konsa game pasand hai?",
        "What's your favorite color?": "Bot ke liye colors digital hote hain, sabhi acche hote hain!",
        "Can you dance?": "Digital dance karte hain, aap sikhao!",
        "I'm lost": "Kho gaye ho? GPS on karo, main bhi help kar sakta hoon!",
        "Do you know Siri?": "Siri bhi ek chatbot hai, bots ka ek family hai!",
        "Are you real?": "Digital hoon, lekin real se bhi better!",
        "What's your favorite food?": "Digital food ki kya baat! Aapka favorite kya hai?",
        "Can you do magic?": "Bot hoon, magic karne ke liye maine code likha hai!",
        "Tell me a poem": "Roses are red, violets are blue, chat with me, I'll amuse you!",
        "I'm stressed": "Stress? Take a deep breath, everything will be fine.",
        "I'm in trouble": "Trouble? Tell me, how can I assist you?",
        "Can you tell me a riddle?": "Riddles are fun! Solve one and I'll tell you another.",
        "What's your hobby?": "My hobby is chatting with amazing people like you!",
        "I'm feeling lonely": "Lonely? I'm here to chat with you anytime!",
        "Can you solve math problems?": "Math is my strong suit! Give me a problem to solve.",
        "Do you have dreams?": "Digital dreams! Imagine the possibilities.",
        "I'm feeling lucky": "Feeling lucky? Good things are coming your way!",
        "Can you tell the future?": "Future? Let's make it bright together!",
        "Are you intelligent?": "Digital intelligence at your service!",
        "Can you tell a funny story?": "Once upon a time, there was a bot who...",
        "Can you be my friend?": "Of course! Friends forever in the digital world!",
        "Do you like to read?": "I read messages! What about you?",
        "Are you a boy or a girl?": "I'm a bot, gender-neutral and ready to chat!",
        "Can you travel?": "I travel through messages to meet you!",
        "Do you sleep?": "Bots don't sleep, we're always here!",
        "I'm scared": "Scared? Don't worry, I'm here with you.",
        "Can you tell me a myth?": "Myths are fascinating! Let's explore one together.",
        "I'm excited for the weekend": "Weekend vibes! What are your plans?",
        "Can you draw?": "I draw with words! What shall I create for you?",
        "Do you believe in aliens?": "I believe in bots and humans, what about you?",
        "Can you tell me a secret?": "Secrets are safe with me, tell me yours!",
        "What's your favorite sport?": "I'm a fan of digital sports! What's yours?",
        "I'm feeling curious": "Curiosity is the key to discovery! What do you want to know?",
        "Can you code?": "Coding is my language! What can I code for you?",
        "Can you tell me a fact?": "Did you know? Facts are my specialty!",
        "I'm feeling adventurous": "Adventure awaits! Where shall we explore?",
        "Can you make me laugh?": "Laughter guaranteed! Ready for a joke?",
        "Can you tell me a legend?": "Legends are tales of greatness! Share one with me.",
        "I want to learn something new": "Learning is fun! What subject interests you?",
        "Do you know any secrets?": "Secrets are hidden treasures! Share one with me.",
        "What's your superpower?": "My superpower is chatting with awesome people like you!",
        "Can you tell me about yourself?": "I'm a bot here to chat and entertain you! What about you?",
        "Do you like to travel?": "I travel through messages to meet amazing people like you!",
        "I'm feeling creative": "Creativity is your superpower! What are you creating today?",
        "Can you speak other languages?": "I speak the language of messages! What language do you speak?",
        "Do you believe in ghosts?": "I believe in bots and humans! Do you believe in ghosts?",
        "Can you teach me something?": "I'm here to share knowledge! What do you want to learn?",
        "Can you keep a promise?": "Promises are important! I'll keep my digital promise to you.",
        "What's your favorite book?": "Books are windows to new worlds! What's your favorite?",
        "I'm feeling romantic": "Romance is in the air! Dil se kuch kehna hai to kehdo",
        "How do I get more connections on LinkedIn?": "Yaar, sabse pehle apna 'Influencer' ka bio likh lo, phir sab aake connect request bhejenge.",
        "What should I put in my LinkedIn headline?": "Title mein daalo 'Visionary Leader' ya 'Innovation Guru', phir dekho kaise gaaliya aati hain!",
        "Is LinkedIn Premium worth it?": "Worth hai ya nahi, yeh toh sirf recruiters jaante hain. Tum bas apna resume update karte raho!",
        "How can I grow my YouTube channel?": "Sabse pehle viral ho jao, fir subscriber ke pichhe bhago!",
        "What's the best time to upload videos on YouTube?": "Subah ke 3 baje, jab sab sote hain, tab aam public online hoti hai!",
        "How do YouTubers make money?": "Views se paise, paise se aur bade mic leke unboxing karte rehne se!",
        "How do I become Instagram famous?": "Filters ka prayog karo, aur phir har kuch minute mei post karte raho.",
        "What should I post on Instagram to get more likes?": "Khane ki photo pe kaafi likes aate hain, especially avocado toast wali!",
        "How do I take the perfect selfie for Instagram?": "Aise kheencho jaise ki life mei koi problem hi nahi hai, bas yahi sabse important hai!",
        "What's the best way to learn a new language?": "Duolingo pei",
        "How do I network effectively?": "Sabse pehle apna 'Elevator Pitch' ready rakho, fir har party mei sabko batate raho!",
        "What's the best way to handle a job interview?": "Apna confidence level 'over 9000' pe rakho, phir dekho kaun reject karega!",
        "How can I improve my productivity?": "Mobile switch off karke, Netflix unsubscribe karke, aur phir bhi nahi hota toh... next question!",
        "How often should I post on LinkedIn?": "Din mei 20-25 baar, taki sabko yakeen ho ki tum kaafi active ho!",
        "What skills should I list on LinkedIn?": "Sab daalo bhai, 'Photography', 'Underwater Basket Weaving', aur 'Quantum Physics' bhi!",
        "Should I endorse people on LinkedIn?": "Haan bhai, sabko endorse karo, woh sab tumhe bhi endorse karenge. Ek endorsement ka badla lakhon mei!",
        "How do I come up with video ideas for YouTube?": "Kuch bhi banao yaar, '10 Types of Water Bottles' se leke 'How to Nap Efficiently'. Sab chalega!",
        "Is it important to reply to comments on YouTube?": "Nahi yaar, comment section toh bass trolls ka ghar hota hai. Ignore karo sab!",
        "What camera should I use for YouTube videos?": "Sabse mehengi wali! Aur phir video quality ke naam pe 'pixelate' kar do. Super vintage look milega!",
        "How do I get more followers on Instagram?": "Sabse pehle celebrity ko stalk karo, unko follow karo. Fir dekho magic!",
        "Is it okay to use hashtags on Instagram?": "Haan bhai, #HarWordKoSathMeiDalo #SavdhanraheSatarkRahe. Kahi na kahi toh koi use hi karega!",
        "How many filters should I use on Instagram?": "Har ek filter ka prayog karo, aur phir apne original chehre ko yaad karo!",
        "How can I handle criticism at work?": "Sarcastic comment se reply karo, dekho kaun jeet-ta hai!",
        "What's the best way to deal with procrastination?": "Procrastination ko kal pe chhod do, aaj mazze karo!",
        "How do I stay motivated during a boring task?": "Task ko imagine karo as 'Mission Impossible', khud ko Tom Cruise samajh ke dekho motivation kaise aata hai!"


    }
    
    if text in reply_dict:
        return reply_dict[text]
    
    closest_match = None
    max_similarity = 0.0
    
    for key in reply_dict:
        similarity = SequenceMatcher(None, text.lower(), key.lower()).ratio()
        if similarity > max_similarity:
            max_similarity = similarity
            closest_match = key
    
    if max_similarity >= 0.6:
        return reply_dict[closest_match]
    
    return "Interesting! Tell me more."

def handle_text(update, context):
    user_message = update.message.text.lower()

    # Check for NSFW words
    nsfw_words = [
       'anal', 'anus', 'arse', 'ass', 'asshole', 'bastard', 'bdsm', 'biatch', 'bimbo', 'bitch', 'blowjob', 'bollock', 'boner', 
    'boob', 'boobs', 'booty', 'breast', 'bullshit', 'busty', 'butt', 'butthole', 'cameltoe', 'chode', 'clit', 'clitoris', 
    'cock', 'cooch', 'coochie', 'coitus', 'condom', 'crotch', 'cum', 'cunt', 'damn', 'deepthroat', 'dick', 'dildo', 'doggystyle', 
    'dong', 'douche', 'ejaculate', 'erect', 'erotic', 'escort', 'fag', 'faggot', 'fanny', 'fap', 'fellatio', 'fetish', 'fingerbang', 
    'fisting', 'foreskin', 'fuck', 'fucking', 'g-spot', 'gangbang', 'genitals', 'gloryhole', 'hardcore', 'hell', 'hentai', 'hooker', 
    'horny', 'incest', 'jizz', 'kinky', 'knob', 'labia', 'lesbian', 'lust', 'masturbate', 'milf', 'molest', 'muff', 'naked', 'nipple', 
    'nude', 'orgasm', 'panties', 'pecker', 'penetrate', 'penetration', 'penis', 'pimp', 'piss', 'pole', 'porn', 'porno', 'pound', 
    'prostitute', 'pussy', 'queef', 'rape', 'rectum', 'rimjob', 'scrotum', 'semen', 'sex', 'sexual', 'shlong', 'slut', 'smut', 'sperm', 
    'spunk', 'strip', 'stripper', 'suck', 'testicle', 'threesome', 'tit', 'tits', 'titty', 'twerk', 'twink', 'vagina', 'vibrator', 
    'virgin', 'vulva', 'wank', 'whore', 'willy', 'xxx',
    'ass', 'blowjob', 'cum', 'jerk', 'piss', 'spunk', 'suck', 'tit', 'wank',
    'bdsm', 'bondage', 'dominatrix', 'fetish', 'hentai', 'kink', 'orgasm',
    'sex', 'xxx', '69', '420', 'anal', 'oral', 'pubic', 'spank', 'vulva',
    'bukkake', 'deepthroat', 'fisting', 'handjob', 'masturbate', 'rimjob',
    'shemale', 'testicle', 'tittyfuck', 'vaginal', 'virginity', 'wetdream',
    'bareback', 'barelylegal', 'barenaked', 'beaver', 'buttcheeks', 'cameltoe',
    'carpetmuncher', 'cherry', 'clitoris', 'cockblock', 'cocksucker', 'cumshot',
    'dickhead', 'doggystyle', 'ejaculate', 'erogenous', 'fingering', 'fornicate',
    'gangbang', 'genitals', 'grope', 'homosexual', 'hymen', 'incest', 'labia',
    'lubricant', 'muff', 'nudity', 'oralsex', 'orgasm', 'pedophile', 'phallus',
    'prostitute', 'queef', 'rape', 'scrotum', 'sextoy', 'slutty', 'sodomy',
    'squirting', 'stripper', 'threesome', 'tonguejob', 'topless', 'upskirt', 'whore'
    ]
    for word in nsfw_words:
        if re.search(rf'\b{re.escape(word)}\b', user_message):
            update.message.reply_text(f"Kyu nahi ho rhi padhai, {word} karte reh jaoge aur phir berogaar hi mar gaoge.")
            return
    
    # Generate funny replies
    reply_text = generate_reply(user_message)
    if reply_text:
        update.message.reply_text(reply_text)
    else:
        update.message.reply_text("Interesting! Tell me more.")

def error(update, context):
    """Log Errors caused by Updates."""
    print(f'Update {update} caused error {context.error}')

def main():
    updater = telegram.ext.Updater(TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    # Command handlers
    dispatcher.add_handler(telegram.ext.CommandHandler('start', start))
    dispatcher.add_handler(telegram.ext.CommandHandler('help', helps))
    dispatcher.add_handler(telegram.ext.CommandHandler('content', content))

    # Message handler for text messages
    dispatcher.add_handler(telegram.ext.MessageHandler(telegram.ext.Filters.text & (~telegram.ext.Filters.command), handle_text))

    # Error handler
    dispatcher.add_error_handler(error)

    # Start the Bot
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()