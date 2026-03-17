@echo off
title Local Chat - MichiTheCat
chcp 65001 > nul
streamlit run app.py --server.address 0.0.0.0 --server.port 8501