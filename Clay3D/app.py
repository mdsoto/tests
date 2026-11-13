from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Minerales de arcilla en 3D", layout="wide")

html = Path(__file__).with_name("clay-minerals-3d.html").read_text(encoding="utf-8")
components.html(html, height=1700, scrolling=True)
