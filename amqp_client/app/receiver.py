from proton import Message
from proton.handlers import MessagingHandler
from proton.reactor import Container
from proton import SSLDomain

import os


Path_cert = "./certs/client_certificate.crt"
Path_key = "./certs/private_key.key"
Path_ca = "./certs/root_CA_certificate.crt"



class Receiver(MessagingHandler):

    """
    AMQP receiver client for C-ITS Broker Austria connecting to the topic croads with SSL/TLS authentication.
    
    """
        
    def __init__(self, url, address):
        super().__init__()
        self.url = url
        self.address = address

    def on_start(self, event):

        ssl = SSLDomain(SSLDomain.MODE_CLIENT)
        ssl.set_credentials(Path_cert, Path_key, None)
        ssl.set_trusted_ca_db(Path_ca)
        ssl.set_peer_authentication(SSLDomain.VERIFY_PEER_NAME)
        
        self.conn = event.container.connect(
            self.url,
            ssl_domain = ssl,
        )

        event.container.create_receiver(self.conn, self.address)
        print(f"Connected to {self.url}, listening on {self.address}")

    def on_connection_opened(self, event):
        print("Connection opened successfully!")

    def on_session_opened(self, event):
        print("Session opened successfully!")

    def on_link_opened(self, event):
        print("Link opened successfully! Ready to receive messages.")

    def on_message(self, event):
        print(f"Received message: ")
        for property, value in event.message.properties.items():
            print(f"{property}: {value}")
        print(bytes(event.message.body).hex())


    def on_transport_error(self, event):
        print("Transport/connection error!")
        print(event.connection)
        print(event.TRANSPORT_ERROR)
        print(event.transport.condition)

    def on_connection_closed(self, event):
        print("Connection closed")
        if event.connection and event.connection.remote_condition:
            print(f"Remote condition: {event.connection.remote_condition}")



if __name__ == "__main__":

    listener = Receiver(
        url="amqps://amqp.croads-broker.at:5671",
        address="croads"
    )

    try:
        Container(listener).run()
    except KeyboardInterrupt:
        print("Stopping connection...")
        listener.conn.close()
        Container(listener).stop()
        print("Stopped connection")