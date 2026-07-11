import streamlit as st

# Initialize session state to remember accounts permanently during the session
if 'saved_accounts' not in st.session_state:
    st.session_state['saved_accounts'] = []

row = {'crypto_asset': 'USDT', 'id': 1}

c1, c2, c3, c4 = st.columns(4)

with c4:
    st.markdown(f"<div style='color:#fcd535; font-size:12px; font-weight:bold; margin-bottom:5px;'>Trade {row['crypto_asset']}</div>", unsafe_allow_html=True)
    if st.button(f"Trade {row['crypto_asset']}", key=f"trade_{row['id']}"):
        st.warning("🔒 Secure Escrow Lock Initiated!")
        
    # Check if there are any saved accounts in memory
    if st.session_state['saved_accounts']:
        st.markdown("#### 💳 Active Settlement Gateways:")
        for acc in st.session_state['saved_accounts']:
            st.info(f"ℹ️ {acc[0]} | Holder: {acc[1]} | Account No/Phone: {acc[2]}")
    else:
        st.error("No active localized payment channels configured. Add your Telebirr or CBE account below.")
        
    st.markdown("<hr style='margin:10px 0; border-color:#2b313a;' />", unsafe_allow_html=True)

# --- TAB 2: ACCOUNTS MANAGEMENT ---
st.markdown("### 🏦 Linked Settlement Gateway Management")

a1, a2, a3 = st.columns(3)
with a1:
    acc_type = st.selectbox("Financial Service System:", ["Telebirr Mobile Money", "CBE Birr", "Bank Transfer"])
with a2:
    acc_name = st.text_input("Account Holder Legal Name (English/Amharic):", placeholder="e.g. Abebe Kebede")
with a3:
    acc_num = st.text_input("Account Number or Target Phone Line Number:", placeholder="e.g. 0912345678")

if st.button("➕ Link New Payment Account Channel Vector"):
    if acc_name and acc_num:
        # Append the new account to session state memory
        st.session_state['saved_accounts'].append((acc_type, acc_name, acc_num))
        st.success(f"Successfully linked {acc_type} for {acc_name}!")
        # Rerun the app instantly to show the new account in the top section
        st.rerun()
    else:
        st.error("Please fill out both the Account Holder Name and Account Number!")
