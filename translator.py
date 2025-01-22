from tkinter import Tk, ttk, Text
from googletrans import Translator

translator = Translator()

def traduzir():
    text = ''
    src = ''
    dest = ''
    result = translator.translate()
    return result

window = Tk()
window.title('Translator')

language_list = ['pt', 'es', 'en']

# Input
frame_input = ttk.Frame()

label_input = ttk.Label(
    frame_input,
    text='Input:',
    font=(None, 20)
)

combo_input = ttk.Combobox(
    frame_input,
    values=language_list,
    font=(None, 20)
)
combo_input.set('pt')

label_input.grid(row=0, column=0, padx=10, pady=10)
combo_input.grid(row=0, column=1)
frame_input.pack()

input_text = Text()
input_text.pack(padx=10, fill='both', expand='yes')


#Output
combo_output = ttk.Combobox(values=language_list)
combo_output.pack()

window.mainloop()