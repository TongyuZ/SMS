import time
import threading
import math

from send import Senders, Sender


class Monitor:
    def __init__(self, senders: Senders, update_interval):
        # Initialize the monitor with a list of sender objects and an update interval
        self.senders = senders.senders
        self.num_mes = senders.mes_total()  # Total number of messages to be sent
        self.update_interval = update_interval  # Frequency of updating the display progress

    def start_senders(self):
        # Start each sender as a separate thread
        sender_threads = []

        for sender in self.senders:
            t = threading.Thread(target=self._send_messages, args=(sender,))
            t.start()
            sender_threads.append(t)

        # Wait for all sender threads to finish
        for t in sender_threads:
            t.join()

    def _send_messages(self, sender: Sender):
        # Trigger sending of messages for a sender
        sender.send_messages()

    def display_progress(self):
        # Display the progress of messages sent by all senders
        total_sent = 0
        total_failed = 0

        while True:
            # Calculate successes and failures for all senders based on update_interval
            successes = [sender.num_suc() / sender.get_time() * self.update_interval for sender in self.senders]
            failures = [sender.num_fai() / sender.get_time() * self.update_interval for sender in self.senders]

            # Update total sent and total failed messages
            total_sent += math.floor(sum(successes))
            total_failed += math.floor(sum(failures))

            # Calculate average time taken per message sent
            ave_time = self.update_interval / total_sent if total_sent != 0 else 0

            # Check if all messages are sent
            if total_sent + total_failed >= self.num_mes:
                if total_failed > 0:
                    print("All done but we need to deal with failed ones.")
                    break
                else:
                    print("All messages successfully sent!")
                    break

            # Print the results
            print(f"Messages Sent: {total_sent}")
            print(f"Messages Failed: {total_failed}")
            print(f"Average Time Taken Per Message: {ave_time:.4f}")

            # Pause before the next update
            time.sleep(self.update_interval)
