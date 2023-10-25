import random
import time

from produce import Producer

class Sender:
    def __init__(self, error_rate, mean_time):
        # Initialize sender with error rate and average time per message
        self.error_rate = error_rate
        self.mean_time = mean_time
        self.messages_to_send_count = 0
        self.taken_time = 0


    def get_err(self):
        # Return the sender's error rate
        return self.error_rate

    def messages_to_send(self, count):
        # Set number of messages for this sender to send and calculate time taken
        self.messages_to_send_count = count
        self.taken_time = random.gauss(self.mean_time, self.mean_time/10)

    def send_messages(self):
        # Simulate sending messages by sleeping for the taken time
        time.sleep(self.taken_time)

    def get_time(self):
        # Return the time taken to send the messages
        self.taken_time = random.gauss(self.mean_time, self.mean_time/10)
        return self.taken_time

    def num_fai(self):
        # Calculate and return number of failed messages based on error rate
        return int(self.messages_to_send_count * self.error_rate)

    def num_suc(self):
        # Calculate and return number of successfully sent messages
        return self.messages_to_send_count - self.num_fai()


class Senders:
    def __init__(self, num_senders, error_rates, mean_time, producer: Producer):
        # Initialize a list of senders with given attributes and associate with a producer
        self.senders = [Sender(error_rates[i], mean_time) for i in range(num_senders)]
        self.num_senders = num_senders
        self.num_messages = producer.get_mes_num()

        # Distribute the messages among the senders
        messages_per_sender = self.distri_mes()
        for sender in self.senders:
            sender.messages_to_send(messages_per_sender)

    def get_sen_num(self):
        # Return number of senders
        return self.num_senders

    def mes_total(self):
        # Return total number of messages across all senders
        return self.num_messages

    def distri_mes(self):
        # Distribute messages evenly among all senders
        return self.mes_total() / self.get_sen_num()