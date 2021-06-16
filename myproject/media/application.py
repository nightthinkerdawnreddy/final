import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter.scrolledtext import *
import tkinter.filedialog

# NLP Pkgs
#from spacy_summarization import text_summarizer
#from spacysummarization import text_summarizer

# Web Scraping Pkg

from bs4 import BeautifulSoup
from urllib.request import urlopen

# Structure and Layout
window = Tk()
window.title("Summaryzer GUI")
window.geometry("700x400")
window.config(background='black')

style = ttk.Style(window)
style.configure('lefttab.TNotebook', tabposition='wn', )

# TAB LAYOUT
tab_control = ttk.Notebook(window, style='lefttab.TNotebook')

tab1 = ttk.Frame(tab_control)
tab2 = ttk.Frame(tab_control)
tab3 = ttk.Frame(tab_control)

# ADD TABS TO NOTEBOOK
tab_control.add(tab1, text=f'{"Home":^20s}')
tab_control.add(tab2, text=f'{"File":^20s}')
tab_control.add(tab3, text=f'{"URL":^20s}')


label1 = Label(tab1, text='Summaryzer', padx=5, pady=5)
label1.grid(column=0, row=0)

label2 = Label(tab2, text='File Processing', padx=5, pady=5)
label2.grid(column=0, row=0)

label3 = Label(tab3, text='URL', padx=5, pady=5)
label3.grid(column=0, row=0)


tab_control.pack(expand=1, fill='both')


# Functions
def get_summary():
    raw_text = str(entry.get('1.0', tk.END))
    final_text = text_summarizer(raw_text)
    print(final_text)
    result = '\nSummary:{}'.format(final_text)
    tab1_display.insert(tk.END, result)


# Clear entry widget
def clear_text():
    entry.delete('1.0', END)


def clear_display_result():
    tab1_display.delete('1.0', END)


# Clear Text  with position 1.0
def clear_text_file():
    displayed_file.delete('1.0', END)


# Clear Result of Functions
def clear_text_result():
    tab2_display_text.delete('1.0', END)


# Clear For URL
def clear_url_entry():
    url_entry.delete(0, END)


def clear_url_display():
    tab3_display_text.delete('1.0', END)


# Clear entry widget
def clear_compare_text():
    entry1.delete('1.0', END)


def clear_compare_display_result():
    tab1_display.delete('1.0', END)


# Functions for TAB 2 FILE PROCESSER
# Open File to Read and Process
def openfiles():
    file1 = tkinter.filedialog.askopenfilename(
        filetypes=(("Text Files", ".txt"), ("All files", "*")))
    read_text = open(file1).read()
    displayed_file.insert(tk.END, read_text)


def get_file_summary():
    raw_text = displayed_file.get('1.0', tk.END)
    final_text = text_summarizer(raw_text)
    result = '\nSummary:{}'.format(final_text)
    tab2_display_text.insert(tk.END, result)


# Fetch Text From Url
def get_textone():
    from youtube_transcript_api import YouTubeTranscriptApi
    youtubevideo = "url"
    #youtubevideo ="https://www.youtube.com/watch?v=EpazNsLlPps"
    firstindex = youtubevideo.find("=")
    lastindex = youtubevideo.find("=", firstindex + 1)
    videoid = youtubevideo[firstindex + 1:]
    transcript = YouTubeTranscriptApi.get_transcript(videoid)
    datalist = []
    for i in transcript:
        datalist.append(i['text'])
    import spacy
    from spacy.lang.en.stop_words import STOP_WORDS
    from string import punctuation
    text = ''.join(datalist)
    stopwords = list(STOP_WORDS)
    nlp = spacy.load('en_core_web_sm')
    doc = nlp(text)
    tokens = [token.text for token in doc]
    punctuation = punctuation + '\n'
    wordfrequencies = {}
    for word in doc:
        if word.text.lower() not in stopwords:
            if word.text.lower() not in punctuation:
                if word.text not in wordfrequencies.keys():
                    wordfrequencies[word.text] = 1
                else:
                    wordfrequencies[word.text] += 1
    maxfrequency = max(wordfrequencies.values())
    for word in wordfrequencies.keys():
        wordfrequencies[word] = wordfrequencies[word] / maxfrequency
    sentence_tokens = [sent for sent in doc.sents]
    sentence_score = {}
    for sent in sentence_tokens:
        for word in sent:
            if word.text.lower() in wordfrequencies.keys():
                if sent not in sentence_score.keys():
                    sentence_score[sent] = wordfrequencies[word.text.lower()]
                else:
                    sentence_score[sent] += wordfrequencies[word.text.lower()]
    from heapq import nlargest
    select_length = int(len(sentence_tokens))
    select_length
    summary = nlargest(select_length, sentence_score, key=sentence_score.get)
    final_summary = [word.text for word in summary]
    summary = ' '.join(final_summary)
    print(summary)


