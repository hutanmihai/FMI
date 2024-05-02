// SPDX-License-Identifier: GPL-3.0

pragma solidity ^0.8.20;


contract Proxy {
    address public implementation;

    constructor(address _implementation) {
        implementation = _implementation;
    }

    function setImplementation(address _implementation) public {
        //require(msg.sender == implementation, "incorrect version");
        implementation = _implementation;
    }

    function _delegate() private {
        (bool success, ) = implementation.delegatecall(msg.data);
        require(success);
    }

     fallback() external {
        _delegate();
    }
}

contract ContractA {
    uint256 public value;

    event ChangeVal(uint newVal);

    function setValue(uint256 _newValue) public {
        emit ChangeVal( _newValue );
        value = _newValue;
    }

}


contract UpgradedContractA {
    uint256 public value;

    event ChangeVal(uint newVal);

    function setValue(uint256 _newValue) public {
        emit ChangeVal( _newValue * 10 );
        value = _newValue * 10;
    }
}