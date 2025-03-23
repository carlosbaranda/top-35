
import streamlit as st
import yfinance as yf
import pandas as pd

st.set_page_config(page_title="App Bolsa", layout="wide")
st.title("App de Bolsa - Sin errores de indentación")

tickers = ['AAPL', 'MSFT', 'GOOGL', 'AMZN', 'TSLA', 'META', 'NVDA', 'JPM', 'WMT', 'UNH', 'KO', 'PEP', 'V', 'BAC', 'HD', 'DIS', 'MA', 'PYPL', 'INTC', 'IBM', 'CSCO', 'ORCL', 'NFLX', 'T', 'CVX', 'PFE', 'XOM', 'C', 'MCD', 'BA', 'ABT', 'CRM', 'MRK', 'QCOM', 'NKE', 'AIR.PA', 'ADS.DE', 'ALV.DE', 'BN.PA', 'ENEL.MI', 'ENGI.PA', 'OR.PA', 'SAP.DE', 'SIE.DE', 'SU.PA', 'TTE.PA', 'VOW3.DE', 'DTE.DE', 'DPW.DE', 'BAS.DE', 'BMW.DE', 'SAN.PA', 'MC.PA', 'KER.PA', 'IBE.MC', 'ITX.MC', 'BBVA.MC', 'SGO.PA', 'ISP.MI', 'FER.MC', 'ABI.BR', 'UCG.MI', 'MB.MI', 'MT.AS', 'EL.PA', 'PHIA.AS', 'ZAL.DE', 'GN.CO', 'AD.AS', 'ENI.MI', 'SAN.MC', 'BBVA.MC', 'ITX.MC', 'IBE.MC', 'REP.MC', 'AMS.MC', 'ANA.MC', 'CABK.MC', 'CLNX.MC', 'ENG.MC', 'FER.MC', 'GRF.MC', 'IAG.MC', 'MAP.MC', 'TEF.MC', 'AENA.MC', 'ACS.MC', 'ELE.MC', 'MEL.MC', 'NTGY.MC', 'PHM.MC', 'RED.MC', 'SAB.MC', 'SGRE.MC', 'SOL.MC', 'VIS.MC', 'BKT.MC', 'EUS.MC', 'COL.MC', 'ALM.MC', 'LOG.MC', 'RLD.MC', 'FCC.MC', 'RVE.MC', 'ZOT.MC']
@st.cache_data(ttl=3600)
def obtener_datos(tickers):
    data = []
    for ticker in tickers:
        try:
            stock = yf.Ticker(ticker)
            hist = stock.history(period="90d")
            info = stock.info
            if len(hist) >= 7:
                hoy = (hist["Close"][-1] - hist["Open"][-1]) / hist["Open"][-1] * 100
                semana = (hist["Close"][-1] - hist["Close"][-6]) / hist["Close"][-6] * 100
                ytd = (hist["Close"][-1] - hist["Close"][0]) / hist["Close"][0] * 100
                data.append({
                    "Ticker": ticker,
                    "Nombre": info.get("shortName", ""),
                    "Cambio Día (%)": round(hoy, 2),
                    "Cambio Semana (%)": round(semana, 2),
                    "Cambio YTD (%)": round(ytd, 2)
                })
        except:
            continue
    return pd.DataFrame(data)

