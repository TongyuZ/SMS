class Producer:
    def __init__(self, num_message=1000):
        # Initialize the producer with a total number of messages to produce
        self.num_message = num_message

    def get_mes_num(self):
        # Returns the total number of messages the producer will generate
        return self.num_message

    def generate_messages(self):
        # Generate a list of messages
        return ["Message " + str(i + 1) for i in range(self.num_message)]

