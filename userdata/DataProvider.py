import json
import allure

my_data = open('user_data.json')
global_data = json.load(my_data)


class DataProvider:

    def __init__(self) -> None:
        self.data = global_data

    @allure.step('Выборка UI пользовательских данных')
    def getUI(self, prop: str) -> str:
        ui = self.data.get('ui')
        return ui.get(prop)

    @allure.step('Выборка API пользовательских данных')
    def getAPI(self, prop: str) -> str:
        api = self.data.get('api')
        return api.get(prop)

    @allure.step('Выборка UI пользовательских данных с типом число')
    def getUI_int(self, prop: str) -> int:
        ui = self.data.get('ui')
        return int(ui.get(prop))

    @allure.step('Выборка API пользовательских данных с типом число')
    def getAPI_int(self, prop: str) -> int:
        api = self.data.get('api')
        return int(api.get(prop))
