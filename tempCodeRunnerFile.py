    def display(self):
        while True:
        if self.view == 'list':
            self.show_list()
        elif self.view == 'info':
            self.show_info()
        elif self.view == 'add':
            print()
            self.add_contact()
        elif self.view == 'quit':
            print('\nClosing the contact list...\n')
            break