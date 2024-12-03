# TestSOAP

This project demonstrates a basic SOAP web service built with **Flask** and **Spyne**. The service exposes a single operation, `saludar`, which returns a greeting in Spanish: "¡Hola Mundo desde SOAP en Python!".

## Prerequisites

Before starting, ensure you have the following installed:

- Python 3.7 or higher
- pip (Python package manager)

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/Darkus1t0262/TestSOAP
   cd your-repo 
2. Install the required dependencies:
   ```bash
   pip freeze > requirements.txt
3. Run the service:
   ```bash
   python soap_server.py
## SOAP Endpoint and Testing on Postman
The SOAP endpoint is available at:
http://127.0.0.1:5000/soap
1. Create a New Request
2. Open Postman and click New Request.
3. Set the request method to POST.
4. Enter the URL: http://127.0.0.1:5000/soap.
5. Go to the Body tab.
6. Select raw as the input type.
7. Choose XML from the dropdown (next to the Text label).
8. Paste the following SOAP request:
<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:spy="spyne.examples.helloworld">
   <soapenv:Header/>
   <soapenv:Body>
      <spy:saludar/>
   </soapenv:Body>
</soapenv:Envelope>
9.Go to the Headers tab.
10. Add the following header:
Key: Content-Type
Value: text/xml
11. Click the Send button.






