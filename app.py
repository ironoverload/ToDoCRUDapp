# Core Package
import streamlit as st
import streamlit.components.v1 as stc

# EDA Packages
import pandas as pd

# Import the Functions page db_fxns.app
from db_fxns import *


# Data Viz Pkgs
import plotly.express as px
import matplotlib.pyplot as plt
import matplotlib

matplotlib.use('Agg')

HTML_BANNER = """
    <div style="background-color:#464e5f;padding:10px;border-radius:10px">
    <h1 style="color:white;text-align:center;">ToDo App (CRUD)</h1>
    <p style="color:white;text-align:center;">Built with Streamlit</p>
    </div>
    """


def main():
    stc.html(HTML_BANNER)


if __name__ == '__main__':
    main()
