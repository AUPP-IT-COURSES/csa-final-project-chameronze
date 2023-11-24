from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import requests


root = Tk()
root.title('Real-Time Currency Converter')
root.geometry("500x500")

#create tabs
my_notebook = ttk.Notebook(root)
my_notebook.pack(pady=5)

#create frames 
currency_frame = Frame(my_notebook, width= 480, height=480)
conversion_frame = Frame(my_notebook, width= 480, height=480)

currency_frame.pack(fill="both", expand=1)

#add tabs
my_notebook.add(currency_frame, text="Currencies")
my_notebook.add(conversion_frame, text="Convert")

#disable 2nd tab
my_notebook.tab(1, state="disabled")




###currencies tab###
####################

def lock():
    if not your_currency.get() or not to_currency.get():
        messagebox.showwarning("Warning!", "You Didn't Fill Out All The Fields!")
    else:
        #disable entry box
        your_currency.config(state="disabled")
        to_currency.config(state="disabled")
        #enable rate entry
        rate_entry.config(state="normal")
        #delete old rate
        rate_entry.delete(0,END)
        #get rate
        rate_entry.insert(0, round(getrate(),2))
        #disable rate_entry
        rate_entry.config(state="disabled")
        #enable tab
        my_notebook.tab(1, state="normal")
        #change tab fields
        amount_label.config(text=f'Amount of {your_currency.get()} To Convert To {to_currency.get()}')
        converted_label.config(text=f'Equals This Many {to_currency.get()}')
        convert_button.config(text=f'Convert From {your_currency.get()}')

def unlock():
    #enable entry box
        your_currency.config(state="normal")
        to_currency.config(state="normal")
        #enable tab
        my_notebook.tab(1, state="disabled")
    
def getrate():
    api_key = "d1f4405ce3d8be4212bfe566"
    url = f'https://v6.exchangerate-api.com/v6/{api_key}/pair/{your_currency.get()}/{to_currency.get()}'
    rq = requests.get(url)
    data = rq.json()
    rate = data['conversion_rate']
    return rate

def on_key_release(event):
    value = event.widget.get()
    value = value.strip().lower()
    if value == '':
        data = currency_list
    else:
        data = [x for x in currency_list if value in x.lower()]
    your_currency['values'] = data
  
def on_key_release1(event):
    value = event.widget.get()
    value = value.strip().lower()
    if value == '':
        data = currency_list
    else:
        data = [x for x in currency_list if value in x.lower()]
    to_currency['values'] = data

currency_list = ["AED","AFN","ALL","AMD","ANG","AOA","ARS","AUD","AWG","AZN","BAM","BBD","BDT","BGN","BHD","BIF","BMD","BND","BOB","BRL","BSD","BTN","BWP","BYN","BZD","CAD","CDF","CHF","CLP","CNY","COP","CRC","CUP","CVE","CZK","DJF","DKK","DOP","DZD","EGP","ERN","ETB","EUR","FJD","FKP","FOK","GBP","GEL","GGP","GHS","GIP","GMD","GNF","GTQ","GYD","HKD","HNL","HRK","HTG","HUF","IDR","ILS","IMP","INR","IQD","IRR","ISK","JEP","JMD","JOD","JPY","KES","KGS","KHR","KID","KMF","KRW","KWD","KYD","KZT","LAK","LBP","LRD","LSL","LYD","MAD","MDL","MGA","MKD","MMK","MNT","MOP","MRU","MUR","MVR","MWK","MXN","MYR","MZN","NAD","NGN","NIO","NOK","NPR","NZD","OMR","PAB","PEN","PGK","PHP","PKR","PLN","PYG","QAR","RON","RSD","RUB","RWF","SAR","SBD","SCR","SDG","SEK","SGD","SHP","SLE","SOS","SRD","SSP","STN","SYP","SZL","THB","TJS","TMT","TND","TOP","TRY","TTD","TVD","TWD","TZS","UAH","UGX","USD","UYU","UZS","VES","VND","VUV","WST","XAF","XCD","XDR","XOF","XPF","YER","ZAR","ZMW","ZWL"]    

##your currency box

your = LabelFrame(currency_frame, text="Your Currency")
your.pack(pady=20)
#

your_currency = ttk.Combobox(your, values=currency_list)
your_currency.pack(pady=10, padx=10)
your_currency.bind('<KeyRelease>', on_key_release)


#fake label for width
fake_label_1 = Label(your, text="", width=54)
fake_label_1.pack()

##conversion currency box
#
conversion = LabelFrame(currency_frame, text="Conversion Currency")
conversion.pack(pady=20)

#label1
convert_to_label = Label(conversion, text="Currency To Convert To...")
convert_to_label.pack(pady=10)
#entry1

to_currency = ttk.Combobox(conversion, values=currency_list)
to_currency.pack()
to_currency.bind('<KeyRelease>', on_key_release1)
#label2
current_rate_label = Label(conversion, text="Current Conversion Rate...")
current_rate_label.pack(pady=10)
#entry2
rate_entry = Entry(conversion, font=("Helvetica", 24), state="disabled")
rate_entry.pack(pady=10, padx=10)

#button frame
button_frame = Frame(currency_frame)
button_frame.pack(pady=20)
#lock button
lock_button = Button(button_frame, text="Lock", command=lock)
lock_button.grid(row=0, column=0, padx=10)
#unlock button
unlock_button = Button(button_frame, text="Unlock", command=unlock)
unlock_button.grid(row=0, column=1, padx=10)

###convert tab###
#################
def convert():
    #clear converted entry box
    converted_entry.delete(0, END)

    conversion = float(getrate()) * float(amount_entry.get())
    #round to 2 decimals
    conversion = round(conversion,2)
    #add commas
    conversion = '{:,}'.format(conversion)
    #update entry box
    converted_entry.insert(0, conversion)

def clear():
    amount_entry.delete(0, END)
    converted_entry.delete(0, END)

##amount label frame
amount_label = LabelFrame(conversion_frame, text= "Amount To Convert")
amount_label.pack(pady=20)

amount_entry = Entry(amount_label, font=("Helvetica", 24))
amount_entry.pack(pady=10, padx=10)

convert_button = Button(amount_label, text="Convert From", command=convert)
convert_button.pack(pady=20)

##converted frame
converted_label = LabelFrame(conversion_frame, text="Converted Currency")
converted_label.pack(pady=20)

converted_entry = Entry(converted_label, font=("Helvetica", 24), bd=0, bg="systembuttonface")
converted_entry.pack(pady=10, padx=10)

#clear button
clear_button = Button(conversion_frame, text="Clear", command=clear)
clear_button.pack(pady=20)

#fake label for spacing
spacer = Label(conversion_frame, text="", width=68)
spacer.pack()

root.mainloop()