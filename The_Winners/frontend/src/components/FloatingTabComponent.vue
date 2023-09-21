<template>
    <div class="floating-tab" :class="{ 'expanded': isHovered }" @mouseover="isHovered = true" @mouseleave="isHovered = false">
      <div class="tab-icons">
        <div class="row">
          <div class="col-12">
            <i class="bi bi-telephone-outbound-fill" style="font-size: 30px;"></i>
            <div class="icon-text RalewayFont" v-show="isHovered">
              <a class="text-white" href="tel:+573123543107" style="text-decoration: none;">Llama aquí</a>
            </div>
          </div>
        </div>
        <div class="row">
          <div class="col-12">
            <i class="bi bi-whatsapp" style="font-size: 35px;"></i>
            <div class="icon-text RalewayFont" v-show="isHovered">
              <a class="text-white" href="https://www.wa.link/q747zi" style="text-decoration: none;">WhatsApp</a>
            </div>
          </div>
        </div>
        <div class="row">
          <div class="col-12">
            <i class="bi bi-file-text" style="font-size: 35px;"></i>
            <div @click="$emit('scroll-to-menu')" class="icon-text RalewayFont" v-show="isHovered">
              Menú
            </div>
          </div>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        isHovered: false
      };
    }
  };
  </script>
  
  <style>
.floating-tab {
  position: fixed;
  width: 60px;
  height: 180px;
  top: 200px;
  right: 0px;
  background-color: #A80521;
  border-top-left-radius: 30px;
  border-bottom-left-radius: 30px;
  padding: 10px 10px 10px 15px;
  cursor: pointer;
  z-index: 9999;
  transition: width 0.3s;
}
  
  .floating-tab.expanded {
    width: 150px;
  }
  
  .tab-icons {
    display: flex;
    flex-direction: column;
    color: #fff;
  }
  
  .tab-icons .row {
    margin-bottom: 5px;
    align-items: center;
  }
  
  .tab-icons .col-12 {
    display: flex;
    align-items: center;
  }
  
  .icon-text {
    margin-left: 5px;
  }
  
  .icon-text {
    display: none;
  }
  
  .floating-tab.expanded .icon-text {
    display: block;
  }
  </style>
  