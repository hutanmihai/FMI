// SPDX-License-Identifier: GPL-3.0

pragma solidity ^0.8.20;

import "./MyERC721.sol";

contract ERC721Market is MyERC721{

    
    mapping(uint256 => uint256) public price;
    uint8 private constant mappingSlotIndex = 0;


    uint256 public fee;
    uint256 listingId;

    modifier checkFee(){
        require(fee <= msg.value, 'send fee!');
        _;
    }

    modifier checkTransfer(uint256 balance, uint256 toTransfer){
        require(toTransfer <= balance, 'insufficient funds!');
        _;
    }

    modifier checkPrice(uint _tokenId){
        require(price[_tokenId] <= msg.value, 'send the value of the required NFT');
        _;
    }

    constructor (uint8 _fee) MyERC721(msg.sender){
        fee = _fee;
        listingId = 0;
    }

    
    mapping(uint256 => address) public seller;
    mapping(address => uint256) public deposit;


    function listToken(uint8 _price, uint256 tokenId) checkFee
        public
        payable returns(uint)
    {
        listingId += 1;
        price[tokenId] = _price;
        seller[tokenId] = msg.sender;
        return listingId;
    }

    function depositForToken(uint256 _tokenId) checkPrice(_tokenId) public payable {
        deposit[msg.sender] += msg.value; 
    } 

    function sell(address _to, uint256 _tokenId) public{
        this.transferFrom(msg.sender, _to, _tokenId);
        uint256 _price = price[_tokenId];
        deposit[_to] -= _price;
        address payable payableAdr = payable(address(msg.sender));
        payableAdr.transfer(_price);
    }


    function withdraw(uint amount)  checkTransfer(deposit[msg.sender], amount) public{
        address payable payableAdr = payable(address(msg.sender));
        bool testOk = payableAdr.send(amount);
        require(testOk);
        deposit[msg.sender] -= amount;
    }


    
    function getStorageSlot(uint256 key) public pure returns (bytes32) {

        return keccak256(abi.encode(key, mappingSlotIndex));

    }

    function testGasCost(uint256 key, uint256 value) public  {
        bytes32 slot = getStorageSlot(key);
        assembly {
            sstore(slot,value)
         }
    }  

    function getSlotFee() public pure returns(uint _slot){
        assembly{
            
            _slot:= fee.slot
        }
    }

    function testGasCost2(uint value) public  {
        uint slot = getSlotFee();
        assembly {
            sstore(slot,value)
         }
    }  

}