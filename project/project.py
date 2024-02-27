from tkinter import*
from tkinter import ttk
import tkinter as Tk
import pyttsx3
import random
from tkinter import messagebox
from random import choice
from random import shuffle
import speech_recognition as sr

root=Tk.Tk()
root.title("Indian Encyclodpedia")
root.geometry("400x400")

def main ():
    memory_game_btn= Button(root,text="Khoka Game",padx=30,pady=30,command=memory_game)
    memory_game_btn.pack()


    jumbled_words_btn= Button(root,text="Jumbled Words Game",padx=30,pady=30,command=jumbled_words)
    jumbled_words_btn.pack()


    grammar_training_btn= Button(root,text="Grammar Training",padx=30,pady=30,command=grammar_training)
    grammar_training_btn.pack()

    quit_btn=Button(root,text="Exit",bg='red',padx=30,pady=30,command=quit)
    quit_btn.pack()

    root.mainloop()


def jumbled_words():
    global count
    global answer_label

    Hindi = Toplevel()
    Hindi.title("Vocab Game")
    Hindi.geometry("600x800")
    frame_1 = Frame(Hindi)
    frame_1.grid(row=6, column=0)
    frame_2 = Frame(Hindi)
    frame_2.grid(row=8, column=0)

    global data_into_list
    my_file = open("hindi-words-2.txt", "r", encoding="utf-8")

    count = 0  # Initialize count

    # reading the file
    words_dictionary = {}

    # replacing end splitting the text
    # when newline ('\n') is seen.
    for line in my_file:
        # Split the line into words
        words = line.split()
        if len(words) != 2:
            # Skip lines that don't have exactly two values
            continue

        # Unpack the key and value
        key, value = words

        # Add the key-value pair to the dictionary
        words_dictionary[key] = value

    print(words_dictionary)
    keyword_list = list(words_dictionary.keys())

    my_label = Label(Hindi, text="", font=("Helvetica", 40))
    my_label.grid(row=0, column=0, pady=20)

    def shuffler():
        global word
        word = choice(keyword_list)

        break_apart = list(word)
        shuffle(break_apart)

        global shuffled_word
        shuffled_word = ''
        for letter in break_apart:
            shuffled_word += letter

        my_label.config(text=shuffled_word)

    def meaning():
        global keyword_list
        global word
        global words_dictionary
        global meaning_word
        meaning_word = str(words_dictionary[word])
        meaning_label.config(
            text="Buddy, The meaning of this word is" + " " + meaning_word)

    def answer():
        global word
        global answer_label
        global count
        if word == entry_answer.get():
            entry_answer.delete(0, 'end')
            my_label.config(text=" ")
            Hindi.config(background="green")
            count += 1  # Increment the score
            answer_label.config(
                text="Score: " + str(count) + "/" + str(len(keyword_list)))
        else:
            entry_answer.delete(0, 'end')
            my_label.config(text=" ")
            Hindi.config(background="red")
            answer_label.config(
                text="Do not worry the correct answer is " + word + ". Score: " + str(count) + "/" + str(len(keyword_list)))

    def press(alpha):
        current = entry_answer.get()
        entry_answer.delete(0, 'end')
        entry_answer.insert(0, str(current)+str(alpha))
        print(entry_answer.get())

    entry_answer = Entry(Hindi, font=("Helvetica", 24))
    entry_answer.grid(row=1, column=0, pady=20)

    my_buttin = Button(Hindi, text="Pick Another Word", command=shuffler)
    my_buttin.grid(row=2, column=0, pady=20)

    answer_btn = Button(Hindi, text="Answer", command=answer)
    answer_btn.grid(row=4, column=0)
    answer_label = Label(
        Hindi, text="Score: " + str(count) + "/" + str(len(keyword_list)-1))
    answer_label.grid(row=14, column=0)

    meaning_btn = Button(Hindi, text="English Meaning", command=meaning)
    meaning_btn.grid(row=5, column=0)

    meaning_label = Label(Hindi, text='', font=("Helvetica", 18))
    meaning_label.grid(row=15, column=0)

    Exit_btn = Button(Hindi, text="Exit", command=Hindi.destroy)
    Exit_btn.grid(row=16, column=0)

    # Generate buttons for Hindi alphabets
    hindi_alphabets = ['अ', 'आ', 'इ', 'ई', 'उ', 'ऊ', 'ऋ', 'ॠ', 'ए', 'ऐ', 'ओ', 'औ', 'ं', 'ः', 'अं', 'अः', 'ा', 'ि', 'ी', 'ु', 'ू', 'ृ', 'ॄ', 'ॅ', 'ॆ', 'े', 'ै', 'ॉ', 'ॊ', 'ो', 'ौ', 'क', 'ख', 'ग', 'घ', 'ङ', 'च', 'छ', 'ज', 'झ', 'ञ', 'ट', 'ठ', 'ड', 'ढ', 'ण', 'त', 'थ', 'द', 'ध', 'न', 'प', 'फ', 'ब', 'भ', 'म', 'य', 'र', 'ल', 'व', 'श', 'ष', 'स', 'ह', 'क्ष', 'त्र', 'ज्ञ']

    column_index = 0
    row_index = 0
    for alphabet in hindi_alphabets:
        btn = Button(frame_1, text=alphabet, width=6,
                     command=lambda alpha=alphabet: press(alpha))
        btn.grid(row=row_index, column=column_index)
        column_index += 1
        if column_index > 5:
            column_index = 0
            row_index += 1


