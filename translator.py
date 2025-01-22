from tkinter import Tk, ttk, Text, Button
from googletrans import Translator
from ttkbootstrap import Style

translator = Translator()

style = Style(theme='superhero')
window = style.master
window.title('Translator')

global_frame = ttk.Frame()

def translate(event=None):
    text = input_text.get('1.0', 'end')
    input_language = combo_input.get()
    output_language = combo_output.get()
    result = translator.translate(text=text, src=input_language, dest=output_language)
    output_text.configure(state='normal')
    output_text.delete('1.0', 'end')
    output_text.insert('1.0',result.text)
    output_text.configure(state='disabled')

language_list = ['pt', 'es', 'en']

# Input
frame_input = ttk.Frame(global_frame)

label_input = ttk.Label(
    frame_input,
    text='Input:',
    font=(None, 20)
)

combo_input = ttk.Combobox(
    frame_input,
    values=language_list,
    font=(None, 20),
    state='readonly'
)
combo_input.set('pt')

label_input.grid(row=0, column=0, padx=10, pady=10)
combo_input.grid(row=0, column=1)
frame_input.pack()

input_text = Text(
    global_frame,
    height=10,
    width=50,
)
input_text.pack(padx=10, fill='both', expand='yes')


#Output
frame_output = ttk.Frame(global_frame)

label_output = ttk.Label(
    frame_output,
    text='Output:',
    font=(None, 20),
)

combo_output = ttk.Combobox(
    frame_output,
    values=language_list,
    font=(None, 20),
    state='readonly'
)
combo_output.set('en')
label_output.grid(row=0, column=0, padx=10, pady=10)
combo_output.grid(row=0, column=1)
frame_output.pack()

output_text = Text(
    global_frame,
    state='disabled',
    height=10,
    width=50
)
output_text.pack(padx=10, pady=20, fill='both', expand='yes')

button = ttk.Button(
    global_frame,
    text='Translate!',
    # font=(None, 20),
    command=translate
)
button.pack(fill='both', padx=10, pady=10)

window.bind('<Return>', translate)

global_frame.pack()

window.mainloop()