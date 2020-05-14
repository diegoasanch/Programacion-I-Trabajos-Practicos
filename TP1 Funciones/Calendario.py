from fechas import armarCalendario, mesSiguiente, suma_dias, diadelasemana
from time import localtime, strftime
from tkinter import Tk, Label, Button, Entry, END, Frame, IntVar, Radiobutton, ttk
from random import randint

class SetMode:
    '''
    Set the current color theme for the whole window
    available modes: Light (tkinter default), Dark blue
    '''

    def tab_set(self):
        '''
        Sets all tabs
        '''
        for tab in TABS:
            tab.configure(background=self.bg_style)

    def label_set(self):
        '''
        Sets all labels
        '''
        for label in LABELS:
            label.configure(bg=self.bg_style, fg=self.fg_style, activebackground=self.btn_style)

    def button_set(self):
        '''
        Sets all buttons
        '''
        for button in BUTTONS:
            button.configure(bg=self.btn_style, fg=self.btn_text, activebackground=self.btn_style)

    def output_set(self):
        '''
        Sets all output boxes
        '''

        for box in OUTPUT_BOXES:
            box.configure(bg=self.out_bg, fg=self.out_fg)

    def dark(self, event=None):
        '''
        Updates the init values and changes the
        window color mode to a dark color scheme
        '''

        # Palette from https://colorhunt.co/palette/25729

        dark_bg = '#222831'
        dark_fg = '#00fff5'
        dark_btn = '#00adb5'
        dark_btn_txt = '#222831'
        dark_out = '#393e46'
        dark_out_txt = 'white'

        self.bg_style = dark_bg
        self.fg_style = dark_fg
        self.btn_style = dark_btn
        self.btn_text = dark_btn_txt
        self.out_bg = dark_out
        self.out_fg = dark_out_txt

        self.update()

    def light(self, event=None):
        '''
        Updates the init values and changes the
        window color mode to a light color scheme
        '''

        light_bg = 'SystemButtonFace'
        light_fg = 'black'
        light_btn = 'SystemButtonFace'
        light_btn_txt = 'black'
        light_out = 'white'
        light_out_txt = 'black'

        self.bg_style = light_bg
        self.fg_style = light_fg
        self.btn_style = light_btn
        self.btn_text = light_btn_txt
        self.out_bg = light_out
        self.out_fg = light_out_txt

        self.update()

    def update(self):
        '''
        applies the init color values to the tabs,
        labels, buttons and output boxes
        '''
        self.tab_set()
        self.label_set()
        self.button_set()
        self.output_set()

class Calendar:
    'Manager of the calendar_display unit'

    def __init__(self):
        'starts with current date'

        self.get_date()

    def get_date(self, time_format="%m %Y"):
        '''
        Get current time using time.localtime method, default
        time format = "month, year" accepts other format
        as a str separated by spaces
        '''

        time_now = localtime()
        self.month, self.year = strftime(time_format, time_now).split()

    def update(self, event=None):
        'Updates the calendar display to the entered date'

        self.month = int(mes_entry.get())
        self.year = int(anio_entry.get())

        calendar_text = armarCalendario(self.month, self.year)
        calendar_display.configure(text=calendar_text)

    def prev_month(self, event=None):
        'Turns calendar one month before'

        self.next_month(mov=-1)

    def next_month(self, event=None, mov=1):
        'Turns calendar to one month after the one currently displaying'

        self.month = int(mes_entry.get())
        self.year = int(anio_entry.get())

        self.month, self.year = mesSiguiente(self.month, self.year, mov)

        mes_entry.delete(0,END)
        anio_entry.delete(0,END)
        
        mes_entry.insert(0, str(self.month))
        anio_entry.insert(0, str(self.year))

        self.update()

    def today(self, event=None):
        'Sets calendar to current day/month'

        self.get_date()

        mes_entry.delete(0,END)
        anio_entry.delete(0,END)

        mes_entry.insert(0,self.month)
        anio_entry.insert(0,self.year)

        self.update()
        