def grammar_training():
    global Grammar
    Grammar = Tk.Tk()
    Grammar.title("The Ultimate Pronunciation Game")
    Grammar.geometry("400x400")

    def speak(msg_text, text):
        listener = sr.Recognizer()
        try:
            with sr.Microphone() as source:
                print("listening.....")
                voice = listener.listen(source)
                command = listener.recognize_google(voice, language='hi-IN')
                print(type(command))
                print(command)
                if command == msg_text:
                    text.insert(Tk.END, "Your answer is Correct Hurrayyy")
                else:
                    text.insert(Tk.END, "Your answer is Incorrect. Please try again.")
        except sr.UnknownValueError:
            print("Could not understand audio")
            speak(msg_text, text)
        except sr.RequestError as e:
            print("Could not request results; {0}".format(e))

    def ques_1():
        global top_1
        top_1 = Toplevel()
        top_1.title("हिन्दी उच्चारण का सफ़र")
        top_1.geometry("400x500")

        def inner_speak():
            speak("आपका", text1)

        frame1 = LabelFrame(top_1, text="प्रश्न 1 (Question 1)")
        frame1.pack(pady=20)
        my_message = Message(frame1, text="आपका स्वास्थ्य कैसा है?", font=("Helvetica", 20), aspect=150, justify=Tk.CENTER)
        my_message.pack(pady=10, padx=10)
        text1 = Text(frame1, height=5, width=30, font=12)
        text1.pack()
        answer_btn = Button(frame1, text="उत्तर दिजिये (Answer)\n Please repeat the sentence (कृपया वाक्य दोहराएं)",
                            padx=40, pady=50, command=inner_speak)
        answer_btn.pack()
        next_btn = Button(top_1, text="Next", padx=40, pady=40, command=ques_2)
        next_btn.pack()

    def ques_2():
        global top_2
        top_2 = Toplevel()
        top_2.title("हिन्दी उच्चारण का सफ़र")
        top_2.geometry("400x900")

        def inner_speak():
            speak("मेरा नाम बिटिया है", text3)

        frame2 = LabelFrame(top_2, text="प्रश्न 2 (Question 2)")
        frame2.pack(pady=20)
        my_message = Message(frame2, text="आपका नाम क्या है?", font=("Helvetica", 20), aspect=150, justify=Tk.CENTER)
        my_message.pack(pady=10, padx=10)

        frame3 = LabelFrame(top_2, text="सहायक संकेत (Helpful Hints)")
        frame3.pack(pady=20)
        my_message = Message(frame3,
                             text="When asked about name in Hindi language you can respond by saying \n मेरा नाम__(‘Your name‘)__है",
                             font=("Helvetica", 20), aspect=150, justify=Tk.CENTER)
        my_message.pack(pady=10, padx=10)

        text3 = Text(frame3, height=5, width=30, font=12)
        text3.pack()
        answer_btn = Button(frame3, text="उत्तर दिजिये (Answer)", padx=40, pady=40, command=lambda: speak("मेरा नाम बिटिया है", text3))
        answer_btn.pack()
        next_btn = Button(frame3, text="Next", padx=40, pady=40, command=ques_3)
        next_btn.pack()
        back_btn = Button(frame3, text="Back", padx=40, pady=40, command=top_2.destroy)
        back_btn.pack()
    def ques_3():
        global top_3
        top_3 = Toplevel()
        top_3.title("हिन्दी उच्चारण का सफ़र")
        top_3.geometry("400x900")

        def inner_speak():
            speak("क्या मदद", text4)

        frame4 = LabelFrame(top_3, text="प्रश्न 3 (Question 3)")
        frame4.pack(pady=20)
        my_message = Message(frame4, text="क्या मैं आपकी मदद कर सकता हुँ?", font=("Helvetica", 20), aspect=150, justify=Tk.CENTER)
        my_message.pack(pady=10, padx=10)

        text4 = Text(frame4, height=5, width=30, font=12)
        text4.pack()
        answer_btn = Button(frame4, text="उत्तर दिजिये (Answer)", padx=40, pady=40, command=lambda: speak("क्या मदद", text4))
        answer_btn.pack()
        next_btn = Button(frame4, text="Next", padx=40, pady=40, command=ques_4)
        next_btn.pack()
        back_btn = Button(frame4, text="Back", padx=40, pady=40, command=top_3.destroy)
        back_btn.pack()

    def ques_4():
        global top_4
        top_4 = Toplevel()
        top_4.title("हिन्दी उच्चारण का सफ़र")
        top_4.geometry("400x900")

        def inner_speak():
            speak("आखें", text5)

        frame5 = LabelFrame(top_4, text="प्रश्न 4 (Question 4)")
        frame5.pack(pady=20)
        my_message = Message(frame5, text="मानव शरीर में कितनी आखें होती है?", font=("Helvetica", 20), aspect=150, justify=Tk.CENTER)
        my_message.pack(pady=10, padx=10)
        text5 = Text(frame5, height=5, width=30, font=12)
        text5.pack()

        answer_btn = Button(frame5, text="उत्तर दिजिये (Answer)", padx=40, pady=40, command=lambda: speak("आखें", text5))
        answer_btn.pack()
        next_btn = Button(frame5, text="Next", padx=40, pady=40, command=ques_5)
        next_btn.pack()
        back_btn = Button(frame5, text="Back", padx=40, pady=40, command=top_4.destroy)
        back_btn.pack()

    def ques_5():
        global top_5
        top_5 = Toplevel()
        top_5.title("हिन्दी उच्चारण का सफ़र")
        top_5.geometry("400x900")

        def inner_speak():
            speak("आम", text6)

        frame6 = LabelFrame(top_5, text="प्रश्न 5 (Question 5)")
        frame6.pack(pady=20)
        my_message = Message(frame6, text="आम का रंग कौनसा होता है?", font=("Helvetica", 20), aspect=150, justify=Tk.CENTER)
        my_message.pack(pady=10, padx=10)
        text6 = Text(frame6, height=5, width=30, font=12)
        text6.pack()

        answer_btn = Button(frame6, text="उत्तर दिजिये (Answer)", padx=40, pady=40, command=lambda: speak("आम", text6))
        answer_btn.pack()
        next_btn = Button(frame6, text="Next", padx=40, pady=40, command=ques_6)
        next_btn.pack()
        back_btn = Button(frame6, text="Back", padx=40, pady=40, command=top_5.destroy)
        back_btn.pack()

    def ques_6():
        global top_6
        top_6 = Toplevel()
        top_6.title("हिन्दी उच्चारण का सफ़र")
        top_6.geometry("400x900")

        def inner_speak():
            speak("विद्यालय जाना", text7)

        frame7 = LabelFrame(top_6, text="प्रश्न 6 (Question 6)")
        frame7.pack(pady=20)
        my_message = Message(frame7, text="बच्चों को विद्यालय क्यों जाना चाहिए?", font=("Helvetica", 20), aspect=150, justify=Tk.CENTER)
        my_message.pack(pady=10, padx=10)
        text7 = Text(frame7, height=5, width=30, font=12)
        text7.pack()

        answer_btn = Button(frame7, text="उत्तर दिजिये (Answer)", padx=40, pady=40, command=lambda: speak("विद्यालय जाना", text7))
        answer_btn.pack()
        next_btn = Button(frame7, text="Next", padx=40, pady=40, command=top_6.destroy)
        next_btn.pack()
        back_btn = Button(frame7, text="Back", padx=40, pady=40, command=top_5.destroy)
        back_btn.pack()

        selection_btn = Button(Grammar, text="Namaste \n ", padx=40, pady=40, command=ques_1)
        selection_btn.place(relx=0.5, rely=0.5, anchor=CENTER)






