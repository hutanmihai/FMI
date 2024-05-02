//require('dotenv').config();
const defaultContractAddress = process.env.REACT_APP_CONTRACT_ADDRESS;
const ethers = require('ethers');

const provider = new ethers.BrowserProvider(window.ethereum);

const connectWalletMetamask = (accountChangedHandler) => {
  if (window.ethereum) {
    provider.send("eth_requestAccounts", []).then(async () => {
      provider.getSigner().then(async (account) => {
        accountChangedHandler(account);
      });
    }
    ).catch(async () => { console.log("err"); });
  } else {
    console.log("err");
  }
}

const getBalance = (address) => {
  return provider.getBalance(address);
};

const sendTransaction = async (sender, to, amount) => {
  console.log("sender: " + sender.provider);
  console.log('amount ' + ethers.parseUnits(amount.toString(), 'wei'));
  const transactionResponse = await sender.sendTransaction({
    to,
    value: ethers.parseUnits(amount.toString(), 'wei')
  });

  return transactionResponse.hash;
};


const getContract = async (contractAddress, abi) => {
  const contract = new ethers.Contract(contractAddress, abi, provider);
  return contract;
} 


const getContractSigner = async (contractAddress, abi, signer) => {
  const contract = new ethers.Contract(contractAddress, abi, signer);
  return contract;
} 

module.exports = {
  provider,
  sendTransaction,
  getBalance,
  connectWalletMetamask,
  getContract,
  getContractSigner,
  defaultContractAddress
};


