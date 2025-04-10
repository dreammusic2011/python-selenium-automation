from pages.base_page import Page


class MainPage(Page):

    def open_main_page(self):
        self.open_url('https://www.target.com/login?client_id=ecom-web-1.0.0&ui_namespace=ui'
                      '-default&back_button_action=browser&keep_me_signed_in=true&kmsi_default=false&actions=create_session_request_username')