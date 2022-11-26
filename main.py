from PySimpleGUI import PySimpleGUI as sg
from password_gen import PasswordGenerator


def main() -> None:
    sg.theme('Reddit')
    sg.set_options(font=("Arial", 12))
    layout = [
        [sg.Text('Password penerator')],
        [sg.Text('Password letters amount')], [sg.Input(key='letters',)],
        [sg.Text('Password upper letters amount')], [
            sg.Input(key='upper_letters')],
        [sg.Text('Password symbols amount')], [sg.Input(key='symbols')],
        [sg.Text('Password numbers amount')], [sg.Input(key='numbers')],
        [sg.Text('Chinese characters amount')], [sg.Input(key='chinese')],
        [sg.Text('Password name for saving')], [sg.Input(key='password_name')],
        [sg.Checkbox('Save password', key='save_password')],
        [sg.Button('Generate Password'), sg.Button('Auto generate'), sg.Button('Exit')],
        [sg.Text('Generated password:')], [sg.Text('Password strength: No password generated',
                                                   key='password_strength')], [sg.Input(key='password')]
    ]
    window = sg.Window('Password Generator', layout)
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Exit':
            break
        elif event == 'Generate Password':
            values['letters'] = int(
                values['letters']) if values['letters'] != '' else 0
            values['upper_letters'] = int(
                values['upper_letters']) if values['upper_letters'] != '' else 0
            values['symbols'] = int(
                values['symbols']) if values['symbols'] != '' else 0
            values['numbers'] = int(
                values['numbers']) if values['numbers'] != '' else 0
            values['chinese'] = int(
                values['chinese']) if values['chinese'] != '' else 0
            values['password_name'] = values['password_name'] if values['password_name'] != '' else "My password"
            pg = PasswordGenerator(
                values['password_name'], values['letters'], values['upper_letters'], values['symbols'], values['numbers'])
            pg.generate_password()
            window['password_strength'].update(
                f"Password strength: {pg.get_password_strength()}")
            if values['save_password']:
                try:
                    pg.save_password()
                except Exception as e:
                    sg.popup(f"Error: {e}")
                    continue
            window['password'].update(f"{pg.password}")
            window.refresh()
        elif event == 'Auto generate':
            values['password_name'] = values['password_name'] if values['password_name'] != '' else "My password"
            pg = PasswordGenerator(
                values['password_name'], 5, 5, 5, 5, 5)
            pg.generate_password()
            window['password_strength'].update(
                f"Password strength: {pg.get_password_strength()}")
            if values['save_password']:
                try:
                    pg.save_password()
                except Exception as e:
                    sg.popup(f"Error: {e}")
                    continue
            window['password'].update(f"{pg.password}")
            window.refresh()


if __name__ == '__main__':
    main()
