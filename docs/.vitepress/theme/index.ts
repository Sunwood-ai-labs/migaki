import { h } from 'vue'
import type { Theme } from 'vitepress'
import DefaultTheme from 'vitepress/theme'
import siteLogo from '../../../assets/logo.svg?url'
import './custom.css'

const theme = {
  extends: DefaultTheme,
  Layout: () =>
    h(DefaultTheme.Layout, null, {
      'nav-bar-title-before': () =>
        h('img', {
          class: 'navbar-logo-mark',
          src: siteLogo,
          alt: '',
          'aria-hidden': 'true',
        }),
    }),
} satisfies Theme

export default theme