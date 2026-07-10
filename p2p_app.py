import streamlit as st # This line is present above, otherwise it is not
c1, c2, c3, c4 = st.columns(4)

with c4:
st.markdown(...) # Below is your previous code...
    st.markdown(f"<div style='color:#fcd535; font-size:12px; font-weight:bold; margin-bottom:5px;'>{row['payment_method']}</div>", unsafe_allow_html=True)
    if st.button(f"Trade {row['crypto_asset']}", key=f"trade_{row['id']}"):
                    st.warning("?? Secure Escrow Lock Initiated!")
                    if saved_accounts:
                        st.markdown("#### Send payment using your configured settlement credentials:")
                        for acc in saved_accounts:
                            st.info(f"??? {acc[0]} | Holder: {acc[1]} | Account No/Phone: {acc[2]}")
                    else:
                        st.error("No active localized payment channels configured. Add your Telebirr or Neged Bank accounts in the next tab Panel.")
                    st.markdown("<hr style='margin:10px 0; border-color:#2b313a;' />", unsafe_allow_html=True)

# --- TAB 2: ACCOUNTS MANAGEMENT ---
with tab_accounts:
    st.markdown("### ?? Linked Settlement Gateway Management")
    
    a1, a2, a3 = st.columns(3)
    with a1:
        acc_type = st.selectbox("Financial Service System:", ["Telebirr Mobile Money", "Neged Bank (CBE)"])
    with a2:
        acc_name = st.text_input("Account Holder Legal Name (English/Amharic):", placeholder="e.g. Abebe Kebede")
    with a3:
        acc_num = st.text_input("Account Number or Target Phone Line Number:", placeholder="e.g. 0911223344 or 1000XXXXXXXX")
        
    if st.button("?? Link New Payment Account Channel Vector"):
        if acc_name and acc_num:
            conn = sqlite3.connect('p2p_marketplace.db')
            cursor = conn.cursor()
            cursor.execute("INSERT INTO broker_accounts (account_type, account_name, account_number) VALUES (?, ?, ?)", (acc_type, acc_name, acc_num))
            conn.commit()
            conn.close()
            st.success(f"Success! {acc_type} interface pipeline map linked flawlessly to database framework nodes.")
            st.rerun()
        else:
            st.error("Please input a valid account name and card target routing map sequence.")
            
    st.markdown("---")
    st.markdown("#### Currently Linked Settlement Routing Nodes")
    
    conn = sqlite3.connect('p2p_marketplace.db')
    df_accs = pd.read_sql_query("SELECT * FROM broker_accounts", conn)
    conn.close()
    
    if df_accs.empty:
        st.info("No payment accounts currently mapped. Add an account above to provide instant settlement data to your trade counters.")
    else:
        for _, acc in df_accs.iterrows():
            st.markdown(f"""
            <div class='payment-box'>
                <span style='color:#fcd535; font-weight:bold; font-size:16px;'>?? {acc['account_type']}</span><br/>
                <span style='color:#848e9c;'>Account Holder Name:</span> {acc['account_name']}<br/>
                <span style='color:#848e9c;'>Account Number/Target Route ID:</span> <code>{acc['account_number']}</code>
            </div>
            """, unsafe_allow_html=True)

# --- TAB 3: ADS DEPLOYER ---
with tab_post:
    st.markdown("### ?? Issue Custom Broker Order Liquidity Advertisement")
    p1, p2 = st.columns(2)
    with p1:
        new_adv = st.text_input("Your Registered Broker Handle Name:", value="Ethio_Premium_Node")
        new_type = st.selectbox("Action Operation Order Type:", ["BUY", "SELL"])
        new_asset = st.selectbox("Target Cryptocurrency Escrow:", ["USDT", "BTC"])
        new_fiat = st.selectbox("Settlement Fiat Currency System:", ["ETB", "USD"])
    with p2:
        new_price = st.number_input("Your Fixed Exchange Target Price (Rate per 1 Unit):", min_value=0.01, value=124.50, step=0.10)
        new_qty = st.number_input("Total Liquidity Pool Volume Available Size:", min_value=1.0, value=2500.0)
        new_min = st.number_input("Minimum Transaction Threshold Limit Value:", min_value=1.0, value=1000.0)
        new_max = st.number_input("Maximum Transaction Threshold Limit Value:", min_value=1.0, value=500000.0)
        new_pay_method = st.selectbox("Primary Settlement Method Label for Client View:", ["Telebirr", "CBE (Neged Bank)", "Telebirr / CBE"])

    if st.button("?? Push Live Broker Order Advert"):
        if new_adv:
            conn = sqlite3.connect('p2p_marketplace.db')
            cursor = conn.cursor()
            cursor.execute("INSERT INTO ads (advertiser, trade_type, crypto_asset, fiat_currency, price, available_amount, min_limit, max_limit, payment_method) VALUES (?,?,?,?,?,?,?,?,?)",
                           (new_adv, new_type, new_asset, new_fiat, new_price, new_qty, new_min, new_max, new_pay_method))
            conn.commit()
            conn.close()
            st.success("Your currency liquidity asset path advertisement is live! Refreshing panels...")
            st.rerun()
