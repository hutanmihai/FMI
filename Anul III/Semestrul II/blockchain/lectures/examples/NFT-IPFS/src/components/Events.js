import '../styles/Wallet.css'

import React, { useState, useEffect } from 'react';
import { getContract, defaultContractAddress } from '../utils/EthersUtils';



const ABI = require("../abi.json");

export const Events = () => {
  const [address, setAddress] = useState(defaultContractAddress);
  const [tableData, setTableData] = useState([]);
  const [contract, setContract]  = useState();
  const [newRow, setNewRow] = useState([]);

  useEffect(() => {
    setTableData(prevData => [...prevData, newRow]);
  },[newRow]);


  const handleAddressChange = (e) => {
    setAddress(e.target.value);
  };

  const handleSubscribe = () => {
    getContract(address, ABI).then((contract) => {
      setContract(contract);
      
      if (contract !== undefined){
        console.log(contract);
       contract.on("Transfer", (from, to, tokenId)=>{


            const newRowTransfer = {
                event: "Transfer",
                data1: from,
                data2: to,
                data3: tokenId.toString(),
                data4: ""
            };

            setNewRow(newRowTransfer) ;

        });

        contract.on("Approval", (owner, approved, tokenId)=>{

            const newRowApproval = {
                event: "Approval",
                data1: owner,
                data2: approved,
                data3: tokenId.toString(),
                data4: ""
            };

            setNewRow(newRowApproval) ;
        
        });

    }
      });
  };

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
      <button onClick={handleSubscribe}>Subscribe</button>
      <table>
        <thead>
          <tr>
            <th>Event</th>
            <th>Index 1</th>
            <th>Index 2</th>
            <th>Index 3</th>
            <th>Index 4</th>
          </tr>
        </thead>
        <tbody>
        {tableData.map((rowData, index) => (
    <tr key={index}>
        <td className="tableCell">{rowData.event}</td>
        <td className="tableCell">{rowData.data1}</td>
        <td className="tableCell">{rowData.data2}</td>
        <td className="tableCell">{rowData.data3}</td>
        <td className="tableCell">{rowData.data4}</td>
    </tr>
))}
        </tbody>
      </table>
      </div>
      </div>
    </div>
  );
};

