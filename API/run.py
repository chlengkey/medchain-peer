from apscheduler.schedulers.background import BackgroundScheduler
from flask import Flask, request, jsonify, abort
from flask_restful import Api, Resource
from flask_cors import CORS
from blockchain import Blockchain, Block
from controller.token import Token, Generator
from experiment.keyTest import Cryp

#@app.before_request
#def limit_remote_addr():
#	if request.remote_
# Every 5 seconds check if token is still valid or not
#def sensor():
#    """ Function for test purposes. """
#    print("Scheduler is alive!")

#sched = BackgroundScheduler(daemon=True)
#sched.add_job(sensor,'interval',seconds=30)
#sched.start()

app = Flask(__name__)
api = Api(app)
medChain = Blockchain()

CORS(app)
cors = CORS(app, resources = {r"/*" : { "origin" : "*" }})

# Tokenization
api.add_resource(Token, "/token/check/<string:id>", endpoint="tokenGetter");
api.add_resource(Generator, "/token/generate", endpoint="tokenGenerate");

# Crypto Test
api.add_resource(Cryp, "/crypto/<string:id>")

@app.route('/generate')
def hello():
    medChain.addBlock(Block(1, "data"))
    print(medChain.chain)
    return medChain.getLatestBlock().hash

@app.route('/chain')
def chain():
    return str(medChain.chain)

if __name__ == "__main__":
   app.run(debug=True, host="0.0.0.0")