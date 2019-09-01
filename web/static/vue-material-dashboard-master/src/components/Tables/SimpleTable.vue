<template>
  <div>
    <md-table v-model="signals" :table-header-color="tableHeaderColor">
      <md-table-row slot="md-table-row" slot-scope="{ item }">
        <md-table-cell md-label="ID">{{ item.id }}</md-table-cell>
        <md-table-cell md-label="Desc">{{ item.description }}</md-table-cell>
        <md-table-cell md-label="Center">{{ item.gaussian.center }}</md-table-cell>
        <md-table-cell md-label="Hight">{{ item.gaussian.height }}</md-table-cell>
        <md-table-cell md-label="Width">{{ item.gaussian.width }}</md-table-cell>
        <md-table-cell md-label="T">{{ item.range.T }}</md-table-cell>
        <md-table-cell md-label="MIN_MASS">{{ item.range.MIN_MASS }}</md-table-cell>
        <md-table-cell md-label="MAX_MASS">{{ item.range.MAX_MASS }}</md-table-cell>
        <md-table-cell md-label="MASS_NUM">{{ item.range.MASS_NUM  }}</md-table-cell>
        <md-table-cell md-label="DECAY_RATE">{{ item.range.AMPLITUDE_DECAY_RATE }}</md-table-cell>
      </md-table-row>
    </md-table>
  </div>
</template>

<script>
export default {
  name: "simple-table",
  props: {
    tableHeaderColor: {
      type: String,
      default: ""
    }
  },
  data() {
    return {
      signals: []
    }
  },
  mounted () {
    this.$axios
      .get('http://localhost:5000/api/v1/resources/signals')
      .then(response => (this.signals = response.data))
  }
};
</script>
