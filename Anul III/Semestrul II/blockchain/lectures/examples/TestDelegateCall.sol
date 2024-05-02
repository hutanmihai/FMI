// SPDX-License-Identifier: GPL-3.0

pragma solidity ^0.8.20;

contract A{

    uint256 public fee;
    
    event LogSender(address indexed);
    
    
    function callRecalculate(address contractB, uint baseFee) public {
        (bool success, ) = contractB.call(abi.encodeWithSignature("recalculateFee(uint256)",baseFee));
        require(success);          
    }

    function delegatecallRecalculate(address contractB, uint baseFee) public {
        (bool success, ) = contractB.delegatecall(abi.encodeWithSignature("recalculateFee(uint256)",baseFee));
        require(success);           
    }

    function callGetFee(address contractB) public returns(uint){
        (bool success, bytes memory data) = contractB.call(abi.encodeWithSignature("getFee()"));
        require(success);      
        return abi.decode(data, (uint256));    
    }

    function delegatecallGetFee(address contractB) public returns(uint){
        (bool success, bytes memory data) = contractB.delegatecall(abi.encodeWithSignature("getFee()"));
        require(success); 
        return abi.decode(data, (uint256));           
    }


}


contract B{

    uint256 public fee;
    uint256 public addedFee;

    event LogSender(address indexed);

    function recalculateFee(uint256 baseFee) external {
        fee = baseFee; 
        emit LogSender(msg.sender);
    } 

    function getFee() external view returns(uint256) {
        return fee + addedFee; 
    } 

    function setAddedFee(uint256 _fee) public{
        addedFee = _fee;
    }

}