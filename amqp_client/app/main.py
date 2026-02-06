from receiver import Receiver
from shutdownlistener import GracefulKiller
from proton.reactor import Container


def main():
    listener = Receiver(
        url="amqps://amqp.croads-broker.at:5671",
        address="croads"
    )

    container = Container(listener)

    gracefullKiller = GracefulKiller()
    listeningClient = Container(listener)


    try:
        container.run()
    except KeyboardInterrupt:
        print("\n\nStopping connection...")
        if listener.conn:
            listener.conn.close()
        container.stop()
        print("Stopped connection")

if __name__ == "__main__":
    main()