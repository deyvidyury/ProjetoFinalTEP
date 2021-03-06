import Vue from 'vue'
import Router from 'vue-router'
import Home from '@/components/Home'
import Livros from '@/components/Livros/Livros'
import Livro from '@/components/Livros/Livro'
import CriarLivro from '@/components/Livros/CriarLivro'
import Resenhas from '@/components/Resenhas/Resenhas'
import Resenha from '@/components/Resenhas/Resenha'
import Profile from '@/components/User/Profile'
import Signin from '@/components/User/Signin'
import Signup from '@/components/User/Signup'
import AuthGuard from './AuthGuard'
Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Home',
      component: Home
    },
    {
      path: '/livros',
      name: 'Livros',
      component: Livros
    },
    {
      path: '/livros/new',
      name: 'CriarLivro',
      component: CriarLivro
    },
    {
      path: '/livros/:id',
      name: 'Livro',
      props: true,
      component: Livro
    },
    {
      path: '/resenhas',
      name: 'Resenhas',
      component: Resenhas
    },
    {
      path: '/resenhas/:id',
      name: 'Resenha',
      props: true,
      component: Resenha,
      beforeEnter: AuthGuard
    },
    {
      path: '/profile',
      name: 'Profile',
      component: Profile
    },
    {
      path: '/signin',
      name: 'Signin',
      component: Signin
    },
    {
      path: '/signup',
      name: 'Signup',
      component: Signup
    }
  ],
  mode: 'history'
})
