import DashboardLayout from "@/pages/Layout/DashboardLayout.vue";

import Dashboard from "@/pages/Dashboard.vue";
import UserProfile from "@/pages/UserProfile.vue";
import Signals from "@/pages/Signals.vue";
import Backgrounds from "@/pages/Backgrounds.vue";
import Wavelets from "@/pages/Wavelets.vue";
import Icons from "@/pages/Icons.vue";
import DynamicPlots from "@/pages/DynamicPlots.vue";
import Gallery from "@/pages/Gallery.vue";
import Maps from "@/pages/Maps.vue";
import Notifications from "@/pages/Notifications.vue";
import UpgradeToPRO from "@/pages/UpgradeToPRO.vue";

const routes = [
  {
    path: "/",
    component: DashboardLayout,
    redirect: "/dashboard",
    children: [
      {
        path: "dashboard",
        name: "Dashboard",
        component: Dashboard
      },
      {
        path: "user",
        name: "User Profile",
        component: UserProfile
      },
      {
        path: "signals",
        name: "Signals",
        component: Signals
      },
      {
        path: "wavelets",
        name: "Wavelets",
        component: Wavelets
      },
      {
        path: "backgrounds",
        name: "Backgrounds",
        component: Backgrounds
      },
      {
        path: "dynamic-plots",
        name: "DynamicPlots",
        component: DynamicPlots
      },
      {
        path: "gallery",
        name: "Gallery",
        component: Gallery
      },
      {
        path: "icons",
        name: "Icons",
        component: Icons
      },
      {
        path: "maps",
        name: "Maps",
        meta: {
          hideFooter: true
        },
        component: Maps
      },
      {
        path: "notifications",
        name: "Notifications",
        component: Notifications
      },
      {
        path: "upgrade",
        name: "Upgrade to PRO",
        component: UpgradeToPRO
      }
    ]
  }
];

export default routes;
