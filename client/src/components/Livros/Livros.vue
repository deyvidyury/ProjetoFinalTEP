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
        <v-card class="mb-2" v-for="livro in livros" :key="livro.url">
          <v-container fluid grid-list-lg>
            <v-layout row>
              <v-flex xs5 sm3>
                <v-card-media
                  src="https://images-na.ssl-images-amazon.com/images/I/51Dkevd7neL._SX258_BO1,204,203,200_.jpg"
                  height="100%"
                  contain
                ></v-card-media>
              </v-flex>
              <v-flex xs7 sm9>
                <div>
                  <div class="headline">{{ livro.nome }}</div>
                  <div>{{ livro.autor }}</div>
                  <div>{{ livro.ano }}</div>
                  <div>{{ livro.editora }}</div>
                </div>
                <v-btn flat class="orange--text" :to="'/livros/' + livro.id">
                  <v-icon light class="orange--text">arrow_forward</v-icon>
                  Ver Livro
                </v-btn>
              </v-flex>
            </v-layout>
          </v-container>
        </v-card>
      </v-flex>
    </v-layout>
    <v-layout row wrap class="mb-2">
      <v-flex xs12 sm6 class="text-xs-center text-sm-right">
        <v-btn large router @click="loadPrevious()" class="info" :disabled="!previous">Anterior</v-btn>
      </v-flex>
      <v-flex xs12 sm6 class="text-xs-center text-sm-left">
        <v-btn large router @click="loadNext()" class="info" :disabled="!next">Próximo</v-btn>
      </v-flex>
    </v-layout>
  </v-container>
</template>

<script>
export default {
  computed: {
    livros () {
      return this.$store.getters.livrosCarregados
    },
    previous () {
      return this.$store.getters.previousLivros
    },
    next () {
      return this.$store.getters.nextLivros
    },
    loading () {
      return this.$store.getters.loading
    }
  },
  methods: {
    loadPrevious () {
      this.$store.dispatch('carregaLivros', this.previous)
    },
    loadNext () {
      this.$store.dispatch('carregaLivros', this.next)
    }
  }
}
</script>
