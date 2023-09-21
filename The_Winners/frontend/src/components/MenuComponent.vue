<template>
    <div class="container-fluid py-5 px-0 customBackground">
      <div class="d-flex justify-content-center mb-5">
        <h1 class="text-white RalewayFont" style="font-size: 70px;">Menú</h1>
      </div>
      <div >
        <div class="row row-cols-5 justify-content-around mb-5 px-3 customhover RalewayFont">
        <a 
        class=" col text-align-center px-0 menu_options btn " 
        v-for="(typePhotoEach, index) in typesMenuPhotoEach"
        :key="index = typePhotoEach.id"
        @click="menuFoodEach(index)"
        >{{ typePhotoEach.titulo }}</a>

        <a
          class="col text-align-center px-0 menu_options btn "
          v-for="(typePhotoOnly, index) in typesMenuOnlyPhoto"
          :key="index = typePhotoOnly.id"
          @click="menuFoodOnly(index)"
        >{{ typePhotoOnly.titulo }}</a>


            
      </div>
      
      <div v-if="windowWidth >=768">
        <swiper
          :slidesPerView="1"
          :spaceBetween="30"
          :hashNavigation="{
            watchState: true,
          }"
          :autoplay="{
            delay: 2500,
            disableOnInteraction: false,
          }"
          :pagination="{
            clickable: true,
          }"
          :navigation="false"
          :modules="modules"
          class="mySwiper"
          :breakpoints="{
            '640': {
              slidesPerView: 2,
              spaceBetween: 20,
            },
            '768': {
              slidesPerView: 2,
              spaceBetween: 40,
            },
            '1024': {
              slidesPerView: 2,
              spaceBetween: 50,
            },
          }"
        >
        
          <swiper-slide v-for="(food, index) in foodPhotoEach"
            :key="index" 
            class=" text-white"
            :data-hash="`slide` + index"
            >

            <div class="card h-100" style="border: transparent;background-color: transparent;">
                <div style="overflow: hidden; display: flex; align-items: center; justify-content: center;">
                  <img
                  :src="rootUrl + `/media/` + food.imagen"
                  class="card-img-top"
                  style="object-fit: cover; width: 700px; height: 400px; border-radius: 5px;"
                  alt="..."
                  />
                </div>
                <div class="card-body text-white">

                  <h5 class="card-title" style="width: 100%;color: #fff;"><div style="width: 100%;" class="d-flex justify-content-between">
                    <p class="text-start"><strong>{{ food.titulo }}</strong></p>
                    <p class="text-end">{{ food.precio }}</p>
                  </div>
                </h5>
                  <p class="card-text multiline-content">{{ food.descripcion }}</p>

                </div>
              </div>
          </swiper-slide>
        
        </swiper>
      </div>
        
      <div v-else style="width: 100%;overflow: hidden;">
        <swiper
        :effect="'cards'"
        :grabCursor="true"
        :modules="modules"
        class="mySwiper"
        >
          
          <swiper-slide v-for="(food, index) in foodPhotoEach"
            :key="index" 
            class=" text-white "
            >

            <div class="card h-100 bg-dark">
                <div style="overflow: hidden; max-height: 250px; min-height: 250px; display: flex; align-items: center; justify-content: center;">
                  <img
                  :src="rootUrl + `/media/` + food.imagen"
                  class="card-img-top"
                  style="object-fit: cover; height: 250px; border-radius: 10px; padding: 8px;"
                  alt="..."
                  />
                </div>
                <div class="card-body text-white">

                  <h5 class="card-title" style="color: #F5811C;"><strong>{{ food.titulo }}</strong></h5>
                  <p class="card-text multiline-content">{{ food.descripcion }}</p>
                  <p class="card-text">{{ food.precio }}</p>
                </div>
              </div>
          </swiper-slide>
        
        </swiper>

      </div>

        <div v-if="tempOnly" class="card mb-3 text-white background-card-custom pt-2" style="max-width: 100%;">
          <div class="row g-0 h-100 text-white" style="background-color: transparent;">
            <div class="col-md-4 h-50 p-2 d-flex align-items-center justify-content-center" style="overflow: hidden; max-height: 350px;">
              <img
                :src="rootUrl + `/media/${tempOnly.imagen}`"
                class="img-fluid rounded-start h-50"
                style="object-fit: cover; border-radius: 5px; width: 100%;"
                alt="..."
              />
            </div>
            <div class="col-md-8">
              <div class="card-body text-white" style="background-color: transparent;">
                <h2 class="card-title text-white">{{ tempOnly.titulo }}</h2>
                <div class="row">
                  <div class="col-12" v-for="(food, index) in foodOnlyPhoto" :key="index">
                    <div class="row">
                      <div class="card-text col text-white"><strong>{{ food.titulo }} ---- {{ food.descripcion }}</strong></div>
                      <div class="card-text col text-white text-end">{{ food.precio }}</div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>


        <div v-if="windowWidth >=768">
        <swiper
          :slidesPerView="1"
          :spaceBetween="30"
          :hashNavigation="{
            watchState: true,
          }"
          :autoplay="{
            delay: 2500,
            disableOnInteraction: false,
          }"
          :pagination="{
            clickable: true,
          }"
          :navigation="false"
          :modules="modules"
          class="mySwiper"
          :breakpoints="{
            '640': {
              slidesPerView: 2,
              spaceBetween: 20,
            },
            '768': {
              slidesPerView: 2,
              spaceBetween: 20,
            },
            '1024': {
              slidesPerView: 3,
              spaceBetween: 30,
            },
          }"
        >
        
          <swiper-slide v-for="(drinkType, index) in drinksOnly" :key="index"
            class=" text-white"
            :data-hash="`slide` + index"
            >

            <div  v-if="drinksOnly" class="card" style="background-color: transparent;">
              <div style="overflow: hidden;width: 100%; height: 400px; display: flex; align-items: center; justify-content: center;">
                <img
                  :src="rootUrl + `/media/${drinkType.imagen}`"
                  class="img-fluid rounded-start"
                  style="object-fit: cover; width: 100%; border-radius: 10px;"
                  alt="..."
                />
              </div>
              
              
                <div class="card-body text-white" style="background-color: transparent;">
                  <h2 class="card-title">{{ drinkType.titulo }}</h2>
                  <div class="row" v-for="(drink, index) in drinks" :key="index">
                    <div v-if="drink.pertenece_A_id === drinkType.id" class="row">
                      
                        <p class="card-text col-6 text-left">{{ drink.titulo }}</p>
                        <p class="card-text col-6 text-right" style="text-align: end;">{{ drink.precio }}</p>
                      
                    </div>
                  </div>

              
            </div>

        </div>
        </swiper-slide>
        </swiper>
        </div>



        <div v-else>
        <swiper
        :effect="'cards'"
        :grabCursor="true"
        :modules="modules"
        class="mySwiper"
        >
        
          <swiper-slide v-for="(drinkType, index) in drinksOnly" :key="index" 
            class=" text-white "
            >
            <div  v-if="drinksOnly" class="card bg-dark pt-2" style="background-color: transparent;">
              <div style="padding-top: 5px;overflow: hidden; width: 100%; max-height: 350px; display: flex; align-items: center; justify-content: center;border-radius: 15px;">
                <img
                  :src="rootUrl + `/media/${drinkType.imagen}`"
                  class="img-fluid rounded-start"
                  style=" padding: 8px; object-fit: cover; width: 100%; border-radius: 10px;"
                  alt="..."
                />
              </div>
              
              
                <div class="card-body text-white" style="background-color: transparent;">
                  <h2 class="card-title">{{ drinkType.titulo }}</h2>
                  <div class="row" v-for="(drink, index) in drinks" :key="index">
                    <div v-if="drink.pertenece_A_id === drinkType.id" class="row">
                      
                        <p class="card-text col-6 text-left">{{ drink.titulo }}</p>
                        <p class="card-text col-6 text-right" style="text-align: end;">{{ drink.precio }}</p>
                      
                    </div>
                  </div>

              
            </div>

        </div>
        </swiper-slide>
        </swiper>
        </div>


      </div>
    </div>
  </template>
  
