<template>
    <div class="customBackground2">
        <div class="container-fluid py-5 ">
            <div class="container">
                <h1 class="text-center RalewayFont mb-4  promo_title">Destacados Y Promociones</h1>
            </div>
        </div>
        <div v-if="windowWidth >=768" class="container-fluid pb-5">
            <swiper
            :pagination="{
            clickable: true,
            }"
            :slidesPerView="2"
            :spaceBetween="30"
            :autoplay="{
                delay: 2500,
                disableOnInteraction: false,
            }"
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
                slidesPerView: 3,
                spaceBetween: 50,
            },
            }"
            :modules="modules"
            class="mySwiper"
            >
                <swiper-slide v-for="(card,index) in Promociones" :key="index">
                    <div class="card h-100 w-100" style="border: transparent;">
                        <div class="p-2" style="overflow: hidden;  display: flex;  align-items: center;  justify-content: center;">
                            <img :src="rootUrl + `/media/` + card.imagen" class="img-fluid" style="width: 100%; height: 250px; object-fit: cover; border-radius: 5px;" alt="...">
                        </div>
                        <div class="card-body">
                            <div class="card-title row">
                                <h5 class="col-8 text-start">{{card.titulo}}</h5>
                                <h5 class="col-4 text-end" style="text-align: end;">{{card.precio}}</h5>
                            </div>
                            <p class="card-text text-start">{{card.descripcion}}</p>
                        </div>
                    </div>
                </swiper-slide>
            </swiper>
        </div>
        <div v-else class="container fluid pb-5" style="overflow: hidden;">
            <swiper
            :effect="'cards'"
            :grabCursor="true"
            :modules="modules"
            class="mySwiper custom-width"
            >
                <swiper-slide v-for="(card,index) in Promociones" :key="index">
                    <div class="card h-100 w-100" style="border: transparent;">
                        <div class="p-2" style="overflow: hidden;  display: flex;  align-items: center;  justify-content: center;">
                            <img :src="rootUrl + `/media/` + card.imagen" class="img-fluid" style="width: 100%; height: 250px; object-fit: cover; border-radius: 5px;" alt="...">
                        </div>
                        <div class="card-body">
                            <div class="card-title row">
                                <h5 class="col-8 fs-5 text-start">{{card.titulo}}</h5>
                                <h5 class="col-4 fs-6 text-end" style="text-align: end;">{{card.precio}}</h5>
                            </div>
                            <p class="card-text fs-6 text-start">{{card.descripcion}}</p>
                        </div>
                    </div>
                </swiper-slide>
            </swiper>
        </div>
    </div>
    
</template>


<script>

    import { inject } from 'vue';
    import { Swiper, SwiperSlide } from 'swiper/vue';

    // Import Swiper styles
    import 'swiper/css';
    import 'swiper/css/pagination';
    import 'swiper/css/effect-cards';

    // import required modules

    import { Pagination, EffectCards, Autoplay } from 'swiper/modules';

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
        setup () {
            const data = inject('$data')
            const rootUrl = inject('$rootUrl')
            const Promociones = data.Promociones
            
            return {
                Promociones,
                rootUrl,
                modules: [EffectCards, Autoplay, Pagination],
            }
        }
    }
</script>


<style >

    

    



    @media (max-width: 580px) {
        
        .promo_title{
        font-size: 40px;
        padding-top: 10px;
        }
        

        .swiper {
        width: 87%;
        height: 100%;
        }
        .swiper-card-slide {
        display: flex;
        align-items: center;
        justify-content: center;
        border-radius: 18px;
        font-size: 5px;
        font-weight: bold;
        color: #fff;
        }

    }
    @media (min-width: 581px) and (max-width: 992px){
        .promo_title{
        font-size: 60px;
        margin-top: 30px;
        }

        .swiper {
        width: 100%;
        height: 100%;
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
        .swiper-slide img {
        display: block;
        width: 100%;
        height: 100%;
        object-fit: cover;
        }
    }
    @media(min-width: 993px){
        .promo_title{
        font-size: 75px;
        }
        .swiper {
        width: 100%;
        height: 100%;
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
        .swiper-slide img {
        display: block;
        width: 100%;
        height: 100%;
        object-fit: cover;
        }
    }

</style>

