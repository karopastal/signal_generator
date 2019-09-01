<template>
  <div class="wrapper" :class="{ 'nav-open': $sidebar.showSidebar }">
    <notifications></notifications>

    <side-bar>
      <mobile-menu slot="content"></mobile-menu>
      <sidebar-link to="/dashboard">
        <md-icon>dashboard</md-icon>
        <p>Dashboard</p>
      </sidebar-link>
      <sidebar-link to="/signals">
        <md-icon>assessment</md-icon>
        <p>Signals</p>
      </sidebar-link>
      <sidebar-link to="/backgrounds">
        <md-icon>waves</md-icon>
        <p>Backgrounds</p>
      </sidebar-link>
       <sidebar-link to="/wavelets">
        <md-icon>graphic_eq</md-icon>
        <p>Wavelets</p>
      </sidebar-link>
      <sidebar-link to="/gallery">
        <md-icon>bubble_chart</md-icon>
        <p>Gallery</p>
      </sidebar-link>
    </side-bar>

    <div class="main-panel">
      <top-navbar></top-navbar>

      <dashboard-content> </dashboard-content>

      <content-footer v-if="!$route.meta.hideFooter"></content-footer>
    </div>
  </div>
</template>
<style lang="scss"></style>
<script>
import TopNavbar from "./TopNavbar.vue";
import ContentFooter from "./ContentFooter.vue";
import DashboardContent from "./Content.vue";
import MobileMenu from "@/pages/Layout/MobileMenu.vue";

export default {
  components: {
    TopNavbar,
    DashboardContent,
    ContentFooter,
    MobileMenu
  }
};
</script>
