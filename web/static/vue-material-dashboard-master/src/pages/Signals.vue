<template>
  <div class="content">
    <div class="md-layout">
      <div
        class="md-layout-item md-medium-size-100 md-xsmall-size-100 md-size-100"
      >
        <md-card>
          <md-card-header data-background-color="purple">
            <h4 class="title">Signals</h4>
            <p class="category">edit by clicking on a signal</p>
          </md-card-header>
          <md-card-content>
            <signals-table table-header-color="black"></signals-table>
          </md-card-content>
        </md-card>
      </div>
    </div>
  </div>
</template>

<script>
import { SignalsTable, OrderedTable } from "@/components";

export default {
  components: {
    OrderedTable,
    SignalsTable
  }
};
</script>
