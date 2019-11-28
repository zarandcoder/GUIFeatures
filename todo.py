import tkinter as tk


class Todo(tk.Tk):
    def __init__(self, tasks=None):
        super().__init__()

        if not tasks:
            self.tasks = []
        else:
            self.tasks = tasks

        self.wm_title('ToDo - Main')
        self.wm_geometry('300x400')

        initial_task = tk.Label(self, text='### Add your items ###', bg='lightgrey', fg='black', pady=10)
        self.tasks.append(initial_task)

        for task in self.tasks:
            task.pack(side=tk.TOP, fill=tk.X)

        self.task_create = tk.Text(self, heigh=3, bg='white', fg='black')

        self.task_create.pack(side=tk.BOTTOM, fill=tk.X)
        self.task_create.focus_set()

        self.bind('<Return>', self.add_task)

        self.colour_schemes = [
            {'bg':'lightgrey', 'fg':'black'},
            {'bg':'grey', 'fg':'white'}
        ]

    def add_task(self, event=None):
        task_text = self.task_create.get(1.0, tk.END).strip()
        if len(task_text) > 0:
            new_task = tk.Label(self, text=task_text, pady=10)
            _, task_style_choice = divmod(len(self.tasks), 2)

            my_scheme_choice = self.colour_schemes[task_style_choice]

            new_task.configure(bg=my_scheme_choice['bg'])
            new_task.configure(fg=my_scheme_choice['fg'])

            new_task.pack(side=tk.TOP, fill=tk.X)

            self.tasks.append(new_task)
        self.task_create.delete(1.0, tk.END)


if __name__ == '__main__':
    todo = Todo()
    todo.mainloop()