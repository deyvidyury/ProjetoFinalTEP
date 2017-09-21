<template>
  <v-container>
    <v-layout>
      <v-flex xs12 class="text-xs-center">
        <v-progress-circular 
        indeterminate 
        class="primary--text"
        :width="7"
        :size="70"
        v-if="loading"></v-progress-circular>
      </v-flex>
    </v-layout>
    <v-layout row wrap v-if="!loading">
      <v-flex xs12 class="mt-2">
        <v-layout row wrap>
          <v-flex xs5 sm3>
            <img src="https://images-na.ssl-images-amazon.com/images/I/51Dkevd7neL._SX258_BO1,204,203,200_.jpg" alt="" height="200px">
          </v-flex>
          <v-flex xs7 sm9>
            <h4>{{ user.username }}</h4>
            <p>Email: {{ user.email }}</p>
          </v-flex>
        </v-layout>
      </v-flex>
    </v-layout>
  </v-container>
</template>

<script>
export default {
  computed: {
    user () {
      return this.$store.getters.user
    },
    loading () {
      return this.$store.getters.loading
    }
  }
}
</script>
<template>
  <div>
    Profile Component
  </div>
</template>