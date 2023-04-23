from tkinter import *
from tkinter.ttk import Combobox

class StoryGenerator:
    @staticmethod
    def ep1():
        story = Tk()
        story.title("The Detective")
        story.geometry('1000x1000')

        Label(story, text=f'''\t
        {name}: Hello. I am detective {noun} and you are..,

        {friend}: {teacher}.

        {name}: You are here today on suspicion of second 
        \t  degree robbery.

        {friend}: {excl}!

        {name}: That's right! For {number} eggs were stolen
        \t from {store} and the crime scene has your {potb}
        \t written all over it.

        {friend}: That is {silly}!

        {name}: Where were you on the night of {holiday}?

        {friend}: We were watching....{movie}.

        {name}: Then, why does the security camera show you 
        \t {verb} just {distance} from the crime scene. I am 
        \t through with playing games, Where are you from?

        {friend}: (dramatically says...) {country}!!
        
        {name}: Yeah, just as I suspected. You know one of the best 
        \t parts of being a detective is that I get to lock up 
        \t criminals like you and go home to my children and my pet {animal} 
        \t and say {dialogue}!
        
        {friend}: Okay, I did it, I did the robbery but I only did it to buy 
        \t myself little {potb} implants.
        
        {name}: I knew it all along! And everytime I solve a crime, I 
        \t like to sing my favourite song {rhyme}.''', font=("Arial Bold", 11), justify='left').pack()
        Button(story, text="Close", command=story.destroy).pack(pady=10)

main = Tk()
main.geometry("250x250")
main.title("MaD LiBs Theatre")
main.wm_iconbitmap("Logo.ico")

