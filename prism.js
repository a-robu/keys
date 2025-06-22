// PrismJS SSH authorized_keys language definition
// Place this file as prism.js in your repo root
// Requires Prism.js core (loaded from CDN in index.html)

(function (Prism) {
  Prism.languages.ssh = {
    'comment': /#[^\n]*/,
    'string': {
      pattern: /"(?:\\.|[^\\"])*"|'(?:\\.|[^\\'])*'/,
      greedy: true
    },
    'keyword': /\b(?:ssh-(?:rsa|dss|ed25519)|ecdsa-sha2-nistp(?:256|384|521))\b/,
    'number': /\b\d+\b/,
    'operator': /\s+/,
    'punctuation': /[=]/,
    'user': /\b[a-zA-Z0-9._-]+@[a-zA-Z0-9._-]+\b/
  };
  Prism.hooks.add('wrap', function(env) {
    if (env.type === 'keyword') {
      env.attributes.class = 'token keyword ssh-keytype';
    }
  });
}(Prism));