def memory_game():
    Khoka = Toplevel()

    Khoka.title("Khoka Game")
    Khoka.geometry("460x450")

    global winner
    global count
    global answer_list
    global answer_dict
    # set winner counter to 0
    winner=0

    #creating the matches
    game_list = ["सेब","सेब","केला","केला","अंगूर","अंगूर","आम","आम","संतरा","संतरा","टमाटर","टमाटर"]
    #shuffle the matches
    random.shuffle(game_list)

    my_frame = Frame(Khoka)
    my_frame.pack(pady=10)

    #essential variable for keeping the track of how many times the grid was clicked as after two trials
    #we should reset the state
    count=0
    #helps us keep track of which tiles or buttons were pressed and helps us to keep track of their position
    answer_list=[]
    #helps us to keep track of which number has been assigned to which button in the form of key, value format
    answer_dict={}


    #resttting the game
    def reset():
        global game_list, winner
        winner=0
        #creating the matches
        game_list = ["सेब","सेब","केला","केला","अंगूर","अंगूर","आम","आम","संतरा","संतरा","टमाटर","टमाटर"]
        #shuffle the matches
        random.shuffle(game_list)
        #reset the label
        my_label.config(text="")

        #reset the tiles
        button_list = [b0,b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,b11]
        #loop through the buttons for changing the colors
        for button in button_list:
            button.config(text=" ",bg="SystemButtonFace",state="normal")




    # winning function
    def win():
        my_label.config(text="बधाई हो, आपकी जीत हुई है")
        button_list = [b0,b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,b11]
        #loop through the buttons for changing the colors
        for button in button_list:
            button.config(bg="yellow")

    def button_click(b,number):
        global count, answer_list,answer_dict,winner
        if b["text"]==' ' and count < 2:

            b["text"]= game_list[number]
            #add number to answer list
            answer_list.append(number)
            #add number and button to answer dictionary
            answer_dict[b]=game_list[number]
            count+=1

            #start to determine correct or not
        if len(answer_list)==2:
            if game_list[answer_list[0]]==game_list[answer_list[1]]:
                my_label.config(text="Match")
                for key in answer_dict:
                    key["state"]="disabled"
                count=0
                answer_list=[]
                answer_dict={}
                #increment the winner counter
                winner+=1
                if winner==6:
                    win()
            else:
                my_label.config(text="doh!")
                count=0
                answer_list=[]
                #pop up box
                messagebox.showinfo("Incorrect!")
                #resetting the buttons
                for key in answer_dict:
                    key["text"] = " "
                    answer_dict = {}

    b0=Button(my_frame,text=' ',font=("Helvetica",20),height=3,width=6,command=lambda:button_click(b0,0))
    b1=Button(my_frame,text=' ',font=("Helvetica",20),height=3,width=6,command=lambda:button_click(b1,1))
    b2=Button(my_frame,text=' ',font=("Helvetica",20),height=3,width=6,command=lambda:button_click(b2,2))
    b3=Button(my_frame,text=' ',font=("Helvetica",20),height=3,width=6,command=lambda:button_click(b3,3))
    b4=Button(my_frame,text=' ',font=("Helvetica",20),height=3,width=6,command=lambda:button_click(b4,4))
    b5=Button(my_frame,text=' ',font=("Helvetica",20),height=3,width=6,command=lambda:button_click(b5,5))
    b6=Button(my_frame,text=' ',font=("Helvetica",20),height=3,width=6,command=lambda:button_click(b6,6))
    b7=Button(my_frame,text=' ',font=("Helvetica",20),height=3,width=6,command=lambda:button_click(b7,7))
    b8=Button(my_frame,text=' ',font=("Helvetica",20),height=3,width=6,command=lambda:button_click(b8,8))
    b9=Button(my_frame,text=' ',font=("Helvetica",20),height=3,width=6,command=lambda:button_click(b9,9))
    b10=Button(my_frame,text=' ',font=("Helvetica",20),height=3,width=6,command=lambda:button_click(b10,10))
    b11=Button(my_frame,text=' ',font=("Helvetica",20),height=3,width=6,command=lambda:button_click(b11,11))

    b0.grid(row=0,column=0)
    b1.grid(row=0,column=1)
    b2.grid(row=0,column=2)
    b3.grid(row=0,column=3)
    b4.grid(row=1,column=0)
    b5.grid(row=1,column=1)

    b6.grid(row=1,column=2)
    b7.grid(row=1,column=3)
    b8.grid(row=2,column=0)
    b9.grid(row=2,column=1)
    b10.grid(row=2,column=2)
    b11.grid(row=2,column=3)

    my_label= Label(Khoka, text="")
    my_label.pack(pady=20)

    #creating a menu
    my_menu= Menu(Khoka)
    Khoka.config(menu=my_menu)

    option_menu=Menu(my_menu, tearoff=False)
    my_menu.add_cascade(label="Options",menu=option_menu)
    option_menu.add_command(label="Reset Game",command=reset)
    option_menu.add_separator()
    option_menu.add_command(label="Exit Game",command=Khoka.destroy)

main()
