<template>
  <div class="container-fluid px-0">
    <div class="video-wrapper">
      <video ref="videoRef" :src="videoUrl" class="video-element" autoplay muted></video>
      <div class="video-caption container">
        <h2 class="RalewayFont multimedia_title" style="color: #A80521;">{{ videoContent.titulo }}</h2>
        <p class="text-white description_Multimedia RalewayFont ">{{ videoContent.descripcion }}</p>
        <a @click="$emit('scroll-to-menu')" class="btn btn-outline-light button_Multimedia RalewayFont" style="border-radius: 50px;" >Menú</a>
      </div>
    </div>
  </div>
</template>

<script>
import { ref, onMounted, inject, computed } from 'vue';

export default {
  setup() {
    const data = inject('$data');
    const videoRef = ref(null);
    const playVideo = () => {
      videoRef.value.play();
    };

    const restartVideo = () => {
      videoRef.value.currentTime = 0;
      videoRef.value.play();
    };

    onMounted(() => {
      videoRef.value.addEventListener('ended', restartVideo);
      playVideo(); // Reproducir el video automáticamente al montar el componente
    });

    const videoPath = data.Multimedia_Principal[0].video;
    const videoContent = data.Multimedia_Principal[0];

    const videoUrl = computed(() => {
      const baseUrl = window.location.origin; // Reemplaza con la URL de tu servidor Django
      return `${baseUrl}/media/${videoPath}`;
    });

    return {
      videoRef,
      videoContent,
      restartVideo,
      videoUrl
    };
  }
};
</script>


  
  <style>
  .video-wrapper {
    position: relative;
    width: 100%;
    padding-bottom: 56.25%; /* 16:9 aspect ratio */
    overflow: hidden;
  }
  
  .video-element {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    object-fit: cover;
  }
  
  .video-caption {
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    text-align: center;
    color: #fff;
  }
  
  .video-caption h2 {
    margin-bottom: 10px;
  }
  
  .video-caption p {
    margin-bottom: 20px;
  }

  @media (max-width: 580px) {
  .multimedia_title{
    font-size: 30px;
    padding-top: 110px;
    }

  }

  @media (min-width: 581px) and (max-width: 992px){
    .multimedia_title{
      font-size: 50px;
      margin-top: 30px;
    }
  }
  @media(min-width: 993px){
    .multimedia_title{
      font-size: 80px;
    }
  }
  @media (max-width: 576px) {
  /* Estilos para pantallas más pequeñas (hasta 576px) */
  .description_Multimedia {
    font-size: 1rem; /* Tamaño de fuente para pantallas pequeñas */
  }
  .button_Multimedia{
    font-size: 1rem;
  }
  .video-wrapper{
    height: 400px;
  }
}

@media (min-width: 577px) and (max-width: 991px) {
  /* Estilos para pantallas de tamaño mediano (de 577px a 991px) */
  .description_Multimedia {
    font-size: 1.2rem; /* Tamaño de fuente para pantallas medianas */
  }
  .button_Multimedia{
    font-size: 1.1rem;
  }
  .video-wrapper{
    height: 600px;
  }
}

@media (min-width: 992px) {
  /* Estilos para pantallas más grandes (a partir de 992px) */
  .description_Multimedia {
    font-size: 2rem; /* Tamaño de fuente para pantallas grandes */
  }
  .button_Multimedia{
    font-size: 1.5rem;
  }
}
  </style>