def inputScreen(topic):
    def redirect():
        global name
        global friend
        global noun
        global teacher
        global distance
        global verb
        global movie
        global potb
        global excl
        global holiday
        global animal
        global store
        global silly
        global number
        global country
        global dialogue
        global rhyme

        name = val_name.get()
        friend= val_friend.get()
        noun= val_noun.get()
        teacher= val_teacher.get()
        distance= val_distance.get()
        excl= val_excl.get()
        movie= val_movie.get()
        potb= val_potb.get()
        holiday= val_holiday.get()
        animal= val_animal.get()
        verb = val_verb.get()
        store= val_store.get()
        silly= val_silly.get()
        number= val_number.get()
        country= val_country.get()
        dialogue= val_dialogue.get()
        rhyme= val_rhyme.get()

        story = StoryGenerator()
        if topic == "Detective":
            story.ep1()
        else:
            pass

    inputs = Tk()
    inputs.title("LET'S PLAY!")
    inputs.geometry('500x600')

    Label(inputs, text="Let's build the Story!", font=("Comic Sans MS Bold",14), justify='left').pack(side=TOP, pady=7)
    first = Frame(inputs)
    Label(first, text="Enter your name: ").pack(side=LEFT)
    val_name= Entry(first, width=16)
    val_name.pack(side=LEFT, padx=50)
    first.pack(side=TOP, pady=2)
    second = Frame(inputs)
    Label(second, text="Enter your friend's name: ").pack(side=LEFT)
    val_friend = Entry(second, width=20)
    val_friend.pack(side=LEFT, padx=50)
    second.pack(side=TOP, pady=2)
    third = Frame(inputs)
    Label(third, text="Enter a male name : ").pack(side=LEFT)
    val_noun = Entry(third, width=15)
    val_noun.pack(side=LEFT, padx=65)
    third.pack(side=TOP, pady=2)
    fourth = Frame(inputs)
    Label(fourth, text="Enter the name of your favourite teacher : ").pack(side=LEFT)
    val_teacher = Entry(fourth, width=20)
    val_teacher.pack(side=LEFT, padx=30)
    fourth.pack(side=TOP, pady=2)
    fifth = Frame(inputs)
    Label(fifth, text="Select an expression : ").pack(side=LEFT)
    val_excl = Combobox(fifth, state='readonly', width=20, values=["flibbertigibbet","whippersnapper","bumfuzzle","hullaballoo"])
    val_excl.current()
    val_excl.pack(side=LEFT, padx=51)
    fifth.pack(side=TOP, pady=2)
    sixth = Frame(inputs)
    Label(sixth, text="Enter a store's name : ").pack(side=LEFT)
    val_store = Entry(sixth, width=23)
    val_store.pack(side=LEFT, padx=43)
    sixth.pack(side=TOP, pady=2)
    seventh = Frame(inputs)
    Label(seventh, text="Select one from these Parts of the body: ").pack(side=LEFT)
    val_potb = Combobox(seventh, state='readonly', width=20,values=["tonsil","toe", "nose", "ear"])
    val_potb.current()
    val_potb.pack(side=LEFT, padx=19)
    seventh.pack(side=TOP, pady=2)
    eighth = Frame(inputs)
    Label(eighth, text="Select a distance : ").pack(side=LEFT)
    val_distance = Combobox(eighth, state='readonly', width=20, values=["1/2 mm","3000 miles","999 light years"])
    val_distance.current()
    val_distance.pack(side=LEFT, padx=28)
    eighth.pack(side=TOP, pady=2)
    ninth = Frame(inputs)
    Label(ninth, text="Select a silly word : ").pack(side=LEFT)
    val_silly = Combobox(ninth, state='readonly', width=20,values=["bamboozle","abracadabra","dillydally"])
    val_silly.current()
    val_silly.pack(side=LEFT, padx=37)
    ninth.pack(side=TOP, pady=2)
    tenth = Frame(inputs)
    Label(tenth, text="Enter the name of a holiday : ").pack(side=LEFT)
    val_holiday = Entry(tenth, width=10)
    val_holiday.pack(side=LEFT, padx=42)
    tenth.pack(side=TOP, pady=2)
    eleventh = Frame(inputs)
    Label(eleventh, text="Enter a movie title! : ").pack(side=LEFT)
    val_movie = Entry(eleventh, width=20)
    val_movie.pack(side=LEFT, padx=57)
    eleventh.pack(side=TOP, pady=2)
    twelth = Frame(inputs)
    Label(twelth, text="Enter a country : ").pack(side=LEFT)
    val_country = Entry(twelth, width=10)
    val_country.pack(side=LEFT, padx=76)
    twelth.pack(side=TOP, pady=2)
    thirteenth = Frame(inputs)
    Label(thirteenth, text="Enter a number : ").pack(side=LEFT)
    val_number = Entry(thirteenth, width=10)
    val_number.pack(side=LEFT, padx=76)
    thirteenth.pack(side=TOP, pady=2)
    fourteenth = Frame(inputs)
    Label(fourteenth, text="Enter an animal : ").pack(side=LEFT)
    val_animal = Entry(fourteenth, width=10)
    val_animal.pack(side=LEFT, padx=76)
    fourteenth.pack(side=TOP, pady=2)
    fifteenth=Frame(inputs)
    Label(fifteenth, text="Enter a verb ending in -ing : ").pack(side=LEFT)
    val_verb = Entry(fifteenth, width=15)
    val_verb.pack(side=LEFT, padx=33)
    fifteenth.pack(side=TOP, pady=2)
    sixteenth = Frame(inputs)
    Label(sixteenth, text="Enter a movie dialogue xD : ").pack(side=LEFT)
    val_dialogue = Entry(sixteenth, width=30)
    val_dialogue.pack(side=LEFT, padx=10)
    sixteenth.pack(side=TOP, pady=2)
    seventeenth = Frame(inputs)
    Label(seventeenth, text="Enter a children's rhyme : ").pack(side=LEFT)
    val_rhyme = Entry(seventeenth, width=24)
    val_rhyme.pack(side=LEFT, padx=35)
    seventeenth.pack(side=TOP, pady=2)
    eighteenth = Frame(inputs)
    Button(eighteenth, text="Close", command=inputs.destroy,bg="blue", fg="white").pack(side=RIGHT, padx=10, pady=10)
    Button(eighteenth, text="Submit", bg="blue", fg="white", command=redirect).pack(side=RIGHT, padx=10, pady=10)
    eighteenth.pack(side=TOP, pady=5)

Label(main, text="MaD LiBs tHeAtRE", font=("Comic Sans MS Bold", 17), justify='center').pack(pady=10)

bt = Frame(main)
Button(bt, text="The Detective", command=lambda clicked="Detective": inputScreen(clicked), bg="blue", fg="white", padx=8).pack(pady=5)
Button(bt, text="Close", command=main.destroy, padx=7,bg="black",fg="white").pack(pady=8)
bt.pack()

main.mainloop()
