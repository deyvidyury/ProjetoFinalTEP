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
            <h4>{{ resenha.livro.nome }}</h4>
            <p>Autor: {{ resenha.livro.autor }}</p>
            <p>Ano: {{ resenha.livro.ano }}</p>
            <p>Editora: {{ resenha.livro.editora }}</p>
          </v-flex>
        </v-layout>
        <v-divider class="mt-2"></v-divider>
        <v-layout row wrap class="mt-2">
          <v-flex xs12>
            <h5 class="text-xs-center">Resenha escrita por <strong>{{ resenha.dono }}</strong></h5>
            <p class="text-xs-center"><em>Em: {{ resenha.criado | date }}</em></p>
            <p class="texto">{{ resenha.texto }}</p>
          </v-flex>
        </v-layout>
        <v-divider class="mt-2"></v-divider>
        <v-layout row wrap class="mt-2">
          <v-flex xs6>
            <p class="texto">Nota: <star-rating :rating="resenha.nota.estrelas__avg" :read-only="true" :increment="0.01"></star-rating></p>
          </v-flex>
          <v-flex xs6>
            <p class="texto">Dê sua nota: <star-rating @rating-selected ="setRating"></star-rating></p>
          </v-flex>
        </v-layout>
        <v-divider class="mt-2"></v-divider>
        <v-layout row wrap class="mt-2">
          <v-flex xs12>
            <p class="texto"><strong>Comentários</strong></p>
            <v-list>
              <template v-for="comentario in resenha.comentarios">
                <v-list-tile avatar>
                  <v-list-tile-avatar>
                    <img src="https://image.freepik.com/icones-gratis/imagem-avatar-homem-para-o-perfil_318-68886.jpg"/>
                  </v-list-tile-avatar>
                  <v-list-tile-content>
                    <v-list-tile-title v-html="comentario.nome+' - em '+comentario.criado"></v-list-tile-title>
                    <v-list-tile-sub-title v-html="comentario.comentario"></v-list-tile-sub-title>
                  </v-list-tile-content>
                </v-list-tile>
              </template>
            </v-list>
          </v-flex>
        </v-layout>
      </v-flex>
    </v-layout>
  </v-container>
</template>

<script>
export default {
  props: ['id'],
  computed: {
    resenha () {
      return this.$store.getters.resenhaCarregada(this.id)
    },
    loading () {
      return this.$store.getters.loading
    }
  },
  methods: {
    setRating (rating) {
      // this.rating = rating;
      this.$store.dispatch('avaliar', {resenha: this.id, nota: rating})
    }
  }
}
</script>
