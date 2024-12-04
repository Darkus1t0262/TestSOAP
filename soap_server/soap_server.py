from spyne import Application, ServiceBase, rpc, String
from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication
from flask import Flask, Response, request

# Define the SOAP service
class HolaMundoService(ServiceBase):
    @rpc(_returns=String)
    def saludar(ctx):
        return "¡Hola Mundo desde SOAP en Python!"

# Create a Spyne application
soap_app = Application(
    [HolaMundoService],
    tns="spyne.examples.helloworld",
    in_protocol=Soap11(validator="lxml"),
    out_protocol=Soap11(),
)

# Create a WSGI application for Spyne
soap_application = WsgiApplication(soap_app)

# Initialize Flask app
app = Flask(__name__)

# Define a route for SOAP requests
@app.route("/soap", methods=["POST"])
def soap():
    # Capture the WSGI response from Spyne
    environ = request.environ
    headers_set = []
    headers_sent = []

    def start_response(status, headers, exc_info=None):
        headers_set[:] = [status, headers]
        return headers_sent.append

    response_body = soap_application(environ, start_response)

    # Combine the response headers and body
    status, headers = headers_set
    response = Response(response_body, status=int(status.split(" ")[0]), headers=dict(headers))
    return response

if __name__ == "__main__":
    app.run(debug=True)
