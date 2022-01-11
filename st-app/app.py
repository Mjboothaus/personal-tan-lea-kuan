import streamlit as st
import streamlit.components.v1 as components
from pathlib import Path
#import pandas as pd
#import numpy as np

from dynaconf import settings

st.header("LKT Market Watch")

st.subheader("by Emmeline Booth")
# st.write(settings.NAME)

def load_ticker_template():
  with open("ticker_template.html") as f:
    contents = f.read()
  return contents

contents = load_ticker_template()

CODE_1 = "ASX:ANZ"
LABEL_1 = "ANZ Bank"
CODE_2 = "ASX:CBA"
LABEL_2 = "Commonwealth Bank"
CODE_3 = "ASX:NAB"
LABEL_3 = "National Aust Bank"
CODE_4 = "ASX:WBC"
LABEL_4 = "Westpac Bank"
CODE_5 = "ASX:MQG"
LABEL_5 = "Macquarie Bank"


contents = contents.replace("[CODE_1]", CODE_1)
contents = contents.replace("[LABEL_1]", LABEL_1)

contents = contents.replace("[CODE_2]", CODE_2)
contents = contents.replace("[LABEL_2]", LABEL_2)

contents = contents.replace("[CODE_3]", CODE_3)
contents = contents.replace("[LABEL_3]", LABEL_3)

contents = contents.replace("[CODE_4]", CODE_4)
contents = contents.replace("[LABEL_4]", LABEL_4)

contents = contents.replace("[CODE_5]", CODE_5)
contents = contents.replace("[LABEL_5]", LABEL_5)


# st.write(contents)

components.html(contents)

st.markdown("by [DataBooth.com.au](https://wwww.databooth.com.au)")