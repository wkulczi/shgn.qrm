<template>
  <div>
    <nav class="sticky">
      <ul>
        <li>
          <NuxtLink to="/" exact>Home</NuxtLink>
        </li>
        <li>
          <NuxtLink to="/graphs" exact>Graphs</NuxtLink>
        </li>
        <li>
          <NuxtLink to="/tables" exact>Tables</NuxtLink>
        </li>
        <li>
          <NuxtLink to="/timelapse" exact>Timelapse</NuxtLink>
        </li>
        <li>
          <NuxtLink to="/about" exact>About</NuxtLink>
        </li>
      </ul>
    </nav>
    <main>
      <Nuxt />
    </main>
  </div>
</template>

<script>
export default {
  data() {
    return {}
  },
  head() {
    return {
      title: 'shgn',
      link: [
        { rel: 'stylesheet', href: '/bootstrap/bootstrap.min.css' },
        { rel: 'stylesheet', href: 'video-js.css' },
      ],
      script: [
        { src: '/bootstrap/bootstrap.bundle.min.js', type: 'text/javascript' },
        { src: '/dash.all.min.js', type: 'text/javascript' },
        { src: '/video.min.js', type: 'text/javascript' },
        { src: '/videojs-dash-min.js', type: 'text/javascript' },
      ],
    }
  },
}
</script>

<style>
a {
  text-decoration: none;
  color: inherit;
}

a.nuxt-link-active {
  font-weight: 500;
  color: #18974b;
}

a:hover {
  color: #00c58e;
}

ul {
  list-style-type: none;
  padding: 0;
  display: flex;
  justify-content: center;
  flex-wrap: wrap;
}
li {
  margin: 0 0.5rem;
  padding: 0.25rem;
  font-size: 1.2rem;
}

nav {
  padding: 14px 1rem 0;
  overflow: hidden;
}

.sticky {
  display: flex;
  flex-flow: row wrap;
  justify-content: center;
  position: fixed;
  top: 0;
  width: 100%;
}

main {
  margin: 0 auto;
  padding: 0 1rem;
  max-width: 1280px;
  text-align: center;
}

html {
  font-family: 'Source Sans Pro', -apple-system, BlinkMacSystemFont, 'Segoe UI',
    Roboto, 'Helvetica Neue', Arial, sans-serif;
  font-size: 16px;
  word-spacing: 1px;
  -ms-text-size-adjust: 100%;
  -webkit-text-size-adjust: 100%;
  -moz-osx-font-smoothing: grayscale;
  -webkit-font-smoothing: antialiased;
  box-sizing: border-box;
}

*,
*::before,
*::after {
  box-sizing: border-box;
  margin: 0;
}

.button--green {
  display: inline-block;
  border-radius: 4px;
  border: 1px solid #3b8070;
  color: #3b8070;
  text-decoration: none;
  padding: 10px 30px;
}

.button--green:hover {
  color: #fff;
  background-color: #3b8070;
}

.button--grey {
  display: inline-block;
  border-radius: 4px;
  border: 1px solid #35495e;
  color: #35495e;
  text-decoration: none;
  padding: 10px 30px;
  margin-left: 15px;
}

.button--grey:hover {
  color: #fff;
  background-color: #35495e;
}

.btn-simplified {
  font-weight: normal;
  text-transform: none !important;
  letter-spacing: 0.4px;
}
.btn-simplified:hover {
  background-color: #134745;
  -webkit-transition: all 550ms ease;
  transition: all 550ms ease;
  color: #ecf5ee;
}
</style>
