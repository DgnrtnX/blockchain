import React, { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';
import logo from '../asset/logo.png';
import banner_img from '../asset/transparency.jpg';
import { API_BASE_URL } from '../config';


function App() {
  const [walletInfo, setWalletInfo] = useState({});

  useEffect(() => {
    fetch(`${API_BASE_URL}/wallet/info`)
      .then(response => response.json())
      .then(json => setWalletInfo(json));
  }, []);

  const { address, balance } = walletInfo;

  return (
    <div className="App">
    <img className="section-img" src={banner_img} alt="banner-img" />
      <div className="main-section">
      <Link to="/blockchain" className="btn-neon">Blockchain</Link>
      <Link to="/conduct-transaction"className="btn-neon">Conduct a Transaction</Link>
      <Link to="/transaction-pool"className="btn-neon">Transaction Pool</Link>
      </div>
      <br />
      <div className="WalletInfo">
        <div className="txt">Address: {address}</div>
        <div className="txt">Balance: {balance}</div>
      </div>
    </div>
  );
}

export default App;