def get_url_summary():
    summary = url_display.get('1.0', tk.END)
    final_text = text_summarizer(summary)
    result = '\nSummary:{}'.format(final_text)
    tab3_display_text.insert(tk.END, result)

# COMPARER FUNCTIONS


# MAIN NLP TAB
l1 = Label(tab1, text="Enter Text To Summarize")
l1.grid(row=1, column=0)

entry = Text(tab1, height=10)
entry.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

# BUTTONS
button1 = Button(tab1, text="Reset", command=clear_text,
                 width=12, bg='#03A9F4', fg='#fff')
button1.grid(row=4, column=0, padx=10, pady=10)

button2 = Button(tab1, text="Summarize", command=get_summary,
                 width=12, bg='#ced', fg='#fff')
button2.grid(row=4, column=1, padx=10, pady=10)

button3 = Button(tab1, text="Clear Result",
                 command=clear_display_result, width=12, bg='#03A9F4', fg='#fff')
button3.grid(row=5, column=0, padx=10, pady=10)

button4 = Button(tab1, text="Main Points", width=12, bg='#03A9F4', fg='#fff')
button4.grid(row=5, column=1, padx=10, pady=10)

# Display Screen For Result
tab1_display = Text(tab1)
tab1_display.grid(row=7, column=0, columnspan=3, padx=5, pady=5)

# FILE PROCESSING TAB
l1 = Label(tab2, text="Open File To Summarize")
l1.grid(row=1, column=1)

displayed_file = ScrolledText(tab2, height=7)  # Initial was Text(tab2)
displayed_file.grid(row=2, column=0, columnspan=3, padx=5, pady=3)

# BUTTONS FOR SECOND TAB/FILE READING TAB
b0 = Button(tab2, text="Open File", width=12, command=openfiles, bg='#c5cae9')
b0.grid(row=3, column=0, padx=10, pady=10)

b1 = Button(tab2, text="Reset ", width=12,
            command=clear_text_file, bg="#b9f6ca")
b1.grid(row=3, column=1, padx=10, pady=10)

b2 = Button(tab2, text="Summarize", width=12,
            command=get_file_summary, bg='blue', fg='#fff')
b2.grid(row=3, column=2, padx=10, pady=10)

b3 = Button(tab2, text="Clear Result", width=12, command=clear_text_result)
b3.grid(row=5, column=1, padx=10, pady=10)

b4 = Button(tab2, text="Close", width=12, command=window.destroy)
b4.grid(row=5, column=2, padx=10, pady=10)

# Display Screen
# tab2_display_text = Text(tab2)
tab2_display_text = ScrolledText(tab2, height=10)
tab2_display_text.grid(row=7, column=0, columnspan=3, padx=5, pady=5)

# Allows you to edit
tab2_display_text.config(state=NORMAL)

# URL TAB
l1 = Label(tab3, text="Enter URL To Summarize")
l1.grid(row=1, column=0)

raw_entry = StringVar()
url_entry = Entry(tab3, textvariable=raw_entry, width=50)
url_entry.grid(row=1, column=1)

datalist=[]
def get_text():
    from youtube_transcript_api import YouTubeTranscriptApi
    #youtubevideo = "url"
    youtubevideo = url_entry.get()
    print(youtubevideo)
    firstindex = youtubevideo.find("=")
    lastindex = youtubevideo.find("=", firstindex + 1)
    videoid = youtubevideo[firstindex + 1:]in
    transcript = YouTubeTranscriptApi.get_transcript(videoid)
    #datalist = []
    for i in transcript:
        datalist.append(i['text'])
    url_display = ScrolledText(tab3, height=10)
    url_display.grid(row=7, column=0, columnspan=3, padx=5, pady=5)
    url_display.insert(INSERT," ".join(datalist))
    #import spacy
    #from spacy.lang.en.stop_words import STOP_WORDS
    #from string import punctuation
    #text = ''.join(datalist)
    #stopwords = list(STOP_WORDS)
    #nlp = spacy.load('en_core_web_sm')
    #doc = nlp(text)
    #tokens = [token.text for token in doc]
    #punctuation = punctuation + '\n'
    #wordfrequencies = {}
    #for word in doc:
        #if word.text.lower() not in stopwords:
            #if word.text.lower() not in punctuation:
                #if word.text not in wordfrequencies.keys():
                    #wordfrequencies[word.text] = 1
                #else:
                    #wordfrequencies[word.text] += 1
    #maxfrequency = max(wordfrequencies.values())
    #for word in wordfrequencies.keys():
        #wordfrequencies[word] = wordfrequencies[word] / maxfrequency
    #sentence_tokens = [sent for sent in doc.sents]
    #sentence_score = {}
    #for sent in sentence_tokens:
        #for word in sent:
            #if word.text.lower() in wordfrequencies.keys():
                #if sent not in sentence_score.keys():
                    #sentence_score[sent] = wordfrequencies[word.text.lower()]
                #else:
                    #sentence_score[sent] += wordfrequencies[word.text.lower()]
    #from heapq import nlargest
    #select_length = int(len(sentence_tokens))
    #select_length
    #summary = nlargest(select_length, sentence_score, key=sentence_score.get)
    #final_summary = [word.text for word in summary]
    #summary = ' '.join(final_summary)
    # print(summary)
    # label87=Label(tab3,text=summary)
    #label87.grid(row=7, column=0, columnspan=3, padx=5, pady=5)
    #tab2_display_text = ScrolledText(tab2, height=10)
    #tab2_display_text.grid(row=7, column=0, columnspan=3, padx=5, pady=5)
    #tab2_display_text.insert(INSERT, summary)
