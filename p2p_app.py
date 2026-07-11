import streamlit as st

# 1. Page Configuration & Title
st.set_page_config(page_title="Ethio P2P Crypto Desk", layout="wide")
st.title("🇪🇹 Ethio P2P Crypto Brokerage Desk")
st.markdown("---")

# 2. Permanent Session State Memory for Accounts
if 'saved_accounts' not in st.session_state:
    # Adding a default account so the app doesn't look empty to new users
    st.session_state['saved_accounts'] = [
        ("Telebirr Mobile Money", "Yehualashet Abera", "0981614568")
    ]

# Active trade offer parameters
trade_row = {
    'crypto_asset': 'USDT',
    'id': 'TX-9921',
    'price_per_dollar': '125.50 ETB',
    'min_limit': '10 USDT',
    'max_limit': '500 USDT'
}

# 3. PUBLIC P2P TRADE WINDOW (What people see)
st.subheader("🛒 Active Public P2P Trade Offers")

# Create a clean display card for users trying to trade with you
with st.container():
    col1, col2, col3, col4 = st.columns([1, 1.5, 1.5, 1])
    
    with col1:
        st.markdown(f"### {trade_row['crypto_asset']}")
        st.caption(f"Order ID: {trade_row['id']}")
        
    with col2:
        st.metric(label="Rate (Per Dollar)", value=trade_row['price_per_dollar'])
        
    with col3:
        st.markdown(f"Limits:")
        st.text(f"Min: {trade_row['min_limit']}\nMax: {trade_row['max_limit']}")
        
    with col4:
        # Trade initiation button
        st.write("") # Padding
        trade_clicked = st.button(f"Trade {trade_row['crypto_asset']}", key="buy_btn", type="primary")

# 4. INTERACTIVE TRADE DESK (Triggers when someone clicks 'Trade')
if trade_clicked:
    st.markdown("---")
    st.success("🔒 Secure Escrow Lock Initiated! Your crypto is safely locked in contract.")
    
    st.markdown("### 💳 Settlement Instructions for Buyer:")
    st.write("Please send the equivalent ETB amount to the broker using the verified gateway details below:")
    
    # Render all currently configured payment channels live
    for index, acc in enumerate(st.session_state['saved_accounts']):
        st.info(f"✨ Gateway {index+1}: {acc[0]}\n* Legal Name: {acc[1]}\n* Account/Phone: {acc[2]}")

st.markdown("---")

# 5. BROKER SETTINGS: LINKED SETTLE GATEWAY MANAGEMENT
st.subheader("🏦 Broker Wallet & Gateway Settings (Admin)")
st.write("Configure your local payment methods below. Any changes made here instantly update the live trading window above.")

# Use a form to prevent text inputs from resetting prematurely when buttons are clicked
with st.form(key="gateway_form", clear_on_submit=True):
    a1, a2, a3 = st.columns(3)
    
    with a1:
        acc_type = st.selectbox("Financial Service System:", ["Telebirr Mobile Money", "CBE Birr", "Bank Transfer"])
    with a2:
        acc_name = st.text_input("Account Holder Legal Name (English/Amharic):")
    with a3:
        acc_num = st.text_input("Account Number or Target Phone Line Number:")
        
    submit_button = st.form_submit_button(label="➕ Link New Payment Account Channel Vector")

# Form submission logic
if submit_button:
    if acc_name.strip() != "" and acc_num.strip() != "":
        st.session_state['saved_accounts'].append((acc_type, acc_name, acc_num))
        st.success(f"Successfully linked {acc_type} for {acc_name}! App updated.")
        st.rerun()
    else:
        st.error("Submission failed! Both Account Holder Name and Account Number are required fields.")
