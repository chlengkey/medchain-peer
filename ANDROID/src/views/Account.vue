<template>
	<ion-page style="font-family:Inter">
		<ion-content>
			<div class="mb-3 px-6 pt-8">
				<img class="w-24 mb-2" src="../assets/logo.png">
				<p class="text-xl font-bold">Akun</p>
				<p class="text-sm text-gray-500">Silahkan mengatur data diri anda disini</p>
			</div>

			<div class="px-2">

				<!-- Nama Pengguna -->
				<ion-item>
					<ion-label position="stacked">Nama Pengguna</ion-label>
					<ion-input @IonInput="user.username = $event.target.value"></ion-input>
				</ion-item>

				<!-- Kata Sandi -->
				<ion-item>
					<ion-label position="stacked">Kata Sandi</ion-label>
					<ion-input type="password" @IonInput="user.password = $event.target.value"></ion-input>
				</ion-item>

				<!-- Nama Depan -->
				<ion-item class="mt-5">
					<ion-label position="stacked">Nama Depan</ion-label>
					<ion-input @IonInput="user.firstname = $event.target.value"></ion-input>
				</ion-item>

				<!-- Nama Belakang -->
				<ion-item>
					<ion-label position="stacked">Nama Belakang</ion-label>
					<ion-input @IonInput="user.lastname = $event.target.value"></ion-input>
				</ion-item>

            <!-- Jenis Kelamin -->
				<ion-item>
					<ion-label position="stacked">Jenis Kelamin</ion-label>
               <ion-select value="gender" interface="action-sheet">
               <ion-select-option value="pria">Pria</ion-select-option>
               <ion-select-option value="wanita">Wanita</ion-select-option>
               </ion-select>
				</ion-item>

            <!-- Tanggal Lahir -->
				<ion-item>
					<ion-label position="stacked">Tanggal Lahir</ion-label>
					<ion-input type="date" @IonInput="user.dob = $event.target.value"></ion-input>
				</ion-item>

				<div class="mx-3 mt-4 flex text-sm">
					<button class="font-semibold bg-green-100 text-green-700 px-4 py-2 rounded">Simpan</button>
					<button class="font-semibold text-red-700 px-5 py-2 rounded">Batal</button>
				</div>
			</div>
		</ion-content>
	</ion-page>
</template>