//https://docs.pinata.cloud/quickstart/react


import '../styles/Wallet.css'

import React, { useState, useEffect } from 'react';
import { getContractSigner, defaultContractAddress } from '../utils/EthersUtils';
import { useWallet } from '../utils/Context';

const JWT = process.env.REACT_APP_IPFS_JWT;
const GATEWAY = process.env.REACT_APP_IPFS_GATEWAY;

const ABI = require("../abi.json");

export const IpfsLoader = () => {
  const [selectedFile, setSelectedFile] = useState(null);
  const [cid, setCid] = useState();
  const [address, setAddress] = useState(defaultContractAddress);
  const [contract, setContract]  = useState();
  const { wallet, initializeWalletm } = useWallet();

  const handleFileChange = (event) => {
    setSelectedFile(event.target.files[0]);
  };

  const handlePinFileToIPFS = async () => {
    if (!selectedFile) {
      console.log('No file selected');
      return;
    }

    const formData = new FormData();
    formData.append('file', selectedFile);

    const pinataMetadata = JSON.stringify({
      name: selectedFile.name,
    });
    formData.append('pinataMetadata', pinataMetadata);

    const pinataOptions = JSON.stringify({
      cidVersion: 0,
    });
    formData.append('pinataOptions', pinataOptions);

    try {
      console.log(JWT);
      const res = await fetch(
        'https://api.pinata.cloud/pinning/pinFileToIPFS',
        {
          method: "POST",
          headers: {
            Authorization: `Bearer ${JWT}`,
          },
          body: formData,
        }
      );
      const resData = await res.json();
      setCid(resData.IpfsHash);

      const tokenID = await contract.safeMint("0x50497E8c0272D6c3d37fCe08F8c36AF336E34c10", resData.IpfsHash);
      console.log(tokenID);
      console.log(resData.IpfsHash);
    } catch (error) {
      console.log(error);
    }
  };

  const handleAddressChange = (e) => {
    setAddress(e.target.value);
    console.log(wallet);
    getContractSigner(e.target.value, ABI, wallet).then((contract) => {
      console.log(contract);
      setContract(contract);
    });
  }

  return (
    <div className="App">
        <div className="App-header">
        <div className="input-container">
      <input
        type="text"
        value={address}
        onChange={handleAddressChange}
        placeholder="contract address"
      /> 

      <input type="file" onChange={handleFileChange} />
      <button onClick={handlePinFileToIPFS}>Pin to IPFS</button>
      {cid && (
        <img
          src={`https://${GATEWAY}/ipfs/${cid}`}
          alt="ipfs image"
        />
      )}
      </div>
      </div>
    </div>
  );
};

