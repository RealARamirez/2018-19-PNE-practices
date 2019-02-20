from server_proccessor import command_proccessor

class request:
    def __init__(self, command):
        self.command = command

    def request_list(self):
        content = self.command
        content_list = content.splitlines()
        for i in range(0, len(content_list)-1):
            content_list[i] = content_list[i].strip(" ")
        return content_list

    # We need to check if the user is asking it to be alive or for doing calculations
    def alive_checker(self):
        seq = self.request_list()[0]
        if seq == "":
            return "ALIVE"
        else:
            return True

    # We need to check if the sequence is valid
    def seq_checker(self):
        seq = self.request_list()[0]
        for b in seq:
            if b == "A" or b == "T" or b == "G" or b == "C":
                Answer = "OK"
            else:
                Answer = "ERROR"
                break
        return Answer

    # Main program, using the method defined in server_processor, this method will process and give the solution
    def main_function(self):
        seq = self.request_list()[0]
        command_list = self.request_list()[1:]
        solution = "\n"
        for elem in command_list:
            solution.join(command_proccessor(seq, elem))
        return solution