def summarize():
    import nltk
    from nltk.corpus import stopwords
    from nltk.tokenize import word_tokenize, sent_tokenize
    import googletrans
    from googletrans import Translator
    translator=Translator()
    # Input text - to summarize
    text = " ".join(datalist)
    languagedetect=translator.detect(text)
    language="english"
    if languagedetect.lang=="ar":
        language="arabic"
    elif languagedetect.lang=="az":
        language="azerbaijani"
    elif languagedetect.lang=="da":
        language="danish"
    elif languagedetect.lang=="nl":
        language="dutch"
    elif languagedetect.lang=="en":
        language="english"
    elif languagedetect.lang=="fi":
        language="finnish"
    elif languagedetect.lang=="fr":
        language="french"
    elif languagedetect.lang=="de":
        language="german"
    elif languagedetect.lang=="el":
        language="greek"
    elif languagedetect.lang=="hu":
        language="hungarian"
    elif languagedetect.lang=="id":
        language="indonesian"
    elif languagedetect.lang=="it":
        language="italian"
    elif languagedetect.lang == "kk":
        language="kazakh"
    elif languagedetect.lang=="ne":
        language="nepali"
    elif languagedetect.lang=="no":
        language="norwegian"
    elif languagedetect.lang=="pt":
        language="portuguese"
    elif languagedetect.lang=="ro":
        language="romanian"
    elif languagedetect.lang=="ru":
        language="russian"
    elif languagedetect.lang=="sl":
        language="slovenian"
    elif languagedetect.lang=="es":
        language="spanish"
    elif languagedetect.lang=="sv":
        language="swedish"
    elif languagedetect.lang=="tg":
        language="tajik"
    elif languagedetect.lang=="tr":
        language="turkish"
    else:
        language="english"

    # Tokenizing the text
    stopWords = set(stopwords.words(language))
    words = word_tokenize(text)

    # Creating a frequency table to keep the
    # score of each word

    freqTable = dict()
    for word in words:
        word = word.lower()
        if word in stopWords:
            continue
        if word in freqTable:
            freqTable[word] += 1
        else:
            freqTable[word] = 1

    # Creating a dictionary to keep the score
    # of each sentence
    sentences = sent_tokenize(text)
    sentenceValue = dict()

    for sentence in sentences:
        for word, freq in freqTable.items():
            if word in sentence.lower():
                if sentence in sentenceValue:
                    sentenceValue[sentence] += freq
                else:
                    sentenceValue[sentence] = freq



    sumValues = 0
    for sentence in sentenceValue:
        sumValues += sentenceValue[sentence]

    # Average value of a sentence from the original text

    average = int(sumValues / len(sentenceValue))

    # Storing sentences into our summary.
    summary = ''
    for sentence in sentences:
        if (sentence in sentenceValue) and (sentenceValue[sentence] > (1.2 * average)):
            summary += " " + sentence
    print(summary)


    tab3_display_text = ScrolledText(tab3, height=10)
    tab3_display_text.grid(row=10, column=0, columnspan=3, padx=5, pady=5)
    tab3_display_text.insert(INSERT, summary)
    url_display = ScrolledText(tab3, height=10)
    url_display.grid(row=7, column=0, columnspan=3, padx=5, pady=5)
    url_display.insert(INSERT," ".join(datalist))

    

# BUTTONS
button1 = Button(tab3, text="Reset", command=clear_url_entry,
                 width=12, bg='#03A9F4', fg='#fff')
button1.grid(row=4, column=0, padx=10, pady=10)

button2 = Button(tab3, text="Get Text", command=get_text,
                 width=12, bg='#03A9F4', fg='#fff')
button2.grid(row=4, column=1, padx=10, pady=10)

button3 = Button(tab3, text="Clear Result",
                 command=clear_url_display, width=12, bg='#03A9F4', fg='#fff')
button3.grid(row=5, column=0, padx=10, pady=10)

button4 = Button(tab3, text="Summarize", command=summarize,
                 width=12, bg='#03A9F4', fg='#fff')
button4.grid(row=5, column=1, padx=10, pady=10)

# Display Screen For Result
url_display = ScrolledText(tab3, height=10)
url_display.grid(row=7, column=0, columnspan=3, padx=5, pady=5)

tab3_display_text = ScrolledText(tab3, height=10)
tab3_display_text.grid(row=10, column=0, columnspan=3, padx=5, pady=5)


window.mainloop()
