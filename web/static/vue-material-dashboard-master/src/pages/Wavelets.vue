<template>
  <div class="content">
    <div class="md-layout">
      <div
        class="md-layout-item md-medium-size-100 md-xsmall-size-100 md-size-100"
      >
        <md-card>
          <md-card-header data-background-color="purple">
            <h4 class="title">Wavelets</h4>
            <p class="category">edit by clicking on a wavelet</p>
          </md-card-header>
          <md-card-content>
            <wavelets-table table-header-color="black"></wavelets-table>
          </md-card-content>
        </md-card>
      </div>
    </div>
  </div>
</template>

<script>
import { WaveletsTable, OrderedTable } from "@/components";

export default {
  components: {
    OrderedTable,
    WaveletsTable
  }
};
</script>
