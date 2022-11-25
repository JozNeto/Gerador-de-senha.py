from os import system, name
from PySimpleGUI import PySimpleGUI as sg
from password_gen import PasswordGenerator


def clear() -> None:
    system('cls' if name == 'nt' else 'clear')


def main() -> None:
    sg.theme('Reddit')
    sg.set_options(font=("Roboto", 12))
    layout = [
        [sg.Text('Password Generator')],
        [sg.Text('Password letters amount')], [sg.Input(key='letters')],
        [sg.Text('Password upper letters amount')], [sg.Input(key='upper_letters')],
        [sg.Text('Password symbols amount')], [sg.Input(key='symbols')],
        [sg.Text('Password numbers amount')], [sg.Input(key='numbers')],
        [sg.Text('Password name for saving')], [sg.Input(key='password_name')],
        [sg.Checkbox('Save password', key='save_password')],
        [sg.Button('Generate Password'), sg.Button('Exit')],
        [sg.Text('Generated password:')], [sg.Input(key='password')]
    ]
    window = sg.Window('Password Generator', layout)
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Exit':
            break
        elif event == 'Exit':
            break
        elif event == 'Generate Password':
            try:
                values['letters'] = int(values['letters']) if values['letters'] != '' else 0
                values['upper_letters'] = int(values['upper_letters']) if values['upper_letters'] != '' else 0
                values['symbols'] = int(values['symbols']) if values['symbols'] != '' else 0
                values['numbers'] = int(values['numbers']) if values['numbers'] != '' else 0
            except ValueError:
                sg.popup('Please, enter a number')
                continue
            values['password_name'] = values['password_name'] if values['password_name'] != '' else "My password"
            pg = PasswordGenerator(values['password_name'], values['letters'], values['upper_letters'], values['symbols'], values['numbers'])
            pg.generate_password()
            if values['save_password']:
                pg.save_password()
            window['password'].update(f"{pg.password}")
            window.refresh()


if __name__ == '__main__':
    main()