class SumaDias:

    def get_date(self, time_format="%d %m %Y"):
        '''
        Get current time using time.localtime method, default
        time format = "month, year" accepts other format
        as a str separated by spaces
        '''

        time_now = localtime()
        self.day, self.month, self.year = strftime(time_format, time_now).split()

    def today(self, event=None):
        'Sets calendar to current day/month'

        self.get_date()

        sum_dia_entry.delete(0,END)
        sum_mes_entry.delete(0,END)
        sum_anio_entry.delete(0,END)
        sum_sumdias_entry.delete(0,END)

        sum_dia_entry.insert(0,self.day)
        sum_mes_entry.insert(0,self.month)
        sum_anio_entry.insert(0,self.year)

        self.make_sum()



    def make_sum(self, event=None):

        self.day = int(sum_dia_entry.get())
        self.month = int(sum_mes_entry.get())
        self.year = int(sum_anio_entry.get())

        try:
            self.to_sum = int(sum_sumdias_entry.get())
        except:
            self.to_sum = 0

        new_d, new_m, new_y = suma_dias(self.day, self.month, self.year, self.to_sum)
        
        weekday = diadelasemana(new_d, new_m, new_y)
        days = ['sunday', 'monday', 'tuesday','wednesday', 'thursday', 'friday', 'saturday']
        
        new_date = f'{days[weekday]},   {new_d} / {new_m} / {new_y}'
        
        new_date_output.configure(text=new_date)




# - Main

window = Tk()
window.title('Calendario')
window.geometry('500x480')

TAB_CONTROL = ttk.Notebook(window)
TAB_CALENDAR = Frame(window)
TAB_SUMADIAS = Frame(window)
TAB_DIASENTRE = Frame(window)

TAB_CONTROL.add(TAB_CALENDAR, text='Calendar')
TAB_CONTROL.add(TAB_SUMADIAS, text='Suma Dias')
TAB_CONTROL.add(TAB_DIASENTRE, text='Dias Entre')

TAB_CONTROL.pack(expand=1, fill='both')

# -- Init

mode = SetMode()
calendar = Calendar()
suma = SumaDias()

# Calendar tab ------------------

CAL_HEADER = Label(TAB_CALENDAR, text='Calendario', font='none 20')
CAL_HEADER.grid(column=0, row=0, pady=5)

dark_btn_state = IntVar()
dark_btn_state.set(0)

dark_mode_btn = Radiobutton(TAB_CALENDAR, text='Dark Mode', value=1, command=mode.dark, var=dark_btn_state)
dark_mode_btn.grid(column=0, row=0, sticky='NE')

light_mode_btn = Radiobutton(TAB_CALENDAR, text='Light Mode', value=0, command=mode.light, var=dark_btn_state)
light_mode_btn.grid(column=0, row=0, sticky='SE')

# Entry

cal_entry_bar = Frame(TAB_CALENDAR)
cal_entry_bar.grid(column=0, row=1)

MES_LBL = Label(cal_entry_bar, text='Mes:')
MES_LBL.grid(column=0, row=0, padx=5)

mes_entry = Entry(cal_entry_bar, width=3, font='none 10 bold')
mes_entry.grid(column=1, row=0, pady=4)

ANIO_LBL = Label(cal_entry_bar, text='Año:')
ANIO_LBL.grid(column=2, row=0, padx=5)

anio_entry = Entry(cal_entry_bar, width=5, font='none 10 bold')
anio_entry.grid(column=3, row=0, padx=5)

filler = Label(cal_entry_bar, text='    ')
filler.grid(column=0, row=1)

# -- Buttons

GO_BTN = Button(cal_entry_bar, text='GO', command=calendar.update)
GO_BTN.grid(column=4, row=0, padx=5)

TODAY_BTN = Button(cal_entry_bar, text='Today', command=calendar.today)
TODAY_BTN.grid(column=1, row=1, pady=4, padx=20)

PREV_BTN = Button(cal_entry_bar, text='<', width=3, command=calendar.prev_month)
PREV_BTN.grid(column=2, row=1)

NEXT_BTN = Button(cal_entry_bar, text='>', width=3, command=calendar.next_month)
NEXT_BTN.grid(column=3, row=1)

# -- Calendar Display

