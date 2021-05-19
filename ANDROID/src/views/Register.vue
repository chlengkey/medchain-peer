<template>
	<div style="font-family:Inter" class="mt-5">

		<div class="mb-3 px-4">
			<p class="text-xl font-semibold">Formulir Pendaftaran</p>
			<p class="text-xs text-gray-500">Silahkan mengisi data dibawah</p>
		</div>

		<!-- Nama Depan -->
		<ion-item>
			<ion-label position="floating">Nama Depan</ion-label>
			<ion-input @IonInput="pengguna.nama_depan = $event.target.value"></ion-input>
		</ion-item>

		<!-- Nama Belakang -->
		<ion-item>
			<ion-label position="floating">Nama Belakang</ion-label>
			<ion-input @IonInput="pengguna.nama_belakang = $event.target.value"></ion-input>
		</ion-item>

		<div class="px-3 mt-3">
			<ion-button>Daftar</ion-button>
		</div>

	</div>
</template>

<script type="text/javascript">
	
	const NodeRSA = require('node-rsa');
	const axios = require('axios');
	const key = new NodeRSA({b: 512});
	import { crypto } from '@/function.js';

	export default{
		data(){
			return{
				pengguna : {
					nama_depan : "",
					nama_belakang : ""
				}
			}
		},
		created(){
			
			let privates = key.exportKey("pkcs1-private-pem");
			let publics  = key.exportKey("pkcs8-public-pem");
			/*
			const clientDecrypt = new NodeRSA(privates);

			// Key from server
			let public_key = "-----BEGIN PUBLIC KEY-----\nMIICSDANBgkqhkiG9w0BAQEFAAOCAjUAMIICMAKCAicAjL9SFajgiJEPYVHEsoz8\no/oaHeWqOPMPe78wW2zFphUWCWpAPYSOuariz+UFCB2e3aPthq1HCOU6qsWOhseO\ngDIPe5VIXtcHdXnv353pj4anx2cuu+t6pGAEGSODZ1CA0PBJOgEeyYzsaMDmL0Q5\n5OHxjpqI3lE4glzxjxhB45V/og6lJlYEflRCwJfF5S/9CJr+tCSjsEC9u9eVEOJY\ndoXq2Ey14Fy+PKZUFceArlZDvnPZ+Cw7602Gyeu0xjWCxgOBvmY39cNp10mwTG6a\nxGWYcHsnBKzupXeZhP2qXVx0+0kzffIV57ekbbtUQrnpglssANFALipFlW6e1uW1\niKdXOCEfeIY8Fgak0TatqB1qJu5bj6vPCUui+xPqsoEvh5RtNRg2vc8dH4ED3BTO\n+nqGte8h7rC1/g5SQa09iKKRqOa0decti4pBLUlr36b1+sXwYGs/STEnMTCPAKvo\n1ZRgpVSWW2EKqPYWSpUK+L7jXkEK+4/goW8DGUO573sYFuu1lIpFlfZg+fAWYx0i\nkr2XsegRDvHjr48mOwEg0vGw/8HFodTnFaLTifRNgUkzOymbIWF5whccCP/zj2ne\nkTLH9nq4QZrBXkrjeYII6L669WvxvxDrjEFvQJvz+9/SD3SiajBBIwpXUpyv69/r\nEi+krm7ncYyRrFjrpPivzz41wQLFCDAFDqki9jQvNOyY6Ru1ICINMJbd3vvtV+pT\n5O2VYADzgwIDAQAB\n-----END PUBLIC KEY-----"

			const text= "ini sayang olek pe private key"
			// Encrypt using public key
			const fromServer     = new NodeRSA(public_key);
			const encryptedPriv  = fromServer.encrypt(text, 'base64');
			const data           = {"payload" : encryptedPriv}

			axios.post("http://127.0.0.1:5000/token/generate", data)
				 .then(response => {
				 	let io = clientDecrypt.decrypt(response.data.io, 'utf-8');
				 	console.log(response.data);
				 	console.log(io);
				 })*/
			let data = new crypto("tes","tes");
			localStorage.setItem("private", privates);
			localStorage.setItem("public", publics);
		}
	}
</script>