df = obtener_datos(tickers)
df["Mercado"] = df["Ticker"].map({'AAPL': 'NYSE', 'MSFT': 'NYSE', 'GOOGL': 'NYSE', 'AMZN': 'NYSE', 'TSLA': 'NYSE', 'META': 'NYSE', 'NVDA': 'NYSE', 'JPM': 'NYSE', 'WMT': 'NYSE', 'UNH': 'NYSE', 'KO': 'NYSE', 'PEP': 'NYSE', 'V': 'NYSE', 'BAC': 'NYSE', 'HD': 'NYSE', 'DIS': 'NYSE', 'MA': 'NYSE', 'PYPL': 'NYSE', 'INTC': 'NYSE', 'IBM': 'NYSE', 'CSCO': 'NYSE', 'ORCL': 'NYSE', 'NFLX': 'NYSE', 'T': 'NYSE', 'CVX': 'NYSE', 'PFE': 'NYSE', 'XOM': 'NYSE', 'C': 'NYSE', 'MCD': 'NYSE', 'BA': 'NYSE', 'ABT': 'NYSE', 'CRM': 'NYSE', 'MRK': 'NYSE', 'QCOM': 'NYSE', 'NKE': 'NYSE', 'AIR.PA': 'EuroStoxx', 'ADS.DE': 'EuroStoxx', 'ALV.DE': 'EuroStoxx', 'BN.PA': 'EuroStoxx', 'ENEL.MI': 'EuroStoxx', 'ENGI.PA': 'EuroStoxx', 'OR.PA': 'EuroStoxx', 'SAP.DE': 'EuroStoxx', 'SIE.DE': 'EuroStoxx', 'SU.PA': 'EuroStoxx', 'TTE.PA': 'EuroStoxx', 'VOW3.DE': 'EuroStoxx', 'DTE.DE': 'EuroStoxx', 'DPW.DE': 'EuroStoxx', 'BAS.DE': 'EuroStoxx', 'BMW.DE': 'EuroStoxx', 'SAN.PA': 'EuroStoxx', 'MC.PA': 'EuroStoxx', 'KER.PA': 'EuroStoxx', 'IBE.MC': 'España', 'ITX.MC': 'España', 'BBVA.MC': 'España', 'SGO.PA': 'EuroStoxx', 'ISP.MI': 'EuroStoxx', 'FER.MC': 'España', 'ABI.BR': 'EuroStoxx', 'UCG.MI': 'EuroStoxx', 'MB.MI': 'EuroStoxx', 'MT.AS': 'EuroStoxx', 'EL.PA': 'EuroStoxx', 'PHIA.AS': 'EuroStoxx', 'ZAL.DE': 'EuroStoxx', 'GN.CO': 'EuroStoxx', 'AD.AS': 'EuroStoxx', 'ENI.MI': 'EuroStoxx', 'SAN.MC': 'España', 'REP.MC': 'España', 'AMS.MC': 'España', 'ANA.MC': 'España', 'CABK.MC': 'España', 'CLNX.MC': 'España', 'ENG.MC': 'España', 'GRF.MC': 'España', 'IAG.MC': 'España', 'MAP.MC': 'España', 'TEF.MC': 'España', 'AENA.MC': 'España', 'ACS.MC': 'España', 'ELE.MC': 'España', 'MEL.MC': 'España', 'NTGY.MC': 'España', 'PHM.MC': 'España', 'RED.MC': 'España', 'SAB.MC': 'España', 'SGRE.MC': 'España', 'SOL.MC': 'España', 'VIS.MC': 'España', 'BKT.MC': 'España', 'EUS.MC': 'España', 'COL.MC': 'España', 'ALM.MC': 'España', 'LOG.MC': 'España', 'RLD.MC': 'España', 'FCC.MC': 'España', 'RVE.MC': 'España', 'ZOT.MC': 'España'})

# --- Filtro por mercado ---
st.subheader("🌍 Filtrar por mercado")
mercados_disponibles = df["Mercado"].dropna().unique().tolist()
seleccion_mercados = st.multiselect("Selecciona uno o varios mercados:", mercados_disponibles, default=mercados_disponibles)

# --- Selección de número máximo de valores ---
st.subheader("🔢 Número máximo de valores a mostrar")
max_valores = st.slider("Selecciona cuántos valores quieres mostrar (máx 100):", min_value=5, max_value=100, value=35)

df = df[df["Mercado"].isin(seleccion_mercados)]
df_vista = df.head(max_valores)



# --- Tabla resumen de top caída ---
st.subheader("📉 Top Caída por Periodo")

def obtener_peores(df, columna):
    if columna in df.columns:
        return df.sort_values(columna, ascending=True).head(top_n)[["Ticker", "Nombre", columna]]
    return pd.DataFrame()

col_down_dia = obtener_peores(df, "Cambio Día (%)")
col_down_semana = obtener_peores(df, "Cambio Semana (%)")
col_down_ytd = obtener_peores(df, "Cambio YTD (%)")

c1, c2, c3 = st.columns(3)
with c1:
    st.markdown("**📉 Día**")
    st.dataframe(col_down_dia, use_container_width=True)
with c2:
    st.markdown("**📉 Semana**")
    st.dataframe(col_down_semana, use_container_width=True)
with c3:
    st.markdown("**📉 YTD**")
    st.dataframe(col_down_ytd, use_container_width=True)

