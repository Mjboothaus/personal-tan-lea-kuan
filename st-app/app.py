import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import numpy as np

st.header("LKT Market Watch")
st.markdown("by [DataBooth.com.au](https://wwww.databooth.com.au)")

# https://www.tradingview.com/widget/ticker-tape/

components.html("""
<div class="tradingview-widget-container">
  <div class="tradingview-widget-container__widget"></div>
  <script type="text/javascript" src="https://s3.tradingview.com/external-embedding/embed-widget-ticker-tape.js" async>
  {
  "symbols": [
    {
      "proName": "ASX:CBA",
      "title": "CBA"
    },
    {
      "proName": "ASX:WBC",
      "title": "Westpac"
    },
    {
      "proName": "ASX:AMP",
      "title": "AMP"
    },
    {
      "proName": "ASX:IAG",
      "title": "Insurance Australia Group"
    }
  ],
  "showSymbolLogo": true,
  "colorTheme": "light",
  "isTransparent": false,
  "displayMode": "adaptive",
  "locale": "en"
}
  </script>
</div>
""")
