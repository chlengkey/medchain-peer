from apscheduler.schedulers.background import BackgroundScheduler
from flask import Flask
from blockchain import Blockchain, Block

def sensor():
    """ Function for test purposes. """
    print("Scheduler is alive!")

sched = BackgroundScheduler(daemon=True)
sched.add_job(sensor,'interval',seconds=30)
sched.start()

app = Flask(__name__)
medChain = Blockchain()


@app.route('/generate')
def hello():
    medChain.addBlock(Block(1, "data"))
    print(medChain.chain)
    return medChain.getLatestBlock().hash

@app.route('/chain')
def chain():
    return str(medChain.chain)

if __name__ == '__main__':
    app.run(host="0.0.0.0")
