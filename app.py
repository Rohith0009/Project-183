from tkinter import *
import json
import requests

root = Tk()
root.title("Country Details")
root.geometry("1600x1600")

root.configure(background="pale green")

heading = Label(root, text="Capital City Name", font=("Arial", 30), bg="pale green")
heading.place(relx=0.5, rely=0.05, anchor=CENTER)

entry = Entry(root, font=("Arial", 30), bg="white")
entry.place(relx=0.5, rely=0.15, anchor=CENTER)

Country = Label(root, text="Country: ", font=("Arial", 23), bg="pale green")
Country.place(relx=0.5, rely=0.35, anchor=CENTER)
Region = Label(root, text="Region: ", font=("Arial", 23), bg="pale green")
Region.place(relx=0.5, rely=0.45, anchor=CENTER)
Language = Label(root, text="Language: ", font=("Arial", 23), bg="pale green")
Language.place(relx=0.5, rely=0.55, anchor=CENTER)
Population = Label(root, text="Population: ", font=("Arial", 23), bg="pale green")
Population.place(relx=0.5, rely=0.65, anchor=CENTER)
Area = Label(root, text="Area: ", font=("Arial", 23), bg="pale green")
Area.place(relx=0.5, rely=0.75, anchor=CENTER)


def get_details():
    Api_Request = requests.get(f"https://restcountries.com/v2/capital/{entry.get()}")
    Out = json.loads(Api_Request.content)
    Country["text"] = f"Country: {Out[0]['name']}"
    Region["text"] = f"Region: {Out[0]['region']}"
    Language["text"] = f"Region: {Out[0]['languages']}"
    Population["text"] = f"Region: {Out[0]['population']}"
    Area["text"] = f"Region: {Out[0]['area']}"


btn = Button(
    text="Check Details",
    font=("Arial", 26),
    bg="pale turquoise",
    command=get_details,
)
btn.place(relx=0.5, rely=0.25, anchor=CENTER)

root.mainloop()
