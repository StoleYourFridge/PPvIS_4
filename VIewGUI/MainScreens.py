from kivy.app import App
from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivymd.app import MDApp
from kivymd.uix.datatables import MDDataTable
from Model.BankComponents.BanknotesStorage import BANKNOTES_DENOMINATIONS


class DenominationInputComponent(BoxLayout):
    def get_input_data(self):
        return [self.ids.first_input.text,
                self.ids.second_input.text,
                self.ids.third_input.text,
                self.ids.forth_input.text,
                self.ids.fifth_input.text,
                self.ids.sixth_input.text,
                self.ids.seventh_input.text,
                self.ids.eighth_input.text]

    def clear_input_data(self):
        self.ids.first_input.text = ""
        self.ids.second_input.text = ""
        self.ids.third_input.text = ""
        self.ids.forth_input.text = ""
        self.ids.fifth_input.text = ""
        self.ids.sixth_input.text = ""
        self.ids.seventh_input.text = ""
        self.ids.eighth_input.text = ""


class StartScreen(Screen):
    def on_add_new_user_press(self):
        self.manager.current = "AddNewUserScreen"

    def on_work_with_existing_users_press(self):
        self.manager.current = "ChooseEntityScreen"


class AddNewUserScreen(Screen):
    banknotes_denominations = [str(denomination) for denomination in BANKNOTES_DENOMINATIONS]

    def on_back_press(self):
        self.clear_info()
        self.manager.current = "StartScreen"

    def on_apply_information_press(self):
        self.ids.dialog_window.text = self.manager.controller.add_user_account_entity_validated(
                                                                  self.ids.name_input.text,
                                                                  self.ids.bank_storage_input.get_input_data(),
                                                                  self.ids.user_storage_input.get_input_data(),
                                                                  self.ids.bank_bill_input.text,
                                                                  self.ids.user_phone_bill_input.text,
                                                                  self.ids.card_password_input.text)

    def clear_info(self):
        self.ids.name_input.text = ""
        self.ids.bank_bill_input.text = ""
        self.ids.user_phone_bill_input.text = ""
        self.ids.card_password_input.text = ""
        self.ids.dialog_window.text = "DialogWindow"
        self.ids.bank_storage_input.clear_input_data()
        self.ids.user_storage_input.clear_input_data()


class PasswordCheckerScreen(Screen):
    def refresh_attempts_amount(self):
        self.ids.attempts_amount.text = "Attempts remain: " + str(self.manager.controlle.get_amount_of_attempts())

    def clear_input(self):
        self.ids.password_input.text = ""

    def clear_dialog_window(self):
        self.ids.dialog_window.text = "Dialog Window"

    def refresh_buttons_state(self):
        if self.ids.dialog_window.text == "Blocked":
            self.ids.apply_button.disabled = True
            self.ids.bank_call_button.disabled = True
        elif self.manager.controller.get_amount_of_attempts() == 0:
            self.ids.apply_button.disabled = True
            self.ids.bank_call_button.disabled = False
        else:
            self.ids.apply_button.disabled = False
            self.ids.bank_call_button.disabled = True

    def start_working_call(self):
        self.refresh_attempts_amount()
        self.clear_input()
        self.clear_dialog_window()
        self.refresh_buttons_state()

    def on_apply_password_press(self):
        answer = self.manager.controller.password_checker(self.ids.password_input.text)
        if answer == "Correct":
            self.manager.current = "ActionDecisionScreen"
        elif answer == "Blocked":
            self.ids.dialog_window.text = "Blocked"
            self.refresh_buttons_state()
            self.clear_input()
        else:
            self.ids.dialog_window.text = answer
            self.refresh_attempts_amount()
            self.clear_input()
            self.refresh_buttons_state()

    def on_bank_call_press(self):
        self.manager.controller.bank_call()
        self.refresh_attempts_amount()
        self.refresh_buttons_state()

    def on_back_press(self):
        self.manager.current = "ChooseEntityScreen"


class MainScreensApp(App):
    def build(self):
        return PasswordCheckerScreen()


if __name__ == "__main__":
    test_app = MainScreensApp()
    test_app.run()
