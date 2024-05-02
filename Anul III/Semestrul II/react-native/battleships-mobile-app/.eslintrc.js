module.exports = {
  root: true,
  extends: ['universe/native'],
  plugins: ['unused-imports'], // Add the plugin here
  rules: {
    // Add or update your rules configuration here
    'unused-imports/no-unused-imports': 'error', // Report unused imports as errors
    'unused-imports/no-unused-vars': [
      'warn', // or 'error' to treat as an error
      { vars: 'all', varsIgnorePattern: '^_', args: 'after-used', argsIgnorePattern: '^_' },
    ],
  },
}