calendar_display = Label(TAB_CALENDAR, text='', font='consolas 11' , width=56, height=17, relief='groove')
calendar_display.grid(column=0, row=2, padx=20, pady=17)


# Suma dias tab ------------------

SUM_HEADER = Label(TAB_SUMADIAS, text='Suma Dias', font='none 20')
SUM_HEADER.grid(column=0, row=0, pady=5, padx=170)

sum_entry_bar = Frame(TAB_SUMADIAS)
sum_entry_bar.grid(column=0, row=1, padx=50, pady=50)

S_FECHA_LBL = Label(sum_entry_bar, text='Fecha:', font='none 12')
S_FECHA_LBL.grid(column=0, row=0, padx=10)

S_DAY_LBL = Label(sum_entry_bar, text='Dia:')
S_DAY_LBL.grid(column=1, row=0)

sum_dia_entry = Entry(sum_entry_bar, width=3, font='none 10 bold')
sum_dia_entry.grid(column=2, row=0, pady=4)

S_MES_LBL = Label(sum_entry_bar, text='Mes:')
S_MES_LBL.grid(column=3, row=0, padx=5)

sum_mes_entry = Entry(sum_entry_bar, width=3, font='none 10 bold')
sum_mes_entry.grid(column=4, row=0, pady=4)

S_ANIO_LBL = Label(sum_entry_bar, text='Año:')
S_ANIO_LBL.grid(column=5, row=0, padx=5)

sum_anio_entry = Entry(sum_entry_bar, width=5, font='none 10 bold')
sum_anio_entry.grid(column=6, row=0, padx=5)

S_DASUMAR_LBL = Label(sum_entry_bar, text='A sumar:', font='none 12')
S_DASUMAR_LBL.grid(column=0, row=1, padx=10)

S_SDAY_LBL = Label(sum_entry_bar, text='Dias:')
S_SDAY_LBL.grid(column=1, row=1)

sum_sumdias_entry = Entry(sum_entry_bar, width=3, font='none 10 bold')
sum_sumdias_entry.grid(column=2, row=1, padx=5)
sum_sumdias_entry.focus()
sum_sumdias_entry.insert(0,'0')

SUM_BTN = Button(sum_entry_bar, text='GO',width=5, command=suma.make_sum)
SUM_BTN.grid(column=3, row=1, padx=20)

sum_output = Frame(TAB_SUMADIAS)
sum_output.grid(column=0, row=2)

NEW_DATE_LBL = Label(sum_output, text='New date:', font='none 15')
NEW_DATE_LBL.grid(column=0, row=0, pady=30, padx=20, sticky='W')

new_date_output = Label(sum_output, text='dd/mm/aaaa', font='none 15')
new_date_output.grid(column=1, row=0)

SUM_TODAY_BTN = Button(sum_entry_bar, text='Today', width=5, command=suma.today)
SUM_TODAY_BTN.grid(column=4, row=1)


# Startup

TABS = [window, cal_entry_bar, TAB_CALENDAR, TAB_DIASENTRE, TAB_SUMADIAS, sum_output, sum_entry_bar]
LABELS = [CAL_HEADER, MES_LBL, ANIO_LBL, dark_mode_btn, light_mode_btn, filler, S_FECHA_LBL, S_DAY_LBL, S_MES_LBL, S_ANIO_LBL,S_SDAY_LBL, S_DASUMAR_LBL, NEW_DATE_LBL, SUM_HEADER]
BUTTONS = [GO_BTN, PREV_BTN, NEXT_BTN, TODAY_BTN, SUM_BTN, SUM_TODAY_BTN]
OUTPUT_BOXES = [calendar_display, mes_entry, anio_entry, new_date_output, sum_dia_entry, sum_mes_entry, sum_anio_entry, sum_sumdias_entry]

mode.light()
calendar.today()
suma.today()

# Binded commands

window.bind('<Return>', calendar.update)
window.bind('<Left>', calendar.prev_month)
window.bind('<Right>', calendar.next_month)
window.bind('<t>', calendar.today)
window.bind('<Control-,>', mode.dark)
window.bind("<Control-.>", mode.light)

window.mainloop()
