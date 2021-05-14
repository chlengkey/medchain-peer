<template>
    <card>
        <!--<h5 slot="header" class="title">Rekam Medis Pasien</h5>-->
        <p>tes</p>
        <div class="row">
            <div class="col-md-6 pr-md-1">
                <base-input label="Nama Depan"
                            v-model="model.firstName"
                            placeholder="First Name"
                            disabled>
                </base-input>
            </div>
            <div class="col-md-6 pr-md-1">
                <base-input label="Nama Belakang"
                            v-model="model.lastName"
                            placeholder="Last Name"
                            disabled>
                </base-input>
            </div>
        </div>
    </card>
</template>