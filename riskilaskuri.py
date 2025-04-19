import streamlit as st
import matplotlib.pyplot as plt

st.set_page_config(page_title="Riskinhallintalaskuri", layout="centered")
st.title("Riskinhallintalaskuri")

st.subheader("Riskiarvio")
seuraus = st.number_input("Riski: Suurin mahdollinen seuraus (€)", min_value=0.0, value=500000.0, step=10000.0)
todennakoisyys = st.slider("Todennäköisyys (%)", 0.0, 100.0, 1.0, step=0.1)
odotusarvo = seuraus * (todennakoisyys / 100)

st.markdown(f"**Odotusarvo (riski):** {odotusarvo:,.2f} €")

st.subheader("Hallintakeino")
hinta = st.number_input("Hallintakeinon kustannus (€)", min_value=0.0, value=2000.0, step=100.0)
teho = st.slider("Riskin pienennys (%)", 0.0, 100.0, 80.0, step=1.0)

uusi_todennakoisyys = todennakoisyys * (1 - teho / 100)
uusi_odotusarvo = seuraus * (uusi_todennakoisyys / 100)
säästö = odotusarvo - uusi_odotusarvo
nettohyöty = säästö - hinta

st.markdown(f"**Hallintakeinon jälkeen odotusarvo:** {uusi_odotusarvo:,.2f} €")
st.markdown(f"**Riskin pieneneminen:** {säästö:,.2f} €")
st.markdown(f"**Hallintakeinon hinta:** {hinta:,.2f} €")
st.markdown(f"**Nettohyöty:** {nettohyöty:,.2f} €")

if nettohyöty > 0:
    st.success("✅ Hallintakeino on taloudellisesti kannattava!")
elif nettohyöty == 0:
    st.info("ℹ️ Hallintakeino on juuri ja juuri kannattava.")
else:
    st.warning("⚠️ Hallintakeino ei ole taloudellisesti kannattava.")

fig, ax = plt.subplots()
ax.bar(["Alkuperäinen riski", "Jäljelle jäävä riski", "Hallintakeinon hinta"],
       [odotusarvo, uusi_odotusarvo, hinta],
       color=["red", "orange", "blue"])
ax.set_ylabel("€")
ax.set_title("Riskin hajautus ja hallintakeinon vaikutus")
st.pyplot(fig)
