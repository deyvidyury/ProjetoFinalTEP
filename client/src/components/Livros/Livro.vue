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
          <v-flex xs5 sm4 class="pa-2">
            <img src="https://images-na.ssl-images-amazon.com/images/I/51Dkevd7neL._SX258_BO1,204,203,200_.jpg" alt="" width="100%">
          </v-flex>
          <v-flex xs7 sm8>
            <h4>{{ livro.nome }}</h4>
            <p>Autor: {{ livro.autor }}</p>
            <p>Ano: {{ livro.ano }}</p>
            <p>Editora: {{ livro.editora }}</p>
            <v-divider></v-divider>
            <h5>Resenhas</h5>
            <v-list two-line>
              <v-list-tile avatar ripple v-for="(resenha, index) in livro.resenhas" :key="resenha.id" @click="loadResenha(resenha)">
                <v-list-tile-content>
                  <v-list-tile-title>{{ resenha.dono }}</v-list-tile-title>
                  <v-list-tile-sub-title class="grey--text text--darken-4">{{ resenha.criado | date }}</v-list-tile-sub-title>
                  <v-list-tile-sub-title>{{ resenha.texto | truncate(100, '...') }}</v-list-tile-sub-title>
                  <v-list-tile-sub-title class="mb-1">Nota: {{ resenha.nota.estrelas__avg  }}</v-list-tile-sub-title>
                </v-list-tile-content>
                <v-divider v-if="index + 1 < livro.resenhas.length"></v-divider>
              </v-list-tile>
            </v-list>
          </v-flex>
        </v-layout>
      </v-flex>
    </v-layout>
  </v-container>
</template>

<script>
import router from '../../router'
export default {
  props: ['id'],
  computed: {
    livro () {
      return this.$store.getters.livroCarregado(this.id)
    },
    loading () {
      return this.$store.getters.loading
    }
  },
  methods: {
    loadResenha (resenha) {
      router.push({path: `/resenhas/${resenha.id}`})
    }
  }
}
</script>
