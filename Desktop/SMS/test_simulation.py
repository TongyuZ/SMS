import unittest
from unittest.mock import patch, Mock
from produce import Producer
from send import Sender, Senders
from monitor import Monitor


# Unit tests for the Producer class
class TestProducer(unittest.TestCase):

    # Validate that a default Producer instance generates 1000 messages
    def test_default_num_messages(self):
        producer = Producer()  # Instantiate the Producer class
        # Check if the number of messages is the default 1000
        self.assertEqual(producer.get_mes_num(), 1000)  

    # Ensure that the Producer generates the correct sequence of messages
    def test_generate_messages(self):
        producer = Producer(num_message=5)  # Instantiate Producer with 5 messages
        # Check if the messages generated match the expected sequence
        self.assertEqual(producer.generate_messages(), ["Message 1", "Message 2", "Message 3", "Message 4", "Message 5"])

# Unit tests for the Sender class
class TestSender(unittest.TestCase):

    # Set up context for the tests in this class
    def setUp(self):
        # Create a sender instance with specified error rate and mean time
        self.sender = Sender(error_rate=0.1, mean_time=10)

    # Check if messages are being sent with the designated error rate
    def test_sender_errors(self):
        self.sender.messages_to_send(10)
        # Assert that 1 message fails and 9 pass
        self.assertEqual(self.sender.num_fai(), 1) 
        self.assertEqual(self.sender.num_suc(), 9)

    # Ensure that the time taken for sending messages is within the expected range
    def test_sender_time(self):
        # Assert time is within the range of 7 to 13 units
        self.assertTrue(7 <= self.sender.get_time() <= 13)  

# Unit tests for the Senders class (a collection of individual Sender objects)
class TestSenders(unittest.TestCase):

    # Set up context for the tests in this class
    def setUp(self):
        # Create a producer instance with 100 messages
        self.producer = Producer(num_message=100)
        # Create a Senders instance with 10 individual senders
        self.senders = Senders(num_senders=10, error_rates=[0.1]*10, mean_time=2, producer=self.producer)

    # Ensure that the Senders object correctly initializes with the given number of senders
    def test_initialization(self):
        # Assert that there are 10 senders in the Senders instance
        self.assertEqual(len(self.senders.senders), 10)

    # Validate that messages are evenly distributed among all senders
    def test_message_distribution(self):
        # Get number of messages assigned to each sender
        messages_per_sender = self.senders.distri_mes()
        # Assert each sender receives 10 messages
        self.assertEqual(messages_per_sender, 10) 

# Unit tests for the Monitor class
class TestMonitor(unittest.TestCase):

    # Set up context for the tests in this class
    def setUp(self):
        # Set up a producer with 100 messages
        self.producer = Producer(num_message=100)
        # Set up Senders with 10 individual senders
        self.senders = Senders(num_senders=10, error_rates=[0.1] * 10, mean_time=2, producer=self.producer)
        # Create a Monitor instance for the senders with a fast update interval
        self.monitor = Monitor(senders=self.senders, update_interval=0.01)

    # Mock function to simulate sending messages without waiting
    def mock_send_messages(self, sender):
        sender.messages_to_send_count = 0
        sender.taken_time = 0

    # Test the progress display functionality
    @patch('time.sleep', Mock(side_effect=InterruptedError))
    def test_display_progress(self):
        # Ensure that the mocked sleep function raises an exception after one loop
        with self.assertRaises(InterruptedError):
            self.monitor.display_progress()

    # Test if all senders start as expected
    @patch('monitor.Monitor._send_messages')
    def test_start_senders(self, mock_send_messages):
        # Mock actual message sending to speed up tests
        mock_send_messages.side_effect = self.mock_send_messages
        self.monitor.start_senders()
        # Ensure all 10 senders were activated
        self.assertEqual(mock_send_messages.call_count, 10)



if __name__ == "__main__":
    unittest.main()
