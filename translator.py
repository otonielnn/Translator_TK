from tkinter import ttk, Text, Toplevel
from googletrans import Translator
from ttkbootstrap import Style

translator = Translator()

style = Style(theme='superhero')
window = style.master
window.title('Translator')

global_frame = ttk.Frame(window)
global_frame.pack(fill='both', expand='yes')

def translate(event=None):
    text = input_text.get('1.0', 'end')
    input_language = combo_input.get()
    output_language = combo_output.get()
    result = translator.translate(text=text, src=input_language, dest=output_language)
    output_text.configure(state='normal')
    output_text.delete('1.0', 'end')
    output_text.insert('1.0', result.text)
    output_text.configure(state='disabled')

    with open('traducoes.txt', mode='a', newline='', encoding='UTF-8') as arquivo:
        arquivo.write(f'{text.strip()}|{input_language}|{result.text.strip()}|{output_language}\n')

def delete_translation(table):
    selected_line = table.selection()
    if selected_line:
        table.delete(selected_line)
        with open('traducoes.txt', mode='w', newline='', encoding='UTF-8') as arquivo:
            for linha in table.get_children():
                linha = table.item(linha)['values']
                arquivo.write(f'{linha[0]}|{linha[1]}|{linha[2]}|{linha[3]}\n')

def edit_translation(table, window):

    edit_translation_frame = ttk.Frame(window)
    edit_translation_frame.pack(fill='both', expand='yes')

    label_translation = ttk.Label(
    edit_translation_frame,
    text='Edit Tranlation:',
    font=(None, 20)
)
    label_translation.pack(padx=10, fill='both', expand='yes')

    new_translation = Text(edit_translation_frame, height=10, width=50)
    new_translation.pack(padx=10, fill='both', expand='yes')

    selected_line = table.selection()

    if not selected_line:
        return
    
    if selected_line:
        line = table.item(selected_line)['values']
        translation = line[2]
        new_translation.insert('1.0', translation)
    
    def save_translation():
        new_text = new_translation.get('1.0', 'end').strip()
        table.item(selected_line, values=(line[0], line[1], new_text, line[3]))
        with open('traducoes.txt', mode='w', newline='', encoding='UTF-8') as arquivo:
            for linha in table.get_children():
                linha = table.item(linha)['values']
                arquivo.write(f'{linha[0]}|{linha[1]}|{linha[2]}|{linha[3]}\n')
        window.destroy()

    button_save_translation = ttk.Button(edit_translation_frame, text='Save Translation', command=save_translation)
    button_save_translation.pack(fill='both', padx=10, pady=10)
    
    button_cancel = ttk.Button(edit_translation_frame, text='Cancel', command=edit_translation_frame.destroy)
    button_cancel.pack(fill='both', padx=10, pady=10)

def history():
    history_window = Toplevel(window)
    history_window.title('History')

    history_frame = ttk.Frame(history_window)
    history_frame.pack(fill='both', expand='yes')

    tabela = ttk.Treeview(history_frame, columns=('Input', 'Input Language', 'Output', 'Output Language'), show='headings')
    tabela.heading('Input', text='Input')
    tabela.heading('Input Language', text='Input Language')
    tabela.heading('Output', text='Output')
    tabela.heading('Output Language', text='Output Language')

    tabela.column('Input', width=200, anchor="center")
    tabela.column('Input Language', width=200, anchor="center")
    tabela.column('Output', width=200, anchor="center")
    tabela.column('Output Language', width=200, anchor="center")

    with open('traducoes.txt', mode='r', newline='', encoding='UTF-8') as arquivo:
        for linha in arquivo:
            linha = linha.strip().split('|')
            tabela.insert('', 'end', values=(linha[0], linha[1], linha[2], linha[3]))

    tabela.pack(fill='both', expand='yes', padx=10, pady=10)

    button_close_history = ttk.Button(history_frame, text='Close History', command=lambda: history_window.destroy())
    button_close_history.pack(fill='both', padx=10, pady=10)

    button_delete_translation = ttk.Button(history_frame, text='Delete Translation', command=lambda: delete_translation(tabela))
    button_delete_translation.pack(fill='both', padx=10, pady=10)

    button_edit_translation = ttk.Button(history_frame, text='Edit Translation', command=lambda: edit_translation(tabela, history_window))
    button_edit_translation.pack(fill='both', padx=10, pady=10)

language_list = ['pt', 'es', 'en', 'fr', 'de', 'it', 'ru', 'ja', 'ko', 'ar', 'hi']

# Input
frame_input = ttk.Frame(global_frame)

label_input = ttk.Label(
    frame_input,
    text='Input:',
    font=(None, 10)
)

combo_input = ttk.Combobox(
    frame_input,
    values=language_list,
    font=(None, 10),
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

# Output
frame_output = ttk.Frame(global_frame)

label_output = ttk.Label(
    frame_output,
    text='Output:',
    font=(None, 10),
)

combo_output = ttk.Combobox(
    frame_output,
    values=language_list,
    font=(None, 10),
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

button_translate = ttk.Button(
    global_frame,
    text='Translate!',
    command=translate
)
button_translate.pack(fill='both', padx=10, pady=10)

button_history = ttk.Button(
    global_frame,
    text='History',
    command=history
)
button_history.pack(fill='both', padx=10, pady=10)

window.bind('<Return>', translate)

window.mainloop()