<script>
  import { ref, inject, onMounted } from 'vue';

  import { Swiper, SwiperSlide } from 'swiper/vue';

  // Import Swiper styles
  import 'swiper/css';

  import 'swiper/css/effect-cards';
  import 'swiper/css/pagination';
  import 'swiper/css/navigation';

  // import required modules
  import { Autoplay,EffectCards, Pagination, Navigation } from 'swiper/modules';
  
  export default {
    components: {
      Swiper,
      SwiperSlide,
    },
    data() {
            return {
                windowWidth: window.innerWidth
            };
        },
        created() {
            window.addEventListener('resize', this.handleResize);
        },
        beforeDestroy() {
            window.removeEventListener('resize', this.handleResize);
        },
        methods: {
            handleResize() {
            this.windowWidth = window.innerWidth;
            }
        },
    setup() {
      const data = inject('$data');
      const typesMenuPhotoEach = data.Tipos_De_Comida_Imagen_Por_Producto;
      const typesMenuOnlyPhoto = data.Tipos_De_Comida_Unica_Imagen;
      const foodPhotoEach = ref(null);
      const foodOnlyPhoto = ref(null);
      const tempOnly = ref(null);
      const drinksOnly = ref(null);
      const drinks = ref(null);
      const rootUrl = inject('$rootUrl')
  
      const menuFoodEach = (type_id) => {
        foodPhotoEach.value = data.Comidas_Imagen_Por_Producto.filter(
          (food) => food.Pertenece_A_id === type_id
        );
        tempOnly.value = '';
        foodOnlyPhoto.value = '';
        drinksOnly.value = '';
        drinks.value = '';
      };
  
      const menuFoodOnly = (type_id) => {
        foodOnlyPhoto.value = data.Comidas_Unica_Imagen.filter(
          (food) => food.Pertenece_A_id === type_id
        );
        const temp = data.Tipos_De_Comida_Unica_Imagen.filter(
          (temp) => temp.id === type_id
        );
        tempOnly.value = temp[0];
        console.log(data);
        foodPhotoEach.value = '';
        drinksOnly.value = '';
        drinks.value = '';
      };
  
      const menuBebidas = () => {
        drinksOnly.value = data.Tipo_De_Bebida;
        drinks.value = data.Bebidas;
        tempOnly.value = '';
        foodOnlyPhoto.value = '';
        foodPhotoEach.value = '';
      };
      
      onMounted( () => {
        menuFoodEach(data.Tipos_De_Comida_Imagen_Por_Producto[0].id)
      });
      return {
        typesMenuPhotoEach,
        typesMenuOnlyPhoto,
        menuFoodEach,
        menuFoodOnly,
        foodPhotoEach,
        foodOnlyPhoto,
        tempOnly,
        menuBebidas,
        drinksOnly,
        drinks,
        rootUrl,
        modules: [ Autoplay, EffectCards, Pagination, Navigation],

      };
    },
  };
