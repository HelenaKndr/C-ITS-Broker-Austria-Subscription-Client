# C-ITS Broker Austria AMQP Subscription Client with Apache Qpid Proton

This client allows subscription to the C-ITS Broker Austria using Apache Qpid Proton. 

## Prerequesites
- Apache Qpid Proton: 
```bash
pip install python-qpid-proton
```
- C-ITS Broker Austria Certificates: Certficates can be requrested via c-itsbrokerat@austriatech.at

## Certificate Setup
You need three certificate files from AustriaTech:

1. Your client certificate
2. Your private key
3. The CA root certificate

Place all 3 certificate files in the `certs/` directory and update the paths in `receiver.py`.

## Running the docker file
Start docker compose with the command 

 ```
 docker compose up -d --build
 ```

## Expected output
 ```
Connected to amqps://amqp.croads-broker.at:5671, listening on croads
Connection opened successfully!
Session opened successfully!
Link opened successfully! Ready to receive messages.
Received message:
```

## Work in Progress:

Running locally with
```bash
   python main.py
```
