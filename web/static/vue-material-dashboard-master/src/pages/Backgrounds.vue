<template>
  <div class="content">
    <div class="md-layout">
      <div
        class="md-layout-item md-medium-size-100 md-xsmall-size-100 md-size-100"
      >
        <md-card>
          <md-card-header data-background-color="purple">
            <h4 class="title">Backgrounds</h4>
            <p class="category">edit by clicking on a background</p>
          </md-card-header>
          <md-card-content>
            <backgrounds-table table-header-color="black"></backgrounds-table>
          </md-card-content>
        </md-card>
      </div>
    </div>
  </div>
</template>

<script>
import { BackgroundsTable, OrderedTable } from "@/components";

export default {
  components: {
    OrderedTable,
    BackgroundsTable
  }
};
</script>
