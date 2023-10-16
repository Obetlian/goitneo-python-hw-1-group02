class AssistantBot:
    def __init__(self):
        # Словник для зберігання контактів
        self.contacts = {}

    def hello(self):
        return "How can I help you?"

    def add_contact(self, name, phone):
        self.contacts[name] = phone
        return f"Контакт {name} збережено з номером {phone}."

    def find_contact(self, name):
        phone = self.contacts.get(name, None)
        if phone:
            return f"{name}: {phone}"
        else:
            return f"Контакт {name} не знайдено."

    def update_contact(self, name, new_phone):
        if name in self.contacts:
            self.contacts[name] = new_phone
            return f"Номер {name} оновлено до {new_phone}."
        else:
            return f"Контакт {name} не знайдено."

    def list_contacts(self):
        return '\n'.join([f"{name}: {phone}" for name, phone in self.contacts.items()])

    def command_handler(self, command, *args):
        if command == "hello":
            return self.hello()
        elif command == "add" and len(args) == 2:
            return self.add_contact(args[0], args[1])
        elif command == "phone" and len(args) == 1:
            return self.find_contact(args[0])
        elif command == "change" and len(args) == 2:
            return self.update_contact(args[0], args[1])
        elif command == "all":
            return self.list_contacts()
        else:
            return "Невідома команда!"

    def run(self):
        print("Бот-помічник готовий до роботи!")
        while True:
            user_input = input("> ").strip().lower()
            if user_input in ['exit', 'close']:
                print("До побачення!")
                break
            command_parts = user_input.split()
            print(self.command_handler(command_parts[0], *command_parts[1:]))

if __name__ == "__main__":
    bot = AssistantBot()
    bot.run()

