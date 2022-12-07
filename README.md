# TEXTBOT
### TEXTBOT is a python bot which uses [PYTEXTNOW](https://github.com/leogomezz4t/PyTextNow_API) and [TEXTNOW](https://www.textnow.com/) to create a sms bot for basic services. Can also be used as a framework for modification.

# UNFINISHED, STILL IN VERY EARLY STAGES

## INFO
- Developer - Ben Song
- Discord - fgdxfg bjnm jgvhbubb#4917

## INSTALLING



## Installation

```bash
npm install --save-dev @babel/plugin-transform-react-jsx
```

## Usage

### Via `.babelrc` (Recommended)

**.babelrc**

```json
{
  "plugins": ["@babel/plugin-transform-react-jsx"]
}
```

### Via CLI

```bash
babel --plugins @babel/plugin-transform-react-jsx script.js
```

### Via Node API

```javascript
require("@babel/core").transform("code", {
  plugins: ["@babel/plugin-transform-react-jsx"]
});
```

## Options

### `pragma`

**Type:** `string`  
**Default:** `React.createElement`

The function used when compiling JSX expressions.

```json
{
  "plugins": [
    ["@babel/plugin-transform-react-jsx", {
      "pragma": "dom"
   

