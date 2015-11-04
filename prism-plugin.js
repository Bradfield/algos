import prism from 'prismjs'


const pythonCode = /```python\n([\s\S]+?)```/gm

const pythonGrammar = {
  'triple-quoted-string': {
    pattern: /"""[\s\S]+?"""|'''[\s\S]+?'''/,
    alias: "string",
  },
  comment: {
    pattern: /(^|[^\\])#.*/,
    lookbehind: !0,
  },
  string: /("|')(?:\\?.)*?\1/,
  "function": {
    pattern: /((?:^|\s)def[ \t]+)[a-zA-Z_][a-zA-Z0-9_]*(?=\()/g,
    lookbehind: !0,
  },
  'class-name': {
    pattern: /(\bclass\s+)[a-z0-9_]+/i,
    lookbehind: !0,
  },
  keyword: /\b(?:as|assert|async|await|break|class|continue|def|del|elif|else|except|exec|finally|for|from|global|if|import|in|is|lambda|pass|print|raise|return|try|while|with|yield)\b/,
  'boolean': /\b(?:True|False)\b/,
  number: /\b-?(?:0[bo])?(?:(?:\d|0x[\da-f])[\da-f]*\.?\d*|\.\d+)(?:e[+-]?\d+)?j?\b/i,
  operator: /[-+%=]=?|!=|\*\*?=?|\/\/?=?|<[<=>]?|>[=>]?|[&|^~]|\b(?:or|and|not)\b/,
  punctuation: /[{}[\];(),.:]/,
}


const highlight = (match, group) => `
  <pre><code class="language-python">${prism.highlight(group, pythonGrammar)}</code></pre>`


export const highlightCode = files => {
  for (let path in files) {
    if (path.search('\.md$') !== -1) {
      const file = files[path]
      const replaced = file.contents.toString('utf8').replace(pythonCode, highlight)
      file.contents = new Buffer(replaced, 'utf8')
    }
  }
}
