// Import
const NodeRSA = require('node-rsa');
export const VUE_APP_API = "http://127.0.0.1:5000"

export class crypto {

  constructor(privateKey="", publicKey=""){
  	if(privateKey == "" && publicKey == ""){
  		this.private = localStorage.getItem('private');
    	this.public  = localStorage.getItem('public');
  	}
    this.cryptoFunc = new NodeRSA(this.private);
  }

  getPublic(){
  	return this.public;
  }
  
  encrypt(msg){
  	console.log(this.public);
  	return this.cryptoFunc.encrypt(msg, 'base64');
  }

  decrypt(msg){
  	return this.cryptoFunc.decrypt(msg, 'utf-8');
  }

  encryptPrivateKey(){
  	const app = this;
  	return this.encrypt(app.private);
  }

  encryptUsingPublicKey(publicKey, msg){
  	const cryptoInstance = new NodeRSA(publicKey);
  	return cryptoInstance.encrypt(msg, 'base64');
  }

  encryptPrivateKeyUsingPublic(publicKey){
  	const cryptoInstance = new NodeRSA(publicKey);
  	return cryptoInstance.encrypt(this.private, 'base64');
  }
  
}