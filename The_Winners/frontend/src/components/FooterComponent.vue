<template>
    <div class="container-fluid p-2 p-md-3 px-md-5 bg-dark  ">
        <div class="container-fluid py-3 d-flex align-items-center justify-content-center">
            <img class="img-fluid pt-2" src="../assets/logo/Logo_The_Winners.png" alt="None" style="width:10em;">
        </div>
        <div class ="row row-cols-2 row-cols-md-4 g-2 g-lg-4 ">
            <div class="col ">
                <div class="card h-100 bg-transparent text-white border-0">
                    <div class="card-body ">
                        <h5 class="card-title mb-4 pb-3 RalewayFont">Contacto:</h5>
                        <p class="card-text">Telefono: {{ Contacto.telefono }}</p>
                        <p class="card-text">Correo: {{ Contacto.email }}</p>
                        <p class="card-text">Dirección: {{ Contacto.direccion }}</p>
                    </div>
                </div>
            </div>
            <div class="col">
                <div class="card h-100 bg-transparent text-white border-0">
                    <div class="card-body">
                        <h5 class="card-title mb-4 pb-3 RalewayFont">Sitio:</h5>
                        <p class="card-text">Home</p>
                        <p class="card-text">Menu</p>
                        <p class="card-text">Restaurantes</p>
                    </div>
                </div>
            </div>
            <div class="col">
                <div class="card h-100 bg-transparent text-white border-0">
                    <div class="card-body">
                        <h5 class="card-title mb-4 pb-3 RalewayFont">Legal:</h5>
                        <p class="card-text">Política de privacidad</p>
                        <p class="card-text">Términos y condiciones</p>
                        <p class="card-text">Cookies</p>
                    </div>
                </div>
            </div>
            <div class="col ">
                <div class="card h-100 bg-transparent text-white border-0">
                    <div class="card-body ">
                        <h5 class="card-title mb-4 pb-3 RalewayFont">Nuestras Redes:</h5>
                        <p class="card-text fs-2"><i class="bi bi-instagram pe-3"></i>  <i class="bi bi-facebook pe-3"></i> <i class="bi bi-tiktok"></i></p>

                    </div>
                </div>
            </div>
        </div>
    </div>
    <div class="container-fluid py-1 d-flex align-items-center justify-content-center fs-5"  style="background-color: #A90422; ">
        <h6 class="text-center RalewayFont">© 2023 La Madre | Design by Paginas Web Colombia</h6>
    </div>
</template>
<script>
    import { inject } from 'vue';
    export default {
        setup () {
            const data = inject('$data');
            const Contacto = data.Contacto[0]
        return{
            Contacto
        }
        },
    }
</script>
<style>
.custom-border-color {
    border-color: #A90422;
}
</style>