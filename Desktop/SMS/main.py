from produce import Producer
from send import Sender, Senders
from monitor import Monitor

def main():
    # initialize producer, senders, monitor
    producer = Producer(num_message=1000)
    num_senders = 5
    error_rates = [0.05 for _ in range(num_senders)]
    mean_time = 10
    senders = Senders(num_senders, error_rates, mean_time, producer)
    monitor = Monitor(senders, update_interval=1)

    # start sending messages
    monitor.start_senders()

    # monitor the progress
    monitor.display_progress()


if __name__ == "__main__":
    main()
