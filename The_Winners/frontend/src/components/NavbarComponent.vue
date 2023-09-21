<template>
  <div v-bind:class="['navbar-container', { 'navbar-fixed': isNavbarFixed }]">
    <div class="container-fluid">
      <nav class="navbar navbar-expand-lg ">
        <div class="container-fluid">
          <img src="../assets/logo/Logo_The_Winners.png" width="200" class="img-fluid ms-lg-5 img-responsive img-fluid-sm img-fluid-lg img-nav-responsive" alt="...">
          <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation" style="background-color: #A80521;">
            <i class="bi bi-list" style="font-size: 30px; color: #fff;"></i>
          </button>
          <div class="collapse navbar-collapse text-white" id="navbarNav">
            <ul class="navbar-nav ms-auto ">
              <li class="nav-item fs-3">
                <a class="nav-link active RalewayFont" aria-current="page" href="#" style="color: #A80521;">Inicio</a>
              </li>
              <li class="nav-item">
                <a class="nav-link fs-3 text-white RalewayFont" @click="$emit('scroll-to-menu')" style="cursor: pointer;">Menú</a>
              </li>
              <li class="nav-item">
                <a class="nav-link fs-3 text-white RalewayFont" @click="$emit('scroll-to-restuarant')" style="cursor: pointer;">Restaurantes</a>
              </li>
              <li class="nav-item">
                <a class="nav-link fs-3 text-white RalewayFont" href="https://www.wa.link/q747zi" target="_blank" style="cursor: pointer;">Domicilios</a>
              </li>
              <li class="nav-item d-flex align-items-center ms-lg-5">
                <a class="bi bi-facebook fs-3 RalewayFont text-white" href="https://www.facebook.com/TheWinnersSportsBar/" target="_blank" style="cursor: pointer;"></a>
                <a class="bi bi-instagram fs-3 RalewayFont ms-3 d-lg-none text-white" href="https://www.instagram.com/thewinnerssportsbar/?igshid=YmMyMTA2M2Y%3D" target="_blank" style="cursor: pointer;"></a>
              </li>
              <li class="nav-item d-lg-flex align-items-center d-none ms-lg-3">
                <a class="bi bi-instagram fs-3 RalewayFont text-white" href="https://www.instagram.com/thewinnerssportsbar/?igshid=YmMyMTA2M2Y%3D" target="_blank" style="cursor: pointer;"></a>
              </li>
            </ul>
          </div>
        </div>
      </nav>
    </div>
  </div>
</template>

<script>
import { ref, onMounted, onUnmounted } from 'vue';

export default {
  setup() {
    const isNavbarFixed = ref(false);

    const handleScroll = () => {
      isNavbarFixed.value = window.pageYOffset > 0;
    };

    onMounted(() => {
      window.addEventListener('scroll', handleScroll);
    });

    onUnmounted(() => {
      window.removeEventListener('scroll', handleScroll);
    });

    return {
      isNavbarFixed
    };
  }
};
</script>

<style>
.navbar-container {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  z-index: 999;
  transition: background-color 0.3s ease;
}

.navbar-fixed {
  position: fixed;
  background-color: #212529;
}


@media (max-width: 580px) {
  .img-nav-responsive{
    width: 80px;
  }
}

@media (min-width: 581px) and (max-width: 992px){
  .img-nav-responsive{
    width: 90px;
  }
}
</style>