</script>
  
<style >
.customBackground {
  background-image: url(../assets/utilities/Fondo-Menu-The-Winners.jpg);
  background-size: cover;
  background-position: center;
  background-attachment: fixed;
  height: 100%;
}

.customBackground1{
  background-image: url('../assets/utilities/Fondo-Menu-The-Winners.jpg');
  background-size: cover;
  background-position: center;
  background-attachment: fixed;
  height: 100%; /* Ajusta la altura según tus necesidades */
}
.customBackground2{
  background-image: url('../assets/utilities/Mural-pibe.jpg');
  background-size: cover;
  background-position: center;
  background-attachment: fixed;
  height: 100%; /* Ajusta la altura según tus necesidades */
}
.customhover a{
  color: #fff;
  transition: 250ms;
}

.customhover a:hover{
  color: #F5811C;
}

.swiper-pagination-bullet {
    background-color: #F5811C; /* Cambia el color según tus preferencias */
  }

@media (width < 768){
  .swiper {
  width: 240px;
  height: 320px;
  }
  .swiper-slide {
    display: flex;
    align-items: center;
    justify-content: center;
    border-radius: 18px;
    font-size: 22px;
    font-weight: bold;
    color: #fff;
  }
  
}
@media (width >= 768){
  .swiper {
  width: 100%;
  height: auto;
  margin-left: auto;
  margin-right: auto;
}

.swiper-slide {
  text-align: left;
  font-size: 18px;
  background: transparent;
  /* Center slide text vertically */
  display: flex;
  justify-content: center;
  align-items: center;
}





.swiper-button-next,
.swiper-button-prev {
    width: 50px;
    height: 50px;
    border-radius: 25px;
    background-color: #F5811C;
    color: #fff; /* Cambia el color según tus preferencias */
}
}

@media (max-width: 580px) {
  .menu_title{
    font-size: 40px;
    padding-top: 10px;
  }
  .menu_options{
    font-size:15px;
    margin-bottom: 20px;
  }
  .background-card-custom{
    background-color: #212529;
  }
}
@media (min-width: 581px) and (max-width: 992px){
  .menu_title{
    font-size: 60px;
    margin-top: 30px;
  }
  .menu_options{
    font-size:20px;
  }
  .background-card-custom{
    background-color: transparent;
  }
}

@media(min-width: 993px){
  .menu_title{
    font-size: 75px;
  }
  .menu_options{
    font-size:26px;
  }
  .background-card-custom{
    background-color: transparent;
  }
}
</style>