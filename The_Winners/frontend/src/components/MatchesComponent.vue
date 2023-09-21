<template>
    <div class="container-fluid customBackground p-0">
        <div class="container-fluid py-5 ">
            <div class="container">
                <h1 class="text-center RalewayFont pb-4 promo_title" style="color: #fff;">Ven Y Pasa Un Buen Rato</h1>
            </div>
        </div>

        <div class="table_container" v-if="control">
            <div class="d-flex justify-content-center py-4">
                <h5 class="d-flex mb-4 text-white" style="font-size: 2.5rem; letter-spacing: 1px;">La Programación del: {{ fecha_partidos.dia }} / {{ fecha_partidos.mes }} / {{ fecha_partidos.año }}</h5>
            </div>
            <div class="row g-0 pb-5">
                <div class="col-3">
                    <h5 class="text-white">
                        TORNEO
                    </h5>
                </div>
                <div class="col-6">
                    <h5 class="text-white">
                        PARTIDO
                    </h5>
                </div>    
                <div class="col-3">
                    <h5 class="text-white">
                        HORA
                    </h5>
                </div> 
            </div>
            <!--Ud coge este row completo y le hace v-for-->

            <div class="row g-0 pb-5" v-for="(partido, index) in partidos">
                <div class="col-3 d-flex align-items-center justify-content-center">
                    <p class="m-0 text-white">{{ partido.torneo }}</p>
                </div>

                <div class="col-6">
                    <div class="row g-0 justify-content-center" style="height: 100%;">
                        <div class="col-5 d-flex team_section">
                            <div class="d-flex flex-column flex-md-row team_left" style="width: 100%;">

                                <div class="d-flex order-1 order-md-2 justify-content-center align-items-center">
                                    <div class="d-flex justify-content-center align-items-center icon_container">
                                        <img :src="`${rootUrl}/media/${partido.imagen_equipo1}`" alt="Equipo 1" class="img-flex icon_photo" style="object-fit: cover; height: 100%; width: 100%;">
                                    </div>
                                </div>
                                <div class="d-flex order-2 order-md-1 align-items-center justify-content-center">
                                    <p class="d-flex m-0 text-white">{{ partido.equipo_1 }}</p>
                                </div>
                                
                            </div>
                        </div>

                        <div class="col-2 col-md-1 d-flex justify-content-center align-items-center">
                            <p class="m-0 text-white">vs.</p>
                        </div>
                        
                        <div class="col-5 d-flex team_section">
                            <div class="d-flex flex-column flex-md-row team_right" style="width: 100%;">

                                <div class="d-flex order-1 order-md-1 justify-content-center align-items-center">
                                    <div class="d-flex justify-content-center align-items-center icon_container">
                                        <img :src="`${rootUrl}/media/${partido.imagen_equipo2}`" alt="Equipo 1" class="img-flex icon_photo" style="object-fit: cover; height: 100%; width: 100%;">
                                    </div>
                                </div>
                                <div class="d-flex order-2 order-md-2 align-items-center justify-content-center">
                                    <p class="d-flex m-0 text-white">{{ partido.equipo_2 }}</p>
                                </div>
                                
                            </div>
                        </div>

                    </div>
                </div>

                <div class="col-3 d-flex align-items-center justify-content-center">
                    <p class="m-0 p-0 text-white">{{ partido.hora }}</p>
                </div>
            </div>

            <!--Aquí acaba el v-for-->        

        </div>
        
        <div v-else>
            <h2 class="text-center RalewayFont text-white" style="font-size: 50px;margin-bottom: 0; padding-bottom: 200px;">¡Tomemonos Un Descanso Para Compartir!</h2>
        </div>
        

    </div>
</template>
<script>
import { inject, ref } from 'vue';
export default {
    setup () {
        const data = inject('$data')
        const fecha_partidos = ref(null)
        const control = ref(null)
        const partidos = ref(null)
        const rootUrl = inject('$rootUrl')

        if (data.Fecha_Partidos[0]){
            fecha_partidos.value = data.Fecha_Partidos[0];
            partidos.value = data.Partidos;
            control.value = true;
        } else {
            fecha_partidos.value = [{titulo: '¡TOMEMONOS UN DESCANSO Y VEN A COMPARTIR CON NOSOTROS!'}];
            control.value = false;

        }
        return {
            fecha_partidos,
            partidos,
            control,
            rootUrl
        }
    }
}
</script>
<style scoped>
    .customBackground {
        background-image: url(../assets/utilities/campos-de-futbol.jpg);
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
        height: 100%;

    }

    .team_left {
        justify-content: end;
    }
    .team_right {
        justify-content: start;
    }
    .icon_photo{
            object-fit: cover; 
            height: 100%; 
            width: 100%;
        }
    
    @media (max-width: 580px){
        h5 {
            font-size: 1.2rem;
            text-align: center;
        }
        p{
            font-size: 0.9rem;
            text-align: center;
        }
        .icon_container{
            overflow: hidden;
            height: 14vw;
            width: 14vw;
            border-radius: 50%;
        }
        .team_section{
            align-items: start;
        }
    }
    @media (min-width: 581px){
        
        .table_container{
            padding: 0px 40px;
        }
        h5 {
            font-size: 1.5rem;
            text-align: center;
        }
        .icon_container{
            overflow: hidden;
            height: 5vw;
            width: 5vw;
            border-radius: 50%;
        }
        .team_section{
            align-items: center;
        }
    }
    
    @media (min-width: 581px) and (max-width: 992px){
        p{
            font-size: 1.2rem;
            text-align: center;
            padding: 0px 10px;
        }
    }

    @media (min-width: 993px){
        p{
            font-size: 1.6rem;
            text-align: center;
            padding: 0px 10px;
        }
    }

  </style>