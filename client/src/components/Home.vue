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
      <v-flex xs12 md7 class="mt-2">
        <v-card class="mb-2" v-for="resenha in resenhas" :key="resenha.url">
          <v-container fluid grid-list-lg>
            <v-layout row>
              <v-flex xs5>
                <v-card-media
                  src="https://images-na.ssl-images-amazon.com/images/I/51Dkevd7neL._SX258_BO1,204,203,200_.jpg"
                  height="100%"
                  contain
                ></v-card-media>
              </v-flex>
              <v-flex xs7>
                <div>
                  <div class="headline">{{ resenha.livro.nome }}</div>
                  <div>{{ resenha.dono }}</div>
                  <div>{{ resenha.criado | date }}</div>
                  <div v-if="resenha.nota.estrelas__avg">Nota: {{ resenha.nota.estrelas__avg }}</div>
                  <div v-else>Nota: <small>Sem avaliações</small></div>
                </div>
                <v-btn flat class="orange--text" :to="'/resenhas/' + resenha.id">
                  <v-icon light class="orange--text">arrow_forward</v-icon>
                  Ler Resenha
                </v-btn>
              </v-flex>
            </v-layout>
          </v-container>
        </v-card>
      </v-flex>

      <v-flex xs12 md4 offset-md1  class="mt-2">
        <v-card class="mb-2" v-for="livro in livros" :key="livro.id">
          <v-container fluid grid-list-lg>
            <v-layout row>
              <v-flex xs5>
                <v-card-media
                  src="https://images-na.ssl-images-amazon.com/images/I/51Dkevd7neL._SX258_BO1,204,203,200_.jpg"
                  height="100%"
                  contain
                ></v-card-media>
              </v-flex>
              <v-flex xs7>
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
  </v-container>
</template>

<script>
export default {
  computed: {
    resenhas () {
      return this.$store.getters.resenhasMaisRecentes
    },
    livros () {
      return this.$store.getters.livrosCarregados
    },
    loading () {
      return this.$store.getters.loading
    }
  }
}
</script>
