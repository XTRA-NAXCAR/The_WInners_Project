<template>
  <div class="container-fluid py-4 customBackground1">
    <div class="container mb-3">
        <h1 class="text-center mb-5 RalewayFont map_title" style=" color: #fff;">¡Visítanos!</h1>
        <div class="row-cols m-3" v-for="(card, index) in Mapa" :key="index">
            <div class="card" style="border: transparent; background-color: transparent">
                <div class="row g-0">
                    <div class="col-5 col-md-4 h-100" style=";overflow: hidden; align-items: center;  justify-content: center; object-fit:cover;">
                        <img :src="rootUrl + `/media/${card.imagen}`" class=" " style="height:220px; width:100%;object-fit: cover;border-radius: 5px;  " alt="...">
                    </div>
                    <div class="col-7 col-md-8 h-100">
                        <div class="card-body">
                            <h5 class="card-title pb-5 RalewayFont" style="color: #fff;">{{ card.titulo }}</h5>
                            <p class="card-text RalewayFont" style="color: #fff;">Telefono: {{ card.telefono }}</p>
                            <p class="card-text RalewayFont" style="color: #fff;">Dirección: {{ card.direccion }}</p>
                            <p class="card-text RalewayFont" style="color: #fff;">Correo: {{ card.email }}</p>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <GoogleMap
            class="my-5 px-2"
            style="width: 100%; height:60vh;"
            api-key="AIzaSyD7cf5pD4u32w9k2zEnjq19nd8WlGmm-ls"  
            :center="{ lat:5.8307185378511805, lng:-73.03316379301276 }" 
            :zoom="17.5" :minZoom="14" 
            :fullscreenControl="false" 
            :streetViewControl="false"
            :options="mapOptions">
                <Marker v-for="(coordinate, index) in Mapa" :key="index" :options="{ position: {lat: parseFloat(coordinate.latitud), lng: parseFloat(coordinate.longitud)} }" />
        </GoogleMap>
    </div>
  </div>
</template>


<script>
import { inject } from 'vue';
import { GoogleMap, Marker } from 'vue3-google-map';

export default {
  components: { GoogleMap, Marker },
  setup() {
    const data = inject('$data');
    const Mapa = data.Mapa;
    const rootUrl = inject('$rootUrl')

    const filteredMapa = Mapa.filter(coordinate => {
      // Aquí debes agregar tu lógica de filtrado
      // Por ejemplo, si quieres quitar los marcadores de hoteles,
      // tiendas y farmacias, puedes hacer algo como esto:
      return (
        coordinate.tipo !== 'hotel' &&
        coordinate.tipo !== 'tienda' &&
        coordinate.tipo !== 'farmacia'
      );
    });

    const mapOptions = {
      styles: [
        {
          featureType: 'poi',
          stylers: [{ visibility: 'off' }] // Oculta los puntos de interés
        },
        {
          featureType: 'poi.business',
          stylers: [{ visibility: 'off' }] // Oculta los negocios (almacenes, etc.)
        },
        {
          featureType: 'transit',
          stylers: [{ visibility: 'off' }] // Oculta el transporte público
        },
        {
          featureType: 'administrative',
          elementType: 'labels.text.fill',
          stylers: [{ visibility: 'off' }] // Oculta las etiquetas administrativas
        },
        {
          featureType: 'road',
          elementType: 'labels',
          stylers: [{ visibility: 'off' }] // Oculta las etiquetas de carreteras
        },
        {
          featureType: 'landscape',
          elementType: 'labels',
          stylers: [{ visibility: 'off' }] // Oculta las etiquetas del paisaje
        },
        
      ]
    };

    return {
      mapOptions,
      Mapa: filteredMapa,
      rootUrl
    };
  }
};
</script>

<style>
  @media (max-width: 580px) {
        .map_title{
        font-size: 40px;
        padding-top: 10px;
        }

    }

    @media (min-width: 581px) and (max-width: 992px){
        .map_title{
        font-size: 60px;
        margin-top: 30px;
        }
    }
    @media(min-width: 993px){
        .map_title{
        font-size: 75px;
        }
    }
  
</style>
