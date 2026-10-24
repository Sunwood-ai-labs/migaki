import { defineConfig } from 'vitepress'

const github = 'https://github.com/Sunwood-ai-labs/evidence-informed-design'

const englishNavigation = [
  { text: 'Install', link: '/guide/install' },
  { text: 'Research', link: '/guide/research' },
  { text: 'Checklist', link: '/guide/checklist' },
  { text: 'Verification', link: '/guide/verification' },
]

const japaneseNavigation = [
  { text: 'インストール', link: '/ja/guide/install' },
  { text: '研究と根拠', link: '/ja/guide/research' },
  { text: 'チェックリスト', link: '/ja/guide/checklist' },
  { text: '検証', link: '/ja/guide/verification' },
]

export default defineConfig({
  base: '/evidence-informed-design/',
  title: 'Evidence-informed design',
  description: 'A Codex skill for reviewing grouping, hierarchy, and visual clutter with evidence and artifact checks.',
  head: [
    ['link', { rel: 'icon', href: '/evidence-informed-design/favicon.svg', type: 'image/svg+xml' }],
    ['meta', { name: 'theme-color', content: '#122f3b' }],
  ],
  locales: {
    root: {
      label: 'English',
      lang: 'en-US',
      title: 'Evidence-informed design',
      description: 'A Codex skill for reviewing grouping, hierarchy, and visual clutter with evidence and artifact checks.',
      themeConfig: {
        nav: englishNavigation,
        sidebar: [
          {
            text: 'Guide',
            items: [
              { text: 'Install the skill', link: '/guide/install' },
              { text: 'Research and scope', link: '/guide/research' },
              { text: 'Design checklist', link: '/guide/checklist' },
              { text: 'Verify a design decision', link: '/guide/verification' },
            ],
          },
        ],
        outline: { label: 'On this page' },
        docFooter: { prev: 'Previous page', next: 'Next page' },
        socialLinks: [{ icon: 'github', link: github }],
      },
    },
    ja: {
      label: '日本語',
      lang: 'ja-JP',
      title: '根拠に基づく情報デザイン',
      description: '研究と経験則を設計判断に使い、成果物で確認するCodexスキルです。',
      themeConfig: {
        nav: japaneseNavigation,
        sidebar: [
          {
            text: 'ガイド',
            items: [
              { text: 'スキルをインストールする', link: '/ja/guide/install' },
              { text: '研究と根拠の範囲', link: '/ja/guide/research' },
              { text: '設計チェックリスト', link: '/ja/guide/checklist' },
              { text: '設計判断を検証する', link: '/ja/guide/verification' },
            ],
          },
        ],
        outline: { label: 'このページの内容' },
        docFooter: { prev: '前のページ', next: '次のページ' },
        socialLinks: [{ icon: 'github', link: github }],
      },
    },
  },
})
