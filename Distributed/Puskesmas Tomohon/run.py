#!/usr/bin/env python3

#from apscheduler.schedulers.background import BackgroundScheduler
# Import Flask Instance
from flask import Flask, request, jsonify, abort
from flask_restful import Api, Resource
from flask_cors import CORS

# Import Medical Chain Instance
import Token
import Blockchain
import Data
from experiment.keyTest import Cryp

"""
@app.before_request
def limit_remote_addr():
	if request.remote_
# Every 5 seconds check if token is still valid or not
def sensor():
    print("Scheduler is alive!")

sched = BackgroundScheduler(daemon=True)
sched.add_job(sensor,'interval',seconds=30)
sched.start()
"""

app = Flask(__name__)
api = Api(app)

CORS(app)
cors = CORS(app, resources = {r"/*" : { "origin" : "*" }})

components = [Token, Blockchain, Data]

for component in components:
    print(component.register(api))
    #component.register(api)

# Crypto Test
api.add_resource(Cryp, "/crypto/<string:id>")
"""
@app.route('/generate')
def hello():
    medChain.addBlock(Block(1, "data"))
    print(medChain.chain)
    return medChain.getLatestBlock().hash

@app.route('/chain')
def chain():
    return str(medChain.chain)"""

if __name__ == "__main__":
   app.run(debug=True)