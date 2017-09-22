<template>
  <v-container>
    <v-layout row>
      <v-flex xs12 sm6 offset-sm3>
        <h4 class="primary--text text-xs-center">Create a new Meetup</h4>
      </v-flex>
    </v-layout>
    <v-layout row>
      <v-flex xs12>
        <form @submit.prevent="onCreateBook">
          <v-layout row>
            <v-flex xs12 sm6 offset-sm3>
              <v-text-field
                name="nome"
                label="Nome"
                id="nome"
                v-model="nome"
                required></v-text-field>
            </v-flex>
          </v-layout>
          <v-layout row>
            <v-flex xs12 sm6 offset-sm3>
              <v-text-field
                name="autor"
                label="Autor"
                id="autor"
                v-model="autor"
                required></v-text-field>
            </v-flex>
          </v-layout>
          <v-layout row>
            <v-flex xs12 sm6 offset-sm3>
              <v-text-field
                name="ano"
                label="Ano"
                id="ano"
                v-model="ano"
                required></v-text-field>
            </v-flex>
          </v-layout>
          <v-layout row>
            <v-flex xs12 sm6 offset-sm3>
              <v-text-field
                name="editora"
                label="Editora"
                id="editora"
                v-model="editora"
                required></v-text-field>
            </v-flex>
          </v-layout>
          <v-layout row>
            <v-flex xs12 sm6 offset-sm3>
              <v-text-field
                name="isbn"
                label="ISBN"
                id="isbn"
                v-model="isbn"
                ></v-text-field>
            </v-flex>
          </v-layout>
          <v-layout row>
            <v-flex xs12 sm-6 offset-sm3>
              <v-btn primary :disabled="!formIsValid" type="submit">Adicionar Livro</v-btn>
            </v-flex>
          </v-layout>
        </form>
      </v-flex>
    </v-layout>
  </v-container>
</template>

<script>
  export default {
    data () {
      return {
        nome: '',
        autor: '',
        ano: '',
        editora: '',
        isbn: ''
      }
    },
    computed: {
      formIsValid () {
        return this.nome !== '' && this.autor !== '' && this.ano !== '' && this.editora !== ''
      }
    },
    methods: {
      onCreateBook () {
        if (this.formIsValid) {
          const livro = {
            nome: this.nome,
            autor: this.autor,
            ano: this.ano,
            editora: this.editora,
            isbn: this.isbn
          }
          console.log(livro)
          this.$store.dispatch('criarLivro', livro)
          this.$router.push('/livros')
        }
      }
    }
  }
</script>