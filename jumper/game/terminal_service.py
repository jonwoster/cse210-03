class Terminal_service:
    
    # This class is used to get input from the users and output messages to the user

    def read_letter(self, prompt):
        # This method receives a prompt as an argument and shows that to the user to get input
        # it then returns the input from the user
        return input(prompt)
        
    def write_text(self, text):
        # This method receives text as an argument and shows that to the user
        # Returns nothing.
        print(text)
