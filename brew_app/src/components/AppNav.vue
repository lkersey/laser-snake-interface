<template>
  <div>
    <h2>Nav Bar</h2>
    <nav>
      <router-link v-for="link in links"
      :key="link.id"
      :to="link.page">{{ link.text }}
      </router-link>
    </nav>
  </div>
</template>

<script>
export default {
  name: 'AppNav',
  data () {
    return {
      links: [
        {
          id: 0,
          text: 'Home',
          page: '/'
        },
        {
          id: 1,
          text: 'Set up',
          page: '/set-up'
        }
      ]
    }
  }
}
</script>
